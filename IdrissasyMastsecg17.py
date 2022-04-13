"""
Demander et afficher information d'un électeur
"""

# Afficher informations personnes

def afficher_informations_personne(nom, age):
    print()
    print("Vous vous appelez " + nom + ", Vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age + 1) + " ans")


    if age >= 18:
        print("Vous êtes majeur, vous êtes électeur ")
    else:
        print("Vous êtes mineur, vous ne pouvez pas voter")


# Deffinition des fonctions


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR: Vous devez rentrez un nombre pour l'age ")
    return age_int


# Appel des Fonctions

# Demander les noms

nom1 = demander_nom()
nom2 = demander_nom()

# nom = ""
# while nom == "":
#     nom = input("Quel est votre nom ? ")

# Demander les ages


age1 = demander_age(nom1)
age2 = demander_age(nom2)

# age = 0
# while age == 0:
#     age_str = input("Quel est votre age ? ")
#     try:
#         age = int(age_str) + 1
#     except:
#         print("ERREUR: Vous devez rentrez un nombre pour l'age ")


# Afficher les informations


afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)


# print("Vous vous appelez " + nom1 + ", Vous avez " + str(age1) + " ans")
# print("L'an prochain vous aurez " + str(age1 + 1) + " ans")
#
#
# print("Vous vous appelez " + nom2 + ", Vous avez " + str(age2) + " ans")
# print("L'an prochain vous aurez " + str(age2 + 1) + " ans")

"""
  Boucle whie pour exiger d'entrer un nombre
"""

