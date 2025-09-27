import tkinter as tk
#for images
from tkinter import PhotoImage as PHI
#for importing graphicos
import pathlib as PL
import Shape_GameGrid_PackingPuzzle as SGP
import PackingPuzzleWizard_working as PPW

class PuzzleWizardDomain(tk.Frame):

    def __init__(self, master = None):

        #NEEDED CLASSES FOR SHIT TO WORK
        #THIS IS NOT FOR TK STUFF
        #ALL BACK END

        super().__init__(master)
        self.master = master
        self.pack()
        self.setUpGamedata()
        self.setUpGameVisuals()
        self.set_up_Base_Frame()
        self.set_Up_Mother_Frames()
        self.setUpGridAndPuzzleFrame(self.leftframe)
        self.setUpWizardSwichFrame(self.middleframe)
        self.setUpOptionsFrame(self.rightframe)
        #all of the frames and widget constructors/setups go here
        #setting up of nessisary data would also go here
        #do not be afraid to have way to many set up functions, better safe then sorry

    def setUpWizardSwichFrame(self, desired_frame):
        """sets up the frame containg:
        * wizard artwork
        * iteration count
        * manual switch"""

        self.WizardPicture = tk.Label(master=desired_frame,image=self.theWizard)
        self.iterationCount = tk.Label(master=desired_frame,text="DEBUG_TEXT")
        self.manualSwitch = tk.Checkbutton(master= desired_frame,text="manual mode toggle")

        self.WizardPicture.grid(row=0,column=0)
        self.iterationCount.grid(row=1,column=0)
        self.manualSwitch.grid(row=2,column=0)

    def setUpGridAndPuzzleFrame(self, desired_Frame):
        """desired is left right or middle"""
        self.PuzzleName = tk.LabelFrame(master=desired_Frame,text="DEBUG_TEXT",padx= 30,pady= 30,)
        self.listScrollBar = tk.Scrollbar(master=self.PuzzleName)
        self.listOfBlocks = tk.Listbox(master=self.PuzzleName,selectmode="single",yscrollcommand=self.listScrollBar)
        self.PuzzleCanvas = tk.Canvas(master=self.PuzzleName,background="goldenrod")
        #GET THE CUSTOM CLASS FOR THE CANVAS DONE

        # self.gameGridRepresentation
        self.PuzzleName.pack(fill="both",expand="yes")
        self.listScrollBar.grid(row=0,column=0)
        self.listOfBlocks.grid(row=0,column=1)
        self.PuzzleCanvas.grid(row=0,column=2)

    def setUpOptionsFrame(self, desired_Frame):
        """Sets up the frame that contains:
        * create puzzle button
        * browse and solve puzzle button
        * quit button
         ALL THE ABOVE ARE PART OF 
         A DROP MENU
        * file select
        * file select scroll bar
        """
        self.create_puzzle_button = tk.Button(master=desired_Frame,text="create puzzle")
        self.browse_and_solve_button = tk.Button(master=desired_Frame,text="browse and solve")
        self.quit_prog_button = tk.Button(master=desired_Frame,text="quit")
        self.file_label = tk.Label(master=desired_Frame, text="OPTIONS")
        self.file_select_scroll_bar = tk.Scrollbar(master=desired_Frame)
        self.file_select = tk.Listbox(master=desired_Frame,yscrollcommand=self.file_select_scroll_bar)

        self.create_puzzle_button.grid(row=0,column=0)
        self.browse_and_solve_button.grid(row=0,column=1)
        self.quit_prog_button.grid(row=0,column=2)
        self.file_label.grid(row=1,column=0)
        self.file_select_scroll_bar.grid(row=2,column=1)
        self.file_select.grid(row=2,column=0)

    def setUpGamedata(self):
        pass

    def setUpGameVisuals(self):
        """loads graphics"""
        self.theWizard = tk.PhotoImage(file=PL.Path(__file__).parent / "graphics" / "theWizard.png")

    def set_up_Base_Frame(self):
        """sets up the boiler plate frame to contain everything"""
        self.gameframe = tk.Frame(master = self, padx=30, pady=30, background="black")
        self.gameframe.pack(expand="yes",fill="both")

    def set_Up_Mother_Frames(self):
        """Sets up the 3 base frames everything will work off of"""
        self.leftframe = tk.Frame(master = self.gameframe, background = "green", padx=30, pady=30)
        self.middleframe = tk.Frame(master = self.gameframe, background = "blue", padx=30, pady=30)
        self.rightframe = tk.Frame(master = self.gameframe, background = "red", padx=30, pady=30)

        self.leftframe.grid(row=0,column=0)
        self.middleframe.grid(row=0,column=1)
        self.rightframe.grid(row=0,column=2)


#create root window

root = tk.Tk()
game = PuzzleWizardDomain(root)
root.mainloop()
#create sub windows