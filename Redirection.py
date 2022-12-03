# coding: utf-8

import cgi
import sys
import codecs
import Users_accounts as UA
import module_playlist as MP
import sqlite3 as s
import chemin as c

Chemin = c.chemin()
base = s.connect(Chemin)

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


form = cgi.FieldStorage()
page = form.getvalue("page")
cookie = None
iduser = UA.Informations_Cookies("Id")
redirection = None

## Redirection après la page Home
if page == None:
    Id = UA.Informations_Cookies("Id")
    if Id != None:
        UA.Cookie_Create(["Id","First_Name","Name"],[Id,UA.Informations_Cookies("First_Name"),UA.Informations_Cookies("Name")])
        redirection = """<script>
    window.onload = function(){
    window.location.href = "Bin/Site/Html/User.html";
    }
</script>
"""
    else:
        redirection = """<script>
    window.onload = function(){
    window.location.href = "Bin/Site/Html/Login.html";
    }
</script>
"""

## Redirection après la page login
if page == "login":  
    First_Name = form.getvalue("First_Name")
    Name = form.getvalue("Name")
    Password = form.getvalue("Password")
    login = UA.Login(First_Name,Name,Password)
    if login == False:
        redirection = """<script>
    window.onload = function(){
    window.location.href = "Bin/Site/Html/Login.html";
    }
</script>
"""
    else:
        UA.Cookie_Create(["Id","First_Name","Name"],[login,First_Name,Name])
        redirection = """<script>
    window.onload = function(){
    window.location.href = "Bin/Site/Html/User.html";
    }
</script>
"""

## Redirection après la page create
if page == "create":
    First_Name = form.getvalue("First_Name")
    Name = form.getvalue("Name")
    Password = form.getvalue("Password")
    date = form.getvalue("date")
    gender  = form.getvalue("Gender")
    if gender == "Man":
        gender = 0
    else:
        gender = 1
    country = form.getvalue("country")
    create = UA.Create(First_Name, Name, date, country, Password, gender)
    if create == True:
        redirection = """<script>
    window.onload = function(){
    window.location.href = "Bin/Site/Html/Login.html";
    }
</script>
"""
    else:
        redirection = """<script>
    window.onload = function(){
    window.location.href = "Bin/Site/Html/Create.html";
    }
</script>
"""

## Redirection après la page search
if page == "search":
    track = form.getvalue("track")
    artist = form.getvalue("artist")
    album = form.getvalue("album")
    if artist == None and album == None:
        UA.Cookie_Create(["Ecoute"],[track+":Tracks"])
        redirection = """<script>
        window.onload = function(){
        window.location.href = "Tracks.py";
        }
        </script>
        """
    if track == None and album == None:
        UA.Cookie_Create(["Ecoute"],[artist+":Artists"])
        redirection = """<script>
        window.onload = function(){
        window.location.href = "Artist.py";
        }
        </script>
        """
    if artist == None and track == None:
        UA.Cookie_Create(["Ecoute"],[album+":Scrapbooks"])
        redirection = """<script>
        window.onload = function(){
        window.location.href = "Albums.py";
        }
        </script>
        """

## Redirection après la page artist
if page == "artist":
    track = form.getvalue("track")
    album = form.getvalue("album")
    if album == None:
        UA.Cookie_Create(["Ecoute"],[track+":Tracks"])
        redirection = """<script>
        window.onload = function(){
        window.location.href = "Tracks.py";
        }
        </script>
        """
    if track == None:
        UA.Cookie_Create(["Ecoute"],[album+":Scrapbooks"])
        redirection = """<script>
        window.onload = function(){
        window.location.href = "Albums.py";
        }
        </script>
        """

## Redirection après la page album
if page == "album":
    track = form.getvalue("track")
    UA.Cookie_Create(["Ecoute"],[track+":Tracks"])
    redirection = """<script>
        window.onload = function(){
        window.location.href = "Tracks.py";
        }
        </script>
        """

## Redirection après déconnection
if page == "disconnect":
    UA.Delete_Cookie(["Name","First_Name","Id"])
    redirection = """<script>
    window.onload = function(){
    window.location.href = "Bin/Site/Html/Home.html";
    }
</script>
"""

## Redirection après playlist
if page == "playlist":
    namep = form.getvalue("playlist")
    UA.Cookie_Create(["Playlist"],[namep])
    redirection = """<script>
    window.onload = function(){
    window.location.href = "User_playlist.py";
    }
</script>"""

## Redirection après user_playlist
if page == "delete-user_playlist":
    cursor = base.cursor()
    idp = UA.Informations_Cookies("Playlist")
    ch = f"DELETE FROM Playlists WHERE IdPlaylist = '{idp}' AND IdUser = '{iduser}';"
    cursor.execute(ch)
    base.commit()
    UA.Delete_Cookie(["Playlist"])
    redirection = """<script>
    window.onload = function(){
    window.location.href = "Playlist.py";
    }
</script>"""

## Redirection après user_playlist
if page == "userplay":
    track = form.getvalue("track")
    UA.Cookie_Create(["Ecoute"],[f"{track}:Tracks"])
    redirection = """<script>
    window.onload = function(){
    window.location.href = "Tracks.py";
    }
    </script>
    """

## Execution HTML
print("Content-type: text/html; charset=utf-8\n")

html = f'''<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <link rel="icon" type="image/png" sizes="16x16" href="Bin/Site/Images/Playsic.png">
    <title>Playsic</title>
</head>
<body>
    <h1>Redirection...</h1>
    {redirection}
</body>
</html>
'''

print(html)