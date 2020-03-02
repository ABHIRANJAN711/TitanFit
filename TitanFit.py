#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 00:19:58 2020

@author: lgomez
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:44:31 2020

@author: lgomez
"""
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from threading import Thread
from DBMS_Project import *
import sqlite3



#from PIL import Image, ImageTk





#CSUF_Logo = Image.open("./Logos/CSUF.png")

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
       
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        

        # Creation of main tkinter window
        container.pack(side="top", fill="both", expand = True)
     
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
       

        self.frames = {}

        for F in (MenuPage, LoginPage, RegisterPage, UserPage, BMIPage, CalorieSelectPage, CalorieLosePage,CalorieGainPage, WorkoutPage ): #initialize classes - each class is an individual frame

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        # Selecting First page on GUI
        self.showFrame(MenuPage)
        
        self.s = ttk.Style()
        self.s.configure('my.TButton', font=('Deja Vu Sans Mono' , 25, 'bold'))
        

    # Add showFrame event to each page
    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")
        
class MenuPage(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self,parent)
        
      
        
#        # Add CSUF Logo
#        render = ImageTk.PhotoImage(CSUF_Logo)
#        img = ttk.Label(self, image=render)
#        img.image = render
#        img.place(relx=1.0, rely=0.0, anchor="ne")
        
        self.msp_controller=controller
        
        
#         Welcome label on MainMenuPage
        self.msp_label = ttk.Label(self, text="Welcome Titan", font= ('Arial' , 50, 'bold',),borderwidth = 2, relief = "groove")
        self.msp_label.pack(side="top",pady=20) # size of window
 

        # Creation of Add Machine button. Button returns to AddMachinePage when pressed
        loginButton = ttk.Button(self, text="Login", style='my.TButton', command=lambda: controller.showFrame(LoginPage))
        loginButton.pack(side="top", pady = 10)
#        loginButton.place(x = 480,y = 325 )
       
        
        # Creation of Delete button
        registerButton = ttk.Button(self, text="Register",style='my.TButton', command=lambda: controller.showFrame(RegisterPage))
        registerButton.pack(side = "top", pady = 0)
#        registerButton.place(x = 480,y = 375 )
        
  
            
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self,parent)
        self.controller=controller
        
        # Welcome label on LoginPage - font type/size - bold
        self.login_label = ttk.Label(self, text="Enter login Information", font= ('Deja Vu Sans Mono' , 30, 'bold'))
        self.login_label.pack(padx = 50, pady = 10) # size of window
        
        # Creation of input box and label for *username
        self.username_label = ttk.Label(self, text = "Username", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.username_label.pack
        self.username_label.place(x = 20,y = 100 )
        
        self.username_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15, ))
        self.username_entry.pack
        self.username_entry.place(x = 110, y = 100 )
       
        #Creation of Input box and label for password
        self.password_label = ttk.Label(self, text = "Password", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.password_label.pack
        self.password_label.place(x = 20,y = 150 )
        
        self.password_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15,), show = '*')
        self.password_entry.pack(side = 'top')
        self.password_entry.place(x = 110 , y= 150)
        
          # Creation of back button. Button returns to MainPage when pressed
        self.amp_ms_btn = ttk.Button(self, text="Back", style='my.TButton', command=lambda: controller.showFrame(MenuPage))
        self.amp_ms_btn.pack(side="bottom") 
        
        # Creation of login button. 
        self.amp_ab_btn = ttk.Button(self, text="Login", style='my.TButton', command=lambda: self.login_user())
        self.amp_ab_btn.pack(side="bottom") 
        
      
    
        
            
    def login_user(self):
           
            with sqlite3.connect('students.db') as db:
                cursor = db.cursor()
                finduser = ("Select * FROM studentlist WHERE Username=? AND Password=?")
                cursor.execute(finduser,[(self.username_entry.get()),(self.password_entry.get())])
                results = cursor.fetchall()
                
                
                if results:
                    for i in results:
                       self.controller.showFrame(UserPage)
                       
                else:
       
                    message = ttk.Label( text = 'Username or Password incorrect. Try again!')
                    message.pack(side = "top")

        
        
        
        
        
        

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)
        self.controller=controller
        self.db_name = 'students.db'
        self.message = ttk.Label(text='')
        self.message.pack
    
        account_label = ttk.Label(self, text="Create New Account", font= ('Arial' , 30, 'bold',),borderwidth = 2, relief = "groove")
        account_label.pack(side="top",pady=20) # placement of label on page 
        
        
        #first name label creation and placement 
        fname_label = ttk.Label(self, text="First Name:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        fname_label.pack
        fname_label.place(x=350,y=120)
        #name entry creation and placement
        self.fname_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15))
        self.fname_entry.pack
        self.fname_entry.place(x=450,y=120)
        
        #Last name label creation and placement 
        lname_label = ttk.Label(self, text="Last Name:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        lname_label.pack
        lname_label.place(x=350,y=160)
        #Last name entry creation and placement
        self.lname_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15))
        self.lname_entry.pack
        self.lname_entry.place(x=450,y=160)
        
        
        
        
        #email label creationa and placement
        email_label = ttk.Label(self, text="Email:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        email_label.pack
        email_label.place(x=350,y=200)
        #email entry creation and placement
        self.email_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15))
        self.email_entry.pack
        self.email_entry.place(x=450,y=200)
        
        
        
        #username label creationa and placement
        username_label = ttk.Label(self, text="Username:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        username_label.pack
        username_label.place(x=350,y=240)
        #email entry creation and placement
        self.username_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15))
        self.username_entry.pack
        self.username_entry.place(x=450,y=240)
        
        #password label creationa and placement
        password_label = ttk.Label(self, text="Password:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        password_label.pack
        password_label.place(x=350,y=280)
        #password entry creation and placement
        self.password_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15))
        self.password_entry.pack
        self.password_entry.place(x=450,y=280)
        
        #height and cm label creation and placement
        height_label = ttk.Label(self, text="Height:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        height_label.pack
        height_label.place(x=350,y=320)
        cm_label = ttk.Label(self, text="cm", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        cm_label.pack
        cm_label.place(x=665,y=324)
        #height entry creation and placement
        self.height_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15))
        self.height_entry.pack
        self.height_entry.place(x=450,y=320)
        
        
        
        #weight and kg label creation and placement
        weight_label = ttk.Label(self, text="Weight:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        weight_label.pack
        weight_label.place(x=350,y=360)
        kg_label = ttk.Label(self, text="kg", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        kg_label.pack
        kg_label.place(x=665,y=364)
        #weight entry creation and placement
        self.weight_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15))
        self.weight_entry.pack
        self.weight_entry.place(x=450,y=360)
        
        
        #age label creation and placement
        age_label = ttk.Label(self, text="Age:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        age_label.pack
        age_label.place(x=350,y=400)
        #age entry creation and placement
        self.age_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15))
        self.age_entry.pack
        self.age_entry.place(x=450,y=400)
        
    
        
        
        #Gender Label creation placement 
        Gender_label = ttk.Label(self, text="Gender:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        Gender_label.pack
        Gender_label.place(x=350,y=440)
        #Gender selection box creation and placement 
        GenderEntry = ttk.Combobox(self, values=["Male", "Female"])
        GenderEntry.pack
        GenderEntry.place(x=450,y=440)
        
        
        
        
        #Creation of button that creates new account
        
        registerButton = ttk.Button(self, text="Register", style='my.TButton', command=lambda: self.add_record())
        registerButton.pack 
        registerButton.place(x=470 ,y= 500)
        
        # Creation of back button, Returns to MenuPage
        backButton = ttk.Button(self, text="back", style='my.TButton', command=lambda: controller.showFrame(MenuPage))
        backButton.pack 
        backButton.place(x=470 ,y= 550)

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result  
        
    ''' Add New Record '''

    def validation(self):
        return len(self.fname_entry.get()) != 0 and len(self.lname_entry.get()) != 0 and len(self.username_entry.get()) != 0 and \
               len(self.email_entry.get()) != 0 and len(self.password_entry.get()) != 0 and len(self.age_entry.get()) != 0 and \
               len(self.weight_entry.get()) != 0 and len(self.height_entry.get()) != 0

    def add_record(self):
        
        if self.validation():
            query = 'INSERT INTO studentlist VALUES (NULL,?,?,?,?,?,?,?,?)'
            parameters = (self.fname_entry.get(), self.lname_entry.get(), self.username_entry.get(),
                          self.email_entry.get(), self.password_entry.get(), self.age_entry.get(), self.height_entry.get(), self.weight_entry.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Record {} {} added!'.format(self.fname_entry.get(),self.lname_entry.get())
            self.controller.showFrame(LoginPage)
            print(parameters)    
            
            '''Empty the fields'''
            self.fname_entry.delete(0, END)
            self.lname_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.age_entry.delete(0, END)
            self.height_entry.delete(0, END)
            self.weight_entry.delete(0, END)

        else:
            self.message['text'] = 'Fields not completed! Complete all fields...'
    

class UserPage(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self,parent)
        
      

        self.msp_controller=controller
        
        
#         Welcome label on MainMenuPage
        self.msp_label = ttk.Label(self, text="Hello User", font= ('Arial' , 50, 'bold',),borderwidth = 2, relief = "groove")
        self.msp_label.pack(side="top",pady=20) # size of window
 

        # Creation of BMI calculation button
        loginButton = ttk.Button(self, text="BMI", style='my.TButton', command=lambda: controller.showFrame(BMIPage))
        loginButton.pack(side="top", pady = 10)
#        loginButton.place(x = 480,y = 325 )
       
        
        # Creation of calorie intake button
        registerButton = ttk.Button(self, text="Caloric intake",style='my.TButton', command=lambda: controller.showFrame(CalorieSelectPage))
        registerButton.pack(side = "top", pady = 0)
#        registerButton.place(x = 480,y = 375 )
        
               
        # Creation of Delete button
        registerButton = ttk.Button(self, text="Workout",style='my.TButton', command=lambda: controller.showFrame(WorkoutPage))
        registerButton.pack(side = "top", pady = 0)
#        registerButton.place(x = 480,y = 375 )
        
        
class BMIPage(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self,parent)
        
      

        self.controller=controller
        
        
        # Calculate BMI label
        self.BMIlabel = ttk.Label(self, text="Calculate BMI", font= ('Arial' , 50, 'bold',),borderwidth = 2, relief = "groove")
        self.BMIlabel.pack(side="top",pady=20) # size of window
 
        self.BMIlabel2 = ttk.Label(self, text="Fill in all information below", font= ('Arial' , 25,),borderwidth = 2, relief = "groove")
        self.BMIlabel2.pack(side="top",pady=20) # size of window
 
        #ft and in label creation and placement
        self.height_label = ttk.Label(self, text="Height:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.height_label.pack
        self.height_label.place(x=350,y=220)
        self.in_label = ttk.Label(self, text="in", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.in_label.pack
        self.in_label.place(x=650,y=224)
        self.ft_label = ttk.Label(self, text="ft", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.ft_label.pack
        self.ft_label.place(x=540,y=224)
        
        
        
        #height entry creation and placement
        self.heightft_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15), width = 7)
        self.heightft_entry.pack
        self.heightft_entry.place(x=450,y=220)
        self.heightin_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15), width = 7)
        self.heightin_entry.pack
        self.heightin_entry.place(x=560,y=220)
        
        
        
        #weight and lb label creation and placement
        self.weight_label = ttk.Label(self, text="Weight:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.weight_label.pack
        self.weight_label.place(x=350,y=260)
        self.lb_label = ttk.Label(self, text="lb", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.lb_label.pack
        self.lb_label.place(x=665,y=264)
        #weight entry creation and placement
        self.weight_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15))
        self.weight_entry.pack
        self.weight_entry.place(x=450,y=260)
        
        
        #age label creation and placement
        self.age_label = ttk.Label(self, text="Age:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.age_label.pack
        self.age_label.place(x=350,y=300)
        #age entry creation and placement
        self.age_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15))
        self.age_entry.pack
        self.age_entry.place(x=450,y=300)
        
    
        
        
        #Gender Label creation placement 
        self.Gender_label = ttk.Label(self, text="Gender:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.Gender_label.pack
        self.Gender_label.place(x=350,y=340)
        #Gender selection box creation and placement 
        self.GenderEntry = ttk.Combobox(self, values=["Male", "Female"])
        self.GenderEntry.pack
        self.GenderEntry.place(x=450,y=340)
        

        # Creation of BMI calculation button
        self.BMIButton = ttk.Button(self, text="BMI", style='my.TButton', command=lambda: self.BMICalculation())
        self.BMIButton.pack
        self.BMIButton.place(x = 480,y = 525 )
       
        backbutton = ttk.Button(self, text="Back", style='my.TButton', command=lambda: self.controller.showFrame(UserPage))
        backbutton.pack
        backbutton.place(x = 480,y = 560 )
  
        
        
        
    def BMICalculation(self):
        
        height = (int(self.heightft_entry.get()) * 12) + int(self.heightin_entry.get())
        weight = int(self.weight_entry.get())
        bmi = (weight / (height*height)) *703
        BMI = format(bmi, '.2f')
        print(BMI)
        
        self.BMIlabel.destroy()
        self.BMIlabel2.destroy()
        self.height_label.destroy()
        self.in_label.destroy()
        self.ft_label.destroy()
        self.heightft_entry.destroy()
        self.heightin_entry.destroy()
        self.weight_label.destroy()
        self.lb_label.destroy()
        self.weight_entry.destroy()
        self.age_label.destroy()
        self.age_entry.destroy()
        self.Gender_label.destroy()
        self.GenderEntry.destroy()
        self.BMIButton.destroy()
        
###############################################################################
#        Things to do :
#        Add BMI chart picture
#        Make sure warnings appear when all information isn't filled in 
#        Make sure sure warnings reset when we change frames
#        Make sure information can be filled in multiple times 
###############################################################################

        BMITitle = ttk.Label(self, text="Your BMI", font= ('Arial' , 50, 'bold',),borderwidth = 2, relief = "groove")
        BMITitle.pack(side="top",pady=20)
        
        BMI1_label = ttk.Label(self, text=BMI, font= ('Deja Vu Sans Mono' , 30, 'bold'))
        BMI1_label.pack
        BMI1_label.place(x=490,y=200)
       
      
        


class CalorieSelectPage(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self,parent)
    
        self.controller=controller
        
         
        # Calculate BMI label
        self.BMIlabel = ttk.Label(self, text="Caloric Intake", font= ('Arial' , 50, 'bold',),borderwidth = 2, relief = "groove")
        self.BMIlabel.pack(side="top",pady=20) # size of window
        
          #Weight goals label and entry
        WGoals_label = ttk.Label(self, text="What are your weight goals?", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        WGoals_label.pack
        WGoals_label.place(x=350,y=120)
        #name entry creation and placement
        self.WGoalsEntry = ttk.Combobox(self, values=["Loose Weight", "Gain Muscle"])
        self.WGoalsEntry.pack
        self.WGoalsEntry.place(x=560,y=120)
      
  
         
        continuebutton = ttk.Button(self, text="Continue", style='my.TButton', command=lambda: self.WGoals() )
        continuebutton.pack
        continuebutton.place(x = 480,y = 350 )  
            
  
        
        backbutton = ttk.Button(self, text="Back", style='my.TButton', command=lambda: self.controller.showFrame(UserPage))
        backbutton.pack
        backbutton.place(x = 480,y = 400 )  
            
        
    def WGoals(self):
    
        if (self.WGoalsEntry.get() == "Loose Weight"):
            self.controller.showFrame(CalorieLosePage)    
        elif(self.WGoalsEntry.get() == "Gain Weight"):
            self.controller.showFrame(CalorieGainPage) 
         
            
            
            
class CalorieLosePage(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self,parent)
    
        self.controller=controller   
        
        
        #Weight Loss top label
        self.WLosslabel = ttk.Label(self, text="Lose Weight", font= ('Arial' , 50, 'bold',),borderwidth = 2, relief = "groove")
        self.WLosslabel.pack(side="top",pady=20) # size of window         
       
        
        self.label = ttk.Label(self, text="Fill in all information below", font= ('Arial' , 30,),borderwidth = 2, relief = "groove")
        self.label.pack(side="top",pady=20) # size of window
 
        
 
        #Weight goals label and entry
        self.WGoals_label = ttk.Label(self, text="Pounds lost in a week?", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.WGoals_label.pack
        self.WGoals_label.place(x=350,y=180)
        #name entry creation and placement
        self.WLWGoalsEntry = ttk.Combobox(self, values=["0.5lbs", "1lb", "2lbs"])
        self.WLWGoalsEntry.pack
        self.WLWGoalsEntry.place(x=630,y=180)
      
        
        
        
        #ft and in label creation and placement
        self.WLheight_label = ttk.Label(self, text="Height:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.WLheight_label.pack
        self.WLheight_label.place(x=350,y=220)
        self.WLin_label = ttk.Label(self, text="in", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.WLin_label.pack
        self.WLin_label.place(x=650,y=224)
        self.WLft_label = ttk.Label(self, text="ft", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.WLft_label.pack
        self.WLft_label.place(x=540,y=224)
        
        
        
        #height entry creation and placement
        self.WLheightft_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15), width = 7)
        self.WLheightft_entry.pack
        self.WLheightft_entry.place(x=450,y=220)
        self.WLheightin_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15), width = 7)
        self.WLheightin_entry.pack
        self.WLheightin_entry.place(x=560,y=220)
        
        
        
        #weight and lb label creation and placement
        self.WLweight_label = ttk.Label(self, text="Weight:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.WLweight_label.pack
        self.WLweight_label.place(x=350,y=260)
        self.WLlb_label = ttk.Label(self, text="lb", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.WLlb_label.pack
        self.WLlb_label.place(x=665,y=264)
        #weight entry creation and placement
        self.WLweight_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15))
        self.WLweight_entry.pack
        self.WLweight_entry.place(x=450,y=260)
        
        
        #age label creation and placement
        self.WLage_label = ttk.Label(self, text="Age:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.WLage_label.pack
        self.WLage_label.place(x=350,y=300)
        #age entry creation and placement
        self.WLage_entry = ttk.Entry(self, font= ('Deja Vu Sans Mono' , 15))
        self.WLage_entry.pack
        self.WLage_entry.place(x=450,y=300)
        
    
        
        
        #Gender Label creation placement 
        self.WLGender_label = ttk.Label(self, text="Gender:", font= ('Deja Vu Sans Mono' , 15, 'bold'))
        self.WLGender_label.pack
        self.WLGender_label.place(x=350,y=340)
        #Gender selection box creation and placement 
        self.WLGenderEntry = ttk.Combobox(self, values=["Male", "Female"])
        self.WLGenderEntry.pack
        self.WLGenderEntry.place(x=450,y=340)
        


        self.continuebutton = ttk.Button(self, text="Calorie Count", style='my.TButton', command=lambda: self.WlossCalc() )
        self.continuebutton.pack
        self.continuebutton.place(x = 445,y = 400 )  
            
  
        
        backbutton = ttk.Button(self, text="Back", style='my.TButton', command=lambda: self.controller.showFrame(UserPage))
        backbutton.pack
        backbutton.place(x = 480,y = 440 )  


    
      # For Men
      #  
        # maintence is 1.18 x bmr
        #lose 0.5 pound is 1.057 x bmr
        #lose 1 pound is 0.93 x bmr
        #lose 2 pounds is 0.678 x bmr
        
      # For Women
      #  
        # maintence is 1.18 x bmr
        #lose 0.5 pound is 1.057 x bmr
        #lose 1 pound is 0.93 x bmr
        #lose 2 pounds is 0.678 x bmr
                



    def WlossCalc(self):
        
        
        
        WLheight = (int(self.WLheightft_entry.get()) * 12) + int(self.WLheightin_entry.get())
        WLweight = int(self.WLweight_entry.get())
         
           
            #calculate Adult Male BMR
        MenBMR = int(66 + (6.3 * WLweight) + (12.9 * WLheight) - (6.8 * int(self.WLage_entry.get())))
        #calculate Adult Female BMR
        WomenBMR = int(655 + (4.3 * WLweight) + (4.7 * WLheight) - (4.7 * int(self.WLage_entry.get())))
        
#     if statment for Male loosing 0.5 lbs 
        if (self.WLWGoalsEntry.get() == "0.5lbs" and self.WLGenderEntry.get() == "Male"):
            
           calories = round(1.057*MenBMR)
           
           
           self.WLosslabel.destroy()
           self.continuebutton.destroy()
           self.WLosslabel.destroy
           self.label.destroy()
           self.WGoals_label.destroy()
           self.WLWGoalsEntry.destroy()
           self.WLheight_label.destroy()
           self.WLin_label.destroy()
           self.WLft_label.destroy()
           self.WLheightft_entry.destroy()
           self.WLheightin_entry.destroy()
           self.WLweight_label.destroy()
           self.WLlb_label.destroy()
           self.WLweight_entry.destroy()
           self.WLage_label.destroy()
           self.WLage_entry.destroy()
           self.WLGender_label.destroy()
           self.WLGenderEntry.destroy()
           
           
           self.CClabel = ttk.Label(self, text="Calorie Count", font= ('Arial' , 50, 'bold',),borderwidth = 2, relief = "groove")
           self.CClabel.pack(side="top",pady=20) # size of window         
           self.DCClabel = ttk.Label(self, text="Your daily calorie count to loose 0.5 pounds in a week is :", font= ('Arial' , 15),borderwidth = 2, relief = "groove")
           self.DCClabel.pack
           self.DCClabel.place(x=350,y=180)
           self.Ccalorielabel = ttk.Label(self, text=calories, font= ('Arial' , 20, 'bold',),borderwidth = 2, relief = "groove")
           self.Ccalorielabel.pack
           self.Ccalorielabel.place(x=480, y=210)
           self.calorieslabel = ttk.Label(self, text="calories", font= ('Arial' , 20, 'bold',),borderwidth = 2, relief = "groove")
           self.calorieslabel.pack
           self.calorieslabel.place(x=550, y=210)
        
        elif (self.WLWGoalsEntry.get() == "1lb" and self.WLGenderEntry.get() == "Male"):
               
           calories = round(0.93*MenBMR)
           
           
           self.WLosslabel.destroy()
           self.continuebutton.destroy()
           self.WLosslabel.destroy
           self.label.destroy()
           self.WGoals_label.destroy()
           self.WLWGoalsEntry.destroy()
           self.WLheight_label.destroy()
           self.WLin_label.destroy()
           self.WLft_label.destroy()
           self.WLheightft_entry.destroy()
           self.WLheightin_entry.destroy()
           self.WLweight_label.destroy()
           self.WLlb_label.destroy()
           self.WLweight_entry.destroy()
           self.WLage_label.destroy()
           self.WLage_entry.destroy()
           self.WLGender_label.destroy()
           self.WLGenderEntry.destroy()
           
           
           self.CClabel = ttk.Label(self, text="Calorie Count", font= ('Arial' , 50, 'bold',),borderwidth = 2, relief = "groove")
           self.CClabel.pack(side="top",pady=20) # size of window         
           self.DCClabel = ttk.Label(self, text="Your daily calorie count to loose 1 pound in a week is :", font= ('Arial' , 15),borderwidth = 2, relief = "groove")
           self.DCClabel.pack
           self.DCClabel.place(x=350,y=180)
           self.Ccalorielabel = ttk.Label(self, text=calories, font= ('Arial' , 20, 'bold',),borderwidth = 2, relief = "groove")
           self.Ccalorielabel.pack
           self.Ccalorielabel.place(x=480, y=210)
           self.calorieslabel = ttk.Label(self, text="calories", font= ('Arial' , 20, 'bold',),borderwidth = 2, relief = "groove")
           self.calorieslabel.pack
           self.calorieslabel.place(x=550, y=210)
           
        elif (self.WLWGoalsEntry.get() == "2lbs" and self.WLGenderEntry.get() == "Male"):
             
           calories = round(0.678*MenBMR)
           self.WLosslabel.destroy()
           self.continuebutton.destroy()
           self.WLosslabel.destroy
           self.label.destroy()
           self.WGoals_label.destroy()
           self.WLWGoalsEntry.destroy()
           self.WLheight_label.destroy()
           self.WLin_label.destroy()
           self.WLft_label.destroy()
           self.WLheightft_entry.destroy()
           self.WLheightin_entry.destroy()
           self.WLweight_label.destroy()
           self.WLlb_label.destroy()
           self.WLweight_entry.destroy()
           self.WLage_label.destroy()
           self.WLage_entry.destroy()
           self.WLGender_label.destroy()
           self.WLGenderEntry.destroy()
           
           
           self.CClabel = ttk.Label(self, text="Calorie Count", font= ('Arial' , 50, 'bold',),borderwidth = 2, relief = "groove")
           self.CClabel.pack(side="top",pady=20) # size of window         
           self.DCClabel = ttk.Label(self, text="Your daily calorie count to loose 2 pound in a week is :", font= ('Arial' , 15),borderwidth = 2, relief = "groove")
           self.DCClabel.pack
           self.DCClabel.place(x=350,y=180)
           self.Ccalorielabel = ttk.Label(self, text=calories, font= ('Arial' , 20, 'bold',),borderwidth = 2, relief = "groove")
           self.Ccalorielabel.pack
           self.Ccalorielabel.place(x=480, y=210)
           self.calorieslabel = ttk.Label(self, text="calories", font= ('Arial' , 20, 'bold',),borderwidth = 2, relief = "groove")
           self.calorieslabel.pack
           self.calorieslabel.place(x=550, y=210)

        if (self.WLWGoalsEntry.get() == "0.5lbs" and self.WLGenderEntry.get() == "Female"):
            
           calories = round(1.004*WomenBMR)
           
           
           self.WLosslabel.destroy()
           self.continuebutton.destroy()
           self.WLosslabel.destroy
           self.label.destroy()
           self.WGoals_label.destroy()
           self.WLWGoalsEntry.destroy()
           self.WLheight_label.destroy()
           self.WLin_label.destroy()
           self.WLft_label.destroy()
           self.WLheightft_entry.destroy()
           self.WLheightin_entry.destroy()
           self.WLweight_label.destroy()
           self.WLlb_label.destroy()
           self.WLweight_entry.destroy()
           self.WLage_label.destroy()
           self.WLage_entry.destroy()
           self.WLGender_label.destroy()
           self.WLGenderEntry.destroy()
           
           
           self.CClabel = ttk.Label(self, text="Calorie Count", font= ('Arial' , 50, 'bold',),borderwidth = 2, relief = "groove")
           self.CClabel.pack(side="top",pady=20) # size of window         
           self.DCClabel = ttk.Label(self, text="Your daily calorie count to loose 0.5 pounds in a week is :", font= ('Arial' , 15),borderwidth = 2, relief = "groove")
           self.DCClabel.pack
           self.DCClabel.place(x=350,y=180)
           self.Ccalorielabel = ttk.Label(self, text=calories, font= ('Arial' , 20, 'bold',),borderwidth = 2, relief = "groove")
           self.Ccalorielabel.pack
           self.Ccalorielabel.place(x=480, y=210)
           self.calorieslabel = ttk.Label(self, text="calories", font= ('Arial' , 20, 'bold',),borderwidth = 2, relief = "groove")
           self.calorieslabel.pack
           self.calorieslabel.place(x=550, y=210)
        
        elif (self.WLWGoalsEntry.get() == "1lb" and self.WLGenderEntry.get() == "Female"):
               
           calories = round(0.85*WomenBMR)
           
           
           self.WLosslabel.destroy()
           self.continuebutton.destroy()
           self.WLosslabel.destroy
           self.label.destroy()
           self.WGoals_label.destroy()
           self.WLWGoalsEntry.destroy()
           self.WLheight_label.destroy()
           self.WLin_label.destroy()
           self.WLft_label.destroy()
           self.WLheightft_entry.destroy()
           self.WLheightin_entry.destroy()
           self.WLweight_label.destroy()
           self.WLlb_label.destroy()
           self.WLweight_entry.destroy()
           self.WLage_label.destroy()
           self.WLage_entry.destroy()
           self.WLGender_label.destroy()
           self.WLGenderEntry.destroy()
           
           
           self.CClabel = ttk.Label(self, text="Calorie Count", font= ('Arial' , 50, 'bold',),borderwidth = 2, relief = "groove")
           self.CClabel.pack(side="top",pady=20) # size of window         
           self.DCClabel = ttk.Label(self, text="Your daily calorie count to loose 1 pound in a week is :", font= ('Arial' , 15),borderwidth = 2, relief = "groove")
           self.DCClabel.pack
           self.DCClabel.place(x=350,y=180)
           self.Ccalorielabel = ttk.Label(self, text=calories, font= ('Arial' , 20, 'bold',),borderwidth = 2, relief = "groove")
           self.Ccalorielabel.pack
           self.Ccalorielabel.place(x=480, y=210)
           self.calorieslabel = ttk.Label(self, text="calories", font= ('Arial' , 20, 'bold',),borderwidth = 2, relief = "groove")
           self.calorieslabel.pack
           self.calorieslabel.place(x=550, y=210)
           
        elif (self.WLWGoalsEntry.get() == "2lbs" and self.WLGenderEntry.get() == "Female"):
             
           calories = round(0.5*WomenBMR)
           self.WLosslabel.destroy()
           self.continuebutton.destroy()
           self.WLosslabel.destroy
           self.label.destroy()
           self.WGoals_label.destroy()
           self.WLWGoalsEntry.destroy()
           self.WLheight_label.destroy()
           self.WLin_label.destroy()
           self.WLft_label.destroy()
           self.WLheightft_entry.destroy()
           self.WLheightin_entry.destroy()
           self.WLweight_label.destroy()
           self.WLlb_label.destroy()
           self.WLweight_entry.destroy()
           self.WLage_label.destroy()
           self.WLage_entry.destroy()
           self.WLGender_label.destroy()
           self.WLGenderEntry.destroy()
           
           
           self.CClabel = ttk.Label(self, text="Calorie Count", font= ('Arial' , 50, 'bold',),borderwidth = 2, relief = "groove")
           self.CClabel.pack(side="top",pady=20) # size of window         
           self.DCClabel = ttk.Label(self, text="Your daily calorie count to loose 2 pound in a week is :", font= ('Arial' , 15),borderwidth = 2, relief = "groove")
           self.DCClabel.pack
           self.DCClabel.place(x=350,y=180)
           self.Ccalorielabel = ttk.Label(self, text=calories, font= ('Arial' , 20, 'bold',),borderwidth = 2, relief = "groove")
           self.Ccalorielabel.pack
           self.Ccalorielabel.place(x=480, y=210)
           self.calorieslabel = ttk.Label(self, text="calories", font= ('Arial' , 20, 'bold',),borderwidth = 2, relief = "groove")
           self.calorieslabel.pack
           self.calorieslabel.place(x=550, y=210)       
        
class CalorieGainPage(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self,parent)
        self.controller=controller            
       
      
class WorkoutPage(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self,parent)
    
        self.controller=controller 
        
        # Workout page top label
        self.BMIlabel = ttk.Label(self, text="What Do You Want to Workout", font= ('Arial' , 50, 'bold',),borderwidth = 2, relief = "groove")
        self.BMIlabel.pack(side="top",pady=20) # size of window
        
        
        
       
         

#--------------------------------------------------------
# Main
#--------------------------------------------------------   
app = MainWindow()

def close(event): #Function to close GUI with Esc key
    app.quit()   # quit app
    app.destroy()

# Binds close function to CTRL-Q
app.bind('<Control-Key-Q>', close)

app.geometry('1080x600')

app.title("TitanFit")
#app.overrideredirect(True)
#app.overrideredirect(False)
#app.attributes('-fullscreen',True) # Causes GUI to fill screen    

app.mainloop()
app.quit()
