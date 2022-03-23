# HTMX-Django-Experiments
 Playing with HTMX features on a basic Django web app

 Will eventually use Alpine.js (or try out hyperscript) where it is helpful, and Tailwind for styling 

 May incorporate the django-htmx package at some point

 DEMOS:
 - CRUD (ROOT/crud): demonstrating CRUD behaviours, with no full page reloads. Uses SQLite DB.
    - Click to edit, in-line Add & Delete 
 - Keyboard (ROOT/keyboard): Using keyboard shortcuts to trigger HTMX events
    - Change colour of a div with buttons/key presses
    - TODO: More advanced example of keyboard shortcuts? Maybe livesearch on each 'keyup changed' trigger event

OTHER IDEAS:
 - the live markdown editor & viewer from django-htmx site?
  - a certificate generator: enter text that live updates in a styled html preview of the certificate, plus a button to generate HTML portion as PDF using weasyprint 
 - need to create a landing page to direct users to the various apps/demos