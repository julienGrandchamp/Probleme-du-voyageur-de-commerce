# Résolution exacte

## Rappel du problème
William Rowan Hamilton posa l’une des première fois le problème du voyageur de commerce dès 1859 avec l’énoncé suivant : 

> « Un voyageur de commerce doit visiter une et une seule fois un nombre fini de villes et revenir à son point d’origine. Trouvez l’ordre de visite des villes qui minimise la distance totale parcourue par le voyageur ».



## Méthode de résolution exacte naïve
Il est actuellement impossible de trouver une résolution exacte à ce problème pour un grand nombre de villes, car la complexité est exponentielle. Regardons cela ensemble par une approche de résolution exacte naïve, en pratiquant une recherche exhaustive de tous les chemins possibles :
1.	Posons $n$ points, qui représentent des villes. 
```{figure} schema_1.png
---
align: center
width: 50%
---
```
2.	Il existe alors $n!$ chemins possibles, car on ne peut passer qu’une seule fois dans chaque ville. 
3.	Le point de départ n’influençant pas la longueur totale du trajet, on se retrouve avec $(n-1)!$ chemins différents. 
```{figure} schema_2.png
---
align: center
width: 60%
---
```
4.	Enfin, étant donné qu’on peut parcourir le chemin dans les deux sens sans modifier la longueur du trajet total, on peut diviser encore l’expression par deux. Par exemple, pour les quatre villes a,b,c,d, les paires de chemins abcd et dcba, cdab et badc, *etc.* ont la même longueur. 
Ainsi, on obtient $\frac{(n-1)!}{2}$  chemins candidats à considérer pour obtenir la bonne réponse.
```{figure} schema_3.png
---
align: center
width: 60%
---
```

Le problème est que les résultats obtenus par l’expression mathématique $\frac{(n-1)!}{2}$ sont énormes compte tenu de la complexité du problème. Pour donner un exemple, pour un trajet comportant $71$ villes, le nombre de chemins à comparer pour obtenir le plus court trajet est de $5\cdot 10^{80}$ ! Cela devient très vite ingérable. 
Pour illustrer cela par un autre exemple, admettons qu’un ordinateur est capable d’évaluer un trajet en une demi-microseconde. Alors, le problème du voyageur avec $5$ points est possible en $6$ microsecondes, le cas avec $10$ villes en $0.09$ secondes, mais le cas à $20$ villes prendrait $964$ ans à être calculé ! On ne peut ainsi pas calculer des techniques parfaites pour trouver le meilleur trajet, mais il est possible d’approximer cette réponse par d’autres techniques demandant moins de ressources.



## Procédure par Séparation et Évaluation (PSE)
Cherchons à présent une méthode de résolution exacte un peu moins naïve et plus efficace. Pour cela, nous allons utiliser la **Procédure par Séparation et Évaluation**, abrégée par les initiales **PSE**. C’est une méthode qui repose sur le parcours d’un arbre de recherche auquel on va couper la simulation dans certaines branches lorsqu’il est évident que ce n’est pas le chemin optimal. 

### Différentes définitions
Avant cela, il est important de définir certains termes qui vont avoir leur importance dans l’application de cette méthode :
1.	Un **arbre de recherche** est un schéma représentant toutes les solutions possibles sous la forme d’embranchements. Un exemple de cet arbre se situe plus bas.
2.	Pour cette méthode, il est aussi important de définir les bornes inférieures et supérieures.

    Une **borne inférieure** est une valeur qui est égale ou inférieure à la valeur de la meilleure solution possible. Dans le cas présent, il suffit pour l’obtenir d’additionner le poids des $N$ distances les plus proches entre deux villes. Même si cette solution a une grande probabilité de ne pas être réalisable, la valeur de la solution optimale ne pourra pas être plus petite que la borne inférieure. 

    La **borne supérieure**, quant à elle, est une limite qu'aucune solution optimale ne pourra jamais dépasser. Dans ce cas, cette valeur est un trajet quelconque, car si on prend la mauvaise solution on obtient une valeur supérieure à celle qu’on recherche, et dans le cas généralement extrêmement rare où l’on obtient la bonne réponse, la bonne réponse n’est pas en-dessous de la borne supérieure choisie. Pour obtenir des résultats moins variables, on peut aussi utiliser des algorithmes approchés se basant sur des approximations.


### Lecture d'un arbre de recherche
Regardons à présent l'arbre de recherche ci-dessous et tentons de le comprendre.

```{figure} schema_4.png
---
align: center
width: 60%
---
```

Nous avons les villes $1$, $2$, $3$ et $4$. Nous partons d'une ville, défini provisoirement par $1$ (la longueur d'un trajet est aucunement influencée par le point de départ). Nous appelons $1$ le **nœud initial**. Nous avons alors trois possibilités de trajet, menant chacun aux trois villes restantes. Ces possibilités constituent les trois embranchements initiaux de l’arbre. Chacun des embranchements se sépare à son tour en deux embranchements pour les deux villes restantes, formant des nœuds possédant à nouveau des embranchements jusqu’à ce que cela ne soit plus possible. 
```{figure} schema_5.png
---
align: center
width: 80%
---
```
À présent que cet arbre de recherche est formé et compris, il nous faut trouver le trajet optimal. C'est là que la PSE intervient.


Le principe de la PSE est de couper l’exploration de l’arbre à la hauteur de certains nœuds afin de réduire la quantité nécessaire de calculs pour trouver la réponse. Pour savoir quand couper la simulation, nous procédons de la manière suivante :
1. Calculer la borne supérieure en additionnant toutes les distances et en multipliant par deux (car il faut revenir au point de départ). Cette borne est fixe.
2. Calculer la borne inférieure en additionnant la distance entre la ville de départ et la ville la plus proche.
3. Explorer toutes les options pour le prochain embranchement, en calculant la borne inférieure pour chacune de ces options.
4. Couper les embranchements dont la borne inférieure est supérieure ou égale à la borne supérieure.
5. Répéter les étapes 3, 4 et 5 jusqu'à ce qu'il ne reste qu'une seule ville non visitée.
6. Trouver le chemin le plus court parmi toutes les configurations restantes.

Cette méthode permet ainsi d'augmenter la rapidité des calculs, car permet de couper les branches inutiles à explorer. Cependant, ce n'est pas une méthode sufisamment efficace pour permettre de calculer le trajet optimal comportant le passage au travers d'un grand nombre de villes.

## Exemple
Prenons les 3 villes suivantes ainsi que la distance les séparant:
```{figure} schema_6.png
---
align: center
width: 70%
---
```
On peut alors constuire l'arbre de recherche suivant:
```{figure} schema_7.png
---
align: center
width: 60%
---
```