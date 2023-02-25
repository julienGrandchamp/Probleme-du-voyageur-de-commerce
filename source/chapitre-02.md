# Résolution exacte

## Rappel du problème
William Rowan Hamilton posa l’une des première fois le problème du voyageur de commerce dès 1859 avec l’énoncé suivant : 

« Un voyageur de commerce doit visiter une et une seule fois un nombre fini de villes et revenir à son point d’origine. Trouvez l’ordre de visite des villes qui minimise la distance totale parcourue par le voyageur ».



## Méthode de résolution exacte naïve
Il est actuellement impossible de trouver une résolution exacte à ce problème pour un grand nombre de villes, car la complexité est exponentielle. Regardons cela ensemble par une approche de résolution exacte naïve, en pratiquant une recherche exhaustive de tous les chemins possibles :
1)	Posons n points, qui représentent des villes. 
2)	Il existe alors n! chemins possibles, car on ne peut passer qu’une seule fois dans chaque ville. 
3)	Le point de départ n’influençant pas la longueur totale du trajet, on se retrouve avec (n-1)! chemins différents. 
4)	Enfin, étant donné qu’on peut parcourir le chemin dans les deux sens sans modifier la longueur du trajet total, on peut diviser encore l’expression par deux. Par exemple, pour les quatre villes a,b,c,d, les paires de chemins abcd et dcba, cdab et badc, *etc.* ont la même longueur. 
Ainsi, on obtient 1/2 (n-1)!  chemins candidats à considérer pour obtenir la bonne réponse.


Le problème est que les résultats obtenus par l’expression mathématique 1/2 (n-1)! sont énormes compte tenu de la complexité du problème. Pour donner un exemple, pour un trajet comportant 71 villes, le nombre de chemins à comparer pour obtenir le plus court trajet est de 5*10^80 ! Cela devient très vite ingérable. 
Pour illustrer cela par un autre exemple, admettons qu’un ordinateur est capable d’évaluer un trajet en une demi-microseconde. Alors, le problème du voyageur avec 5 points est possible en 6 microsecondes, le cas avec 10 villes en 0,09 secondes, mais le cas à 20 villes prendrait 964 ans à être calculé ! On ne peut ainsi pas calculer des techniques parfaites pour trouver le meilleur trajet, mais il est possible d’approximer cette réponse par d’autres techniques demandant moins de ressources.



## Procédure par Séparation et Évaluation (PSE)
Cherchons à présent une méthode de résolution exacte un peu moins naïve et plus efficace. Pour cela, nous allons utiliser la procédure par Séparation et Évaluation, abrégée par les initiales PSE. C’est une méthode qui repose sur le parcours d’un arbre de recherche auquel on va couper la simulation dans certaines branches lorsqu’il est évident que ce n’est pas le chemin optimal. 

Avant cela, il est important de définir certains termes qui vont avoir leur importance dans l’application de cette méthode :
1)	Un arbre de recherche est un schéma représentant toutes les solutions possibles sous la forme d’embranchements. Par exemple, désignons les villes 1, 2, 3 et 4. Partons d’une première ville, que nous appelons « nœud initial » et que nous nommons 1. Nous avons alors trois possibilités de trajet, menant chacun aux trois villes restantes. Ces possibilités constituent les trois embranchements initiaux de l’arbre. Chacun des embranchements se sépare à son tour en deux embranchements pour les deux villes restantes, formant des nœuds possédant à nouveau des embranchements jusqu’à ce que cela ne soit plus possible. À ce moment-là, l’arbre de recherche est entièrement complété.




2)	Pour cette méthode, il est aussi important de définir les bornes inférieures et supérieures. 
Une borne inférieure est une valeur qui est égale ou inférieure à la valeur de la meilleure solution possible. Dans le cas présent, il suffit pour l’obtenir d’additionner le poids des N distances les plus proches entre deux villes. Même si cette solution a une grande probabilité de ne pas être réalisable, la valeur de la solution optimale ne pourra pas être plus petite que la borne inférieure. 
La borne supérieure, quant à elle, est une limite qu'aucune solution optimale ne pourra jamais dépasser. Dans ce cas, cette valeur est un trajet quelconque, car si on prend la mauvaise solution on obtient une valeur supérieure à celle qu’on recherche, et dans le cas généralement extrêmement rare où l’on obtient la bonne réponse, la bonne réponse n’est pas en-dessous de la borne supérieure choisie. Pour obtenir des résultats moins variables, on peut aussi utiliser des algorithmes approchés se basant sur des approximations.

Le principe de la PSE est de couper l’exploration de l’arbre à la hauteur de certains nœuds afin de réduire la quantité nécessaire de calculs pour trouver la réponse. Pour savoir quand couper la simulation, nous procédons de la manière suivante :
1)	À chaque nœud visité, nous calculons la borne inférieure en additionnant la somme des trajets déjà effectués et la somme des plus petits trajets restants. 
2)	La norme supérieure est établie au début de l’algorithme généralement à l’aide d’un algorithme approché décrit plus bas et reste fixe.
3)	À chaque nœud, nous regardons si la borne inférieure est supérieure ou non à la borne supérieure. Si tel est le cas, il est alors inutile de continuer l’embranchement et nous pouvons stopper les calculs relatifs à celui-ci. 

Cette méthode permet ainsi d'augmenter la rapidité des calculs, car permet de couper les branches inutiles à explorer. Cependant, ce n'est pas une méthode sufisamment efficace pour permettre de calculer le trajet optimal comportant le passage au travers d'un grand nombre de villes.
