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
pointer = base.cursor()

String = UA.Informations_Cookies("Playlist") 
iduser = UA.Informations_Cookies("Id")
ch = f"SELECT Tracks.Name,a.Name FROM Possède_Posséder_par as ppp INNER JOIN Tracks ON(ppp.IdTrack = Tracks.IdTrack) INNER JOIN Scrapbooks as s ON(Tracks.IdScrapbook = s.IdScrapbook) INNER JOIN Artists as a ON(s.IdArtist = a.IdArtist) INNER JOIN Playlists ON(Playlists.IdPlaylist = ppp.IdPlaylist) WHERE ppp.IdPlaylist = {String} AND Playlists.IdUser = {iduser}"
musiques = pointer.execute(ch)
musique = musiques.fetchall()
musiques = []
for y in musique:
    musiques.append([y[0],y[1]])
ch = f'SELECT Tracks.URL FROM Tracks INNER JOIN Possède_Posséder_par as ppp ON(ppp.IdTrack = Tracks.IdTrack) INNER JOIN Playlists ON(Playlists.IdPlaylist = ppp.IdPlaylist) WHERE ppp.IdPlaylist = {String}'
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
    <meta name="page_type" content="np-template-header-footer-from-plugin">
    <title>Ecoute</title>
    <link rel="stylesheet" href="Bin/Site/Css/nicepage.css" media="screen">
    <link rel="stylesheet" href="Bin/Site/Css/User_playlist.css" media="screen">
    <link rel="stylesheet" href="Bin/Site/Css/style.css">
	  <link rel="stylesheet" href="Bin/Site/Css/demo.css">
    <script class="u-script" type="text/javascript" src="Bin/Site/Script/jquery.js" defer=""></script>
    <script class="u-script" type="text/javascript" src="Bin/Site/Script/nicepage.js" defer=""></script>
    <script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <meta name="generator" content="Nicepage 4.4.3, nicepage.com">
    <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i">
    <script type="application/ld+json">{
		"@context": "http://schema.org",
		"@type": "Organization",
		"name": "Playsic Home",
		"logo": "Bin/Site/Images/2213592-images-logo-musique-vectoriel.png"
}</script>
    <meta name="theme-color" content="#478ac9">
    <meta property="og:title" content="Ecoute">
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
          </div>
</nav>
      </div></header>
    <section class="u-clearfix u-white u-section-1" id="carousel_d6e4">
      <div class="u-clearfix u-sheet u-sheet-1">
        <div class="u-shape u-shape-svg u-text-palette-2-base u-shape-1">
          <svg class="u-svg-link" preserveAspectRatio="none" viewBox="0 0 160 150" style=""><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg-40dc"></use></svg>
          <svg class="u-svg-content" viewBox="0 0 160 150" x="0px" y="0px" id="svg-40dc"><path d="M43.2,126.9c14.2,1.3,27.6,7,39.1,15.6c8.3,6.1,19.4,10.3,32.7,5.3c11.7-4.4,18.6-17.4,21-30.2c2.6-13.3,8.1-25.9,15.7-37.1
	c8.3-12.1,10.8-27.9,5.3-42.7C150.5,20.3,134.6,9,117,7.6C107.9,6.9,98.8,5,90.1,1.9C83-0.6,75-0.7,67.4,2.1
	c-9.9,3.7-17,11.6-20.1,21c-3.3,10.1-10.9,18-20.6,22.2c-0.1,0-0.1,0.1-0.2,0.1c-20.3,8.9-31,32-24.6,53.2
	C6.9,115.6,25.2,125.2,43.2,126.9z"></path></svg>
        </div>
        <div>
                <div class="u-form u-form-1" style="margin-top: -950px;">
          <form action="Redirection.py" method="POST">
            <input type="hidden" name="page" value="delete-user_playlist">
            <div class="u-align-center u-form-group u-form-submit">
              <input type="submit" value="Delete" class="u-btn u-btn-submit u-button-style">
            </div>
          </form>
        </div>
        <div class="u-form u-form-2">
            <div class="u-align-center u-form-group">
              <a href="Search.py" style="margin-top: 1%" class="u-btn">Add music</a>
            </div>
          </form>
        </div>
         <main style="background: transparent; margin-top: 140px;max-width: 2000px;">
     <!-- Start DEMO HTML (Use the following code into your project)-->
 <div class="simple-audio-player" id="simp" data-config='{"shide_top":false,"shide_btm":false,"auto_load":true}' style='background: transparent;color: black;font-size: 18px;max-width: 700px;'>
  <div class="simp-playlist">
    <ul>'''
print(html)
for i in range(0,len(urls)):
      print(f'<li style="background: transparent;"><span class="simp-source" data-src="{urls[i]}">{musiques[i][0]}</span><span class="simp-desc">{musiques[i][1]}</span></li>')
html = '''
    </ul>
  </div>  
     <!-- END EDMO HTML (Happy Coding!)-->
 </main>
      </div>
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