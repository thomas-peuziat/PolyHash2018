## HashCode 2018 - City Plan

#### Membres de l'équipe 'Pandiculation' :
* Couty Killian
* Gauducheau Clément
* Peuziat Thomas


### Descriptif général du projet
Le but général du projet est d'optimiser le placement de bâtiments dans une ville.
La ville est représentée par une matrice vierge. Il faut donc placer un maximum de résidences, possédant un certain nombre
d'habitants, à côté de bâtiments utilitaires différents (boulangerie, supermarché, pharmacie...).


#### Partage des tâches :

Scoring -> Killian<br/>
Parser -> Thomas<br/>
Structure de données (classes + méthodes) -> Clément<br/>
Solver random -> Thomas<br/>
Optimisation scoring -> Killian, Clément<br/>
Recherches (algorithmes existants) -> Killian, Thomas, Clément<br/>
Implémentation de la solution finale -> Killian, Thomas, Clément<br/>


### Procédure d'installation 
Pour installer notre projet, il suffit de le télécharger depuis la plateforme de GitLab.<br/>
NB: Penser à installer les bibliothèques nécéssaires (cf: Rubrique "Bibliothèques nécéssaires" ci-dessous)


### Procédure d'exécution
Pour exécuter, il faut lancer la programme 'main.py'. Dans ce fichier, il faut spécifier le nom du fichier
contenant les projets urbains que vous voulez utiliser. Puis la méthode par laquelle vous voulez faire l'optimisation du placement.<br/>
<br/>
Exemple : <br/>
trials_max = 1000000<br/>
error_max = 1000000<br/>
generation_max = 8<br/>
filename = "a_example"<br/>

solver.random_solver_solution(filename, trials_max, error_max)<br/>
OU <br/>
solver.advanced_random_solver_solution(filename, trials_max, error_max)<br/>
OU <br/>
solver.elitist_solver_solution(filename, error_max, generation_max)<br/>



### Détail de la stratégie mise en oeuvre
Notre stratégie principale est un algorithme élitiste.<br/>
Tout d'abord, on effectue un placement aléatoire des bâtiments lors d'une première génération.
Puis, on ré-utilise les meilleures configurations pour générer de nouvelles solutions.
Une configuration comprend 1 Résidence et les Utilitaires placés autour permettant de gagner des points. 
Pour cela, il faut calculer les meilleures configurations : on divise le score que nous rapporte la configuration par sa taille dans la ville ce qui nous donne une densité de point.
Une fois le score de toutes les configurations trouvé, on les trie et on ne garde que les 'n' premières
 ('n' étant calculé grâce à la génération actuelle, le nombre de génération maximale et le nombre de configurations dans la matrice).

### Performances

|         Maps          |     Score      |   Temps d'exécution |
| :-------------------: |: ------------: | :-----------------: |
| a_example             |     125        |      1 min          |
| b_short_walk          |     1 304 539  |      24 H           |
| c_going_green         |     4 784 885  |      24 H           |
| d_wide_selection      |     3 055 729  |      24 H           |
| e_precise_fit         |     3 830 455  |      24 H           |
| f_different_footprints|     1 227 733  |      24 H           |


### Description de l'organisation du code
Le code est organisé en différents package.<br/>
'Model' contient le modèle de données, ici c'est donc les classes 'Project' (super-classe de 'Utility' et 'Residential') et la classe 'CityPlan'.<br/>
Ensuite, on trouve le package 'utils' qui contient le 'parser' (gestion des inputs et outputs), 'scoring' qui permet d'effectuer le calcul du score et 'solver' qui contient nos trois algorithmes d'optimisations.
Enfin, le dossier 'data' contient deux sous-dossiers, un pour les inputs et l'autre pour les outputs.<br/>

### Bugs et limitations connues
A ce jour, nous avons repéré un problème lors de l'utilisation de l'algorithme élitiste. En effet, il y a plusieurs générations de créées et parfois le calcul du score sur une génération est incorrect.


#### Bibliothèques nécéssaires

* numpy 1.15.2
* scipy 1.1.0
* Pillow 5.3.0