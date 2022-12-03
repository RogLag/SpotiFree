# coding: utf-8

import cgi
import sys
import codecs
import Users_accounts as UA
import Algo_Search as S

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
search = form.getvalue("search")

## Actualisation de la page Search:
def Actualisation(search):
  result_liste = S.Search(search)
  if result_liste == ["None",["None"],[]]:
        return "Vide"
  return result_liste

## Execution HTML
print("Content-type: text/html; charset=utf-8\n")

html = '''<!DOCTYPE html>
<html style="font-size: 16px;">
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <link rel="icon" type="image/png" sizes="16x16" href="Bin/Site/Images/Playsic.png">
    <meta name="page_type" content="np-template-header-footer-from-plugin">
    <title>Playsic</title>
    <link rel="stylesheet" href="Bin/Site/Css/nicepage.css" media="screen">
<link rel="stylesheet" href="Bin/Site/Css/Search.css" media="screen">
    <script class="u-script" type="text/javascript" src="Bin/Site/Script/jquery.js" defer=""></script>
    <script class="u-script" type="text/javascript" src="Bin/Site/Script/nicepage.js" defer=""></script>
    <meta name="generator" content="Nicepage 4.4.3, nicepage.com">
    <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i">
    <script type="application/ld+json">{
		"@context": "http://schema.org",
		"@type": "Organization",
		"name": "Playsic Home",
		"logo": ""Bin/Site/Images/Playsic.png"
}</script>
    <meta name="theme-color" content="#478ac9">
    <meta property="og:title" content="Search">
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
    <section class="u-align-center u-clearfix u-image u-section-1" id="sec-0fc3" data-image-width="1920" data-image-height="1200">
      <div class="u-clearfix u-sheet u-valign-middle u-sheet-1">
        <div class="u-clearfix u-expanded-width u-gutter-10 u-layout-wrap u-layout-wrap-1">
          <div class="u-gutter-0 u-layout">
            <div class="u-layout-row">
              <div class="u-size-30">
                <div class="u-layout-col">
                  <div class="u-align-left u-container-style u-layout-cell u-left-cell u-size-60 u-layout-cell-1">
                    <div class="u-container-layout u-container-layout-1">
                      <div class="u-form u-form-1">
                        <form action="Search.py" method="POST" style="padding: 10px" name="form-5">
                          <div class="u-form-group u-form-name u-label-none u-form-group-1">
                            <label for="name-5359" class="u-label">Music</label>
                            <input type="text" placeholder="What music do you want to listen to ?" id="name-5359" name="search" class="u-border-1 u-border-grey-30 u-input u-input-rectangle" required="">
                          </div>
                          <div class="u-align-center u-form-group u-form-submit u-form-group-2">
                            <input type="submit" value="Search" class="u-btn u-btn-submit u-button-style">
                          </div>
                        </form>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="u-size-30">
                <div class="u-layout-col">
                  <div class="u-container-style u-layout-cell u-right-cell u-size-60 u-layout-cell-2">
                    <div class="u-container-layout u-container-layout-2">
                      <h2 class="u-align-center u-text u-text-1">Result of the search :</h2>
                      <div class="fr-view u-clearfix u-rich-text u-text u-text-2">'''
print(html)
if search != None:
  result = Actualisation(search)
  if result == "Vide":
    print('<p class="u-align-center">Not Found</p>')
  else:
    if result[0] != "None":
      print(f'''<form action="Redirection.py">
      <input type="hidden" name="artist" value="{result[0]}"/>
      <input type="hidden" name="page" value="search"/>
      <input type=submit value="Artist : {result[0]}" class="u-align-center"/></form>''')
    print('<br>')
    if result[1][0] != "None":
          for i in result[1]:
            print(f'''<form action="Redirection.py">
      <input type="hidden" name="album" value="{i}"/>
      <input type="hidden" name="page" value="search"/>
      <input type=submit value="Albums : {i}" class="u-align-center"/></form>''')
    print('<br>')
    if result[2] != []:
      for y in result[2]:
          print(f'''<form action="Redirection.py">
        <input type="hidden" name="track" value="{y}"/>
        <input type="hidden" name="page" value="search"/>
        <input type=submit value="- {y}" class="u-align-center"/></form>''')
html =                       '''</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <footer class="u-align-center u-clearfix u-footer u-grey-80 u-footer" id="sec-006f"><div class="u-clearfix u-sheet u-sheet-1">
        <p class="u-align-left u-small-text u-text u-text-variant u-text-1">Copyright © 2022 Playsic Inc. All rights reserved.</p>
      </div></footer>
  </body>
</html>
'''

print(html)