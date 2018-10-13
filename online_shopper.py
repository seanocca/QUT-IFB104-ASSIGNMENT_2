#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic floategrity" and Section E/2.1 "Student Code of Conduct".
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
#  matching, and Graphical User floaterface design to produce a useful
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

############Globals Variables#########################################
#Global variables for everything in the code
global file_name
global dvd_title_img_price, dvr_title_img_price, dresses_title_img_price, mobile_title_img_price
global everything, total_cost

#####################Change the American Dollar to AUD################
def price_change(us_dollar):
    global aud_dollar
    #Change us_dollar to aud_dollar as of 25/5/2017
    aud_dollar = float(us_dollar) * 1.34

##################Create Variable for HTML File#######################
file_name = 'invoice.html'

##########################Image Tags##################################
#Title Image
url_title = 'https://vignette1.wikia.nocookie.net/logopedia/images/b/bb/New-Stop-Shop-Logo-old-764896.JPG.jpeg/revision/latest?cb=20110425200502'
#First Link Roof Mount DVD Player
url_dvd = 'https://www.seicane.com/rss/catalog/category/cid/105/store_id/1/'
#Second Link Car DVR
url_dvr = 'https://www.seicane.com/rss/catalog/category/cid/158/store_id/1/'
#Third Link Womens Dresses
url_dresses = 'http://www.joomlajingle.com/rss/catalog/new/store_id/1/'
#Fourth Link mobile Phones
url_mobile = 'http://www.tigerdirect.com/xml/rsstigercat5116.xml'

##################Lists for Information Centralisation################
#Each list is for each scraped item
dvd_title_img_price = []
dvr_title_img_price = []
dresses_title_img_price = []
mobile_title_img_price = []

####Scraping all the Information From the RSS Feed####################
def find_first(addressone,addresstwo,addressthree,addressfour):
    #Assign each address to one list for better and shorter handling
    scraping = [addressone,addresstwo,addressthree,addressfour]

    #Open each url to get ready for scraping 
    #and read them so that the function can extract info
    wpage_one = urlopen(scraping[0]).read()
    wpage_two = urlopen(scraping[1]).read()
    wpage_three = urlopen(scraping[2]).read()
    wpage_four = urlopen(scraping[3]).read()

    #Scrape each title from each webpage
    dvd_title = findall('\<title\>\<\!\[CDATA\[(.*?)\]\]></title>',wpage_one)
    dvr_title = findall('<title><\!\[CDATA\[(.*?)\]\]></title>',wpage_two)
    dresses_title = findall('<title><\!\[CDATA\[(.*?)\]\]></title>',wpage_three)
    mobile_title = findall('<item><title>(.*?) -',wpage_four)

    #Scrape each image from each webpage
    dvd_img = findall('<img src="(.*?)"',wpage_one)
    dvr_img = findall('<img src="(.*?)"',wpage_two)
    dresses_img = findall('<img src="(.*?)"',wpage_three)
    mobile_img = findall('<img src="(.*?)"/>',wpage_four)

    #Scrape each price from each webpage
    dvd_price = findall('id="product\-price\-[0-9^]+">[A-z<> ="]+\$(.*?)</',wpage_one)
    dvr_price = findall('<span class="price">[A-z^]+\$(.*?)</',wpage_two)
    dresses_price = findall('id="old-price-[0-9^]+">\$(.*?)</span>',wpage_three)
    mobile_price = findall(' - \$(.*?)</title>',wpage_four)

    #Put scraped DVD information into its own list that was initialized earlier
    for dvd_iter in range(len(dvd_price)):
        dvd_title_img_price.append([dvd_title[(dvd_iter)+1],dvd_img[dvd_iter],dvd_price[dvd_iter]])

    #Put scraped DVR information into its own seperate list to be called later
    for dvr_iter in range(len(dvr_price)):
        dvr_title_img_price.append([dvr_title[(dvr_iter)+1],dvr_img[dvr_iter],dvr_price[dvr_iter]])

    #Put scraped Dresses information into a list for later access
    for dresses_iter in range(len(dresses_img)):
        dresses_title_img_price.append([dresses_title[(dresses_iter)+1],dresses_img[dresses_iter],dresses_price[dresses_iter]])

    #Put scraped Mobile information into a list for HTML input
    for mobile_iter in range(len(mobile_img)):
        mobile_title_img_price.append([mobile_title[mobile_iter],mobile_img[mobile_iter],mobile_price[mobile_iter]])   

###########Creating The GUI###########################################
#Create a TKInter window and Title it Online Shopper
online_shopper = Tk()
online_shopper.title('Online Shopper')

#Top labels
Label(online_shopper,font=('Arial',32),fg='blue',text="Welcome to Stop & Shop Online Shopping",wraplength=500).grid(row=0,column=0,pady=20)
Label(online_shopper,font=('Arial',16),fg='red',text="Step 1: Choose your Quantities").grid(row=1,column=0,pady=20)

#Create a frame to make a grid formation for the spinboxes
frame = Frame(online_shopper)
frame.grid(row=2)

#Spinbox grid within a frame within a grid to get the standard square response
Label(frame,font=('Arial',10),text="Car DVD Players").grid(row=2,column=0)
dvd = Spinbox(frame,font=('Arial'),from_=0,to=4,width=2)
dvd.grid(row=2,column=1,sticky=W)
Label(frame,font=('Arial',10),text="Car DVR Camera Recorder").grid(row=2,column=2)
dvr = Spinbox(frame,font=('Arial'),from_=0,to=12,width=2)
dvr.grid(row=2,column=3,sticky=W)
Label(frame,font=('Arial',10),text="Female Dresses").grid(row=3,column=0)
dresses = Spinbox(frame,font=('Arial'),from_=0,to=159,width=2)
dresses.grid(row=3,column=1,sticky=W)
Label(frame,font=('Arial',10),text="Mobile Phones").grid(row=3,column=2)
mobile = Spinbox(frame,font=('Arial'),from_=0,to=10,width=2)
mobile.grid(row=3,column=3,sticky=W)

#Labels beneath spinboxes for display quality
Label(online_shopper,font=('Arial',16),fg='gold',text="Step 2: When Ready, Print your Invoice").grid(row=4,column=0,pady=20)

##############Save Order Into Databse#################################
#Setup a container Variable
descripter = []

def save_order():
    #Connect to the database shoppey_trolley.db
    shop = connect('shopping_trolley.db')
    
    #Open up a cursor
    data = shop.cursor()

    #Clear the database
    deleting = """DELETE FROM Purchases"""
    data.execute(deleting)
    shop.commit()
    
    #Put all the titles and prices of the items purchased into the database
    for every in range(len(descripter)):
        #Making sure that the Title goes in the description 
        if (every == 0) or ((every % 2) == 0):
            #Write Query and commit to database 
            query = """INSERT INTO Purchases(Description, Price) VALUES ('{}', {})""".format(descripter[every],descripter[every+1])
            data.execute(query)
            shop.commit()
    
    #Check if there is an order to be saved then update progress bar depending on the result
    if len(descripter) >= 1:
        prog.config(text = 'Order Saved')
        online_shopper.update()
    else:
        prog.config(text = 'Please Place an Order')
        online_shopper.update()

    #Close the database connection
    shop.close()

################Create HTML File for the Invoice######################
def invoice():
    #Empty the HTML file
    open(file_name,'w').close()
    #Open and Create new HTML file named receipt
    receipt = open(file_name,'w')
    #Make the HTML code a global
    global setup

    #HTML Necessity Setup File
    setup = """<!DOCTYPE html><html>
    <title>Receipt</title><body><head>
    <style>
        h1 {{text-align: center;}}
        h4 {{text-align: center;}}
        h5 {{text-align: center;}}
        #respond_image {{
            width: 200px;
            height: auto;}}
        table, tr, td {{
            border: 3px solid black;
            width: 25%;
            text-align: center;
            font-family: arial;
            font-size: 20px;}}
    </style></head>
    <h1>Stop & Shop Receipt</h1>
    <center><img src = '{}' height = 200 width = 400></center>"""

    #Get the values entered by the user from the GUI
    dvd_num = float(dvd.get())
    dvr_num = float(dvr.get())
    dresses_num = float(dresses.get())
    mobile_num = float(mobile.get())

    #Open the receipt file
    receipt = open(file_name,'w')

    #Check to see if any variables have been selected
    if dvd_num == 0.0 and dvr_num == 0.0 and dresses_num == 0.0 and mobile_num == 0.0:
        #Update setup HTML to demonstrate that nothing has been purchased
        setup = setup + """<h4>There is No Charge</h4>\n<h4>Please Choose an Item to Purchase</h4>"""
        setup = setup.format(url_title)
        receipt.write(setup)
        #Update progress bar to show no item has been chosen
        prog.config(text = 'Please Choose an Item')
        online_shopper.update()
    else:
        #Update progress bar to show images downloading
        prog.config(text = 'Downloading Images...')
        online_shopper.update()

        #Scrape all the data for the rest of the HTML file
        find_first(url_dvd,url_dvr,url_dresses,url_mobile)

        ################Write Up HTML Code for File Creation##########
        def main_html():
            global setup
            total_cost = 0
            #Enter last line of real invoice
            setup = setup + """<h4>Your Total Invoice is: ${}</h4>\n<table align = 'center'>"""

            ##Get The Scraped Data and Insert it Into The HTML File###
            def write_to_html(one,two,three):
                global setup
                write_to = """\n<tr>\n<td
<h5>%s</h5><br>
<img src='%s', alt= 'image missing dc' id= 'respond_image'><br>
<p>The cost: $%s</p>\n</td>\n</tr>""" % (one,two,three)
                setup = setup + write_to

                #Update progress bar
                prog.config(text = 'Writing HTML...')
                online_shopper.update()

            #Get the scraped data and format to into the HTML code
            if dvd_num > 0.0:
                for redo in range(int(dvd_num)):
                    dvd_stuff = dvd_title_img_price[redo]
                    price_change(dvd_stuff[2])
                    write_to_html(dvd_stuff[0],dvd_stuff[1],dvd_stuff[2])
                    #Put into list for the database
                    descripter.append(dvd_stuff[0])
                    descripter.append(aud_dollar)
                    #Update Total Cost
                    total_cost = total_cost + float(aud_dollar)

            #Get the scraped data and format to into the HTML code
            if dvr_num > 0.0:
                for redo in range(int(dvr_num)):
                    dvr_stuff = dvr_title_img_price[redo]
                    price_change(dvr_stuff[2])
                    write_to_html(dvr_stuff[0],dvr_stuff[1],dvr_stuff[2])
                    #Put into list for the database
                    descripter.append(dvr_stuff[0])
                    descripter.append(aud_dollar)
                    #Update Total Cost
                    total_cost = total_cost + float(aud_dollar) 

            #Get the scraped data and format to into the HTML code
            if dresses_num > 0.0:
                for redo in range(int(dvd_num)):
                    dresses_stuff = dresses_title_img_price[redo]
                    write_to_html(dresses_stuff[0],dresses_stuff[1],dresses_stuff[2])
                    #Put into list for the database
                    descripter.append(dresses_stuff[0])
                    descripter.append(dresses_stuff[2])
                    #Update Total Cost
                    total_cost = total_cost + float(dresses_stuff[2])

            #Get the scraped data and format to into the HTML code
            if mobile_num > 0.0:
                for redo in range(int(mobile_num)):
                    mobile_stuff = mobile_title_img_price[redo]
                    write_to_html(mobile_stuff[0],mobile_stuff[1],mobile_stuff[2])
                    #Put into list for the database
                    descripter.append(mobile_stuff[0])
                    descripter.append(mobile_stuff[2])
                    #Update Total Cost
                    total_cost = total_cost + float(mobile_stuff[2])

            #Put the values into the HTML code
            setup = setup.format(url_title,str(total_cost))

            #Write up HTML
            receipt.write(setup)

            #Add links for RSS feeds and Title image
            receipt.write("""</table>
<p align='center'>It's What Yah Get Links</p>
<ol align = 'center' style="list-style: none">
<li><a href = '{}'>Title Image</a><br></li>
<li><a href = '{}'>DVD Players</a><br></li>
<li><a href = '{}'>DVR Recorder's</a><br></li>
<li><a href = '{}'>Dresses</a><br></li>
<li><a href = '{}'>Mobile Phones</a><br></li>
</ol>""".format(url_title,url_dvd,url_dvr,url_dresses,url_mobile))
        
        #Enter HTML opener
        main_html()
        #Update progress bar
        prog.config(text = 'Done!')
        online_shopper.update()
        #End HTML code
        receipt.write("\n</body>\n</html>")
        receipt.close()

#####################Finish Creating The GUI##########################
Button(online_shopper,font=('Arial'),text="Invoice",command=invoice).grid(row=5,column=0)
Label(online_shopper,font=('Arial',16),fg='dark green',text="Step 3: Watch your Order's Progress").grid(row=6,column=0,pady=10)

prog = Label(online_shopper,font=('Arial',12),fg='red',text='Ready...')
prog.grid(row=7,column=0,pady=10)

Label(online_shopper,font=('Arial',16),fg='dark green',text="Step 4: Save Your Order").grid(row=8,column=0,pady=10)
Button(online_shopper,font=('Arial'),text="Save Order",command=save_order).grid(row=9,column=0,pady=10)

#End TKinter GUI loop
online_shopper.mainloop()