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
    <meta name="page_type" content="np-template-header-footer-from-plugin">
    <title>Artist</title>
    <link rel="stylesheet" href="Bin/Site/Css/nicepage.css" media="screen">
<link rel="stylesheet" href="Bin/Site/Css/Ranking.css" media="screen">
    <script class="u-script" type="text/javascript" src="Bin/Site/Script/jquery.js" defer=""></script>
    <script class="u-script" type="text/javascript" src="Bin/Site/Script/nicepage.js" defer=""></script>
    <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i">
    
    <script type="application/ld+json">{
		"@context": "http://schema.org",
		"@type": "Organization",
		"name": "Playsic Home",
		"logo": "Bin/Site/Images/2213592-images-logo-musique-vectoriel.png"
}</script>
    <meta name="theme-color" content="#478ac9">
    <meta property="og:title" content="Artist">
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
          </div>
        </nav>
      </div></header> 
    <section class="u-align-center u-clearfix u-section-1" id="sec-51da">
      <div class="u-clearfix u-sheet u-sheet-1">
        <h2 class="u-text u-text-default u-text-1">Ranking</h2>
        <p class="u-text u-text-2"> This page presents Playsic's 3 rankings for its music and artists!</p>
        <div class="u-clearfix u-expanded-width u-gutter-50 u-layout-wrap u-layout-wrap-1">
          <div class="u-layout">
            <div class="u-layout-row">
              <div class="u-container-style u-layout-cell u-left-cell u-size-30 u-layout-cell-1">
                <div class="u-border-2 u-border-grey-25 u-container-layout u-container-layout-1">
                  <h4 class="u-align-center u-text u-text-3">Musics</h4>
                  <div class="u-clearfix u-layout-wrap u-layout-wrap-2">
                    <div class="u-layout">
                      <div class="u-layout-row">
                        <div class="u-container-style u-layout-cell u-size-41 u-layout-cell-2">
                          <div class="u-container-layout u-container-layout-2">
                            <h6 class="u-align-center u-text u-text-4">Name</h6>
                            <p class="u-text u-text-default u-text-5"> Exemple de texte. Lorem ipsum dolor sit amet, consectetur adipiscing elit nullam nunc justo sagittis suscipit ultrices.</p>
                          </div>
                        </div>
                        <div class="u-container-style u-layout-cell u-size-19 u-layout-cell-3">
                          <div class="u-container-layout u-container-layout-3">
                            <h6 class="u-align-center u-text u-text-6">Listen</h6>
                            <p class="u-text u-text-7"> Exemple de texte. Lorem ipsum dolor sit amet, consectetur adipiscing elit nullam nunc justo sagittis suscipit ultrices.</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="u-container-style u-layout-cell u-right-cell u-size-30 u-white u-layout-cell-4">
                <div class="u-border-2 u-border-grey-25 u-container-layout u-container-layout-4">
                  <h4 class="u-align-center u-text u-text-8">Artists</h4>
                  <div class="u-clearfix u-layout-wrap u-layout-wrap-3">
                    <div class="u-layout">
                      <div class="u-layout-row">
                        <div class="u-container-style u-layout-cell u-size-41 u-layout-cell-5">
                          <div class="u-container-layout u-expanded u-container-layout-5">
                            <h6 class="u-align-center u-text u-text-9">Name</h6>
                            <p class="u-text u-text-default u-text-10"> Exemple de texte. Lorem ipsum dolor sit amet, consectetur adipiscing elit nullam nunc justo sagittis suscipit ultrices.</p>
                          </div>
                        </div>
                        <div class="u-container-style u-layout-cell u-size-19 u-layout-cell-6">
                          <div class="u-container-layout u-expanded u-container-layout-6">
                            <h6 class="u-align-center u-text u-text-11">Listen</h6>
                            <p class="u-text u-text-12"> Exemple de texte. Lorem ipsum dolor sit amet, consectetur adipiscing elit nullam nunc justo sagittis suscipit ultrices.</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    
    <footer class="u-align-center u-clearfix u-footer u-grey-80 u-footer" id="sec-ec1b"><div class="u-clearfix u-sheet u-sheet-1">
        <p class="u-align-left u-small-text u-text u-text-variant u-text-1">Copyright&nbsp;© 2022 Playsic Inc. Tous droits réservés.</p>
      </div></footer>
    <section class="u-backlink u-clearfix u-grey-80">
      <a class="u-link" href="https://nicepage.com/css-templates" target="_blank">
        <span>CSS Templates</span>
      </a>
      <p class="u-text">
        <span>created with</span>
      </p>
      <a class="u-link" href="" target="_blank">
        <span>Website Builder Software</span>
      </a>. 
    </section>
  </body>
</html>
'''

print(html)