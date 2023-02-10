from math import sqrt

def multi_matrice(matrice,size):
    """Retourne la martice au carré

    Args:
        matrice (list): tout les éléments de la matrice
        size (int): taille de ligne et de colonne de la matrice

    Returns:
        list: tout les éléments de la matrice au carré
    """
    multiplied = []
    for c in range(size):
        for l in range(size):
            num = 0
            for elt in range(size):
                num += matrice[elt+c*size] * matrice[elt*size+l]
            multiplied.append(num)
    return multiplied
    
def crypte_key(key):
    """Retrourne la clé crypté de maniere a ne pas que la clé soit décryptable

    Args:
        key (str): clé

    Returns:
        str: clé cryptée
    """
    matrice = []
    for letter in key:
        matrice.append(ord(letter))
    size_matrice = round(sqrt(len(matrice)))+1
    for _ in range(size_matrice**2-len(matrice)):
        matrice.append(0)
    matrice = multi_matrice(matrice,size_matrice)
    crypte = ''
    for code in matrice:
        crypte += chr(code%94+33)
    return crypte

def crypte_pwd(pwd,key):
    """Retourne le mot de passe crypté avec la clé

    Args:
        pwd (str): mot de passe
        key (clé): clé

    Returns:
        str: mot de passe crypté
    """
    crypte = []
    for i in range(len(pwd)):
        crypte.append(ord(pwd[i])*ord(key[i%len(key)]))
    return crypte

def uncrypte_pwd(pwd,key):
    """Retourne le mot de passe décrypté avec la clé

    Args:
        pwd (str): mot de passe
        key (clé): clé

    Returns:
        str: mot de passe décrypté
    """
    crypte = ''
    for i in range(len(pwd)):
        crypte += chr(int(pwd[i])//ord(key[i%len(key)]))
    return crypte

def write_pwd(website,pwd,file='password.txt'):
    """Inscrit le mot de passe et son site correspondant dans le fichier

    Args:
        website (str): site web du mdp
        pw (str): mot de passe crypté
        file (str, optional): fichier. Defaults to 'password.txt'.
    """
    f = open(file, 'a')
    write = website + ' : ' + '\n'
    f.write(write)
    for nb in pwd:
        write = str(nb) + '\n'
        f.write(write)
    f.close()

def get_key(file='password.txt'):
    """Retourne la clé inscrite dans le fichier

    Args:
        file (str, optional): fichier. Defaults to 'password.txt'.
    
    Returns:
        str: clé cryptée
    """
    f = open(file , 'r')
    key = f.readline().split('\n')
    f.close()
    return key[0]

def get_pwd(website,file='password.txt'):
    """Retourne le mot de passe correspondant au site

    Args:
        website (str): site web du mdp

    Returns:
        str: mot de passe crypté
    """
    f = open(file)
    fichier= f.readlines()
    f.close()
    pwd_trouve = False
    password = []
    for pw in fichier:
        pwd = pw.split('\n')[0]
        if pwd_trouve:
            if ' :' in pwd:
                break
            password.append(pwd)
        else :
            pwd = pwd.split(' ')
            if pwd != [] and website == pwd[0]:
                pwd_trouve = True
    return password
