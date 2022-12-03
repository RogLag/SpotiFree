# coding: utf-8

import cgi
import sys
import codecs
import Users_accounts as UA

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

formulaire = cgi.FieldStorage()     
Id = UA.Informations_Cookies("Id")    
form = formulaire.getvalue("form")
## Actualisation de la page Account:
    # Formulaire 1:
if form == "form-password":
    PS1 = formulaire.getvalue("password1")
    PS2 = formulaire.getvalue("password2")
    PS3 = formulaire.getvalue("password3")
    PS = UA.Information_BDD("Users","Pass_Word",Id,"IdUser")
    PS1 = UA.Hachage(PS1)
    if PS1 == PS:
      if PS2 == PS3:
        UA.modif_BDD2("Users",Id,"Pass_Word",UA.Hachage(PS2))

## Execution HTML
print("Content-type: text/html; charset=utf-8\n")

html = '''<!DOCTYPE html>
<html style="font-size: 16px;">
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="page_type" content="np-template-header-footer-from-plugin">
    <title>Settings</title>
    <link rel="stylesheet" href="Bin/Site/Css/nicepage.css" media="screen">
    <link rel="stylesheet" href="Bin/Site/Css/Settings.css" media="screen">
    <script class="u-script" type="text/javascript" src="Bin/Site/Script/jquery.js" defer=""></script>
    <script class="u-script" type="text/javascript" src="Bin/Site/Script/nicepage.js" defer=""></script>
    <script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <meta name="generator" content="Nicepage 4.4.3, nicepage.com">
    <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i">
    
    
    
    <script type="application/ld+json">{
		"@context": "http://schema.org",
		"@type": "Organization",
		"name": "Playsic Home",
		"logo": "Bin/Site/Images/Playsic.png"
}</script>
    <meta name="theme-color" content="#478ac9">
    <meta property="og:title" content="Settings">
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
    <section class="u-clearfix u-image u-section-1" id="sec-280f" data-image-width="1980" data-image-height="1320" style="background-image: url('../Images/Background_Profile.jpg');">
      <div class="u-clearfix u-sheet u-sheet-1" style="min-height: 848px;">
        <h2 class="u-text u-text-default u-text-1" style="  text-decoration: underline !important;
        margin: 123px auto 0;">Settings :</h2>
        <div class="u-clearfix u-expanded-width u-gutter-0 u-layout-wrap u-layout-wrap-1">
          <div class="u-layout">
            <div class="u-layout-row">
              <div class="u-align-left u-container-style u-layout-cell u-left-cell u-size-23 u-layout-cell-1">
                <div class="u-container-layout u-container-layout-1"><span class="u-icon u-icon-1"><svg class="u-svg-link" preserveAspectRatio="xMidYMin slice" viewBox="0 0 54 54"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg-e3f4"></use></svg><svg class="u-svg-content" viewBox="0 0 54 54" x="0px" y="0px" id="svg-e3f4" style="enable-background:new 0 0 54 54;"><path d="M51.22,21h-5.052c-0.812,0-1.481-0.447-1.792-1.197s-0.153-1.54,0.42-2.114l3.572-3.571
	c0.525-0.525,0.814-1.224,0.814-1.966c0-0.743-0.289-1.441-0.814-1.967l-4.553-4.553c-1.05-1.05-2.881-1.052-3.933,0l-3.571,3.571
	c-0.475,0.475-0.997,0.574-1.352,0.574c-0.5,0-0.997-0.196-1.364-0.539C33.324,8.984,33,8.534,33,7.832V2.78
	C33,1.247,31.753,0,30.22,0H23.78C22.247,0,21,1.247,21,2.78v5.052c0,1.218-0.997,1.945-1.961,1.945c-0.354,0-0.876-0.1-1.351-0.574
	l-3.571-3.571c-1.052-1.052-2.883-1.05-3.933,0l-4.553,4.553c-0.525,0.525-0.814,1.224-0.814,1.967c0,0.742,0.289,1.44,0.814,1.966
	l3.572,3.571c0.573,0.574,0.73,1.364,0.42,2.114S8.644,21,7.832,21H2.78C1.247,21,0,22.247,0,23.78v6.438C0,31.752,1.247,33,2.78,33
	h5.052c0.812,0,1.481,0.447,1.792,1.197s0.153,1.54-0.42,2.114l-3.572,3.571c-0.525,0.525-0.814,1.224-0.814,1.966
	c0,0.743,0.289,1.441,0.814,1.967l4.553,4.553c1.051,1.051,2.881,1.053,3.933,0l3.571-3.571c0.475-0.475,0.997-0.574,1.352-0.574
	c0.963,0,1.96,0.728,1.96,1.945v5.051C21,52.752,22.247,54,23.78,54h6.439c1.533,0,2.78-1.248,2.78-2.781v-5.051
	c0-1.218,0.997-1.945,1.96-1.945c0.354,0,0.877,0.1,1.352,0.574l3.571,3.571c1.052,1.052,2.883,1.05,3.933,0l4.553-4.553
	c0.525-0.525,0.814-1.224,0.814-1.967c0-0.742-0.289-1.44-0.814-1.966l-3.572-3.571c-0.573-0.574-0.73-1.364-0.42-2.114
	S45.356,33,46.168,33h5.052c1.533,0,2.78-1.248,2.78-2.781V23.78C54,22.247,52.753,21,51.22,21z M34,27c0,3.859-3.141,7-7,7
	s-7-3.141-7-7s3.141-7,7-7S34,23.141,34,27z"></path></svg></span>
                </div>
              </div>
              <div class="u-align-left u-container-style u-layout-cell u-right-cell u-size-37 u-layout-cell-2">
                <div class="u-container-layout u-container-layout-2">
                  <div class="u-form u-form-1">
                    <form action="Settings.py" method="POST" style="padding: 10px;">
                      <div class="u-form-group u-form-name">
                        <label for="name-a0b7" class="u-label">Old Password</label>
                        <input type="password" placeholder="Enter your old password" id="name-a0b7" name="password1" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white" required="">
                      </div>
                      <div class="u-form-email u-form-group">
                        <label for="email-a0b7" class="u-label">New Password</label>
                        <input type="password" placeholder="Enter your new password" id="email-a0b7" name="password2" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white" required="">
                      </div>
                      <div class="u-form-group u-form-group-3">
                        <label for="text-8d66" class="u-label">New Password</label>
                        <input type="password" id="text-8d66" name="password3" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white" placeholder="Enter your new password a second time">
                      </div>
                      <input type="hidden" value="form-password" name="form">
                      <div class="u-align-left u-form-group u-form-submit">
                        <input type="submit" value="Submit" class="u-btn u-btn-submit u-button-style">
                      </div>
                    </form>
                  </div>
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
      <script>'''
print(html)
if form == "form-password":
  print("""Swal.fire(
  'Your password has been update !',-
  '',
  'success'
)""")
html=    '''</script>
  </body>
</html>
'''

print(html)