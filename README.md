# UML-Projet-L3TD1G7

Projet UML L3 TD1 G7 2020

## Dépendances

* Python 3.5+
* PyGame 2 (pip install pygame)

## Lancement et Utilisation

* Installer les dépendances : pip install pygame
* Lancer le jeu : python .\UMLProjet.py
return self.__class__.__name__+"(L:{}, H:{}, S:{}, M:{}, P:{}, GP:{}, MM:{}, HS:{}, AC:{}, DC:{}, DOB:{})".format(self.life, self.hydration, self.satiety, self.mentality, self.position, self.go_position, self.movement_mode, self.has_swimsuit, self.arrest_count, self.diplomaCounter, self.diplomaObtainingBonus)

> **Note**: Au cours du jeu, les informations du personnage vont être affichés dans la console. Voici l'explication des noms :
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

> **Note**: Pour mettre en pause le jeu, appuyez sur P

> **Note**: Le jeu a deux arguments optionnels : la largeur et la taille de la map.

> **WARNING**: Attention, les mettre trop petits peuvent générer des soucis et les mettre trop grand, n'affichera pas toute la map.

## Fonctionnalités

* Trois classes personnages jouables
* Cinq bâtiments différents
* Cinq types de cases différents
* Sauvegarde possible via le menu pause
* Chargement possible via le menu principal
* Affichage fait via PyGame
* Génération Aléatoire de la map
* IA Simpliste
