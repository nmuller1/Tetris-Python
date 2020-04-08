""" Projet 3 : Implémentation d'un tetris avec turtle"""

__author__ = "Noëmie Muller"
__matricule__ = "000458865"
__date__ = "27/11/2017"
__cours__ = "info-f-101"
__titulaire__ = "Thierry Massart"
__groupe_tp_ = "4"
__asistant__ = "Fabio Sciamannini"

import random
import turtle
import time

crayon_board, crayon_matrice, crayon_tetriminos, = turtle.Turtle(), turtle.Turtle(), turtle.Turtle()

barre = [[1,1,1,1],[0,0,0,0],'pink']
l_bleu = [[1,0,0,0],[1,1,1,0],'blue']
l_orange = [[0,0,1,0],[1,1,1,0],'orange']
carre = [[0,1,1,0],[0,1,1,0,0],'yellow']
s_vert = [[0,1,1,0],[1,1,0,0],'green']
s_rouge = [[1,1,0,0],[0,1,1,0],'red']
t = [[0,1,0,0],[1,1,1,0],'violet']

def Dessin_Carre(crayon,color = 'black') :
    """
    Dessine un carré avec le crayon correspondant.

    """
    crayon.fillcolor(color)
    crayon.begin_fill()
    for i in range(4) :
        crayon.forward(10)
        crayon.left(90)
    crayon.end_fill()

def TetrisBrick() :
    """
    Choisit la pièce suivante du jeu de manière random.

    """
    liste_tetriminos = [barre,l_bleu,l_orange,carre,s_vert,s_rouge,t]
    indice = random.randint(0,len(liste_tetriminos)-1) 
    """génère aléatoirement un indice de la liste des tetriminos et renvoie
    le tetriminos correspondant"""
    return liste_tetriminos[indice]

def CheckPlace() :
    """
    Vérifie qu'il y a de la place pour insérer le tetriminos en haut de la matrice
    et donc que le jeu n'est pas perdu.

    """
    obstacles = 0
    m = 0
    for i in range(0,2) : 
        n = 0
        for j in range(2,6) :
        #on passe en revue les 8 éléments de la matrice où va être spawn le tetriminos
            if tetriminos[m][n] == 1 and mat_board[i][j] != 0 :
                obstacles += 1
            #vérifie s'il n'y a pas déjà un bloc là où doit se placer chaque bloc du tétriminos
            n+=1
        m +=1
    if obstacles == 0 :
        res = True
    else :
        res = False
    return res  

def SpawnTetriminos() :
    """Spawn le tetriminos généré en haut de la matrice"""
    m = 0
    for i in range(2) : 
        n = 0
        for j in range(2,6) :
        #on passe en revue les 8 éléments de la matrice où va être spawn le tetriminos
            mat_board[i][j] = tetriminos[m][n]
            #on replace dans la matrice les 0 et 1 formant le tetriminos
            #les 1 representent les blocs du tetriminos en mouvement
            n += 1
        m += 1
    return mat_board

def Board() :
    """
    Initialise la grille du jeu.

    """
    crayon_matrice.reset()
    turtle.reset()
    turtle.title("Tetris")
    turtle.bgcolor("black") 
    turtle.setworldcoordinates(-120, 0, 120, 240)
    turtle.tracer(False)
    crayon_board.hideturtle() 
    crayon_board.pencolor("green") 
    for i in range(len(mat_board)) : #on trace un carré pour chaque élément de la matrice
        crayon_board.up()
        crayon_board.goto(-45.25,11.5*i)
        crayon_board.down()
        for j in mat_board[i] :
            Dessin_Carre(crayon_board)
            crayon_board.up()
            crayon_board.forward(11.5)
            crayon_board.down()
    turtle.update()

def DessinTetriminos() :
    """
    Dessine le tetriminos en mouvement.

    """
    crayon_tetriminos.reset()
    crayon_tetriminos.pencolor('black')
    crayon_tetriminos.hideturtle() 
    for i in range(len(mat_board)) :
        crayon_tetriminos.up()
        crayon_tetriminos.goto(-45.25,218.5-11.5*i)
        crayon_tetriminos.down()
        for j in range(len(mat_board[i])) : 
            if mat_board[i][j] == 1 :
                Dessin_Carre(crayon_tetriminos,tetriminos[2])
            #check toute la matrice et dessine un carré de la bonne couleur pour chaque 1 rencontré
            crayon_tetriminos.up()
            crayon_tetriminos.forward(11.5)
            crayon_tetriminos.down()
    turtle.update()

def DessinMatrice() :
    """
    Redessine toute la matrice avec les blocs placés.

    """
    crayon_matrice.reset()
    crayon_matrice.pencolor('black')
    crayon_matrice.hideturtle()
    for i in range(len(mat_board)) :
        crayon_matrice.up()
        crayon_matrice.goto(-45.25,218.5-11.5*i)
        crayon_matrice.down()
        for j in range(len(mat_board[i])) : 
        #check toute la matrice et dessine un carré de la bonne couleur pour chaque bloc rencontré
            if mat_board[i][j] != 0 :
                Dessin_Carre(crayon_matrice,mat_board[i][j])
            crayon_matrice.up()
            crayon_matrice.forward(11.5)
            crayon_matrice.down()
    turtle.update()

def CheckBordBas() :
    """ 
    Vérifie que le tetriminos n'est pas arrivé tout en bas de la crayon_matrice.

    """
    res = True
    for i in range(len(mat_board)) :
        for j in range(len(mat_board[0])) : 
        #check toute la matrice et vérifie que le tetriminos n'est pas sur la dernière ligne
            if mat_board[i][j] == 1 :
                if i == len(mat_board)-1 :
                    res = False
    return res

def CheckBordDroit() :
    """ 
    Vérifie que le tetriminos n'est sur le bord droit de la matrice.

    """
    res = True
    for i in range(len(mat_board)) :
        for j in range(len(mat_board[0])) : #check toute la matrice
        #check toute la matrice et vérifie que le tetriminos n'est pas sur la dernière colonne
            if mat_board[i][j] == 1 :
                if j == len(mat_board[i])-1 :
                    res = False
    return res

def CheckBordGauche() :
    """ 
    Vérifie que le tetriminos n'est sur le bord gauche de la matrice.

    """
    res = True
    for i in range(len(mat_board)) :
        for j in range(len(mat_board[0])) : #check toute la matrice
        #check toute la matrice et vérifie que le tetriminos n'est pas sur la première colonne
            if mat_board[i][j] == 1 :
                if j == 0 :
                    res = False
    return res

def CheckObstacleDessous() :
    """
    Vérifie qu'il n'y a pas d'obstacle en-dessous du tetriminos dans la matrice.

    """
    obstacles = 0
    for i in range(len(mat_board)) :
        for j in range(len(mat_board[0])) : #check toute la matrice
            if mat_board[i][j] == 1 :
                if mat_board[i+1][j] != 0 and mat_board[i+1][j] != 1  :
                #check si il y a un bloc sous chaque 1 qu'on rencontre
                #1 = blocs du tetriminos en mouvement
                #'couleur' = blocs des tetriminos posés
                    obstacles += 1
    if obstacles == 0 :
        res = True
    else :
        res = False
    return res

def Descente() :
    """
    Decrémente tous les blocs du tétriminos d'une ligne dans la matrice.

    """
    for i in range(len(mat_board)-1,-1,-1) :
        for j in range(len(mat_board[0])) : #check toute la matrice
            if mat_board[i][j] == 1 :
                mat_board[i+1][j] = 1 #on incrémente chaque 1 d'une ligne lorsqu'on en croise un
                mat_board[i][j] = 0

def CheckObstacleGauche() :
    """
    Vérifie qu'il n'y a pas d'obstacle à gauche du tetriminos dans la matrice.

    """
    obstacles = 0
    for i in range(len(mat_board)) :
        for j in range(len(mat_board[0])) : #check toute la matrice
            if mat_board[i][j] == 1 :
                if mat_board[i][j-1] != 0 and mat_board[i][j-1] != 1  :
                #check si il y a un bloc à gauche de chaque 1 qu'on rencontre
                #1 = blocs du tetriminos en mouvement
                #'couleur' = blocs des tetriminos posés
                    obstacles += 1
    if obstacles == 0 :
        res = True
    else :
        res = False
    return res

def CheckObstacleDroite() :
    """
    Vérifie qu'il n'y a pas d'obstacle à droite du tetriminos dans la matrice.

    """
    obstacles = 0
    for i in range(len(mat_board)) :
        for j in range(len(mat_board[0])) : #check toute la matrice
            if mat_board[i][j] == 1 :
                if mat_board[i][j+1] != 0 and mat_board[i][j+1] != 1  :
                #check si il y a un bloc à droite de chaque 1 qu'on rencontre
                #1 = blocs du tetriminos en mouvement
                #'couleur' = blocs des tetriminos posés
                    obstacles += 1
    if obstacles == 0 :
        res = True
    else :
        res = False
    return res

def MoveLeft() :
    """
    Déplace le tetriminos d'une colonne vers la gauche.

    """
    if CheckBordGauche() and CheckObstacleGauche() :
        for i in range(len(mat_board)) :
            for j in range(len(mat_board[0])) : #check toute la matrice
                if mat_board[i][j] == 1 :
                    mat_board[i][j-1] = 1 #on décrémente chaque 1 d'une colonne lorsqu'on en croise un
                    mat_board[i][j] = 0
        DessinTetriminos()
        time.sleep(0.001)

def MoveRight() :
    """
    Déplace le tetriminos d'une colonne vers la droite.

    """
    if CheckBordDroit() and CheckObstacleDroite() :
        for i in range(len(mat_board)) :
            for j in range(len(mat_board[0])-1,-1,-1) : #check toute la matrice
                if mat_board[i][j] == 1 :
                    mat_board[i][j+1] = 1 #on incrémente chaque 1 d'une colonne lorsqu'on en croise un
                    mat_board[i][j] = 0
        DessinTetriminos()
        time.sleep(0.001)

def Rotation() :
    """
    Effectue une rotation de 90° sur le tetriminos.

    """
    #à écrire...........

def Speed() :
    """
    Accélère la vitesse de chute du tetriminos.
    """
    global pause
    pause = 0

def NoSpeed() :
    """
    Rétablit à la normale la vitesse de chute du tetriminos.

    """
    global pause 
    pause = 0.5

def RunGame() :
    """
    Contient les controles liés aux flèches pour déplacer les tetriminos.

    """
    turtle.onkeypress(MoveLeft, "Left")
    turtle.onkeypress(MoveRight, "Right")
    turtle.onkeypress(Speed, "Down")
    turtle.onkeyrelease(NoSpeed, "Down")
    turtle.onkeypress(Rotation,"Up")

def Placement() :
    """
    Place définitivement le tétriminos à son dernier emplacement 
    en remplaçeant les 1 par la couleur du bloc.

    """
    for i in range(len(mat_board)) :
        for j in range(len(mat_board[0])) : 
        #check toute la matrice en partant du bas et transforme chaque 1 en bloc définitif 
        #(représenté par sa couleur)
            if mat_board[i][j] == 1 :
                mat_board[i][j] = tetriminos[2]

def CheckLine(ligne) :
    """
    Vérifie si une ligne est remplie.

    """
    i = 0
    while i < len(mat_board[ligne]) and mat_board[ligne][i] != 0 : 
        #passe la ligne en revue et vérifie qu'il n'y a que des zéros
        res = True
        i+=1
    if i != len(mat_board[ligne]) :
        res = False
    return res

def DecalageGrille(ligne = 0) :
    """
    Supprime la ligne complétée et décale d'une ligne tous les blocs au-dessus.

    """
    for i in range(ligne,-1,-1):
        for j in range(len(mat_board[i])):
            mat_board[i][j] = mat_board[i-1][j] 
    #on décrémente d'une ligne tous les éléments de la matrice au-dessus de la ligne complétée
    mat_board[0] = [0 for i in range(len(mat_board[0]))]

def DisplayResult(lignes=0) :
    """
    Affiche le nombre final de lignes completées.

    """
    turtle.hideturtle()
    turtle.tracer(0)
    turtle.pensize(4)
    turtle.pencolor("white")
    turtle.fillcolor("#2C3130")
    turtle.up()
    turtle.goto(-60,155)
    turtle.setheading(0)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(120)
    turtle.setheading(270)
    turtle.forward(65)
    turtle.setheading(180)
    turtle.forward(120)
    turtle.setheading(90)
    turtle.forward(65)
    turtle.end_fill()
    turtle.up()
    turtle.goto(-20,130)
    turtle.pencolor("white")
    turtle.write(lignes, font = ("Arial", 30, "normal"))
    turtle.up()
    turtle.goto(-5,130)
    turtle.write("Rows !", font = ("Arial", 30, "normal"))
    turtle.goto(-35,115)
    turtle.write("New game : Enter 1", font = ("Arial", 18, "normal"))
    turtle.goto(-25,105)
    turtle.write("Quit : Enter 2", font = ("Arial", 18, "normal"))
    time.sleep(1)
        
if __name__ == "__main__" :
    NewGame = 1
    while NewGame == 1 :
        mat_board = [[0 for i in range(8)] for i in range(20)]
        KeepPlaying = 1
        Board()
        RunGame()
        rows = 0
        pause = 0.5 
        while KeepPlaying == 1 : #tant que le jeu n'est pas perdu
            turtle.listen()
            tetriminos = TetrisBrick()
            if CheckPlace() :
                SpawnTetriminos()
                DessinTetriminos()
                while CheckBordBas() and CheckObstacleDessous() : 
                #tant qu'on n'a pas atteint le bord et qu'il n'y a pas d'obstacle
                    Descente()
                    DessinTetriminos()
                    time.sleep(pause)
                Placement()
                DessinMatrice()
                for i in range(len(mat_board)) :
                    if CheckLine(i) :
                        rows += 1
                        DecalageGrille(i)
                DessinMatrice()
            else :
                KeepPlaying = 0
                DisplayResult(rows)
                NewGame = int(turtle.numinput('New Game','Do you want to replay ? 1 = yes, 2 = no'))
                while NewGame != 1 and NewGame != 2 :
                    NewGame = int(turtle.numinput('New Game','Do you want to replay ? 1 = yes, 2 = no'))
