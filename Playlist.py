# coding: utf-8

import cgi
import sys
import codecs
import Users_accounts as UA
import sqlite3
import chemin as c
import module_playlist as mp

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

formulaire = cgi.FieldStorage() 
Chemin = c.chemin()
base = sqlite3.connect(Chemin)

## Actualisation de la page Account:
    # Formulaire Create:
if formulaire.getvalue("name") != "Favorite@":
  if formulaire.getvalue("form") == "Create":
        mp.gestion_playlist(str(formulaire.getvalue("name")))

Id = UA.Informations_Cookies("Id")
pointer = base.cursor()
ch = f'SELECT Name FROM Playlists WHERE IdUser = "{Id}";'
liste_musique = pointer.execute(ch)
liste_playlists = liste_musique.fetchall()
liste_playlist = []
for y in range(0,len(liste_playlists)):
    if liste_playlists[y][0] != "Favorite@":     
        ch = f'SELECT IdPlaylist FROM Playlists WHERE Name = "{liste_playlists[y][0]}" AND IdUser = "{Id}";'
        id_musique = pointer.execute(ch)
        id_musique = id_musique.fetchall()
        id_musique = id_musique[0][0]
        liste_playlist.append((id_musique,liste_playlists[y][0]))


## Execution HTML
print("Content-type: text/html; charset=utf-8\n")

html = '''<!DOCTYPE html>
<html style="font-size: 16px;">
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <link rel="icon" type="image/png" sizes="16x16" href="Bin/Site/Images/Playsic.png">
    <meta name="page_type" content="np-template-header-footer-from-plugin">
    <title>Account</title>
    <link rel="stylesheet" href="Bin/Site/Css/nicepage.css" media="screen">
    <link rel="stylesheet" href="Bin/Site/Css/Playlist.css" media="screen">
    <script class="u-script" type="text/javascript" src="Bin/Site/Script/jquery.js" defer=""></script>
    <script class="u-script" type="text/javascript" src="Bin/Site/Script/nicepage.js" defer=""></script>
    <script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <meta name="generator" content="Nicepage 4.4.3, nicepage.com">
    <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i">
    <link id="u-page-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i|Allerta:400|PT+Sans+Caption:400,700">  
    <script type="application/ld+json">{
		"@context": "http://schema.org",
		"@type": "Organization",
		"name": "Playsic Home",
		"logo": "Bin/Site/Images/Playsic.png"
}</script>
    <meta name="theme-color" content="#478ac9">
    <meta property="og:title" content="Account">
    <meta property="og:description" content="">
    <meta property="og:type" content="website">
  </head>
  <body class="u-body u-xl-mode"><header class="u-clearfix u-header u-header" id="sec-c98e"><div class="u-clearfix u-sheet u-sheet-1">
        <a href="Bin/Site/Html/User.html" class="u-image u-logo u-image-1" data-image-width="276" data-image-height="305">
          <img src="Bin/Site/Images/Playsic.png" class="u-logo-image u-logo-image-1">
        </a>
        <nav class="u-menu u-menu-dropdown u-offcanvas u-menu-1">
          <div class="menu-collapse" style="font-size: 1rem; letter-spacing: 0px;">
            <a class="u-button-style u-custom-left-right-menu-spacing u-custom-padding-bottom u-custom-text-hover-color u-custom-top-bottom-menu-spacing u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="#">
              <svg class="u-svg-link" viewBox="0 0 24 24"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#menu-hamburger"></use></svg>
              <svg class="u-svg-content" version="1.1" id="menu-hamburger" viewBox="0 0 16 16" x="0px" y="0px" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg"><g><rect y="1" width="16" height="2"></rect><rect y="7" width="16" height="2"></rect><rect y="13" width="16" height="2"></rect>
</g></svg>
            </a>
          </div>
          <form action="Redirection.py">
            <input type="hidden" name="page" value="disconnect">
          <div class="u-custom-menu u-nav-container">
            <ul class="u-nav u-unstyled u-nav-1"><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="Bin/Site/Html/Home.html" style="padding: 10px 20px;">Home</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="About.html" style="padding: 10px 20px;">About</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="Contact.html" style="padding: 10px 20px;">Contact</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="Account.py" style="padding: 10px 20px;">Account</a>
</li><li class="u-nav-item"><input type="submit" onmouseout="this.style.color='black'" onmouseover="this.style.color='#E68387';this.style.cursor='pointer'" value="Disconnect" id="disconnect" class="u-nav-link" style="padding: 10px 20px;">
</li></ul>
          </div>
          <div class="u-custom-menu u-nav-container-collapse">
            <div class="u-black u-container-style u-inner-container-layout u-opacity u-opacity-95 u-sidenav">
              <div class="u-inner-container-layout u-sidenav-overflow">
                <div class="u-menu-close"></div>
                <ul class="u-align-center u-nav u-popupmenu-items u-unstyled u-nav-2"><li class="u-nav-item"><a class="u-button-style u-nav-link" href="Home.html" style="padding: 10px 20px;">Home</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="About.html" style="padding: 10px 20px;">About</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="Contact.html" style="padding: 10px 20px;">Contact</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="Account.py" style="padding: 10px 20px;">Account</a>
</li><li class="u-nav-item"><input type="submit" onmouseout="this.style.color='white'" onmouseover="this.style.color='#737373';this.style.cursor='pointer'" value="Disconnect" class="u-nav-link disco" style="padding: 10px 20px; hover">
</li></ul>
              </div>
            </div>
            <div class="u-black u-menu-overlay u-opacity u-opacity-70"></div>
            </form>
        </nav>
      </div></header>
    <section style="margin-top: 5%;" class="u-clearfix u-section-1" id="sec-e928">
      <div class="u-clearfix u-sheet u-sheet-1"><span class="u-file-icon u-icon u-icon-1"><img src="Bin/Site/Images/File.png" alt=""></span>
        <h4 class="u-text u-text-default u-text-1">Your playlists :</h4>
        <div class="u-container-style u-group u-shape-rectangle u-group-1">
          <div class="u-container-layout u-container-layout-1">'''
print(html)
if liste_playlist != []:
      for y in liste_playlist:
          print(f'''<form action="Redirection.py">
        <input type="hidden" name="playlist" value="{y[0]}"/>
        <input type="hidden" name="page" value="playlist"/>
        <input type=submit value="- {y[1]}" class="u-align-center"/></form><br>''')
html = '''          </div>
        </div>
        <h4 class="u-text u-text-default u-text-2">Create Playlist :</h4>
        <div class="u-align-left u-form u-form-1">
          <form action="#" method="POST" name="Create" style="padding: 10px;">
            <div class="u-form-group u-form-name">
              <label for="name-6f4e" class="u-label">Name of the playlist</label>
              <input type="text" placeholder="Enter the playlist name" id="name-6f4e" name="name" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white" required="">
              <input type="hidden" value="Create" name="form">
            </div>
            <div class="u-align-center u-form-group u-form-submit">
              <input type="submit" value="Create" class="u-btn u-btn-submit u-button-style">
            </div>
          </form>
        </div>
      </div>
    </section>
    <footer class="u-align-center u-clearfix u-footer u-grey-80 u-footer" id="sec-006f"><div class="u-clearfix u-sheet u-sheet-1">
        <p class="u-align-left u-small-text u-text u-text-variant u-text-1">Copyright © 2022 Playsic Inc. Tous droits réservés.</p>
    </div>
    </footer>
  </body>
</html>
'''

print(html)