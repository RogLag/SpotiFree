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

cookie = UA.Informations_Cookies("Ecoute") 
Id = UA.Informations_Cookies("Id")
cookie = cookie.split(":")
if cookie[1] == "Tracks":
      String = cookie[0]
      pointer = base.cursor()
      ch = f'SELECT Scrapbooks.Title FROM Scrapbooks INNER JOIN Tracks ON(Tracks.IdScrapbook=Scrapbooks.IdScrapbook) WHERE Tracks.Name = "{String}"'
      inf = pointer.execute(ch)
      inf = inf.fetchall()
      ch = f'SELECT Tracks.IdTrack FROM Tracks WHERE Tracks.Name = "{String}"'
      Idmusic = pointer.execute(ch)
      Idmusic = Idmusic.fetchall()
      Idmusic = Idmusic[0][0]
      ch = f'SELECT Artists.Name FROM Artists INNER JOIN Scrapbooks ON(Artists.IdArtist=Scrapbooks.IdArtist) WHERE Scrapbooks.Title = "{inf[0][0]}"'
      inf2 = pointer.execute(ch)
      inf2 = inf2.fetchall()
      desc = f'''This track is taken from the album <u>{inf[0][0]}</u> of <u>{inf2[0][0]}</u>.'''
      ch = f'SELECT Artists.Image FROM Artists INNER JOIN Scrapbooks ON(Artists.IdArtist=Scrapbooks.IdArtist) WHERE Scrapbooks.Title = "{inf[0][0]}"'
      image = pointer.execute(ch)
      image = image.fetchall()
      image = image[0][0]
      ch = f'SELECT URL FROM Tracks WHERE Name = "{String}"'
      url = pointer.execute(ch)
      url = url.fetchall()
      url = url[0][0] 
      liste_playlist = []
      ch = f'SELECT Playlists.name,Playlists.IdPlaylist FROM Playlists WHERE Playlists.IdUser = "{Id}" and Playlists.Name != "Favorite@";'
      inf3 = pointer.execute(ch)
      inf3 = inf3.fetchall()
      for i in inf3:
            liste_playlist.append(i)
      

## Execution HTML
print("Content-type: text/html; charset=utf-8\n")

html = '''<!DOCTYPE html>
<html style="font-size: 16px;">
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="keywords" content="">
    <meta name="description" content="">
    <meta name="page_type" content="np-template-header-footer-from-plugin">
    <title>Ecoute</title>
    <link rel="stylesheet" href="Bin/Site/Css/Ecoute.css" media="screen">
    <link rel="stylesheet" href="Bin/Site/Css/nicepage2.css" media="screen">
        <link rel="stylesheet" href="Bin/Site/Css/style.css">
	  <link rel="stylesheet" href="Bin/Site/Css/demo.css">
    <script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <script class="u-script" type="text/javascript" src="Bin/Site/Script/jquery2.js" defer=""></script>
    <script class="u-script" type="text/javascript" src="Bin/Site/Script/nicepage2.js" defer=""></script>
    <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i|Open+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i">
    
    
    <script type="application/ld+json">{
		"@context": "http://schema.org",
		"@type": "Organization",
		"name": "Playsic",
		"logo": "images/2213592-images-logo-musique-vectoriel1.png"
}</script>
    <meta name="theme-color" content="#9ac2c7">
    <meta property="og:title" content="Ecoute">
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
    <section class="u-clearfix u-section-1" id="sec-0dc1">
      <div class="u-clearfix u-sheet u-valign-middle u-sheet-12">
        <div class="u-clearfix u-expanded-width u-gutter-30 u-layout-wrap u-layout-wrap-1">
          <div class="u-layout">
            <div class="u-layout-row">
              <div class="u-container-style u-expand-resize u-layout-cell u-left-cell u-size-28 u-layout-cell-1">
                <div class="u-container-layout">
                  <div class="u-align-left u-palette-1-light-1 u-shape u-shape-1"></div>'''
print(html)
print(f'<img class="u-align-left u-image u-image-1" data-image-width="2000" data-image-height="1333" src="{image}"/>')
html = '''
                </div>
              </div>
              <div class="u-align-left u-container-style u-layout-cell u-right-cell u-size-32 u-layout-cell-2">
                <div class="u-container-layout u-container-layout-2">
                  <div class="u-form">
                    <form action="module_add.py" method="POST" class="u-clearfix u-form-spacing-10 u-form-vertical u-inner-form formulaire" source="custom" name="form-1" style="padding: 10px; width: 140px;">
                      <input type="hidden" id="siteId" name="siteId" value="581722517">
                      <input type="hidden" id="pageId" name="pageId" value="1503419854">
                      <div class="u-form-group u-form-select u-label-top u-form-group-1">
                        <label for="select-289b" class="u-label">Select playlist</label>
                        <div class="u-form-select-wrapper">
                          <select id="select-289b" name="selectplaylists" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white" size="5" multiple="multiple">
                          '''
print(html)
for tuple in liste_playlist:
      print(f'<option value="{tuple[0]}:{Idmusic}">{tuple[0]}</option>')
html =                           '''
                          </select>
                          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="12" version="1" class="u-caret"><path fill="currentColor" d="M4 8L0 4h8z"></path></svg>
                        </div>
                      </div>
                      <div class="u-align-center u-form-group u-form-submit u-label-top">
                        <button type="submit" onclick="check1()" value="Add" class="u-btn u-btn-submit u-button-style">Add</button>
                    </form>
                  </div>
                  <div class="u-form u-form-21">
                   <form action="favorite.py" method="POST" class="u-clearfix u-form-spacing-10 u-form-vertical u-inner-form" source="custom" name="form" style="padding: 10px;">
                  <button type="submit" onclick="check()" style="margin-left: 100%;" onclick="python()" class="u-border-hover-palette-3-base u-border-none u-btn u-button-style u-none u-btn-1"><span class="u-file-icon u-icon u-icon-1" style="  font-size: 2.1876em;
  vertical-align: 0px;"><img src="Bin/Site/Images/Heart.png" alt=""></span>
                    </form>
                  </div>
                  <h3 class="u-text u-text-default u-text-14" style="margin: 30px 0 auto 180px;">'''
print(html)
print(String)                  
html =                  '''</h3>
                  <p class="u-text u-text-21">
'''
print(html)
print(f"{desc}</p>")
if url != None:
  print('''<br><main>
     <!-- Start DEMO HTML (Use the following code into your project)-->
 <div class="simple-audio-player" id="simp" data-config='{"shide_top":false,"shide_btm":true,"auto_load":true}'>
  <div class="simp-playlist">
    <ul>''')

  print(f'<li><span class="simp-source" data-src="{url}">{String}</span><span class="simp-desc">{inf2[0][0]}</span></li>')
  print('''    </ul>
  </div>
</div>    
 </main>''')
else:
  print('<h6 class="u-align-center u-text u-text-31">This music is unavailable for the moment.</h6>')
html = '''
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <footer class="u-align-center u-clearfix u-footer u-grey-80 u-footer" id="sec-006f"><div class="u-clearfix u-sheet u-sheet-1">
        <p class="u-align-left u-small-text u-text u-text-variant u-text-1">Copyright © 2022 Playsic Inc. Tous droits réservés.</p>
      </div></footer>
      <script>
      function check(){
        Swal.fire({
  position: 'top-end',
  icon: 'success',
  title: 'The music has been added or deleted in your favorites !',
  showConfirmButton: false,
  timer: 1500,
  color: '#000000'
})
      }
      </script>
      <script>
      function check1(){
        Swal.fire({
  position: 'top-end',
  icon: 'success',
  title: 'The music has been added or deleted in your playlist(s) !',
  showConfirmButton: false,
  timer: 1500,
  color: '#000000'
})
      }
      </script>
      <script  src="Bin/Site/Script/audio.js"></script>
  </body>
</html>
'''

print(html)