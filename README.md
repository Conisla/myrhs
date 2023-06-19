# myrhs
My RH Solution

Ce projet est une application web pour gérer une liste de salariés. Il permet de visualiser, créer, mettre à jour et supprimer des salariés à partir d'une interface conviviale.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre machine :

- Node.js (version X.X.X)
- npm (version X.X.X)
- python (version X.X.X)

## Installation

1. Clonez ce dépôt sur votre machine en utilisant la commande suivante :

   ```shell
   git clone https://github.com/Conisla/myrhs.git

2. Mettre en place la BDD
  Dans pgAdmin créer une database 'myrh' et créer la table salarie comme ceci :
     ```shell
   CREATE TABLE salarie(
   id_salarie INT,
   first_name VARCHAR(50),
   last_name VARCHAR(50),
   phone_number VARCHAR(50),
   email VARCHAR(50),
   email_personnal VARCHAR(50),
   gender VARCHAR(50),
   PRIMARY KEY(id_salarie )
   );

3. Creer un environnement virtuel
   ```shell
    cd myrhs
    py venv -m .env
    .env\Scripts\activate
    
4. Lancer l'API
   ```shell
   pip install -r requirements.txt
    cd back
    py manage.py makemigrations
    py manage.py migrate
    py manage.py runserver

4. Lancer le front
   ```shell
    cd front
    npm i
    npm run serve

