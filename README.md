[![Mock-up](static/readme/mock-up.png)](https://github.com/StephenJ2020/Sportmaster/index.html) 

[Sportmaster - Live Site](https://github.com/StephenJ2020/Sportmaster/index.html)  

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)    
   
 
# Project Overview 
___ 
## Project Description   
**Code Institute: Full Stack Frameworks with Django - Milestone 4 Project**   
   
The Milestone 4 project assignment is to build a full-stack site based around business logic used to control a centrally-owned dataset.  To set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service. I have the option to choose from one of the following two scenarios or to come up with my own idea:   
. Build a ﬁtness subscription application     
. Build a site to sell your graphic design services   
    
I have decided to create an eCommerce site for a local sports shop called Sportmaster.  This is a small family run business who don't currently have a website but they did use Facebook during the various pandemic related lockdowns to offer a "click & collect" service.  This highlighted to me their clear need for a fully functioning eCommerce website.
   
## Project Requirements   
 
### Main Technologies   
. HTML, CSS, JavaScript, Python+Django    
  
. Relational database (recommending MySQL or Postgres)  
  
. Stripe payments    
  
. Additional libraries and APIs    
          
  
### Mandatory Requirements       
1. Django Full Stack Project: Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain.   
2. Multiple Apps: The project must be a brand new Django project, composed of multiple apps (an app for each potentially reusable component in your project).   
3. Data Modeling: Put some effort into designing a relational database schema well-suited for your domain. Make sure to put some thought into the relationships between entities. Create at least 2 custom django models beyond the examples shown on the course (changing the field names of the miniproject models is not customisation)   
4. User Authentication: The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. e.g., a user would have to register to persist their shopping cart between sessions (otherwise it would be lost).    
5. User Interaction: Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).   
6. Use of Stripe: At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout or single payments, or donations, etc. After paying successfully, the user would then gain access to additional functionality/content on the site. Note that for this project you should use Stripe's test functionality, rather than actual live payments.   
7. Structure and Navigation: Incorporate a main navigation menu and structured layout (you might want to use Bootstrap to accomplish this).   
8. Use of JavaScript: The frontend should contain some JavaScript logic you have written to enhance the user experience.   
9. Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.   
10. Version Control: Use Git & GitHub for version control.   
11. Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.   
12. Deployment: Deploy the final version of your code to a hosting platform such as Heroku.    
13. Security: Make sure to not include any passwords or secret keys in the project repository. Make sure to turn off the Django DEBUG mode, which could expose secrets.   
        
          
            
    
# Sportmaster  
------  
## [Table of Contents](#table-of-contents)

- [UX](#ux)
  * [Strategy](#strategy)
  * [User Stories](#user-stories)
  * [Scope](#scope)
  * [Structure](#structure)
  * [Skeleton](#skeleton)
  * [Surface](#surface)
    + [Color Scheme](#color-scheme)
    + [Typography](#typography)
    + [Imagery](#imagery)
- [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks, Libraries, Programs & Platforms Used:](#frameworks--libraries--programs---platforms-used-)
- [Features](#features)
  * [Implemented Features](#implemented-features)
  * [Future Features](#future-features)
- [Bugs & Fixes](#bugs---fixes)
- [Deployment](#deployment)
  * [Deployment Steps](#deployment-steps)
  * [Making a clone to run locally](#making-a-clone-to-run-locally)
  * [How to Fork the respository](#how-to-fork-the-respository)
  * [Making a Local Clone](#making-a-local-clone)
- [Testing](#testing)
  * [Code Validity](#code-validity)
  * [Testing User Stories](#testing-user-stories)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)   
  

# UX
___
## Strategy

* **Project Goals**
    * To create a fully functioning eCommerce site for Sportmaster, a local sports shop in Celbridge, co. Kildare.  
    * To allow users to easily view, filter and search for any item available from this shop.  
    * To allow users to make a safe & secure purchase as conveniently as possible.  
    * To allow users to create a user profile to keep track of their order history and to speed up the purchase process for future purchases.  

* **Business Goals**   
    * To offer their existing customers an alternative to instore shopping as an added convenience.  
    * To have a clean, fresh, modern, professional looking website that can be used as a marketing tool to highlight their range of products to potential new customers.
    * To increase their sales by reaching new customers from outside their immediate physical location.

* **Target audience**
    * The primary target audience are sports enthusiasts in the wider Celbridge and North Kildare area.
    * The secondary target audience are sports enthusiasts from outside of the shops physical location but primarily within Ireland.  


## User Stories

* **As a first time user I want to be able to:**  

    * Clearly understand the purpose of the website.  
    * Easily navigate around the website. 
    * View all the products the website is selling. 
    * Filter products by category. 
    * Filter products by price or alphabetical order.
    * Search for a specific product. 
    * View detailed information about each individual products on a separate page. 
    * Choose the size, change the quantity and add a product to a shopping basket.
    * View a full list of items within the shopping basket with a breakdown of the individual costs.
    * View, update & remove products within my shopping basket. 
    * Easily see in the Navbar the current total of any items within the shopping basket.  
    * Securely checkout and purchase the products within my shopping basket. 
    * Receive an order confirmation on-screen and by email upon completion of my purchase.
    * Register and create a user profile.   
    * Contact the stores owners if I have a query.

   
* **As a returning user I want to be able to:**  
    * Login and out of the website with ease. 
    * View my user profile. 
    * Save default delivery details in order to speed up future purchases.   
    * Update my default delivery details.  
    * View my order history. 
  
  
* **As the site owner I want:**
    * Customers to be able to view the full list of products available for purchase.  
    * Customers to be able to filter products by category, price or alphabetical order.  
    * Customers to be able to select and purchase products as quick & easily as possible.  
    * Customers to be able to add, edit, update or delete products within their shopping basket.
    * Customers to be able to read product reviews prior to making a purchase.  
    * Customers to be able to write product reviews after making a purchase.  
    * Customers to be able to read our product blog about new or featured products.  
    * To be able to maintain & update the website via an Admin panel.  
    * To be able to add, edit, update or delete products from the website.  
    * To be able to add, edit, update or delete blog posts from the website.  
  

[:top:](#Sportmaster)

## Scope  
------  
* 

  
## Structure  
------  
The app consists of ........  
  
## Skeleton
------  
* 
  
  
[:top:](#Sportmaster)
  

## Surface 
-----
### Color Scheme  
  
I have chosen a very bright and vibrant colour palette to reflect the active and sporty nature of the products being sold via the site by Sportmaster.  Plus the sporting colours of the local Celbridge G.A.A. and football teams are white and blue so my colour scheme reflects this.  
![color palette](./static/readme/colour-palette.png)  
To create the color palette I used [Coolors](https://coolors.co/).  



### Typography

* 
  
### Imagery  

**(imagery choice goes here)**  
  
  
  
# Technologies Used  
------  
## Languages
 

## Frameworks, Libraries, Programs & Platforms Used:   



[:top:](#Sportmaster)

# Features  
------  

## Implemented Features
*   

  
  
## Future Features
  

  
  
# Bugs & Fixes  
------  
**Bugs and fixes to go here**  

* Dropdown menus in Navbar not working:  
 - I had been using the Bootstrap 4 classes rather than the updated Bootstrap 5 classes.  
   - Thankfully I found a very helpful post on Slack by Vera which made me realise my error.  
   ![Slack Post](static/readme/bug-data-bs-toggle.png)  
  
* Media files not loading after deployment to Heroku and AWS:  
 - I needed to update the src file path from /media/image-name.jpg to {{ MEDIA_URL }}image-name.jpg  
   - I found the solution to this bug on slack.  
   ![Slack Post](static/readme/load-media-images.png)  

* jQuery not working properly with Bootstrap 5:  
 - The increase / decrease button and the update and remove buttons in the shopping bag wouldn't work properly.  
  - I search Slack for solutions and I looked at the Bootstrap documentation but I couldn't find a suitable solution. It appearead from Slack that many students have faced the same issue and that many had choosen to remove the increase / decrease buttons on desktop devices as their solution as the issue seems to be a duplicate ID with the Mobile Navbar.  
  I chose to strip out Bootstrap 5 and revert to Bootstrap 4 as per the Boutigue Ado Walk-Through project.  
    
* CountyField on Models.py in checkout app cause a migration error:  
 -   
  - https://github.com/saleor/saleor/issues/5352  
    https://pypi.org/project/django-countries/#countryfield  
    https://pythonrepo.com/repo/SmileyChris-django-countries-python-django-utilities  
    https://stackoverflow.com/questions/8484689/django-form-database-error-value-too-long-for-type-character-varying4 
        


  
[:top:](#Sportmaster)

# Deployment  
------  
  
## Deployment Steps  
  
This project was deployed to ..........
  
  
## Making a clone to run locally  
  
It is important to note that this project will not run locally unless an env.py file has been set up by the user which contains the IP, PORT, MONGO_DBNAME, MONGO_URI and SECRET_KEY which have all been kept secret in keeping with best security practices.  
  
1. Log into GitHub.  
2. Select the [respository](https://github.com/StephenJ2020/Sportmaster).    
3. Click the Code dropdown button next to the green Gitpod button.  
4. Download ZIP file and unpackage locally and open with IDE. Alternatively copy the URL in the HTTPS box.  
6. Type 'git clone' and paste the copied URL.  
7. Press Enter. A local clone will be created.  
  
Once the project been loaded into the IDE it is necessary to install the necessary requirements which can be done by typing the following command.  
  
    -pip install -r requirements.txt  
  
    
## How to Fork the respository  
  
By forking the GitHub Repository you make a copy of the original repository on your own GitHub account to view and/or make changes without affecting the original repository by following these simple steps:  
  
1. Log in to GitHub and locate the [StephenJ2020/Sportmaster Repository](https://github.com/StephenJ2020/Sportmaster)  
2. Near the top of the Repository, on the right-hand side of the screen, locate the "Fork" button.  
3. Click this button and you should now have a copy of the original repository in your GitHub account.  
    
## Making a Local Clone 
  
1. Log in to GitHub and locate the [StephenJ2020/Sportmaster Repository](https://github.com/StephenJ2020/Sportmaster)  
2. Under the repository name, click "Clone or download".  
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.  
4. Open Git Bash  
5. Change the current working directory to the location where you want the cloned directory to be made.  
6. Type `git clone`, and then paste the URL you copied in Step 3.  
```  
$ git clone https://github.com/StephenJ2020/Sportmaster  
```  
7. Press Enter. Your local clone will be created.  
```  
$ git clone https://github.com/StephenJ2020/Sportmaster  
> Cloning into `CI-Clone`...  
> remote: Counting objects: 10, done.  
> remote: Compressing objects: 100% (8/8), done.  
> remove: Total 10 (delta 1), reused 10 (delta 1)  
> Unpacking objects: 100% (10/10), done.  
```   

[:top:](#Sportmaster)

# Testing  
------  
## Code Validity

  
## Testing User Stories
* *First time user stories:*
    * 
    * 

* *Returning user stories:*




  
# Credits  
------  
* Table of contents generated with [markdown-toc](http://ecotrust-canada.github.io/markdown-toc/).
* Favicon is taken from [Flaticon](https://www.flaticon.com/).  
* Hero Image - [Homepage]() 
*   " [Homepage](https://unsplash.com/photos/lrQPTQs7nQQ)  
* Delivery - [pinterest](https://www.pinterest.ie/pin/311381761732525673/) 
* Category Card Img - Product Announcements [Austin chan](https://unsplash.com/photos/ukzHlkoz1IE) 
* New Product Announcement Blurb - [Gym Wear](https://www.gymwear.co.uk/blogs/news/v3-apparel)  
  
* Menswear:   
  - Category Card Img [Jonathan Borba](https://unsplash.com/photos/R0y_bEUjiOM)  
  - White Hoodie [Khalid Boutchich](https://unsplash.com/photos/AGwMgxZs1L0)  
  - Gray Hoodie [Khalid Boutchich](https://unsplash.com/photos/p_CAhGaMf8M)  
  - Wetsuit [Khalid Boutchich](https://unsplash.com/photos/JYZeQ4OCFjQ)  
  - Black Jogger Combo [Khalid Boutchich](https://unsplash.com/photos/zlea9jOSvkk)  
  - Black Nike Workout T [Stephen Hsu](https://unsplash.com/photos/HYIozC1WkRg)  
  - Silver Water Bottle [Kate Joie](https://unsplash.com/photos/wxW37QUEYDY)  
  - Gray Baseball Cap [Claudio Schwarz](https://unsplash.com/photos/PH8GUKG-Do0)  
  - Black Water Bottle [Ryan Hoffman](https://unsplash.com/photos/371ROS34quI)  
  - Black Beanie Hat [Ryan Hoffman](https://unsplash.com/photos/2BK0JEwQSpQ)  
  - Black Backpack [Luis Quintero](https://unsplash.com/photos/8TSqJoI-NVs)  
  - Gray Water Bottle [Karl Köhler](https://unsplash.com/photos/dGIEMeN2MV8)  
  - White Baseball Cap [Mediamodifier](https://unsplash.com/photos/ogmenj2NGho)  
  - Nike Runners [Kristian Egelund](https://unsplash.com/photos/wmdcUQ0CJ4c)  
  - Vans [Devin Justesen](https://unsplash.com/photos/GOTdEatppRk)  
  - Reebok [Maureen De Wit](https://unsplash.com/photos/cEot_30k978)  
  - Nike AirMax [Lefteris kallergis](https://unsplash.com/photos/j1GiPlvSGWI)  
  - 

    
* Womenswear:  
  - Category Card Img [Julia Ballew](https://unsplash.com/photos/Gh8QHONEHOE)  
  - Gray Hoodie [Brent Ninaber](https://unsplash.com/photos/DKViOG1pVTM)  
  - Cam. Baseball Cap [Christina @ wocintechchat.com](https://unsplash.com/photos/XmvKl8CDMrk)  
  - White Yoga Set [Alexi Romano](https://unsplash.com/photos/WrxPwb6-wo8)  
  - swimsuit [Elise Wilcox](https://unsplash.com/photos/No9g_Stsmfg)  
  - Bikini Set [kevin turcios](https://unsplash.com/photos/CVg2uKcL-ns)  
  - Nike Pro Shorts [MAX LIBERTINE](https://unsplash.com/photos/Pi4MOqVb85c)  
  - Nike Sports Bra [Danny SwellChasers](https://unsplash.com/photos/ajgM180zHps)  
  - Workout Weights [Derick McKinney](https://unsplash.com/photos/__QqvTI5Edc)  
  - White Sports Bra [Honey Yanibel Minaya Cruz](https://unsplash.com/photos/QP78VWKEtz8)  
  - Rose Yoga Set [Julia Rekamie](https://unsplash.com/photos/Z72YujnOrlY)  
  - Blue Yoga Pants [Tyler Nix](https://unsplash.com/photos/Y1drF0Y3Oe0)  
  - White Water Bottle [Fakurian Design](https://unsplash.com/photos/ziiCdjrca_U)  
  - Alliance Water Bottle [Fakurian Design](https://unsplash.com/photos/M9CFKnKSeZY)  
  - Black Leggings [Christian Bolt](https://unsplash.com/photos/TyGExb_egWo)  
  - Fitbit Watch [David Švihovec](https://unsplash.com/photos/BGGHiSp2Quw)  
  - Filas [Mehdi-Thomas BOUTDARINE](https://unsplash.com/photos/OVUrzAAMTdg)  
  - Nike Air [Ryan Plomp](https://unsplash.com/photos/bySPt2lySzg)  
  - Fit-ish Black Workout T [April Laugh](https://unsplash.com/photos/7FsdvMMi_yY)  
  -
    

* Childernswear:  
  - Category Card Img [Lars Bo Nielsen](https://unsplash.com/photos/zXn5qinCDKg)
  - Disney Sneakers [Bert Ferranco](https://unsplash.com/photos/GR4EEDj6bAE)  
  - Nike ENCAP Runners [Linda Xu](https://unsplash.com/photos/fUEP0djb1hA)  
  - Converse [Andrew Itaga](https://unsplash.com/photos/QNyWeFHjZJY)  
  - Adidas [Shyam Mishra](https://unsplash.com/photos/zuo1zb6mEcY)  
  - Football Skip [Md Mahdi](https://unsplash.com/photos/nOeUbiYBNjk)  
  - Nike Air Sneakers [Malvestida Magazine](https://unsplash.com/photos/Rp-viEAP8Bo)  
  - Pink Nike Runners [Maksim Larin](https://unsplash.com/photos/ezdrvzA1hZw)  
  - Sketchers [Onur Binay](https://unsplash.com/photos/bwFW9PTJZx8)  
  - 
    
      
* Sports:     
 - Category Card Img [Olga Guryanova](https://unsplash.com/photos/ft7vJxwl2RY)
 - Adidas Football Boots [Fachry Zella Devandra](https://unsplash.com/photos/u3YoW5MX26Y)  
 - Nike Football Boots [Tom Sodoge](https://unsplash.com/photos/GgEtIbD0hVo)  
 - White/Gray Adidad Football [Peter Glaser](https://unsplash.com/photos/qWs_Wa1JrKM)  
 - Adidas Black Football Socks [JC Gellidon](https://unsplash.com/photos/HT4y0uWVtn8)  
 - Adidas JFA Football Boots [Braden Hopkins](https://unsplash.com/photos/s6y5jURGxkU)  
 - Adidas Pink Football [Joshua Hoehne](https://unsplash.com/photos/3NyXqusbMsU)  
 -


# Acknowledgements  
------  
*  As always I wish to thank my Mentor Chris Quinn for all his patience, support and advice, I couldn't have asked for a better Mentor - Thank you Chris!  
*  The wonderful Code Institute Tutor Support team   
*  My colleague and peers in the Slack Community who are always there to offer their support and advice and some general good cheer on the tougher days!  

  


[:top:](#Sportmaster)