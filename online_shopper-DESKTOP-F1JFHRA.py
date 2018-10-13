
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10000569  
#    Student name: SEAN O'CONNELL
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  Online Shopper
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for aggregating product data published by a variety of
#  online shops.  See the instruction sheet accompanying this file
#  for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution.)
from urllib import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from Tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression.  (You do NOT need to
# use these functions in your solution, although you will find
# it difficult to produce a robust solution without using
# regular expressions.)
from re import findall, finditer

# Import the standard SQLite functions just in case they're
# needed.
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.

# Name of the invoice file. To simplify marking, your program should
# produce its results using this file name.
global file_name

import os
import webbrowser

file_name = 'invoice.html'
receipt = open(file_name,'w')

global dc_cost,bt_cost,ww_cost,cm_cost,total_cost
global dc_price,bt_price,ww_price,cm_price
global title_img_price
global dvd_stuff,dvr_stuff,dresses_stuff,mobile_stuff

dc_price = 2.87
bt_price = 15.98
ww_price = 159.54
cm_price = 25.99

dc_there = 0
bt_there = 0
ww_there = 0
cm_there = 0


#First Link Roof Mount DVD Player
url_one = 'https://www.seicane.com/rss/catalog/category/cid/105/store_id/1/'

#Second Link Car DVR
url_two = 'https://www.seicane.com/rss/catalog/category/cid/158/store_id/1/'

#Third Link Womens Dresses
url_three = 'http://www.joomlajingle.com/rss/catalog/new/store_id/1/'

#Fourth Link mobile Phones
url_four = 'http://www.tigerdirect.com/xml/rsstigercat5116.xml'

title_img_price = []

def find_first(addressone,addresstwo,addressthree,addressfour):
    scraping = [addressone,addresstwo,addressthree,addressfour]

    wpage_one = urlopen(scraping[0]).read()
    wpage_two = urlopen(scraping[1]).read()
    wpage_three = urlopen(scraping[2]).read()
    wpage_four = urlopen(scraping[3]).read()

    dvd_title = findall('<title><![CDATA[(.*?)]]></title>',wpage_one)
    dvr_title = findall('<title><![CDATA[(.*?)]]></title>',wpage_two)
    dresses_title = findall('<title><![CDATA[(.*?)]]></title>',wpage_three)
    mobile_title = findall('<item><title>(.*?) -',wpage_four)

    dvd_img = findall('<img src="(.*?)"',wpage_one)
    dvr_img = findall('<img src="(.*?)"',wpage_two)
    dresses_img = findall('<img src="(.*?)"',wpage_three)
    mobile_img = findall('<img src="(.*?)"/>',wpage_four)

    dvd_price = findall('id="product\-price\-[0-9^]+">(.*?)</',wpage_one)
    dvr_price = findall('<span class="price">(.*?)</',wpage_two)
    dresses_price = findall('id="old-price-[0-9^]+">(.*?)</span>',wpage_three)
    mobile_price = findall(' - \$(.*?)</title>',wpage_four)

    title_img_price.append([dvd_title,dvd_img,dvd_price])
    title_img_price.append([dvr_title,dvr_img,dvr_price])
    title_img_price.append([dresses_title,dresses_img,dresses_price])
    title_img_price.append([mobile_title,mobile_img,mobile_price])
    
find_first(url_one,url_two,url_three,url_four)

##DVD Attributes
dvd_stuff = title_img_price[0]

##DVR Attributes
dvr_stuff = title_img_price[1]

##Dresses Attributes
dresses_stuff = title_img_price[2]

##Mobile Attributes
mobile_stuff = title_img_price[3]

##Denim Cap
dc_pic = 'http://ak1.polyvoreimg.com/cgi/img-thing/size/l/tid/207088808.jpg'

##Basic Tee
bt_pic = 'http://scene7.zumiez.com/is/image/zumiez/pdp_hero/EPTM.-Basic-Elongated-Drop-Tail-Long-T-Shirt-_254292-front.jpg'

##Wrist Watch
ww_pic = 'https://images-na.ssl-images-amazon.com/images/I/41PJNuJnAKL._AC_SR201,266_.jpg'

##Computer Mouse
cm_pic = 'https://assets.logitech.com/assets/64362/3/wireless-mouse-m325.png'

online_shopper = Tk()

online_shopper.title('Online Shopper')

Label(online_shopper,font=('Arial',32),fg='blue',text="Welcome to 'It's What Yah Get' Online Shopping",wraplength=500).grid(row=0,column=0,pady=20)

Label(online_shopper,font=('Arial',16),fg='red',text="Step 1: Choose your Quantities").grid(row=1,column=0,pady=20)

frame = Frame(online_shopper)
frame.grid(row=2)

Label(frame,font=('Arial',10),text="Car DVD Players").grid(row=2,column=0)
dvd = Spinbox(frame,font=('Arial'),from_=0,to=99,width=2)
dvd.grid(row=2,column=1,sticky=W)
Label(frame,font=('Arial',10),text="Car DVR Camera Recorder").grid(row=2,column=2)
dvr = Spinbox(frame,font=('Arial'),from_=0,to=99,width=2)
dvr.grid(row=2,column=3,sticky=W)

Label(frame,font=('Arial',10),text="Female Dresses").grid(row=3,column=0)
dresses = Spinbox(frame,font=('Arial'),from_=0,to=99,width=2)
dresses.grid(row=3,column=1,sticky=W)
Label(frame,font=('Arial',10),text="Mobile Phones").grid(row=3,column=2)
mobile = Spinbox(frame,font=('Arial'),from_=0,to=99,width=2)
mobile.grid(row=3,column=3,sticky=W)

Label(online_shopper,font=('Arial',16),fg='gold',text="Step 2: When Ready, Print your Invoice").grid(row=4,column=0,pady=20)

def invoice():

    dvd_cost = float(dvd.get()) * dvd_stuff[2]
    dvr_cost = float(dvr.get()) * dvr_stuff[2]
    dresses_cost = float(dresses.get()) * dresses_stuff[2]
    mobile_cost = float(mobile.get()) * mobile_stuff[2]

    total_cost = dvd_cost + dvr_cost + dresses_cost + mobile_cost

    print total_cost

    prog.config(text = 'Downloading Images...')

    #Get the images above from the websites using Regex

    setup = """<!DOCTYPE html><html>
<title>Receipt</title>
<body>
<head>It's What Yah Get Trading Co. Invoice</head><br>
<h1>Your Total Invoice is: $%s</h1>
    """ % (total_cost)
    receipt.write(setup)

    def pic_checker():
        global dc_there,bt_there,ww_there,cm_there

        if dc_cost > 0.0 and dc_there == 0:
            dc_write_to_html = """
<h2>Denim Cap</h2><br>
<img src='%s', alt= 'image missing dc'><br>
<p>The price: $%s</p><br>
<p>The cost: $%s</p><br>""" % (dc_pic,dc_price,dc_cost)
            receipt.write(dc_write_to_html)
            dc_there = dc_there + 1

        if bt_cost > 0.0 and bt_there == 0:
            bt_write_to_html = """
<h2>Basic Tee</h2><br>
<img src='%s', alt= 'image missing bt'><br>
<p>The price: $%s</p><br>
<p>The cost: $%s</p><br>""" % (bt_pic,bt_price,bt_cost)
            receipt.write(bt_write_to_html)
            bt_there = bt_there + 1   

        if ww_cost > 0.0 and ww_there == 0:
            ww_write_to_html = """
<h2>Wrist Watch</h2><br>
<img src='%s', alt= 'image missing bt'><br>
<p>The price: $%s</p><br>
<p>The cost: $%s</p><br>""" % (ww_pic,ww_price,ww_cost)
            receipt.write(ww_write_to_html)
            ww_there = ww_there + 1

        if cm_cost > 0.0 and cm_there == 0:
            cm_write_to_html = """
<h2>Computer Mouse</h2><br>
<img src='%s', alt= 'image missing bt'><br>
<p>The price: $%s</p><br>
<p>The cost: $%s</p><br>""" % (cm_pic,cm_price,cm_cost)
            receipt.write(cm_write_to_html)
            cm_there = cm_there + 1

    for printer in range(5):
        pic_checker()

    receipt.write("</body>\n</html>")

    receipt.close()

    webbrowser.open('file://' + os.path.realpath(file_name))

    prog.config(text = 'Done!')
     
Button(online_shopper,font=('Arial'),text="Invoice",command=invoice).grid(row=5,column=0)

Label(online_shopper,font=('Arial',16),fg='dark green',text="Step 3: Watch your Order's Progress").grid(row=6,column=0,pady=20)

prog = Label(online_shopper,font=('Arial',12),fg='red',text='Ready...')
prog.grid(row=7,column=0, pady = 20)

online_shopper.mainloop()