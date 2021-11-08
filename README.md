# Codewars Companion

Codewars is a great resource for practicing different coding languages and strategies, 
but it lacks any ability to organize your completed katas. Codewars Companion lets you select
and save your completed katas to a favorites list, where you can search, edit, add notes, and delete as you wish.

## Tech

Codewars Companion is built with Django on the front and back, along with HTMX for in-place form rendering and manipulation. The site currently uses two separate Codewars API endpoints in order to gather the necessary kata information for users. Django Allauth allows you to login through your GitHub account.

## How to Use

Access the live site at https://codewarscompanion.herokuapp.com/ or fork and clone this repo. Make sure your username for Codewars Companion corresponds to your username for Codewars (the first API call depends on having this information). Currently, the solutions links open a new tab to your solutions page on Codewars, so make sure you're signed in before clicking.

## Future Considerations

This is very much a proof-of-concept and a work-in-progress. There's a sprinkling of JavaScript for the loading spinner that I will convert to HTMX. I have a script that grabs the usernames of the top 500 Codewars users and then compiles a list of any GitHub repos that contain their kata solutions, so a "hints"-type feature might make it in at some point. I might make a crawler that downloads and archives your solutions in the database to make the site more self-sufficient. And of course, improved UX--while the current grit is an homage to Codewars, there are a number of features I'll add in over time.