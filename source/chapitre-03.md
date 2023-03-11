# Méthode de résolution exacte par la PSE

## Rappel du problème
William Rowan Hamilton posa l’une des première fois le problème du voyageur de commerce dès 1859 avec l’énoncé suivant : 

> « Un voyageur de commerce doit visiter une et une seule fois un nombre fini de villes et revenir à son point d’origine. Trouvez l’ordre de visite des villes qui minimise la distance totale parcourue par le voyageur ».

## Introduction
Cherchons à présent une méthode de résolution exacte un peu moins naïve et plus efficace. Pour cela, nous allons utiliser la **Procédure par Séparation et Évaluation**, abrégée par les initiales **PSE** et nommé **branch & bound** en anglais. C’est une méthode qui repose sur le parcours d’un arbre de recherche auquel on va couper la simulation dans certaines branches lorsqu’il est évident que ce n’est pas le chemin optimal. 

## Notions de base
Avant cela, il est important de définir certains termes qui vont avoir leur importance dans l’application de cette méthode :
1.	Un **arbre de recherche** est un schéma représentant toutes les solutions possibles sous la forme d’embranchements. Un exemple de cet arbre se situe plus bas.
2.	Pour cette méthode, il est aussi important de définir les bornes inférieures et supérieures.

    Une **borne inférieure** est une valeur qui est égale ou inférieure à la valeur de la meilleure solution possible. Dans le cas présent, il suffit pour l’obtenir d’additionner au trajet déjà effectué le poids des $N$ distances les plus proches entre deux villes. Même si cette solution a une grande probabilité de ne pas être réalisable, la valeur de la solution optimale ne pourra pas être plus petite que la borne inférieure. 

    La **borne supérieure**, quant à elle, est une limite qu'aucune solution optimale ne pourra jamais dépasser. Dans ce cas, cette valeur est un trajet quelconque, car si on prend la mauvaise solution on obtient une valeur supérieure à celle qu’on recherche, et dans le cas généralement extrêmement rare où l’on obtient la bonne réponse, la bonne réponse n’est pas en-dessous de la borne supérieure choisie. Pour obtenir des résultats moins variables, on peut aussi utiliser des algorithmes approchés se basant sur des approximations.


## Formation d'un arbre de recherche
Posons la situation suivante: 


```{figure} figures/schema_4.png
---
align: center
width: 50%
---
*Admettons que nous souhaitons traverser de la manière la plus optimale possible les quatre villes affichées.*
```


### Etape par étape
Pour commencer à créer un arbre de recherche, nous devons tout d'abord définir une ville de départ.


```{figure} figures/schema_4a.png
---
align: center
width: 10%
---
*Nous définissons arbitrairement le noeud initial, car cela n'influence pas la longueur du trajet.*
```


Nous appelons cette ville le **nœud initial**. Ensuite, il faut explorer tous les trajets possibles. Pour cela, nous dessinons l'arbre de la manière suivante:


```{figure} figures/schema_4b.png
---
align: center
width: 40%
---
*Sont affichées les destinations restantes possibles.*
```


Cela veut dire qu'à partir de la ville $1$, nous pouvons nous diriger vers la ville $2$, $3$ ou $4$. À partir de là, pour respecter la consigne du problème du voyageur de commerce, nous pouvons uniquement nous diriger vers les noeuds($=$ villes) sur lesquelles nous ne sommes pas déjà passés. Ainsi:


```{figure} figures/schema_4c.png
---
align: center
width: 50%
---
*Nous continuons à procéder de la même manière pour chaque noeud.*
```


Nous poursuivons le même processus jusqu'à ce que nous ayons visité chacune des villes. Nous obtenons enfin:


```{figure} figures/schema_4d.png
---
align: center
width: 50%
---
*Arbre de recherche complété.*
```


Afin de respecter les consignes du problème de voyageur de commerce, il est nécessaire de prendre encore en compte le trajet du retour afin d'avoir comme point d'arrivée le noeud initial.

### En résumé
Pour conclure, nous pouvons résumer l'arbre de la manière suivante:

Nous avons les villes $1$, $2$, $3$ et $4$. Nous partons d'une ville, définie provisoirement par $1$ (la longueur d'un trajet est aucunement influencée par le point de départ), que nous nommons le **nœud initial**. Nous avons alors trois possibilités de trajet, menant chacun à une des trois trois villes qui n'ont pas été visitée. Ces possibilités constituent les trois embranchements initiaux de l’arbre. Chacun des embranchements se sépare à son tour en deux embranchements pour les deux villes restantes (donc non-visitée), formant des nœuds possédant à nouveau des embranchements jusqu’à ce que cela ne soit plus possible. 


```{figure} figures/schema_5.png
---
align: center
width: 80%
---
*Voici à quoi ressemble un arbre de recherche fini.*
```


## Réaliser la PSE
À présent que cet arbre de recherche est formé et compris, il nous faut trouver le trajet optimal. C'est là que la PSE intervient.

### Etapes à réaliser
Le principe de la PSE est de couper l’exploration de l’arbre à la hauteur de certains nœuds afin de réduire la quantité nécessaire de calculs pour trouver la réponse. Pour savoir quand couper la simulation, nous procédons de la manière suivante :
1. Calculer la borne supérieure en suivant un chemin au hasard ou par un algorithme approché. Cette borne est fixe, mais peut toutefois être actualisée lorsqu'un trajet plus court que ladite borne a été décelé.
2. Explorer toutes les options pour le prochain embranchement, en calculant la borne inférieure pour chacune de ces options. Pour cela, on rajoute à la distance déjà parcourue les $x$ distances manquantes les plus courtes de l'embranchement.
3. Couper les embranchements dont la borne inférieure est supérieure ou égale à la borne supérieure.
4. Répéter les étapes 2, 3 et 4 jusqu'à ce que tous les embranchements soient complétés.
5. Trouver le chemin le plus court parmi les configurations restantes.

Cette méthode permet ainsi d'augmenter la rapidité des calculs, car permet de couper les branches inutiles à explorer. Cependant, ce n'est pas une méthode sufisamment efficace pour permettre de calculer le trajet optimal comportant le passage au travers d'un grand nombre de villes.

### Exemple

#### Situation initiale
Prenons les 3 villes suivantes ainsi que la distance les séparant:


```{figure} figures/schema_6.png
---
align: center
width: 70%
---
*Les points oranges représentes les villes à travers lesquels nous souhaitons passer.*
```

#### Création de l'arbre de recherche

On peut alors constuire l'arbre de recherche suivant:


```{figure} figures/schema_7.png
---
align: center
width: 60%
---
*L'arbre de recherche correspondant à la situation ci-dessus posée.*
```


Dans cette notation, les chiffres en gras représentent la distance (souvent nommé "coût") entre deux noeuds. À partir de là, nous pouvons suivre la procédure décrite plus haut.

#### Borne supérieure
Il faut tout d'abord calculer la borne supérieure. Pour Cela,