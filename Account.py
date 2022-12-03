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
if form == "form-1":
    FName = formulaire.getvalue("first_name")
    Name = formulaire.getvalue("name")
    Date = formulaire.getvalue("date")
    Gender = formulaire.getvalue("gender")
    if Gender == "Man":
        Gender = 0
    else:
        Gender = 1
    Country = formulaire.getvalue("country")
    UA.modif_BDD("Users",Id,["FirstName","FamilyName","DateofBirth","Gender","Country"],[f"{FName}",f"{Name}",f"{Date}",f"{Gender}",f"{Country}"])
    UA.Cookie_Create(["Id","First_Name","Name"],[Id,FName,Name])
    # Formulaire 2:
if form == "form-2":
    Telephone = formulaire.getvalue("phoneuser")
    Email = formulaire.getvalue("email")
    Adresse = formulaire.getvalue("address") 
    UA.modif_BDD("Users",Id,["Phone","Email","Adress"],[Telephone,Email,Adresse])
    # Formulaire 3:
if form == "form-3":
    Message = formulaire.getvalue("message")
    UA.modif_BDD("Users",Id,["Message"],[Message])
    
##
First_Name = UA.Information_BDD("Users","FirstName",Id,"IdUser")
Name = UA.Information_BDD("Users","FamilyName",Id,"IdUser")
Date = UA.Information_BDD("Users","DateofBirth",Id,"IdUser")
Gender = UA.Information_BDD("Users","Gender",Id,"IdUser")
if Gender == 0:
    Gender = "Man"
else:
    Gender = "Woman"
Country = UA.Information_BDD("Users","Country",Id,"IdUser")
Mail = UA.Information_BDD("Users","Email",Id,"IdUser")
if Mail == None or Mail == "None":
    Mail = ""
Adress = UA.Information_BDD("Users","Adress",Id,"IdUser")
if Adress == None or Adress == "None":
    Adress = ""
Phone = UA.Information_BDD("Users","Phone",Id,"IdUser")
if Phone == None or Phone == "None":
    Phone = ""
Mess = UA.Information_BDD("Users","Message",Id,"IdUser")
if Mess == None or Mess == "None":
    Mess = ""

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
    <link rel="stylesheet" href="Bin/Site/Css/Account.css" media="screen">
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
    <section class="u-align-center u-clearfix u-image u-section-1" id="carousel_29c9" data-image-width="1980" data-image-height="1320">
      <div class="u-clearfix u-sheet u-valign-bottom-sm u-valign-bottom-xs u-sheet-1">
        <h2 class="u-text u-text-1">Profile</h2>
        <div class="u-clearfix u-expanded-width u-layout-wrap u-layout-wrap-1">
          <div class="u-gutter-0 u-layout">
            <div class="u-layout-row">
              <div class="u-align-left u-container-style u-layout-cell u-size-20 u-layout-cell-1">
                <div class="u-container-layout u-container-layout-1">
                  <h4 class="u-custom-font u-text u-text-2">Details</h4>
                  <div class="u-form u-form-1">
                    <form action="Account.py" method="POST" name="form" style="padding: 10px;">
                      <div class="u-form-group u-form-name">
                        <label for="name-65b5" class="u-label">First Name</label>
                        <input type="text" placeholder="Enter your first name" id="First_Name" name="first_name" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white">
                      </div>
                      <div class="u-form-email u-form-group">
                        <label for="Name" class="u-label">Name</label>
                        <input type="text" placeholder="Enter your name" id="Name" name="name" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white">
                      </div>
                      <div class="u-form-date u-form-group u-form-group-3">
                        <label for="date-8996" class="u-label">Date of birth</label>
                        <input type="date" placeholder="MM/DD/YYYY" id="date" name="date" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white">
                      </div>
                      <div class="u-form-group u-form-select u-form-group-4">
                        <label for="select-019f" class="u-label">Gender</label>
                        <div class="u-form-select-wrapper">
                          <select id="gender" name="gender" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white">
                            <option value="Man">Man</option>
                            <option value="Woman">Woman</option>
                          </select>
                          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="12" version="1" class="u-caret"><path fill="currentColor" d="M4 8L0 4h8z"></path></svg>
                        </div>
                      </div>
                      <div class="u-form-group u-form-select u-form-group-5">
                        <label for="select-4d75" class="u-label">Country</label>
                        <div class="u-form-select-wrapper">
                          <select id="country" name="country" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white">
                            <option value="Afghanistan">Afghanistan</option>
                            <option value="Albania">Albania</option>
                            <option value="Algeria">Algeria</option>
                            <option value="Angola">Angola</option>
                            <option value="Argentina">Argentina</option>
                            <option value="Armenia">Armenia</option>
                            <option value="Australia">Australia</option>
                            <option value="Austria">Austria</option>
                            <option value="Azerbaijan">Azerbaijan</option>
                            <option value="Bahamas">Bahamas</option>
                            <option value="Bahrain">Bahrain</option>
                            <option value="Bangladesh">Bangladesh</option>
                            <option value="Belarus">Belarus</option>
                            <option value="Belgium">Belgium</option>
                            <option value="Belize">Belize</option>
                            <option value="Benin">Benin</option>
                            <option value="Bhutan">Bhutan</option>
                            <option value="Bolivia">Bolivia</option>
                            <option value="Bosnia and Herzegovina">Bosnia and Herzegovina</option>
                            <option value="Botswana">Botswana</option>
                            <option value="Brazil">Brazil</option>
                            <option value="Brunei">Brunei</option>
                            <option value="Bulgaria">Bulgaria</option>
                            <option value="Burkina">Burkina</option>
                            <option value="Burma/Myanmar">Burma/Myanmar</option>
                            <option value="Burundi">Burundi</option>
                            <option value="Cambodia">Cambodia</option>
                            <option value="Cameroon">Cameroon</option>
                            <option value="Canada">Canada</option>
                            <option value="Cape Verde">Cape Verde</option>
                            <option value="Chad">Chad</option>
                            <option value="Chile">Chile</option>
                            <option value="China">China</option>
                            <option value="Colombia">Colombia</option>
                            <option value="Comoros">Comoros</option>
                            <option value="Congo">Congo</option>
                            <option value="Cook Islands">Cook Islands</option>
                            <option value="Costa Rica">Costa Rica</option>
                            <option value="Croatia">Croatia</option>
                            <option value="Cuba">Cuba</option>
                            <option value="Cyprus">Cyprus</option>
                            <option value="Czech Republic">Czech Republic</option>
                            <option value="Denmark">Denmark</option>
                            <option value="Dominican Republic">Dominican Republic</option>
                            <option value="Ecuador">Ecuador</option>
                            <option value="Egypt">Egypt</option>
                            <option value="El Salvador">El Salvador</option>
                            <option value="Equatorial Guinea">Equatorial Guinea</option>
                            <option value="Eritrea">Eritrea</option>
                            <option value="Estonia">Estonia</option>
                            <option value="Ethiopia">Ethiopia</option>
                            <option value="Fiji">Fiji</option>
                            <option value="Finland">Finland</option>
                            <option value="France">France</option>
                            <option value="Gabon">Gabon</option>
                            <option value="Gambia">Gambia</option>
                            <option value="Georgia">Georgia</option>
                            <option value="Germany">Germany</option>
                            <option value="Ghana">Ghana</option>
                            <option value="Greece">Greece</option>
                            <option value="Grenada">Grenada</option>
                            <option value="Guatemala">Guatemala</option>
                            <option value="Guinea">Guinea</option>
                            <option value="Guyana">Guyana</option>
                            <option value="Haiti">Haiti</option>
                            <option value="Honduras">Honduras</option>
                            <option value="Hungary">Hungary</option>
                            <option value="Iceland">Iceland</option>
                            <option value="India">India</option>
                            <option value="Indonesia">Indonesia</option>
                            <option value="Iran">Iran</option>
                            <option value="Iraq">Iraq</option>
                            <option value="Ireland">Ireland</option>
                            <option value="Israel">Israel</option>
                            <option value="Italy">Italy</option>
                            <option value="Ivory Coast">Ivory Coast</option>
                            <option value="Jamaica">Jamaica</option>
                            <option value="Japan">Japan</option>
                            <option value="Jordan">Jordan</option>
                            <option value="Kazakhstan">Kazakhstan</option>
                            <option value="Kenya">Kenya</option>
                            <option value="Kuwait">Kuwait</option>
                            <option value="Kyrgyzstan">Kyrgyzstan</option>
                            <option value="Laos">Laos</option>
                            <option value="Latvia">Latvia</option>
                            <option value="Lebanon">Lebanon</option>
                            <option value="Lesotho">Lesotho</option>
                            <option value="Liberia">Liberia</option>
                            <option value="Libya">Libya</option>
                            <option value="Lithuania">Lithuania</option>
                            <option value="Luxembourg">Luxembourg</option>
                            <option value="Macedonia">Macedonia</option>
                            <option value="Madagascar">Madagascar</option>
                            <option value="Malawi">Malawi</option>
                            <option value="Malaysia">Malaysia</option>
                            <option value="Maldives">Maldives</option>
                            <option value="Mali">Mali</option>
                            <option value="Malta">Malta</option>
                            <option value="Marshall Islands">Marshall Islands</option>
                            <option value="Mauritania">Mauritania</option>
                            <option value="Mauritius">Mauritius</option>
                            <option value="Mexico">Mexico</option>
                            <option value="Micronesia (The Federated States of)">Micronesia (The Federated States of)</option>
                            <option value="Moldova">Moldova</option>
                            <option value="Monaco">Monaco</option>
                            <option value="Mongolia">Mongolia</option>
                            <option value="Morocco">Morocco</option>
                            <option value="Mozambique">Mozambique</option>
                            <option value="Namibia">Namibia</option>
                            <option value="Nepal">Nepal</option>
                            <option value="Netherlands">Netherlands</option>
                            <option value="New Zealand">New Zealand</option>
                            <option value="Nicaragua">Nicaragua</option>
                            <option value="Niger">Niger</option>
                            <option value="Nigeria">Nigeria</option>
                            <option value="North Korea">North Korea</option>
                            <option value="Norway">Norway</option>
                            <option value="Oman">Oman</option>
                            <option value="Pakistan">Pakistan</option>
                            <option value="Palau">Palau</option>
                            <option value="Panama">Panama</option>
                            <option value="Papua New Guinea">Papua New Guinea</option>
                            <option value="Paraguay">Paraguay</option>
                            <option value="Peru">Peru</option>
                            <option value="Philippines">Philippines</option>
                            <option value="Poland">Poland</option>
                            <option value="Portugal">Portugal</option>
                            <option value="Qatar">Qatar</option>
                            <option value="Romania">Romania</option>
                            <option value="Russia">Russia</option>
                            <option value="Rwanda">Rwanda</option>
                            <option value="Saudi Arabia">Saudi Arabia</option>
                            <option value="Senegal">Senegal</option>
                            <option value="Seychelles">Seychelles</option>
                            <option value="Sierra Leone">Sierra Leone</option>
                            <option value="Singapore">Singapore</option>
                            <option value="Slovakia">Slovakia</option>
                            <option value="Slovenia">Slovenia</option>
                            <option value="Solomon Islands">Solomon Islands</option>
                            <option value="Somalia">Somalia</option>
                            <option value="South Africa">South Africa</option>
                            <option value="South Korea">South Korea</option>
                            <option value="Spain">Spain</option>
                            <option value="Sri Lanka">Sri Lanka</option>
                            <option value="Sudan">Sudan</option>
                            <option value="Suriname">Suriname</option>
                            <option value="Swaziland">Swaziland</option>
                            <option value="Sweden">Sweden</option>
                            <option value="Switzerland">Switzerland</option>
                            <option value="Syria">Syria</option>
                            <option value="Tajikistan">Tajikistan</option>
                            <option value="Tanzania">Tanzania</option>
                            <option value="Thailand">Thailand</option>
                            <option value="Togo">Togo</option>
                            <option value="Tonga">Tonga</option>
                            <option value="Tunisia">Tunisia</option>
                            <option value="Turkey">Turkey</option>
                            <option value="Uganda">Uganda</option>
                            <option value="Ukraine">Ukraine</option>
                            <option value="United Arab Emirates">United Arab Emirates</option>
                            <option value="United Kingdom">United Kingdom</option>
                            <option value="United States">United States</option>
                            <option value="Uruguay">Uruguay</option>
                            <option value="Uzbekistan">Uzbekistan</option>
                            <option value="Vanuatu">Vanuatu</option>
                            <option value="Venezuela">Venezuela</option>
                            <option value="Vietnam">Vietnam</option>
                            <option value="Samoa">Samoa</option>
                            <option value="Yemen">Yemen</option>
                            <option value="Yougoslavia">Yougoslavia</option>
                            <option value="Zambia">Zambia</option>
                            <option value="Zimbabwe">Zimbabwe</option>
                          </select>
                          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="12" version="1" class="u-caret"><path fill="currentColor" d="M4 8L0 4h8z"></path></svg>
                        </div>
                      </div>
                      <input type="hidden" value="form-1" name="form">
                      <div class="u-align-left u-form-group u-form-submit">
                        <input type="submit" value="Submit" class="u-btn u-btn-submit u-button-style">
                      </div>
                    </form>
                  </div>
                </div>
              </div>
              <div class="u-align-left u-container-style u-layout-cell u-size-22 u-layout-cell-2">
                <div class="u-container-layout u-container-layout-2">
                  <h4 class="u-custom-font u-text u-text-3">About me</h4>
                  <div class="u-form u-form-2">
                    <form action="Account.py" method="POST" name="form2" style="padding: 10px;">
                      <div class="u-form-email u-form-group">
                        <label for="email-3faf" class="u-label">Email</label>
                        <input type="email" placeholder="Enter a valid email address" id="email-3faf" name="email" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white">
                      </div>
                      <div class="u-form-address u-form-group u-form-group-8">
                        <label for="address-343a" class="u-label">Address</label>
                        <input type="text" placeholder="Enter your adress" id="address-343a" name="address" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white">
                      </div>
                      <div class="u-form-group u-form-phone u-form-group-9">
                        <label for="phone-11e8" class="u-label">Phone</label>
                        <input type="text" pattern="\+?\d{0,3}[\s\(\-]?([0-9]{2,3})[\s\)\-]?([\s\-]?)([0-9]{3})[\s\-]?([0-9]{2})[\s\-]?([0-9]{2})" placeholder="Enter your phone (for ex. +14155552675)" id="phone-11e8" name="phoneuser" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white">
                      </div>
                      <input type="hidden" value="form-2" name="form">
                      <div class="u-align-left u-form-group u-form-submit">
                        <input type="submit" value="Submit" class="u-btn u-btn-submit u-button-style">
                      </div>
                    </form>
                  </div>
                </div>
              </div>
              <div class="u-container-style u-layout-cell u-palette-2-base u-size-18 u-layout-cell-3">
                <div class="u-container-layout u-container-layout-3">
                  <div class="u-image u-image-circle u-preserve-proportions u-image-1" alt="" data-image-width="1280" data-image-height="1280">
                  <img id="image" src="Bin/Site/Images/db68eb226ef6d9f38180e90a4a3815ffb12e90832c8c1eb3fefb0558b2f1e497a5c1261f79a9dcdbd9e7bf0670ebe1404f5fd490f2143521332114_1280.png" class="u-image u-image-circle u-preserve-proportions u-image-1" alt="" data-image-width="1280" data-image-height="1280"></div>
                  <h3 id="NAME" class="u-align-center u-custom-font u-text u-text-4"></h3>
                  <div class="u-form u-form-3">
                    <form action="Account.py" method="POST" name="form3" style="padding: 10px;">
                      <input type="hidden" id="siteId" name="siteId" value="253723268">
                      <input type="hidden" id="pageId" name="pageId" value="861623318">
                      <div class="u-form-group u-form-message">
                        <label for="message" class="u-label">Message</label>
                        <textarea placeholder="Enter your message profile" rows="4" cols="50" id="message" name="message" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white"></textarea>
                      </div>
                      <input type="hidden" value="form-3" name="form">
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
        <p class="u-align-left u-small-text u-text u-text-variant u-text-1">Copyright © 2022 Playsic Inc. All rights reserved.</p>
      </div></footer>
          <script>'''
print(html)
print(f'''var Form = document.forms.form;
          Form.elements.first_name.value = "{First_Name}";
          Form.elements.name.value = "{Name}";
          Form.elements.date.value = "{Date}";
          Form.elements.gender.value = "{Gender}";
          Form.elements.country.value = "{Country}";''')
print(f'''var Form2 = document.forms.form2;
          Form2.elements.email.value = "{Mail}";
          Form2.elements.address.value = "{Adress}";
          Form2.elements.phoneuser.value = "{Phone}";''')
print(f'document.getElementById("NAME").innerHTML = ("<b>{First_Name} {Name}<b>");')
print(f'document.getElementById("message").innerHTML = ("{Mess}");')
if Gender == "Man":
      print("document.getElementById('image').src='Bin/Site/Images/Man.png';")
else:
      print("document.getElementById('image').src='Bin/Site/Images/Woman.png';")
html = '''
    </script>
    <script>'''
print(html)
if form == "form-1" or form == "form-2" or form == "form-3":
      print("""Swal.fire(
  'Your profile has been updated !',-
  '',
  'success'
)""")
html=    '''</script>
  </body>
</html>
'''

print(html)