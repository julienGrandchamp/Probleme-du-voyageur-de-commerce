# Résolution exacte naïve

## Rappel du problème
William Rowan Hamilton posa l’une des première fois le problème du voyageur de commerce dès 1859 avec l’énoncé suivant : 

> « Un voyageur de commerce doit visiter une et une seule fois un nombre fini de villes et revenir à son point d’origine. Trouvez l’ordre de visite des villes qui minimise la distance totale parcourue par le voyageur. »



## Méthode de résolution exacte naïve
Il est actuellement impossible de trouver une méthode de résolution exacte raisonnable à ce problème pour un grand nombre de villes, car la complexité est de $O(n!)$, ce qui devient vite ingérable. Regardons cela ensemble par une approche de résolution exacte naïve, en pratiquant une recherche exhaustive de tous les chemins possibles.

### Résolution intuitive du problème
1.	Posons $n$ points, qui représentent des villes. 


```{figure} figures/schema_1.png
---
align: center
width: 50%
---
*Emplacement des différentes villes.*
```


2.	Il existe alors $n!$ chemins possibles, car on ne peut passer qu’une seule fois dans chaque ville.

3.	Le point de départ n’influençant pas la longueur totale du trajet, on se retrouve avec $(n-1)!$ chemins différents. À noter que le trajet consistant à retourner au point de départ étant unique et obligatoire, nous ne le prenons pas en compte en tant que possibilité de chemin ici.


```{figure} figures/schema_2.png
---
align: center
width: 60%
---
*Explication visuelle de la manière dont nous obtenons $(n-1)!$ chemins différents.*
```


4.	Enfin, étant donné qu’on peut parcourir le chemin dans les deux sens sans modifier la longueur du trajet total, on peut diviser encore l’expression par deux. Par exemple, pour les quatre villes $A,B,C,D$, les paires de chemins $A B C D$ et $D C B A$, $C D A B$ et $B A D C$, *etc.* ont la même longueur. 
Ainsi, on obtient $\frac{(n-1)!}{2}$  chemins candidats à considérer pour obtenir la bonne réponse.


```{figure} figures/schema_3.png
---
align: center
width: 60%
---
*Nous pouvons observer que les deux chemins opposés du schéma possèdent la même distance. Ceci est naturellement valable pour tout trajet opposé.*
```


### Problème de cette pratique
Le problème est que les résultats obtenus par l’expression mathématique $\frac{(n-1)!}{2}$ sont énormes compte tenu de la complexité du problème. Pour donner un exemple, pour un trajet comportant $71$ villes, le nombre de chemins à comparer pour obtenir le plus court trajet est de $5\cdot 10^{80}$ ! Cela devient très vite ingérable. 

Pour illustrer cela par un autre exemple, admettons qu’un ordinateur est capable d’évaluer un trajet en une demi-microseconde. Alors, le problème du voyageur avec $5$ points est possible en $6$ microsecondes, le cas avec $10$ villes en $0.09$ secondes, mais le cas avec $20$ villes prendrait $964$ ans à être calculé ! C'est pourquoi nous n'appliquons pas des algorithmes de résolution exacte dans les milieux industriels, mais plutôt des approximations de la réponse recherchée par d’autres techniques demandant moins de ressources.



