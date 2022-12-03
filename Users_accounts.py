import hashlib
import sqlite3
import http.cookies
import os
import chemin as c

Chemin = c.chemin()
base = sqlite3.connect(Chemin)

## Hacheur de password (Fait entrer un string et ressort celui-ci hacher en sha512):
def Hachage(string):
    Hacheur = hashlib.sha512()
    ch = f'b {string}'
    Hacheur.update(ch.encode('utf-8'))
    return Hacheur.hexdigest()

## Fonction creatrice de compte dans la base de données (Fait entrer toutes les données nécessaires pour un compte sur Playsic et retourne True si le compte est bien créer):
def Create(user_prenom, user_nom, user_birth, user_country, user_pw, user_genre):
    pointeur = base.cursor()
    pw = Hachage(user_pw)
    ch = f'INSERT INTO Users(FamilyName,FirstName,Pass_Word,DateofBirth,Gender,Country) VALUES("{user_nom}","{user_prenom}","{pw}","{user_birth}","{user_genre}","{user_country}");'
    pointeur.execute(ch)
    base.commit()
    return True

## Fonction qui permet a un utilisateur de se connecter (Elle fait une comparaison des hachage de password) (Fait entrer le prenom, le nom et le pw de l'utilisateur et retourne si oui ou non l'utilisateur existe et qu'il peut se connecter):
def Login(prenom,nom,pw):
    pointeur = base.cursor()
    ch = f'SELECT FamilyName,FirstName,Pass_Word,IdUser FROM Users WHERE FamilyName = "{nom}" and FirstName = "{prenom}";'
    list = pointeur.execute(ch)
    list = list.fetchall()
    user_pw = Hachage(pw)
    for n in list:
        if user_pw == n[2]:
            return n[3]
    return False

## Fonction qui met en place des cookies (Fait entrer la liste des clés nécessaires aux cookies et une autre liste avec toutes les données correspondantes. Elle retourne le cookie à print avec CGI):
def Cookie_Create(liste_key,liste_données):
    my_cookie = http.cookies.SimpleCookie()
    for i in range(len(liste_key)):
        x = liste_key[i]
        y = liste_données[i]
        ch = f'{x}'
        my_cookie[ch] = y
        my_cookie[ch]["expires"] = +3600
    return print(my_cookie.output())

## Fonction qui modifie des cookies (Fait entrer la liste des clés nécessaires aux cookies et une autre liste avec toutes les données correspondantes. Elle retourne le cookie modifié à print avec CGI):
def Cookie_Modif(liste_key,liste_données):
    for i in range(0,len(liste_key)):
        my_cookie = http.cookies.SimpleCookie()
        my_cookie[liste_key[i]] = liste_données[i]
    return print(my_cookie.output())

## Fonction qui modifie la base de données (Fait entrer l'ID de l'utilisateur, la table dans laquelle va se faire la modification et deux listes. La 1ere liste contient les entités de la table et l'autre contient les valeurs correspondantes):
def modif_BDD(Table,Id,liste_key,liste_données):
    pointeur = base.cursor()
    for i in range(0,len(liste_key)):
        ch = f'UPDATE {Table} SET {liste_key[i]} = "{liste_données[i]}" WHERE IdUser = "{Id}";'
        pointeur.execute(ch)
        base.commit()

def modif_BDD2(Table,Id,key,données):
    pointeur = base.cursor()
    ch = f'UPDATE {Table} SET {key} = "{données}" WHERE IdUser = "{Id}";'
    pointeur.execute(ch)
    base.commit()

## Fonction qui fait de la prise d'informations dans un cookie (Fait entrer la clé du cookie demandé et retourne la valeur du cookie si elle existe):
def Informations_Cookies(key):
    key = str(key)
    try:
        cookie_value = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
        cookie_value = cookie_value[key].value
        return cookie_value
    except(http.cookies.CookieError, KeyError):
        return None

## Fonction qui permet la suppression de cookie (Fait entrer une liste de clé des cookies à supprimer. Elle retourne le cookie modifié à print avec CGI):
def Delete_Cookie(liste_key):
    for key in liste_key:
        ch = f'{key}'
        my_cookie = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
        my_cookie[ch] = None
        my_cookie[ch]["expires"] = "Thu, 01, Jan 1970 00:00:00 GMT"
    return print(my_cookie.output())

## Fonction qui fait de la prise d'information spécifique dans la base de données:
def Information_BDD(table,recherche,Id,string):
    pointer = base.cursor()
    ch = f'SELECT {recherche} FROM {table} WHERE {string} = "{Id}";'
    liste = pointer.execute(ch)
    liste = liste.fetchall()
    if liste == []:
        return None
    return liste[0][0]

## Fonction qui fait de la prise d'informations dans la base de données:
def Informations_BDD(table,recherche,string):
    result = "%"
    for lettre in string:
        result += f"{lettre}%"
    string = result
    pointer = base.cursor()
    ch = f'SELECT {recherche} FROM {table} WHERE {recherche} like "{string}";'
    liste = pointer.execute(ch)
    liste = liste.fetchall()
    result = []
    for i in liste:
        for y in i:
            result.append(y)
    return result
