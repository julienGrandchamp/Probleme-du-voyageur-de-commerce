# Définition, histoire et utilité

Le problème est nommé pour la première fois dès 1832 dans un manuel à destination de commis voyageurs. Il est ensuite repris par William Rowan Hamilton, qui posa ce problème sous la forme d’un jeu dès 1859 avec l’énoncé suivant : 

« Un voyageur de commerce doit visiter une et une seule fois un nombre fini de villes et revenir à son point d’origine. Trouvez l’ordre de visite des villes qui minimise la distance totale parcourue par le voyageur ». 

Il est ensuite repris par de nombreux mathématiciens et informaticiens, qui l’étudient encore à ce jour.

Ce problème a permis plusieurs évolutions mathématiques, comme l’optimisation linéaire mixte – ou, en anglais, mixed integer programming – et la méthode de séparation et évaluation. Nous ne reviendrons cependant pas sur la première de ces notions dans le cadre de notre projet. 

De manière très théorique, nous avons trouvé de 
nombreux domaines où ce problème pourrait être appliqué. Pour donner quelques exemples, la résolution du problème du commis voyageur pourrait résoudre avec exactitude de nombreux problèmes de logistique, de transport de marchandises ou de personnes, et même dans le monde de l'industrie. En effet, la réponse à ce problème pourrait théoriquement optimiser le fonctionnement des machines, comme percer plusieurs points sur une carte électronique le plus rapidement possible en réduisant au maximum les trajets à effectuer. Cependant, ceci n'apporterait aucune révolution dans ces domaines dans la "vraie vie", car il existe actuellement des algorithmes extrêmement efficaces visant à approximer lesdits trajets optimaux. Le réel intérêt de la résolution de ce problème repose sur ses implications théoriques, notamment au niveau du problème millénaire de Riemann, 
$$P=NP$$
. Cependant, les liens qu'entretiennent le problème du commis voyageur avec l'hypothèse de Riemann ne figureront pas en détails dans ce projet.



```{figure} /workspace/Probleme-du-voyageur-de-commerce/source/arbre_recherches.png
---
align: center
width: 100%
---
légende
```