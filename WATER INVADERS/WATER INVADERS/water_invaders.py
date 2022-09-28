import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init()

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Water Invaders") 
# chargement de l'image de fond
fond = pygame.image.load('mer.jpg')
fond = pygame.transform.scale(fond, (800, 600))
fond2 = pygame.image.load('accueil.PNG')
fond2 = pygame.transform.scale(fond2, (800, 600))
musique = pygame.mixer.music.load("musiquebob.mp3")
bulle = pygame.mixer.Sound("bullesbruit.mp3")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

# creation du joueur
player = space.Joueur()
# creation de la balle
tir = space.Balle(player)
tir.etat = "chargee"
# creation des ennemis
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
    
### BOUCLE DE JEU  ###
running = False # variable pour laisser la fenêtre ouverte
a = True

while a :
    screen.blit(fond2, (0, 0))
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.KEYDOWN:  # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_SPACE:
                a= False# si la touche est la barre espace
                running= True
                pygame.mixer.music.play()
    pygame.display.update()

while running : # boucle infinie pour laisser la fenêtre ouverte
    if player.score < 300 and player.score >= 0:
        # dessin du fond
        screen.blit(fond,(0,0))
        # affichage du score
        text = font.render(f"Score = {player.score} points", 1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.left = 10
        textpos.top = 10
        screen.blit(text, textpos)
        
        # affichage du score à atteindre
        text1 = font.render("Score à atteindre : 300", 1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.left = 500
        textpos.top = 10
        screen.blit(text1, textpos)
        
        # texte pour indiquer que le score a dépassé 300 points
        text2 = font.render("BRAVOOOO", 1, (255, 255, 255))
        
        # texte pour indiquer que le score est négatif
        text3 = font.render("GAME OVER", 1, (255, 255, 255))
        
        # texte pour bouton rejouer
        text4 = font.render("Press space to restart or enter to quit", 1, (255, 255, 255))
        
        # texte pour bouton quitter
        # text5 = font.render("Quitter??", 1, (255, 255, 255))
        
        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                sys.exit() # pour fermer correctement
           
           # gestion du clavier
            if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
                if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                    player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
                if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                    player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
                if event.key == pygame.K_SPACE : # espace pour tirer
                    player.tirer()
                    tir.etat = "tiree"

        ### Actualisation de la scene ###
        # Gestions des collisions
        for ennemi in listeEnnemis:
            if tir.toucher(ennemi):
                ennemi.disparaitre()
                player.marquer(ennemi)
                bulle.play()
        print(f"Score = {player.score} points")

        # placement des objets
        # le joueur
        player.deplacer()
        screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur        
        # la balle
        tir.bouger()
        screen.blit(player.image,[player.position,500]) # appel de la fonction qui dessine le vaisseau du joueur
        # les ennemis
        for ennemi in listeEnnemis:
            ennemi.avancer()
            screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
        
        
        for ennemi in listeEnnemis:
                ennemi.avancer()
                screen.blit(ennemi.image,
                            [ennemi.depart, ennemi.hauteur])  # appel de la fonction qui dessine le vaisseau du joueur
                if ennemi.hauteur > 600:
                    ennemi.disparaitre()
                    ennemi.avancer()
                    if ennemi.nom == 'requin' or ennemi.nom == 'poulpe':
                        player.score -= 10

            
    else:
        
        mouse = pygame.mouse.get_pos()
        click_quitter=  620 <= mouse[0] <=  720 and 540 <= mouse[1] <= 580  # bouton quitter
        click_rejouer=  340 <= mouse[0] <=  440 and 300 <= mouse[1] <= 340  # bouton rejouer
        
        if player.score >= 300 :
            screen.blit(text2, (320,250))
            screen.blit(text4, (180,300))
            # screen.blit(text5, (620,540))
            # if event.type == pygame.MOUSEBUTTONDOWN: 
                # if click_rejouer:
                    # player.score = 0
                # elif click_quitter:
                    # running = False
                    # sys.exit()
        
        if player.score < 0 :
            screen.blit(text3, (320,250))
            screen.blit(text4, (180,300))
            if event.type == pygame.KEYDOWN:  # si une touche a été tapée KEYUP quand on relache la touche
                if event.key == pygame.K_SPACE:  # si la touche est la barre espace
                    running = False
                    screen.blit(fond2, (0, 0))
                    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
                        if event.type == pygame.KEYDOWN:  # si une touche a été tapée KEYUP quand on relache la touche
                            if event.key == pygame.K_SPACE:
                                a= False# si la touche est la barre espace
                                running= True
                                pygame.mixer.music.play()
                    pygame.display.update()
            # screen.blit(text5, (620,540))
            # if event.type == pygame.MOUSEBUTTONDOWN:
                # if click_rejouer:
                    # player.score = 0
                # elif click_quitter:
                    # running = False
                    # sys.exit()
                    
    clock.tick(60)
    pygame.display.update() # pour ajouter tout changement à l'écran
