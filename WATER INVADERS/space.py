import pygame  # necessaire pour charger les images et les sons
import random
import math


class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.sens = "0"
        self.image = pygame.image.load("poisson.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.position = 400
        self.vitesse = 5
        self.score = 0
        
    def tirer(self):
        self.sens = "O"
        
    def deplacer(self):
        if self.sens == "droite" and self.position < 700:
            self.position += self.vitesse
        if self.sens == "gauche" and self.position > 20:
            self.position -= self.vitesse
            
    def marquer(self, ennemi):
        self.score += ennemi.point
            
        

class Balle():
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position + 80
        self.hauteur = 492
        self.image = pygame.image.load("bulles.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.etat = "chargee"
        self.vitesse = 10
        
    def bouger(self):
        if self.etat == "chargee":
            self.depart = self.tireur.position + 80
            self.hauteur = 492
        elif self.etat == "tiree":
            self.hauteur = self.hauteur - self.vitesse
        
        if self.hauteur < 0:
            self.etat = "chargee"
            
    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            self.etat = "chargee"
            return True
  
class Ennemi():
    NbEnnemis = 6
    
    def __init__(self):
        self.depart = random.randint(80,700)
        self.hauteur = 10
        self.type = random.randint(1,3)
        if self.type == 1:
            self.nom = 'poulpe'
            self.point = 15
            self.image = pygame.image.load("poulpe.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 1
        elif self.type == 2:
            self.nom = 'requin'
            self.point = 30
            self.image = pygame.image.load("requin.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 1.5
        elif self.type == 3:
            self.nom = 'bombe'
            self.point = -20
            self.image = pygame.image.load("bombe.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 0.5
    
    
    def avancer(self):
        self.hauteur += self.vitesse
            
    def disparaitre(self):
        self.depart = random.randint(80,700)
        self.hauteur = 10
        if self.type == 1:
            self.image = pygame.image.load("poulpe.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 1
        elif self.type == 2:
            self.image = pygame.image.load("requin.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 1.5
        elif self.type == 3:
            self.image = pygame.image.load("bombe.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 0.5
        
        
        

        
        
        
        