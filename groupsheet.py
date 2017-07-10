#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: AliWang
This script accesses everyones information on Google Sheets and turns it into html for the website.
"""
import glob
import os
import json
import time
import gspread
from oauth2client.client import SignedJwtAssertionCredentials


json_key = json.load(open('creds.json')) # json credentials you downloaded earlier
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

file = gspread.authorize(credentials) # authenticate with Google
sheet = file.open("MSC group info").sheet1 # open sheet


os.remove("group.html")
print("Old file removed.")


f = open('group.html','w')
print("New file created. Inputting information...")


first = '''
<!DOCTYPE html>
<html lang="en">
<head>
<!--
Using Pure Mix template w/ alterations
http://www.tooplate.com/view/2082-pure-mix
-->
<script src="js/head.js"></script>
</head>

<!-- Header section
================================================== -->
<section id="header" class="header-two">
	<div class="container">
		<div class="row">

			<div class="col-md-offset-3 col-md-6 col-sm-offset-2 col-sm-8">
          <div class="header-thumb">
              <h1 class="wow fadeIn" data-wow-delay="1.6s">Meet the Group</h1>
              <h3 class="wow fadeInUp" data-wow-delay="1.9s">collaboration under different perspectives</h3>
          </div>
			</div>

		</div>
	</div>		
</section>


<!-- Portfolio section
================================================== -->
<section id="portfolio">
   <div class="container">
      <div class="row">

         <div class="col-md-12 col-sm-12">
            
               <!-- iso section -->
               <div class="iso-section wow fadeInUp" data-wow-delay="2.0s">

                        <!-- iso box section -->
                        <div class="iso-box-section wow fadeInUp" data-wow-delay="1s">
                           <div class="iso-box-wrapper col4-iso-box">


'''
f.write(first)



people =  int(sheet.acell('E1').value)
for i in range(3,3+people):
	row = sheet.row_values(i)
	name = row[2] + ' ' + row[1]
	email = row[3]
	cellTF = row[5]
	if cellTF == 'Yes':
	    cell = row[4]
	pfp = row[7]
	if row[6] == 'Google Drive':
		pfp = 'https://drive.google.com/uc?id=' + row[7]
	if row[6] == 'None':
		pfp = 'images/personalpics/nopic.png'
	info = row[8]
	if row[9] != "":
		personal = row[9]
	if row[10] != "":
		group = row[10]
	f.write('                           <!-- ' + name + ' TEMPLATE START -->\n')
	f.write('                           <div class="iso-box col-md-3 col-sm-6">\n')
	f.write('                                 <div class="portfolio-thumb">\n')
	f.write('                                    <!-- image link -->\n')
	f.write('                                    <img src="' + pfp + '" class="img-responsive" alt="Portfolio" class="pfp">\n')
	f.write('                                       <div class="portfolio-overlay">\n')
	f.write('                                            <div class="portfolio-item">\n')
	f.write('                                                  <!-- Items here will be displayed by hovering over image -->\n')
	if cellTF == 'Yes':
	    f.write('                                                  <h2>' + cell + '</h2>\n')
	    del cell
	f.write('                                                  <h2><a href="mailto:' + email + '">email</a></h2>\n')
	if row[9] != "":
		f.write('                                                  <h2><a href="' + personal + '">Personal Page</a></h2>\n')
		del personal
	if row[10] != "":
		f.write('                                                  <h2><a href="' + group + '">Group Page</a></h2>\n')
		del group
	f.write('                                            </div>\n')
	f.write('                                       </div>\n')
	f.write('                                 </div>\n')
	f.write('                                 <!-- Items here will be displayed under picture -->\n')
	f.write('                                 <h6>' + name + '</h6>\n')
	f.write('                                 <h5>' + info + '</h5>\n')
	f.write('                                 <h5><a href="mailto:' + email + '">' + email + '</a></h5>\n')
	f.write('                              </div>\n')
	f.write('                              <!-- TEMPLATE END -->\n')

second = '''
								</div>
                        </div>

               </div>

         </div>

      </div>
   </div>
</section>

<!-- Footer section
================================================== -->
<script src="js/footer.js"></script>

<!-- Javascript 
================================================== -->
<script src="js/jquery.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/isotope.js"></script>
<script src="js/imagesloaded.min.js"></script>
<script src="js/wow.min.js"></script>
<script src="js/custom.js"></script>
<!-- Plugin JavaScript -->
<script src="js/jquery.easing.min.js"></script>
<!-- Custom Theme JavaScript
<script src="js/theme.js"></script>
-->

</body>
</html>
'''
f.write(second)

# UPDATING TIME STAMP
sheet.update_acell('A1', 'Last updated: '+ time.strftime("%d/%m/%Y")+ ' ' + time.strftime("%H:%M:%S"))
print('Update successful.')

f.close()