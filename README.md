# UML-Projet-L3TD1G7

Projet UML L3 TD1 G7 2020

## Dépendances

* Python 3.5+
* PyGame 2 (pip install pygame)

## Lancement et Utilisation

* Installer les dépendances : pip install pygame
* Lancer le jeu : python .\UMLProjet.py

Au cours du jeu, les informations du personnage vont être affichés dans la console. Voici l'explication des noms :

* L : Vie
* H : Hydratation
* S : Satiété
* M : Mentalité
* P : Position du personnage
* GP : Position où le personnage veut aller
* MM : Mode de mouvement (0 - Pied, 1 - Vélo, 2 - Voiture)
* HS : True si le personnage a un maillot de bain
* AC : Nombre d'arrestation
* DC : Nombre de diplomes
* DOB : Bonus d'obtention de diplome

Touches pour jouer :

* P : Mettre en pause le jeu
* Flèches : Déplacements

> **Note**: Le jeu a deux arguments optionnels : la largeur et la taille de la map. Exemple : python .\UMLProjet.py 4 6

> **WARNING**: Attention, les mettre trop petits peuvent générer des soucis (il faut minimum 5 cases) et les mettre trop grand, n'affichera pas toute la map (maximum 18 pour n et 14 pour m). Nous recommandons une map de 5 par 5 (valeurs par défaut)

## Fonctionnalités

* Trois classes personnages jouables
* Cinq bâtiments différents
* Cinq types de cases différents
* Sauvegarde possible via le menu pause
* Chargement possible via le menu principal
* Affichage fait via PyGame
* Génération Aléatoire de la map
* Déplacements par le joueur
