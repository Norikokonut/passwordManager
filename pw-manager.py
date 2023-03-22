import encryptPassword.api as api
import os
import generatePassword.generator as generator
import pyperclip

def affiche_menu(options):
    """Print un menu avec comme option les arguments

    Args:
        options (list): option possibles du menu
    """
    maxi = len(max(options,key=len))
    print('╔════'+"═"*maxi+'════╗')
    print("║    "+' '*maxi+"    ║")
    indice = 1
    for option in options:
        print('║   '+str(indice)+'.'+option+' '*(maxi-len(option))+'   ║')
        indice+=1
    print("║    "+' '*maxi+"    ║")
    print('╚════'+"═"*maxi+'════╝')

def main():

    key_crypte = api.get_key()
    key = ' '

    while True:
        key = input('Quel est la clé ? ')
        if api.crypte_key(key) != key_crypte:
            print('Mot de passe incorrect')
        else:
            print('Mot de passe correct')
            break

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        affiche_menu(['Ajouter un mot de passe','Générer un mot de passe','Chercher un mot de passe','Quitter'])
        option = input('Que souhaitez vous faire ? ')

        if option.isdigit() and 0<int(option)<5:
            option=int(option)

            if option == 1:
                website = input('Quel est le site ? ')
                pwd = api.crypte_pwd(input('Quel est le mot de passe ? '),key)
                api.write_pwd(website,pwd)

            elif option == 2:
                carac = " "
                while type(carac) is str:
                    carac = input("Quel est le nombre de caractère de votre mot de passe ? ")
                    if carac.isdecimal():
                        carac = int(carac)
                up = input("Autorisez vous les majuscules ? (y/n) ") != "n"
                num = input("Autorisez vous les chiffres ? (y/n) ") != "n"
                spe = input("Autorisez vous les caractère spéciaux ? (y/n) ") == "y"
                space = input("Autorisez vous les espaces ? (y/n) ") =="y"
                pyperclip.copy(generator.generator(carac,up,num,spe,space))
                print(pyperclip.paste())
                print('le mot de passe à été copier dans le presse papier')

            elif option == 3:
                website = input('Quel est le site ? ')
                pwd = api.uncrypte_pwd(api.get_pwd(website),key)
                if pwd == '':
                    print('Aucun mot de passe pour ce site ')
                else:
                    print(pwd)

            elif option == 4:
                break

        input('Entrer pour continuer ')

main()