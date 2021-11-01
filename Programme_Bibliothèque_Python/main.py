
rom = []
nbRoms = 0
CONST = 3
nom = []
developpeur = []
parution = []
poids = []
console = []


def menu():
    print(" Bibliothèque ")
    print(" 1-Afficher la bibliothèque des jeux ")
    print(" 2-Ajouter un jeu ")
    print(" 3-Rechercher un jeu ")
    print(" 4-supprimer un jeu ")
    print(" 0-Quitter le programme ")


def afficheBibli(nbRoms):
    nb = 0
    if nbRoms == 0:
        print("Aucune Rom dans la bibliotheque.\n")
    else:
        for i in range(nbRoms):
            nb += 1
            afficheRom(i)

        print("\n Votre bibliothèque contient : ", nb, "Roms sur les 100 possibles. \n")


def afficheRom(id):
    print("\nNom : ", nom[id])
    print("Developpeur : ", developpeur[id])
    print("Annee de parution : ", parution[id])
    print("Poids : ", poids[id])


def rechercheRom(nbRoms, chaine):
    pos = -1
    pasTrouve = True
    mot = chaine.upper()
    i = 0

    while i < nbRoms and pasTrouve:

        mot2 = nom[i].upper()

        if mot2 == mot:
            pos = i
            pasTrouve = False

        i = i + 1

    return pos


def ajouterRom(nbRoms):
    if nbRoms > CONST:
        print("Impossible, la liste est pleine")
    else:
        nom.append((input("Entrer un nom de jeu (sans espace ) : ")))
        developpeur.append(input("Entrer le nom du developpeur (sans espace ) : "))
        parution.append(input("Entrer l'annee de parution du jeu : "))

        poidsTemp = int(input("Entrer le poid du jeu (en Ko) : "))

        while poidsTemp < 1:
            poidsTemp = (input(" Erreur de saisie (il faut que le poids du jeu soit positif et supérieur à zéro). \n Entrer le poids du jeu : "))

        nbRoms += 1
        poids.append(poidsTemp)
        return (nbRoms)

def supprimerRom(nbRoms, sup):

    rep = str(input(" Voulez vous supprimer? ( entrer oui ou non) : "))

    while rep != "oui" and rep != "non":

        print(" Erreur de saisie, saisisez soit oui soit non ")
        rep_string = str(input(" Voulez vous supprimer? ( entrer oui ou non) : "))


    if rep == "oui":
        del nom[sup]
        del developpeur[sup]
        del parution[sup]
        del poids[sup]
        nbRoms -= 1
        print("Rom supprimée !")
    else:
        print("Rom non suprimée !")

    return nbRoms

if __name__ == '__main__':

    print("Bibliothèque")

    choix = '6'

    while choix != '0':

        menu()
        choix = input("Entrez votre choix :")

        if choix == '1':
            afficheBibli(nbRoms)
        if choix == '2':
            nbRoms = ajouterRom(nbRoms)
        if choix == '3':
            maChaine = str(input("Veuillez saisir le nom du jeu a rechercher : "))
            id = rechercheRom(nbRoms,maChaine)
            if id != -1:
                afficheRom(id)
            else:
                print("Le nom de Rom que vous cherchez n'existe pas.")
        if choix == '4':
            maChaine = str(input("Veuillez saisir le nom du jeu a supprimer : "))
            id = rechercheRom(nbRoms, maChaine)
            if id != -1:
                nbRoms = supprimerRom(nbRoms, id)
            else:
                print("Le nom de Rom que vous voulez supprimer n'existe pas.")
        if (choix != '1') and (choix != '2') and (choix != '3') and (choix != '4') and (choix != '0'):
            print("C'est pas le bon chiffre.")