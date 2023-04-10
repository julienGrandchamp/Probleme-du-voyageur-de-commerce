# Méthodes de résolution approchée

## Rappel du problème
William Rowan Hamilton posa l’une des première fois le problème du voyageur de commerce dès 1859 avec l’énoncé suivant : 

> « Un voyageur de commerce doit visiter une et une seule fois un nombre fini de villes et revenir à son point d’origine. Trouvez l’ordre de visite des villes qui minimise la distance totale parcourue par le voyageur ».

# Méthode approchée
Comme nous l'avons aperçu plus tôt, le calcul exacte du trajet le plus optimal pour un grand nombre de villes est extrêmement gourmand en calculs. C'est pour cela qu'il existe, aujourd'hui, de nombreux algorithmes d'approximation. Chacun d'eux possède ses avantages et ses inconvénients, tels que le temps de calcul, la fiabilité des solutions, *etc*. 

Nous appelons donc **Méthodes approchées** les méthodes de calcul permettant d'approximer les solutions, *a contrario* des méthodes exactes donnant la réponse optimale mais qui demandent en général beaucoup plus d'énergie. 

Pour le problème du voyageur de commerce, il existe de nombreuses méthodes approchées, tels les algorithmes gloutons (comme la méthode par insertion ou l'algorithme du plus proche voisin), la méthode de l'élastique, l'algorithme de descente locale, l'algorithme du recuit simulé, la recherche tabou et bien d'autres encore. Nous pourrons évidemment pas tout traiter dans ce projet, c'est pourquoi nous allons plutôt nous concentrer sur l'algorithme de Prim, connu aussi sous le nome de **l'algorithme du plus proche voisin**.

## Algorithme de Prim (du plus proche voisin)
'''python
import networkx as nx

# Crée un graphe vide
H= nx.Graph() 

# Ajoute des arêtes au graphe
H.add_edges_from([
    (1,2), 
    (1,3), 
    (3,2), 
    (1,6), 
    (3,5),
    (4,2),
    (2,3),
    (3,1),
    (4,0)])

# Dessine le graphe
nx.draw(H, with_labels=True, font_weight='bold')

# Pour chaque arête dans les 4 premières arêtes
for i in range(4):
    
    # Stocke les deux nœuds de l'arête
    (node1, node2) = list(H.edges)[i]
    
    # Ajoute l'arête (node1, node2) au graphe
    H.add_edge(node1, node2)
    
    # Si le graphe H contient un cycle, supprime l'arête (node1, node2) pour enlever le cycle
    if nx.cycle_basis(H) != []:
        H.remove_edge(node1,node2)

# Crée une liste des arêtes du graphe H et leurs poids
b = list(H.edges(data='weight'))

# Initialise le poids minimal à zéro
min_weight = 0

# Pour chaque arête de b
for i in range(len(b)):
    
    # Stocke les deux nœuds de l'arête et le poids de l'arête
    (src, dest, w) = b[i]
    
    # Ajoute le poids de l'arête au poids total de l'arbre couvrant minimal
    min_weight = min_weight + int(1)

# Affiche le poids total de l'arbre couvrant minimal
print("L'arbre couvrant minimal est ",min_weight)

