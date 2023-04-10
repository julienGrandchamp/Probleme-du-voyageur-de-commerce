# Méthode de résolution exacte par la PSE

## Rappel du problème
William Rowan Hamilton posa l’une des première fois le problème du voyageur de commerce dès 1859 avec l’énoncé suivant : 

> « Un voyageur de commerce doit visiter une et une seule fois un nombre fini de villes et revenir à son point d’origine. Trouvez l’ordre de visite des villes qui minimise la distance totale parcourue par le voyageur. »

## Introduction
Cherchons à présent une méthode de résolution exacte un peu moins naïve et plus efficace. Pour cela, nous allons utiliser la **Procédure par Séparation et Évaluation**, abrégée par les initiales **PSE** et nommé **branch & bound** en anglais. C’est une méthode qui repose sur le parcours d’un arbre de recherche auquel nous allons couper la simulation dans certaines branches lorsqu’il est évident que ce n’est pas le chemin optimal. 

## Notions de base
Avant cela, il est important de définir certains termes qui vont avoir leur importance dans l’application de cette méthode :
1.	Un **arbre de recherche** est un schéma représentant toutes les solutions possibles sous la forme d’embranchements. Un exemple de cet arbre se situe plus bas.
2.	Pour cette méthode, il est aussi important de définir les bornes inférieures et supérieures.

    Une **borne inférieure** est une valeur qui est égale ou inférieure à la valeur de la meilleure solution possible. Dans le cas présent, il suffit pour l’obtenir d’additionner au trajet déjà effectué le poids des $N$ distances les plus proches entre deux villes. Même si cette solution a une grande probabilité de ne pas être réalisable, la valeur de la solution optimale ne pourra pas être plus petite que la borne inférieure. 

    La **borne supérieure**, quant à elle, est une limite qu'aucune solution optimale ne pourra jamais dépasser. Dans ce cas, cette valeur est un trajet quelconque, car nous obtenons dans la très grande majorité des cas (pour un grand nombre de ville) une valeur supérieure à celle qu’on recherche. Dans le cas généralement extrêmement rare où nous obtenons la bonne réponse, ce n'est pas un problème car cette dernière n’est pas en-dessous de la borne supérieure choisie. Pour obtenir des résultats moins variables, nous pouvons aussi utiliser des algorithmes approchés se basant sur des approximations.


## Formation d'un arbre de recherche
Posons la situation suivante: 


```{figure} figures/schema_4.png
---
align: center
width: 50%
---
*Admettons que nous souhaitons parcourir de la manière la plus optimale possible les quatre villes affichées.*
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


Cela veut dire qu'à partir de la ville $1$, nous pouvons nous diriger vers la ville $2$, $3$ ou $4$. À partir de là, pour respecter la consigne du problème du voyageur de commerce, nous pouvons uniquement nous diriger vers les noeuds ($=$ villes) sur lesquelles nous ne sommes pas déjà passés. Ainsi:


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

Nous avons les villes $1$, $2$, $3$ et $4$. Nous partons d'une ville, définie provisoirement par $1$ (la longueur d'un trajet est aucunement influencée par le point de départ), que nous nommons le **nœud initial**. Nous avons alors trois possibilités de trajet, menant chacun à une des trois trois villes qui n'ont pas été visitée. Ces possibilités constituent les trois embranchements initiaux de l’arbre. Chacun des embranchements se sépare à son tour en deux embranchements pour les deux villes restantes (donc non-visitées), formant des nœuds possédant à nouveau des embranchements jusqu’à ce que cela ne soit plus possible. 


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
2. Explorer toutes les options pour le prochain embranchement, en calculant la borne inférieure pour chacune de ces options. Pour cela, nous rajoutons à la distance déjà parcourue les $x$ distances manquantes les plus courtes de l'embranchement.
3. Couper les embranchements dont la borne inférieure est supérieure ou égale à la borne supérieure.
4. Répéter les étapes 2, 3 et 4 jusqu'à ce que tous les embranchements soient complétés.
5. Trouver le chemin le plus court parmi les configurations restantes.

Cette méthode permet ainsi d'augmenter la rapidité des calculs, car elle permet de couper les branches inutiles à explorer. Cependant, ce n'est pas une méthode sufisamment efficace pour permettre de calculer le trajet optimal comportant le passage au travers d'un grand nombre de villes.

### Exemple

#### Situation initiale
Prenons les 3 villes suivantes ainsi que la distance les séparant:


```{figure} figures/schema_6.png
---
align: center
width: 70%
---
*Les points oranges représentent les villes à travers lesquelles nous souhaitons passer.*
```

#### Création de l'arbre de recherche

On peut alors constuire l'arbre de recherche suivant:


```{figure} figures/schema_7.png
---
align: center
width: 80%
---
*L'arbre de recherche correspondant à la situation ci-dessus posée.*
```


Dans cette notation, les chiffres en gras représentent la distance (souvent nommé "coût") entre deux noeuds. À partir de là, nous pouvons suivre la procédure décrite plus haut.

#### Borne supérieure
Il faut tout d'abord calculer la borne supérieure. Pour cela, prenons un chemin au hasard. Disons A,B,C,D et A. Nous avons alors $3+5+2.6+1=11.6$m. Le chemin optimal ne pourra pas être au dessus de cette limite arbitrairement fixée à $11.6$m.

#### Calculer le prochain embranchement
Dans le cadre de cet exemple, nous allons seulement calculer le trajet A, B, D, C, et A. Cependant, il est nécessaire pour la résolution de ce problème de parcourir tous les trajets possibles, ce qui demanderait beaucoup de temps. 

Nous devons calculer la borne inférieure en additionnant à la distance entre A et B ($=$ 3m) les 3 valeurs minimales présentes dans cet embranchement (car nous avons 4 villes moins le B). Ainsi, la borne inférieure vaut $3+2.5+1+2=8.5$m.

#### Comparer les bornes
De cette manière, nous observons que la borne supérieure $>$ la borne inférieure car $11.6$m $>$ $8.5$m. Nous ne pouvons par conséquent pas rejeter cet embranchement. Nous devons donc poursuivre les démarches.

#### Calculer le prochain embranchement
Nous sommes au noeud B du premier embranchement. Nous devons calculer la borne inférieure de l'embranchement menant à la ville D. Nous avons parcouru A, B, D. Il nous reste deux villes à parcourir. 

Borne inférieure $=$ distance parcourue + distance minimale

Borne inférieure $= 3+2.5+1+2 = 8.5$m

#### Comparer les bornes
La borne supérieure est plus grande que la borne inférieure car $11.6\text{m}>8.5\text{m}$. Nous ne pouvons pas couper la simulation pour cette branche.

#### Calculer le prochain embranchement
Nous avons parcouru A, B, D. Nous nous dirigeons à présent vers C. La borne inférieure vaut la distance AB + BD + DC + la distance minimale existante. Nous obtenons alors $3+2.5+2.6+1=9.1$m

#### Comparer les bornes
$9.1\text{m}<11.6\text{m}$, par conséquent nous poursuivons les calculs. 

#### Longueur totale du trajet ABDCA
Nous prenons le dernier chemin restant, qui consiste à revenir au point de départ (et qui est par définition unique). Ainsi, le trajet vaut $3+2.5+2.6+2=10.1\text{m}$. Ce résultat ne nous sert à rien à présent, car il nous faut calculer tous les embranchements pour pouvoir le comparer aux trajets potentiellement optimaux obtenus, afin de savoir si le trajet ABDCA est le plus court possible ou non. En l'occurence, ce chemin est le plus optimal avec son inverse, ACDBA.