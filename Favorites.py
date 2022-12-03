# coding: utf-8

import cgi
import sys
import codecs
import Users_accounts as UA
import sqlite3
import chemin as c

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

formulaire = cgi.FieldStorage() 
Chemin = c.chemin()
base = sqlite3.connect(Chemin)   

Id = UA.Informations_Cookies("Id")
liste_musique = []
pointer = base.cursor()
ch = f"SELECT Tracks.Name,a.Name FROM Possède_Posséder_par as ppp INNER JOIN Tracks ON(ppp.IdTrack = Tracks.IdTrack) INNER JOIN Scrapbooks as s ON(Tracks.IdScrapbook = s.IdScrapbook) INNER JOIN Artists as a ON(s.IdArtist = a.IdArtist) INNER JOIN Playlists ON(Playlists.IdPlaylist = ppp.IdPlaylist) WHERE Playlists.Name = 'Favorite@' AND Playlists.IdUser = {Id}"
musiques = pointer.execute(ch)
musique = musiques.fetchall()
musiques = []
for y in musique:
    musiques.append([y[0],y[1]])
ch = f'SELECT Tracks.URL FROM Tracks INNER JOIN Possède_Posséder_par as ppp ON(ppp.IdTrack = Tracks.IdTrack) INNER JOIN Playlists ON(Playlists.IdPlaylist = ppp.IdPlaylist) WHERE Playlists.Name = "Favorite@" AND Playlists.IdUser = {Id}'
url = pointer.execute(ch)
url = url.fetchall()
urls = []
for y in url:
      urls.append(y[0])

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
    <link rel="stylesheet" href="Bin/Site/Css/Favorites.css" media="screen">
    <link rel="stylesheet" href="Bin/Site/Css/style.css">
	  <link rel="stylesheet" href="Bin/Site/Css/demo.css">
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
  <body class="u-body u-xl-mode" style="font-weight: normal;font-style: normal;"><header class="u-clearfix u-header u-header" id="sec-c98e"><div class="u-clearfix u-sheet u-sheet-1">
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
    <section class="u-clearfix u-section-1" id="sec-51dd">
    <div class="u-clearfix u-sheet u-sheet-1" style="min-height: 1000px;">
    <div>
      <img src="Bin/Site/Images/star.svg" style="height: 1000px;display: block; margin: 0px auto;">
    </div>
                  <main style="background: transparent; margin-top: -690px; width: 500px;">
 <div class="simple-audio-player" id="simp" data-config='{"shide_top":false,"shide_btm":false,"auto_load":true}' style='background: transparent;color: black;font-size: 18px;'>
  <div class="simp-playlist">
    <ul>'''
print(html)
for i in range(0,len(urls)):
      print(f'<li style="background: transparent;color: black;"><span class="simp-source" data-src="{urls[i]}">{musiques[i][0]}</span><span class="simp-desc">{musiques[i][1]}</span></li>')
html = '''
    </ul>
  </div>
</div>    
 </main>
        </div>
    </section>
    <footer class="u-align-center u-clearfix u-footer u-grey-80 u-footer" id="sec-006f"><div class="u-clearfix u-sheet u-sheet-1">
        <p class="u-align-left u-small-text u-text u-text-variant u-text-1">Copyright © 2022 Playsic Inc. Tous droits réservés.</p>
      </div></footer>
      <script  src="Bin/Site/Script/audio.js"></script>
  </body>
</html>
'''

print(html)