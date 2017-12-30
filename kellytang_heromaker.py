'''Author: Kelly Tang
Date:Feb 28 2016
Description: Using an instance of the HeroMaker() class opens a GUI window, with multiple widgets for a user to input a super hero's name, gender, super power, favourite food, and clicks the "Make Hero!" button to generate and display the story in the Tkinter.Text widget'''

import Tkinter

class HeroMaker():
    
    def __init__(self):
        '''this initializer method creates all of the widgets in the window , which includes the Label widgets, Entry widgets, Radiobutton widget, Check button widget, Button widget, and the Tkinter.Text widget to display the text. '''
        
        self.main_window = Tkinter.Tk()
        
        # creating 7 frames, one for each row of widgets
        self.frame1 = Tkinter.Frame()
        self.frame2 = Tkinter.Frame()
        self.frame3 = Tkinter.Frame()
        self.frame4 = Tkinter.Frame()
        self.frame5 = Tkinter.Frame()
        self.frame6 = Tkinter.Frame()
        self.frame7 = Tkinter.Frame()
        
        # first frame containing the Label widget that displays the title
        self.title = Tkinter.Label(self.frame1, text = "Please enter information for your Super Hero, then click on the 'Make Hero' button.")
        
        self.title.pack(side= "left")
        
        # frame 2 containing a Label widget to display prompt to enter hero's name
        # also contains an Entry widget for user to enter hero name
        self.prompt_name = Tkinter.Label(self.frame2, text = "Hero's Name:    ")
        self.name_entry = Tkinter.Entry(self.frame2, width = 42)
        
        self.prompt_name.pack(side = "left")
        self.name_entry.pack(side = "left")
        
        # frame3 with a Label widget to display prompt to choose gender
        # also contains Radiobutton widget for use to choose a gender
        
        self.prompt_gender = Tkinter.Label(self.frame3, text = "Gender: ")
        
        # create an IntVar object to use with the Radiobuttons
        self.radio_var = Tkinter.IntVar()
        
        # set the IntVar object to 1
        self.radio_var.set(1)
        
        # create a 2 radiobuttons, one for each gender
        self.gender_rb1 = Tkinter.Radiobutton(self.frame3, text = "Male", \
                                              variable = self.radio_var, \
                                              value = 1)
        self.gender_rb2 = Tkinter.Radiobutton(self.frame3, text = "Female", \
                                              variable = self.radio_var, \
                                              value = 2)
        
        self.prompt_gender.pack(side = "left")
        self.gender_rb1.pack(side = "left")
        self.gender_rb2.pack(side = "left")
        
        # frame 4 containing Label widget to display prompt to enter a food
        # also contains Entry widget for user to enter hero's favourite food
        self.prompt_food = Tkinter.Label(self.frame4, text = "Favourite Food: ")
        self.food_entry = Tkinter.Entry(self.frame4, width = 42)
        
        self.prompt_food.pack(side= "left")
        self.food_entry.pack(side = "left")
        
        # frame 5 containing a Label widget for a prompt to choose superpower(s)
        # also contains Checkbutton widget to user to choose superpower(s)
        
        self.power_prompt = Tkinter.Label(self.frame5, text = "Super Powers: ")
        
        #create 3 IntVar objects to use with the Checkbuttons
        self.cb_var1 = Tkinter.IntVar()
        self.cb_var2 = Tkinter.IntVar()
        self.cb_var3 = Tkinter.IntVar()
        
        # set the IntVar objects to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)  
        self.cb_var3.set(0)
        
        # create 3 checkbuttons with a superpower each 
        self.power_cb1 = Tkinter.Checkbutton(self.frame5, text = "mind reading"\
                                             , variable = self.cb_var1)
        self.power_cb2 = Tkinter.Checkbutton(self.frame5, text = "invisibility"\
                                             , variable = self.cb_var2)
        self.power_cb3 = Tkinter.Checkbutton(self.frame5, text = "super speed"\
                                             , variable = self.cb_var3)  
        
        self.power_prompt.pack(side= "left")
        self.power_cb1.pack(side="left")
        self.power_cb2.pack(side="left")
        self.power_cb3.pack(side="left")
        
        #frame 6 containg Button widget to call make_hero function once clicked
        self.make_hero_button = Tkinter.Button(self.frame6, text = "Make Hero!", command = self.make_hero )
        
        self.make_hero_button.pack(side = "left")
        
        #frame 7 containing Tkinter.Text widget to display a story including the information the information the user has entered
        #make sure that words don't get cut off when each line ends
        self.textbox = Tkinter.Text(self.frame7, wrap = "word")
        
        self.textbox.pack()
         
        #pack the frames
        self.frame1.pack(anchor ="w")
        self.frame2.pack(anchor = "w")
        self.frame3.pack(anchor = "w")
        self.frame4.pack(anchor = "w")
        self.frame5.pack(anchor = "w")
        self.frame6.pack(anchor = "w")
        self.frame7.pack(anchor = "w")
    
        Tkinter.mainloop()
        
    def make_hero(self):
        '''this method is called when the "Make Hero!" button is clicked, it
        gets the information from all the user inputs, and generates a story using that information, then displays it in the Tkinter.Text widget.'''
        
        #get the hero's and assign the value to self.hero_name
        if self.name_entry.get():
            self.hero_name = self.name_entry.get()
        else:
            self.hero_name = ""
        
        #get the gender that the user selected
        self.gender_choice = self.radio_var.get()
        
        if self.gender_choice == 1:
            self.gender = "male"
            self.pronoun1 = "he"
            self.pronoun2 = "his"
        elif self.gender_choice == 2:
            self.gender = "female"
            self.pronoun1 = "she"
            self.pronoun2 = "her"
            
        #get the hero's favourite food
        if self.food_entry.get():
            self.food = self.food_entry.get()
        else:
            self.food = ""
    
        #get the number of and the name of superpower(s) the user has selected  
        num_powers = 0
        
        if self.cb_var1.get()== 1:
            self.power1 = "mind reading"
            num_powers+=1
        else: 
            self.power1 = ""
            
        if self.cb_var2.get()==1:
            self.power2 = "invisibility"
            num_powers +=1
        else:
            self.power2 = ""
            
        if self.cb_var3.get() == 1:
            self.power3 = "super speed"
            num_powers+=1
        else:
            self.power3 = ""

        if num_powers == 1:
            self.powers = self.power1 + self.power2 +self.power3
        elif num_powers ==2 :
            if (self.cb_var1.get()==1) and (self.cb_var2.get()==1):
                self.powers = self.power1 + " and " + self.power2
            elif (self.cb_var2.get()==1) and (self.cb_var3.get()==1):
                self.powers = self.power2 + " and " + self.power3
            else:
                self.powers = self.power1 + " and " + self.power3   
        else:
            self.powers = self.power1 +", " + self.power2 +",and " +self.power3
            
            
        # create the story with the information of hero    
        story = self.hero_name.title() + ", a local super hero, has saved the day again! " + self.pronoun1.capitalize() + " has defeated the evil homework-stealing villain. Using " + self.powers+", "+self.hero_name.title()+ " has saved the homework of many students from the hands of the villain." +" Now, after a long day of hard work, "+ self.hero_name.title() + " is resting and eating " + self.pronoun2+ " favourite food, "+ self.food+ "!" 
        
        #if an entry is left blank, a warning message is displayed and no story is displayed
        if (self.hero_name == "") or (self.food =="" ) or (num_powers == 0):
            story = "WARNING! You left one or more entries blank. "        
        
        #insert the paragraph in the Tkinter.Text widget
        #delete method used to remove any previous stories from the text box
        self.text = story
        self.textbox.delete(1.0, "end")
        self.textbox.insert("end", self.text)

my_hero = HeroMaker()


