# jeux-de-la-vie
programme du jeu de la vie par convolution

Le programme suivant est une simulation du jeux de la vie. 
Il s'agit d'un automate cellulaire inventé par John Horton Conway en 1970.  Il s'agit d'un jeux de simulation à zéro joueur. 
Le but est de voir l’évolution d'un groupe de cellule sur une grille en fonction de deux règles relativement simple. Il y a donc trois possibilité, pour chaque case de la grille :  la survie d'une cellule déjà présente, la mort d'une cellule, ou la naissance d'une cellule. Ces événements se font selon les règles suivantes : Si une case a exactement trois cellules vivante voisine, alors la cellule vie ( ou elle apparaît s'il n'y en a pas). Si la cellule à strictement moins de deux voisines ou strictement plus de trois voisines alors elle meurt ( soit par isolement soit par étouffement)). 
Ce qui est remarquable par ce jeu simple c'est que les simulations fonts apparaître de nombreuses structures.  on peut trouver des structures stables, des structures périodiques, des structures vaisseaux ou mathusalems, les puffers, les canons, les jardin d'Eden ainsi que les spacefillers ...

Ainsi pour effectuer cette simulation, on considère un tableaux formé de case blanc ( valeurs à 0) et de case noir ( valeurs à 1) qui représentent le motif de départ c'est à dire les cellules vivantes.  Pour chaque cellules il faut regarder le voisinage , c'est à dire les 9 cellules adjacentes. 
L'on peu trouver de nombreux algorithmes de simulations relativement complexes. Le programme suivant que je propose en est un parmi tant d'autre, cependant il est très simplifier en calcules. En effet afin de s’émanciper de double boucle pour vérifier les conditions liés au voisinages, je propose d'effectuer la conditions en sommant les valeurs des pixels voisins par une convolution avec le filtre suivant F : [[1,1,1][1,0,1][1,1,1]]. Ainsi on obtient une matrice de la taille de notre tableaux qui contient en chaque case, la sommes des cellules vivantes autours. Ce qui permet ainsi d’affecter directement les valeurs 0 ou 1 pour faire évoluer le tableau. Ainsi la simulation par le calcule tensoriel est  plus rapide qu'une vérification itérative des conditions à chaque cellules du tableau. 


la simulation permet de tester le premier motif qui conrrespond a trois cellules collé en ligne, on oberserve que le motif et stable périodiquement. 
le deuxieme motif tester est un canon. Il génère des projectiles qui s'en vont à l'infini
![Figure_1-1](https://user-images.githubusercontent.com/58695529/88132078-d3835800-cbde-11ea-8295-553c7a52e243.png)
