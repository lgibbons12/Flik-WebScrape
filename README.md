# FlikisDining-WebScraping

Welcome to My Repository!

I hate waiting in lines at school for lunch, so I thought about ways to fix that.
I landed on creating a pre-order service where students could have their lunches pre-packaged and able to be picked up.
This would decrease lines and make getting food much more efficient.

From that issue, I had the idea to create my own application that ran a possible pre-order system for school lunches.
For me, being successful was taking the data from the website and being able to display it on a web browser so that people could submit pre-orders.


In simple terms, this application uses a robot to:
- log into a menu website 
- store what the menu for the day is
- display it on a form in a website


**Selenium Part!**

In this program, a python application using Selenium logs into a menu service called Nutrislice.

The python library selenium allows me to code a robot to navigate the web browser.
I pass through HTML identifiers like h1 or id = "hello" in order to point the robot in the right direction.
Then, the robot performs whatever actions I tell it to on that element such as typing in "Cannon School" or clicking on a button.

Once it has navigated to the main page, the robot uses selenium to extract all of the text on the web page with the menu.


**RegEx Part!**

Then, using a python library called Regular Expression, I divide the long string from the web page text into a digestible file.
To do this, the code splits the string based on keywords inside of it. The meals are broken up into categories like Soup or Entrees/Sides,
and I use these keywords to break the string into five categories:


- Soup
- Entrees/Sides
- Innovations
- Vegetarian (*I include an edge case in the code because sometimes the menu does not include a vegetarian option*)
- Gluten Free

Once that is accomplished, I use line breaks in the strings to create lists of all of the foods in the different categories
and push all of that to the file (flik.json)

**JSON Pulling!**

This part was the hardest to figure out, but I got it in the end.

Using AJAX (Asynchronous Javascript and XML), I submit a request to pull the data from flik.json to the website.

**Displaying on Screen!**

Then, I display all of the foods on the screen using JQuery, a Javascript library that makes it easier to use Javascript
to add HTML elements to the webpage.




In conclusion, this project was a success and I am very satisfied with the result.


Additionally, I could have the code run once daily using Windows Task Scheduler, I could get my computer to:
- Use Windows PowerShell to run the python script once to get the menu for the day
- Use Windows PowerShell to commit the new JSON file to this repository so the website updates




Unfortuantely, in order for this program to run on a computer other than my own, you must install a chrome webdriver:

https://chromedriver.chromium.org/downloads

Along with downloading selenium from the command line with: --> pip install selenium <--





Sourcing:

TechWithTim Python Selenium Tutorials
- https://www.youtube.com/playlist?list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ 
- Gave me a solid understanding of selenium to apply my knowledge

W3 Schools RegEx
- https://www.w3schools.com/python/python_regex.asp
- Helped me understand how RegEx worked so I could apply it to my python code

GitHub Community
- On the forums I found the AJAX use that allowed me to take the JSON file and use it in my Javascript code

ChatGPT
- Aided me in figuring out what error messages were and possible solutions that I then tried out
