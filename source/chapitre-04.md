# Méthodes de résolution approchée

## Rappel du problème
William Rowan Hamilton posa l’une des première fois le problème du voyageur de commerce dès 1859 avec l’énoncé suivant : 

> « Un voyageur de commerce doit visiter une et une seule fois un nombre fini de villes et revenir à son point d’origine. Trouvez l’ordre de visite des villes qui minimise la distance totale parcourue par le voyageur ».

# Méthode approchée
Comme nous l'avons aperçu plus tôt, le calcul exacte du trajet le plus optimal pour un grand nombre de villes est extrêmement gourmand en calculs. C'est pour cela qu'il existe, aujourd'hui, de nombreux algorithmes d'approximation. Chacun d'eux possède ses avantages et ses inconvénients, tels que le temps de calcul, la fiabilité des solutions, *etc*. 

Nous appelons donc **Méthodes approchées** les méthodes de calcul permettant d'approximer les solutions, *a contrario* des méthodes exactes donnant la réponse optimale mais qui demandent en général beaucoup plus d'énergie. 

Pour le problème du voyageur de commerce, il existe de nombreuses méthodes approchées, tels les algorithmes gloutons (comme la méthode par insertion ou l'algorithme du plus proche voisin), la méthode de l'élastique, l'algorithme de descente locale, l'algorithme du recuit simulé, la recherche tabou et bien d'autres encore. Nous pourrons évidemment pas tout traiter dans ce projet, c'est pourquoi nous allons plutôt nous concentrer sur l'algorithme de Prim, connu aussi sous le nome de **l'algorithme du plus proche voisin**.

## Algorithme de Prim (du plus proche voisin)

