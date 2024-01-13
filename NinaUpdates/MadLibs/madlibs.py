
# https://data-flair.training/blogs/python-mad-libs-generator-game/
#
# So I didn't have too much time for this one. But I think it would be cool to actually
# see this as a game in  your terminal and I saw this tutorial that looked promising with a GUI library (Graphical User Interface )
# Also I made it a class because it's important to show employers you know object oriented programming, not just functional

# Some ideas for this. Make a script that changes and maybe make this a longer script with ascii art and colors.

import pathlib

class MadLibs:
    adj = ''
    verb1 = ''
    verb2 =''
    famous_person =''
    story = ''
    def __init__(self):
        self.startProgram()
    def saveMadLib(self):
        print("Add logic")
        # make logic like this that saves a story to a text file:
        # print('Your story has saved to text.txt')
        # with open( pathlib.Path("text.txt"), "w") as text_file:
            # text_file.write( f"Computer programming is so {self.adj}! It makes me so excited all the time because \ I love to {self.verb1}. Stay hydrated and {self.verb2} like you are {self.famous_person}!")
    def printMadLib(self):
        # interpolation f`{self.adj}` is everything
        self.story = f"Computer programming is so {self.adj}! It makes me so excited all the time because \ I love to {self.verb1}. Stay hydrated and {self.verb2} like you are {self.famous_person}!"
        print(f"{self.story}")
        
    def startProgram(self):
        input("Let's make a game of Mad Libs! [continue]")
        self.adj = input("Adjective: ")
        self.verb1 = input("Verb: ")
        self.verb2 = input("Verb: ")
        self.famous_person = input("Famous person: ")
        self.printMadLib()
        saveLib = input("\n\nSave Mad Lib? (Y / N)")
        self.saveMadLib() if saveLib.lower() == "y" else print("\n Bye!")

game = MadLibs()


