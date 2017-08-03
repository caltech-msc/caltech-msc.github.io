#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: AliWang
This script accesses everyones information on Google Sheets and turns it into html for the website.
Note: There are definitely more efficient ways to do this, but my Python knowledge is currently limited; will be updated as soon as I learn more about using web data with Python
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
sheet = file.open("Article Information").sheet1 # open sheet

os.remove("index.html")
print("Old file removed.")


f = open('index.html','w')
print("New index file created. Inputting information...")


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
    <section id="header" class="header-one parallax-section">
    <div class="container">
    <div class="row">
    
    <div class="col-md-offset-3 col-md-6 col-sm-offset-3 col-sm-8">
    <div class="header-thumb">
    <h1>@MSC:
    <a href="" class="typewrite" data-period="2000" data-type='[ "new research on materials", "testing out protein structures", "new site still updating"]'>
    
    <span class="wrap"></span>
    
    </a>
    </h1>
    </div>
    </div>
    
    </div>
    </div>
    <div class ="container">
    <div class ="row">
    <div class="col-md-offset-3 col-md-6 col-sm-offset-3 col-sm-8">
    
    <a href="#blog" class="btn btn-default page-scroll">Learn More</a>
    
    </div>
    </div>
    </div>
    </section>
    
    <section id = "colorbar" class="wow fadeIn" data-wow-delay="0.5"></section>
    
    <!-- A little a bit about MSC section
    ================================================== -->
    <section id="blog">
    <div class="container">
    
    <div class="row">
    
    <!-- This section is the beginning text of the website. Please edit inside the tags. -->
    <div class="wow fadeInUp col-md-12 col-sm-12" data-wow-delay="0.5s">
    <h1>Bridging the gap between theory and application</h1>
    <p>There has long been the dream that theory (quantum mechanics, molecular dynamics, and statistical mechanics) properly incorporated into computer software could be used to design new drugs, new catalysts.........</p>
    </div>
    
    </div>
    </div>
    </section>
    
    <section id = "colorbar" class="wow fadeIn" data-wow-delay="0.5"></section>
    
    <!-- Research section
    ================================================== -->
    
    <section id="header" class="header-two wow fadeIn parallax-section" data-wow-delay="0.5">
    <div class="container">
    <div class="row">
    
    <div class="col-md-offset-3 col-md-6 col-sm-offset-2 col-sm-8">
    <div class="header-thumb">
    <h1 class="wow fadeIn" data-wow-delay="0.5s">Research</h1>
    <h3 class="wow fadeInUp" data-wow-delay="0.5s">Lastest News and Articles</h3>
    </div>
    </div>
    
    </div>
    </div>
    </section>
    
    
    '''
f.write(first)



number =  int(sheet.acell('C1').value)
if number >= 3:
    for i in range(number,number+3):
    	row = sheet.row_values(i)
    	name = row[1]
    	email = row[2]
        title = row[3]
        date = row[4]
        if row[5] == "Image":
            image= row[6]
        else:
            slides = row[7]
        paragraph = row[8]
        URL = row[9]


        if i%2 = 0:
            f.write('<!-- TEMPLATE START')
            f.write('    ================================================== -->')
            f.write('<section id="blog">')
            f.write('    <div class="container">')
            f.write('        <div class="row">')
            f.write('            <div class="wow fadeInUp col-md-4 col-sm-4" data-wow-delay="1s">')
            f.write('                <div class="blog-thumb">')
            f.write('                    <a href="single-post.html"><h1>' + title + '</h1></a>')
            f.write('                        <div class="post-format">')
            f.write('                        <span>By <a href="mailto:' + email + '">' + name + '</a></span>')
            f.write('                        <span><i class="fa fa-date"></i> ' + date + '</span>')
            f.write('                            </div>')
            f.write('                                <p>' + paragraph + '</p>')
                        
            f.write('                <a href="' + URL + '" class="btn btn-default">Full Article</a>')
            f.write('                    </div>')
            f.write('                        </div>')
            if row[5]== "Image":
                f.write('   <div class="wow fadeInUp col-md-8 col-sm-8" data-wow-delay="0.5s">')
                f.write('   <img src="' + image + '" class="img-responsive">')
                f.write('   </div>')
            else:
                f.write('   <div class="wow fadeInUp col-md-8 col-sm-8" data-wow-delay="0.5s">')
                f.write('   ' + slides)
                f.write('   </div>')
            f.write('      </div>')
            f.write('</div>')
            f.write('</section>')
            f.write('<!-- TEMPLATE END')
            f.write('    ================================================== -->')
        
    # for the other post style
        else:
            f.write('<!-- TEMPLATE START')
            f.write('    ================================================== -->')
            f.write('<section id="blog" class= "grey">')
            f.write('    <div class="container">')
            f.write('        <div class="row">')
            if row[5]== "Image":
                f.write('   <div class="wow fadeInUp col-md-8 col-sm-8" data-wow-delay="0.5s">')
                f.write('   <img src="' + image + '" class="img-responsive">')
                f.write('   </div>')
            else:
                f.write('   <div class="wow fadeInUp col-md-8 col-sm-8" data-wow-delay="0.5s">')
                f.write('   ' + slides)
                f.write('   </div>')
            f.write('            <div class="wow fadeInUp col-md-4 col-sm-4" data-wow-delay="1s">')
            f.write('                <div class="blog-thumb">')
            f.write('                    <a href="single-post.html"><h1>' + title + '</h1></a>')
            f.write('                        <div class="post-format">')
            f.write('                        <span>By <a href="mailto:' + email + '">' + name + '</a></span>')
            f.write('                        <span><i class="fa fa-date"></i> ' + date + '</span>')
            f.write('                            </div>')
            f.write('                                <p>' + paragraph + '</p>')
                        
            f.write('                <a href="' + URL + '" class="btn btn-default">Full Article</a>')
            f.write('                    </div>')
            f.write('                        </div>')
            
            f.write('      </div>')
            f.write('</div>')
            f.write('</section>')
            f.write('<!-- TEMPLATE END')
            f.write('    ================================================== -->')

        
second = '''
			
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



os.remove("research.html")
print("Old file removed.")


r = open('index.html','w')
print("New research file created. Inputting information... (this will take a while if the archive is very large)")

first1 = '''
<!DOCTYPE html>
<html lang="en">
<head>
<!--
Using Pure Mix template w/ alterations
http://www.tooplate.com/view/2082-pure-mix
-->
<script src="js/head.js"></script>
</head>

<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">
<script src="js/nav.js"></script>


<!-- Header section
================================================== -->
<section id="header" class="header-two">
    <div class="container">
        <div class="row">

            <div class="col-md-offset-3 col-md-6 col-sm-offset-2 col-sm-8">
          <div class="header-thumb">
              <h1 class="wow fadeIn" data-wow-delay="0.4s">Research Archive</h1>
          </div>
            </div>

        </div>
    </div>      
</section>



<!-- Blog section
================================================== -->
<section id="blog">

   <div class="container">
      <div class="row">

    <div class="sidebar col-xs-4">

            <div class="wow fadeInUp col-md-12 col-sm-12" data-wow-delay=".4s">
                <h1>______________</h1>
                <h1>FEATURED RESEARCH</h1>
                <p>Hello there! This is an archive of featured posts that appear on the front home page of the MSC. Please feel free to browse!</p>
             </div>
'''
r.write(first1)

number =  int(sheet.acell('C1').value)
if number >= 6:
    for i in range(number+3,number+6):
        row = sheet.row_values(i)
        name = row[1]
        email = row[2]
        title = row[3]
        date = row[4]
        if row[5] == "Image":
            image= row[6]
        else:
            slides = row[7]
        paragraph = row[8]
        URL = row[9]

            r.write('<div class="wow fadeInUp col-md-12 col-sm-12" data-wow-delay=".4s">')
            r.write('      <div class="blog-thumb">')
            if row[5]== "Image":
                r.write('         <a href="' + URL + '"><img src="' + image + '" class="img-responsive" alt="Blog"></a>')
            else:
                r.write('   ' + slides)
            r.write('         <a href="' + URL + '"><h1>' + title + '</h1></a>')
            r.write('            <div class="post-format">')
            r.write('              <span>By <a href="mailto:' + email + '">' + name + '</a></span>')
            r.write('              <span><i class="fa fa-date"></i> ' + date + '</span>')
            r.write('           </div>')
            r.write('           <p>' + paragraph + '</p>')
            r.write('           <a href="' + URL + '" class="btn btn-default">Details</a>')
            r.write('      </div>')
            r.write('</div>')
            

#need to write the list format


second2 = '''
    </div>
    <div class= "main col-xs-8">
    '''
r.write(second2)

if number >= 3:
    for i in range(number,number+3):
        row = sheet.row_values(i)
        name = row[1]
        email = row[2]
        title = row[3]
        date = row[4]
        if row[5] == "Image":
            image= row[6]
        else:
            slides = row[7]
        paragraph = row[8]
        URL = row[9]

            r.write('<div class="wow fadeInUp col-md-12 col-sm-12" data-wow-delay=".4s">')
            r.write('      <div class="blog-thumb">')
            if row[5]== "Image":
                r.write('         <a href="' + URL + '"><img src="' + image + '" class="img-responsive" alt="Blog"></a>')
            else:
                r.write('   ' + slides)
            r.write('         <a href="' + URL + '"><h1>' + title + '</h1></a>')
            r.write('            <div class="post-format">')
            r.write('              <span>By <a href="mailto:' + email + '">' + name + '</a></span>')
            r.write('              <span><i class="fa fa-date"></i> ' + date + '</span>')
            r.write('           </div>')
            r.write('           <p>' + paragraph + '</p>')
            r.write('           <a href="' + URL + '" class="btn btn-default">Details</a>')
            r.write('      </div>')
            r.write('</div>')


closing = '''
        
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
r.write(closing)


# UPDATING TIME STAMP
sheet.update_acell('A1', 'Last updated: '+ time.strftime("%d/%m/%Y")+ ' ' + time.strftime("%H:%M:%S"))
print('Update successful.')

f.close()
r.close()
