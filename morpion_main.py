from upemtk import *
from time import sleep
import doctest



def grille():
    largeur_fenetre = 300
    hauteur_fenetre = 300
    cote = hauteur_fenetre/ 3
    cree_fenetre(largeur_fenetre, hauteur_fenetre)

    for i in range(0,3):
        for j in range(0,3):
            rectangle(cote*j,cote*i,cote+cote*j,cote+cote*i)

    

def affiche_grille():
    j1ouj2 = jouer(tours)
    i,j, x, y = numero_case_clic()
    if grilles[i][j] != "vide":
        return False
    
    else:
        if j1ouj2:
            grilles[i][j] = "croix"
            ligne(j*100+25, i*100+25, j*100+75, i*100+75,epaisseur=4)
            ligne(j*100+25, i*100+75, j*100+75, i*100+25, epaisseur=4)
            mise_a_jour()
            return True
        
        else:
            grilles[i][j] = "rond"
            cercle(j*100+50, i*100+50, 30,epaisseur=4)
            mise_a_jour()
            return True


def numero_case_clic():
    x, y, _ = attente_clic()
    j,i = x // 100 , y//100
    
    return i,j,x,y

def jouer(tours):
    """
    >>> tours = 8
    >>> jouer(tours)
    Au tour du joueur 1 de jouer
    True
    >>> tours
    8
    >>> jouer(9)
    Au tour du joueur 2 de jouer
    False
    >>> jouer(0)
    Au tour du joueur 1 de jouer
    True
    """
    if tours % 2 ==0:
        print("Au tour du joueur 1 de jouer")
        return True
    else:
        print("Au tour du joueur 2 de jouer")
        return False


def est_pleine():
    plein = 0
    for lignes in grilles:
        if "vide" not in lignes:
            plein+=1
    if plein == 3:
        return True


def est_finie():

    Gagne = False
#-------------------Teste si un joueur a gagné--------------------#
    if grilles[0][0] == grilles[0][1] == grilles[0][2] != "vide": #Ligne 1

        Gagne = True
    elif grilles[1][0] == grilles[1][1] == grilles[1][2] != "vide": #Ligne 2

        Gagne = True
    elif grilles[2][0] == grilles[2][1] == grilles[2][2] != "vide": #Ligne 3

        Gagne = True
    elif grilles[0][0] == grilles[1][0] == grilles[2][0] != "vide": #colonne 1

        Gagne = True
    elif grilles[0][1] == grilles[1][1] == grilles[2][1] != "vide": #colonne 2

        Gagne = True
    elif grilles[0][2] == grilles[1][2] == grilles[2][2] != "vide": #colonne 3

        Gagne = True
    elif grilles[0][0] == grilles[1][1] == grilles[2][2] != "vide": #Diagonale 1

        Gagne = True
    elif grilles[0][2] == grilles[1][1] == grilles[2][0] != "vide": #Diagonale 2

        Gagne = True
        
#------Print quel joueur a gagné et retourne que la partie est terminée-------#
    if Gagne:
        if jouer(tours):
            print("Le joueur 2 (ronds) a gagné !")
            print("*******************************\nFermeture dans 10 sec\n*******************************")
            
            return True
        else:
            texte(150,150,"Fin de la partie",couleur="black",taille='10')
            print("Le joueur 1 (croix) a gagné !")
            print("*******************************\nDouble clic pour fermer\n*******************************")
            return True
        

if __name__ == "__main__":
    
    grilles = [["vide","vide","vide"],["vide","vide","vide"],["vide","vide","vide"]]
    grille()
    tours = 0
    print("*******************************\nLe joueur 1 utilise les croix\n*******************************")
    print("Le joueur 2 utilise les ronds\n*******************************")


    while True:
        

        if affiche_grille() == False:
            print("*******************/!\ Erreur /!\*******************")
            print("La case est déjà prise ! \n Changez de case pour continuer !")
            print("*****************************************************")
            tours-=1
        tours += 1

        if est_finie():
            attente_clic()
            attente_clic()
            break
        if est_pleine():
            if est_finie():
                sleep(10)
                break
            print("Egalité personne n'a gagné \n Fin du jeu dans 10 sec")
            sleep(10)
            break
