# Project Mini Magasin - Outils scolaires 

### Projet outils libres pour developpement logiciel
#### Application desktop Python pour gérer les produits et les achats de manière interactive via la console

L'objectif de ce travail pratique est de créer un programme de gestion des achats pour tester l'accès aux données et les
enregistrer dans un format à l'aide de différents outils libres.

Programme qui vous permet de contrôler les ventes d'un supermarché, ainsi que l'entrée dans l'entrepôt de celui-ci.

Chaque produit est identifié par un nom, une quantité en stock et un prix.

Le magasin vend 10 types de produits différents qui sont: cahier, stylo, gomme, crayon ciseaux, compas, surligneurs,
 equerre et rapporteur. Chaque produit est vendu individuellement.
  
Le programme utilise le paradigme de la programmation orientée objet en Python et répond aux exigences suivantes:

1. Ajouter un produit au magasin
2. Modifier l'existence du produit
3. Afficher les produits
4. Rapport de produits en faible stock
5. Obtenez un design flexible

#### Présentation du projet

1. [Structure du programme](#1)
2. [Avant de commencer](#2)
3. [Création de bases de données et de tables](#3)
4. [Exécution](#4)
5. [Opération](#5)
6. [Fonctionnalités en développement](#6)
7. [Liste des modifications](#7)


### <a name="1"></a> Structure du programme

xxx

##### Persistance des données

L'application utilise deux méthodes de persistance des données.

* Une base de données SQLite dans laquelle se trouve une table: MAGASIN. Grâce aux fonctions implémentées dans le fichier controller.py, nous pouvons gérer les informations. La base de données et les informations qu'elle contient seront conservées même si nous terminons l'exécution du programme.

* Fichiers texte .TXT où sont stockées les informations de l'achat à effectuer et qui sont exécutées lors de la sélection de «Charge Receipt et puis Validate.


### <a name="2"></a>Antes de empezar

Pour exécuter l'application, la première chose que vous devez installer sur votre système est Python. Vous pouvez installer la dernière version via:

* [Télécharger à partir du Web Python]( https://www.python.org/downloads/).

L'étape suivante consiste à télécharger les fichiers depuis ce repositoire ou par la console. Pour cela, vous avez besoin du code suivant:

```sh
~$ sudo apt-get install git
~$ git clone https://github.com/Sarouule/ProjetGestionDeStock.git
```
