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
     - Can't seem to get HTMX to send the non-form elements in the post request. Either need to send the inputs and format server side, or use javascript to send the html as a string for PDF rendering
 - My pets (demo'ing OOB Swaps & event triggering - two HTMX approaches to updating non-target elements from one HTMX action)
 TODO: display a temporary flash notification/banner (event trigger) 

OTHER IDEAS:
 - the live markdown editor & viewer from django-htmx site?
 - need to improve landing page to direct users to the various apps/demos
 - example of OOB-Swaps: Pet list page. Enter pet name, gets added to list (target), but also updates other elements (count of pets, temporary pop-up notifying new pet added)

Notes on OOB Swaps/Event Triggering:
- OOB Swap sends the content in the original response, and then replaces the relevant part of the DOM with the returned content
- Event triggering returns a header in the original response, that then triggers another DOM element to send a new request (which will return a response with content that can replace the target element)

 TODO: remove weasyprint & dependencies, then try xhtml2pdf