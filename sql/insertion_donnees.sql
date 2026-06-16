USE magasin_informatique;

INSERT INTO clients (nom, prenom, email, password, adresse, telephone) VALUES
('KOFFI', 'Yves', 'client@test.com', '1234', 'Paris', '0600000001'),
('DUPONT', 'Marie', 'marie@test.com', '1234', 'Lyon', '0600000002');

INSERT INTO produits (nom, description, prix, stock, image) VALUES
('PC Portable Dell', 'Ordinateur portable professionnel', 750.00, 10, 'pc.jpg'),
('Souris Logitech', 'Souris sans fil USB', 25.00, 50, 'souris.jpg'),
('Clavier HP', 'Clavier AZERTY filaire', 30.00, 40, 'clavier.jpg'),
('Écran Samsung 24 pouces', 'Écran Full HD', 140.00, 15, 'ecran.jpg');

INSERT INTO commandes (id_client, date_commande, total, statut) VALUES
(1, '2026-06-02', 775.00, 'validée'),
(2, '2026-06-02', 170.00, 'en cours');

INSERT INTO details_commandes (id_commande, id_produit, quantite, prix_unitaire) VALUES
(1, 1, 1, 750.00),
(1, 2, 1, 25.00),
(2, 3, 1, 30.00),
(2, 4, 1, 140.00);