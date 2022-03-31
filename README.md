# HTMX-Django-Experiments
 Playing with HTMX features on a basic Django web app

 Will eventually use Alpine.js (or try out hyperscript) where it is helpful, and Tailwind for styling 

 May incorporate the django-htmx package at some point

 DEMOS:
 - CRUD (/crud): demonstrating CRUD behaviours, with no full page reloads. Uses SQLite DB.
    - Click to edit, in-line Add & Delete 
 - Keyboard (/keyboard): Using keyboard shortcuts to trigger HTMX events
    - Change colour of a div with buttons/key presses
    - TODO: More advanced example of keyboard shortcuts? Maybe livesearch on each 'keyup changed' trigger event
 - Certificate Generator (/certificate): build a styled certificate
    - live update entered text, with server side validation, to build a styled certificate
    - TODO: button to generate certificate HTML snippet as PDF (weasyprint? xhtml2pdf?)

OTHER IDEAS:
 - the live markdown editor & viewer from django-htmx site?
 - need to improve landing page to direct users to the various apps/demos
 - example of OOB-Swaps: Pet list page. Enter pet name, gets added to list (target), but also updates other elements (count of pets, temporary pop-up notifying new pet added)