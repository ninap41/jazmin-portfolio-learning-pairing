# Nina Notes

I created a version of each project with ideas to elevate where you're at with these languages. In here is an overview of every kind of feature I added to give ideas. As you code more, the complexity of your projects will vary, but I would follow the file structure format in `NinaUpdates` ex: (lyrics --> index, script, css) for html.

## Lyrics

Open `NinaUpdates/lyrics/index.html` in your web browser

A final portfolio project for Web Dev is rarely vanilla html (just an index.html file). You usually find people pair it with internal/external css and javascript. This is called `Vanilla` Web Development and isn't as common as it was a few years ago. Normally, you find devs using Javascript Front-End Web Framework with NodeJs like (React, Angular, Vue, etc ), BUT Vanilla Javascript still very valuable to know and can show off your programming skills. I added a style file, and script.js file to show you the kind of functionality you can add to a Vanilla HTML project. One thing to really look into is showing you can GET data from a server and display the data in html, using a `Third-Party Api`. There may be an `api` for lyrics/songs here: https://github.com/public-apis/public-apis

ex: go to https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2, and you'll see a server generating random cat facts. you can use `axios` to fetch data with javascript.

Additions: There is a css animation at the start I programmed to look like horizontal strips + an animation where a black background fades out. Having a styled page makes a big difference. The animations are stored in styles.css and the intro animation logic is in `script.js`

## Number Game && Mad Libs

`python3 NinaUpdates/MadLibs/madlibs.py`

`python3 NinaUpdates/MadLibs/madlibs.py`

Python final projects usually use a framework (Django, Flask, etc), unless you are coding python for data mutation, machine learning, or OS/linux shell scripting. I think your Python Project should show you can use imported libraries that come with Python & understand Classes & Recursion. I made the MadLib game a class to demonstrate Object Oriented Programming.

Number Game can be kept as Functional Programming. I added validation for when the user submits nothing for input. Employers like to see that you have fallbacks for potential bugs in scenarios like this. I also used a lib of Regex or "RE". It was imported to filter out non-numerical characters. It's standard in all languages for a scenario like this to use Reqex. int() will fail if not provided something that converts into a number, and we can't always trust the user to add a number. The user can also play again. In the second round, the number is between 1-999. Calling a function from within itself shows an understanding of `recursion`. I also added `ascii` colors to different text and pauses during certain responses.
