CREATE DATABASE IF NOT EXISTS magasin_informatique;
USE magasin_informatique;

CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    email VARCHAR(150) UNIQUE,
    password VARCHAR(255),
    adresse VARCHAR(255),
    telephone VARCHAR(20)
);

CREATE TABLE produits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    description TEXT,
    prix DECIMAL(10,2),
    stock INT,
    image VARCHAR(255)
);

CREATE TABLE commandes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_client INT,
    date_commande DATE,
    total DECIMAL(10,2),
    statut VARCHAR(50),
    FOREIGN KEY (id_client) REFERENCES clients(id)
);

CREATE TABLE details_commandes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_commande INT,
    id_produit INT,
    quantite INT,
    prix_unitaire DECIMAL(10,2),
    FOREIGN KEY (id_commande) REFERENCES commandes(id),
    FOREIGN KEY (id_produit) REFERENCES produits(id)
);