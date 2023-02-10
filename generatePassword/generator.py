import random

def stringOfPossibilites(up = True, num = True, spe = False, space = False):
    """Renvois la chaine de caractère de tout les caractères possible en fonction des paramètres

    Args:
        up (bool, optional): True si les Majuscules sont autorisées. Defaults to True.
        num (bool, optional): True si les chiffres sont autorisés. Defaults to True.
        spe (bool, optional): True si les caractères spéciaux sont autorisés. Defaults to False.
        space (bool, optional): True si les espaces sont autorisés. Defaults to False.

    Returns:
        str : chaine de tous les caractères possibles
    """
    chaine = "abcdefghijklmnopqrstuvxyz"
    if up:
        chaine += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num:
        chaine += "0123456789"
    if spe:
        chaine += "@!?./-_+*"
    if space:
        chaine += " "
    return chaine

def generator(numOfCaracters,up = True, num = True, spe = False, space = False):
    """Créé un mot de passe avec les paramètres

    Args:
        numOfCaracters (int): nombre de caractère du mot de passe
        up (bool, optional): True si les Majuscules sont autorisées. Defaults to True.
        num (bool, optional): True si les chiffres sont autorisés. Defaults to True.
        spe (bool, optional): True si les caractères spéciaux sont autorisés. Defaults to False.
        space (bool, optional): True si les espaces sont autorisés. Defaults to False.

    Returns:
        str: mot de passe aléatoire
    """
    password = ""
    chaine = stringOfPossibilites(up,num,spe,space)
    alea = random.SystemRandom()
    for _ in range(numOfCaracters):
        password += chaine[alea.randint(0,len(chaine))-1]
    return password
