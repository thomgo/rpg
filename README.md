# Application de jeu rpg type Donjons et Dragons pour terminal en python orienté objet

Il s'agit d'une application développée dans le cadre de mon poste de formateur en programmation et plus particulièrement pour l'élaboration d'un programme d'apprentissage du python. L'objectif est que les apprenants produisent une application intégrant des concepts de POO intermédiaire qui simule le célèbre jeux Donjons et Dragons sans interface graphique.

Au travers de cet exercice, ils apprennent à :
- Utiliser l'héritage
- Utiliser et redéfinir des méthodes spéciales
- Utiliser les attributs et les méthodes de classe
- Utiliser les décorateurs existants
- Organiser leur code
- Prendre en compte l'utilisateur final dans la production de l'application

## Consignes

Développeur python junior, vous venez d'intégrer une start-up novatrice qui prévoit de révolutionner le jeu de plateau. Son objectif ? Proposer une version informatisée du célèbre jeu Donjons et Dragons qui connaît un succès grandissant.

Vous avez été embauché afin de développer une première mouture implantant les mécaniques de base du jeu avant que votre équipe ne soit renforcée par de nouveaux développeurs et que vous puissiez produire un POC.

Attention cependant, vous êtes jeune et avez tout l'avenir devant vous, vous ne savez donc pas si vous resterez longtemps dans l'entreprise surtout avec le nombre d'offres d'emploi sur le marché. Vous devrez donc produire un code clair et maintenable qu'un éventuel remplaçant sera capable de reprendre sans difficultés. Vous l'aurez compris votre application sera développée en respectant les bonnes pratiques de Python et plus précisément de la POO.

Spécifications fonctionnelles :
- Le joueur peut choisir le type de personnage qu'il souhaite incarner
- Trois classes sont disponibles pour le joueur (guerrier, archer, magicien)
- Le joueur peut nommer son personnage comme il le désire au début du jeu
- Trois classes sont disponibles pour les ennemis (orc, loup, zombie)
- Les personnages ont tous au minimum les caractéristiques suivantes (vie, attaque, défense, agilité, nom)
- Le magicien dispose en plus de mana représentant sa force magique
- Un personnage peut en attaquer un autre, la cible perd alors de la vie en proportion de sa valeur de défense et de la valeur d'attaque de l'assaillant
- Le magicien peut se soigner. Ce sort consomme du mana mais lui redonne de la vie. S'il n'a pas assez de mana, il ne peut pas le lancer
- Un combat est simulé entre le personnage du joueur et un ennemi de votre choix jusqu'à ce que l'un ou l'autre des personnages soit mort. Assurez de tester que la méthode soin du magicien soit fonctionnelle

Spécifications techniques :
- Langage Python 3
- Organisation du code en modules et packages
- Usage de la programmation orientée objet
- Respect du principe DRY
- Essayer de respecter certains des principes SOLID
- Programme exécutable par le lancement d'un fichier main.py

## Pour aller plus loin

Vous pouvez par la suite essayer de transformer votre application en un jeu partiellement fonctionnel. Vous pouvez par exemple rajouter les fonctionnalités suivantes :
- Un narrateur qui raconte une histoire pour donner de la profondeur à votre jeu
- Des temps de pause et de transition pour donner du rythme à votre histoire
- Une console interactive pour les combats, autrement dit, le joueur peut choisir lui-même l'action à exécuter (attaquer, se soigner...) et le combat ne se poursuit pas tant qu'il n'a pas choisi
- Rajouter une méthode fuite qui offre aux personnages une faible chance de quitter le combat sans se battre
- Afficher en temps réel les informations de chaque protagoniste du combat (sa vie et éventuellement son mana si c'est un magicien)
- S'assurer que l'utilisateur ne puisse pas rentrer de commandes non-prévues ou lancer une action qui n'appartient pas à sa classe. Par exemple un archer ne peut pas lancer un sort de soin.
