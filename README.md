
To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!


# Periodic - A menstrual tracking website

The idea to create this website has been born from the need for women to track their period for physical health, mental health and family planning. There are many menstrual tracking apps out there, but they mostly aim their content towards adults and there is a need for more child friendly versions or versions that are sensitive toward cultural and religious attitudes toward sex, therefore providing minimal sexual content. 
The website aims to provide information relevant to various stages of the menstrual cycle, to educate women and girls on how it effects them and how to make the most of each phase. The website will also do product reviews and sell products as a source of revenue. 
The website will present itself a in a gender neutral way to be inclusive of all menstruating people.

## Features

* Navigation bar
* menstrual calendar
* registration and account
* shop
* subscription payment for personal emails and reminders
* Product reviews

## Possible Future Features

* Community Forum
* More accurate tracking capabilities (keeping it simple for the time being)

## User goals
### First time user
Discover information about menstrual cycle
Read Product reviews
Buy products
Sort through products
Search information
Learn about cycle

### Regular User
Get personalised timed emails about menstrual cycle via subscription
Buy menstrual products
Sort through products
Learn about cycle
Search Information
Edit details
Have personal information stored (for tracker, payment details and address for postage)
            
## Site owner goal 
sell products
get payment via subscriptions for information
advertise products

## Wireframes
(use images of site and describe them and what they're for)

## Development

#### Problem
Could not get the navbar dropdown menu to display the options. I ensured the javasciprt was working by adding another elsewehere and checked multiple times that the format matched the documentation and the working example on the products page (categories selection box), I shifted the elements around and tried them in different places.
#### Solution

#### Problem
price sort was not working with category sort. It was resetting the category selection.
#### Solution

#### Problem
Could not get the innerHTML to change when selecting sorting options
#### Solution

#### Problem
Pants category only shows a few pants in main search area because there needs to be an overall 'pants' category
#### Solution

#### Problem
The paragraph breaks were not working in the descriptions of the products.
#### Solution
A bit of research into tamplate language documentation revealed that I needed to use "product.description|linebreaksbr"

#### Problem
The materialize select box is not working
#### Solution
I had put the data-target id in the wrong unordered list.

#### Problem
When adding 2 of the same product but in different sizes to see if they register as seperate items in the basket, they registered as only one and didn't display the sizes selected
#### Solution
After checking the local variables on the error page displayed on the webserver, i discovered that the 'item_with_size' should have been names 'item_size' in order to get the correct information for the code to work.

#### Problem
Subtotal and gran total prices are not working. grand total price had previously worked but now doesn't since adding sizes to the views function and context processor. I think the grand total mayb never worked perfectly. it seems to be increasing but not in a logical manor. I moved "basket = request.session.get('basket', {})" because i thought it was in the wrong place in the basket view, but it didn't totally fix the problem. I found that one line had "request.session.post" when it should have been "request.post", but it still didn't seem to solve the issue.
#### Solution
I deleted the delivery cost percentage and calculation that was inspired by the boutique-ado project and created my own delivery parameters. I then added a subtotal variable to the basket_item dictionary and spotted that the "total" variable needed an extra "+" before the "=" in the variable creation. this fixed the issues.

#### Problem
Ensure quantity select doesn't go below or above certain range
#### Solution

#### Problem
Removing items only works with items that don't have sizes
#### Solution
The key value for the item with sizes was incorrectly spelt.

#### Problem
editing the quantity wasn't working and redirecting to a page error 
#### Solution
one of the jango template links ended with }} rather than %}. The issue was fixed after changing the typo. On closer inspection, the update was working for only the first item in the basket. The problem turned out to be that id attributes were used for the elements, when class attributes need to be used as these elements were replicated for every item added, so more than one were displayed. Once the javascript was updated to retrienve the array of items with a class name rather than a single element with an id attribute, the function worked with all items.

#### Problem
Display of the your_cycle articles were working and randomly stopped working.
#### Solution
The modal wasn't working because the id attribute was long and broken up onto different lines. The modal worked once put onto the same line.

#### Problem
adde messages (dont forget postload javascript and message storage in settings). add basket-update notification
#### Solution

#### Problem
Coul not get card-error to work
#### Solution
needed attribute role to be "alert"

#### Problem
stripe payments were being created but not succeeding
#### Solution
the javascript was not picking up the submit event, so I changed the event listener to listen to the submit button rather than the form.

#### Problem
stripe payments were being processed but price-totals not directing to order info in admin/database
#### Solution
Grand total was not being calculated in the models.py. it was an easy fix to just add the appropriate calculation.

#### Problem
delivery cost is not properly represented in the admin. It looks as is the delivery cost is being calculated in models.py by counting the number of products, including products with different sizes, rather than th number of items
#### Solution
To calculate the total number of items, I took some code from boutique-ado's example an customized for this site.

#### Problem
Trying to set up javascript function to save deliver and billing info to the database was stopping the checkout function from working as it did not recognise the values being requested.
#### Solution
The shipping parameters didn't match the ones laid out in the strip ocumentation. I also had to change the country field in models.py from charfeild to countryfield and import it from django_countries

#### Problem
Terminal presented this on chckout compltion: (checkout vid 15)
Bad Request: /checkout/webhooks/
[07/Oct/2022 12:27:12] "POST /checkout/webhooks/ HTTP/1.1" 400 0
#### Solution
The secret stored in gitpod settings variables had a different name to the variable called in settings.py. There was also an issue with county being referred to as county and not state

#### Problem
Payment intent is called before define
#### Solution
This happens if the full name field is empty

#### Problem
Cannot use the materialise grid system on the form elements
#### Solution

## Testing
### Validators


### Ongoing Problems

## Deployment

## Credits
### Content

### Media
Product item images were taken from PixaBay

### Libraries
Materializecss.com

### Languages Used

### References (code, tutors, other help)
