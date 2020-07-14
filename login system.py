users = {}
status = ""

def TheMenu():
    print(input("Es-tu inscrit [o/n] appuyez sur q pour quitter ?"))
    if status == 'o':
        OldUser()
    elif status == 'n':
        NewUser()    

def NewUser():
    create_login = input("Créez votre identifiant :\t")

if create_login in users:
    print("Nom d'utilisateur déjà prit !")
else:
    create_password = input("Créez votre mot de passe")
    users[create_login] = create_password
    print("Utilisateur crée !")

def OldUser():
    login = input("Rentrer votre identifiant")
    password = input("Rentrer votre mot de passe")

    if login in users and users[login] == password
    print("Utilisateur connecté !")
    else:
        print("Utilisateur non existant ou mot de passe faux.")

while status != "q":
    TheMenu()        


