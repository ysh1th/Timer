import time
import multiprocessing
from tkinter import *
from tkinter import ttk, messagebox
from playsound import playsound
from threading import *

hour_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
20,21,22,23,24]
min_sec_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
20,21,22,23,24,25,26,27,28,9,30,31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
]

class countdown:
    def __init__(self,timer):
        self.window = timer
        self.window.geometry("480x320+0+0")
        self.window.title('Countdown timer')
        self.window.config(bg = '#495C83')
        self.window.resizable(width = False, height = False)

        #declaring a variable to pause the countdown time
        self.pause = False

        #=================================================
        # start and pause buttons are place in 
        #this frame
        self.button_frame = Frame(self.window, bg = "#495C83",
         width = 240, height = 40)
        self.button_frame.place(x = 230, y = 150)
        # this frame is used to show countdown time label
        self.time_frame = Frame(self.window,bg = "#495C83",
         width = 480, height = 120).place(x=0, y = 210)

        #tkinter labels
        time_label = Label(self.window, text="Set Time",
        font = ("times new roman", 25, "bold"), bg = '#495C83',
         fg = 'yellow').place(x=180, y=30)
         
        hour_label = Label(self.window, text="Hour",
         font=("times new roman",15), bg = '#495C83',
          fg = 'white').place(x = 50, y = 70)

        minute_label = Label(self.window, text = 'Minute',
        font=("times new roman", 15),bg = '#495C83',
        fg = 'white').place(x=200, y=70)

        second_label = Label(self.window, text="Second", font = ("times new roman",15),
        bg = '#495C83', fg = 'white').place(x = 350, y = 70)
        # ================================================================
        
        #Tkinter comboboxes
        #combobox for hours
        self.hour = IntVar()
        self.hour_combobox = ttk.Combobox(self.window, width=8, height=10,textvariable=self.hour, font=("times new roman",15))
        self.hour_combobox['values'] = hour_list
        self.hour_combobox.current(0)
        self.hour_combobox.place(x=50,y=110)

        #combobox for minutes
        self.minute = IntVar()
        self.minute_combobox = ttk.Combobox(self.window, width=8, height = 10, textvariable=self.hour, font=('times new roman',15))
        self.minute_combobox['values']=min_sec_list
        self.minute_combobox.current(0)
        self.minute_combobox.place(x=200,y=110)

        #combobox for seconds
        self.second = IntVar()
        self.second_combobox = ttk.Combobox(self.window, width=8, height=10, textvariable=self.second, font=('times new roman',15))
        self.second_combobox['values']= min_sec_list
        self.second_combobox.current(0)
        self.second_combobox.place(x=350,y=110)
        #=================================================================
        
        #tkinter buttons
        #Cancel buttons
        cancel_button=Button(self.window, text='Exit', font=('Helvetivca',12),bd = '4', bg = 'antique white', command=self.cancel).place(x=70,y=150)

        #Set time button
        #when this is presses
        #'Start' and 'Pause' button will 
        #show inside the 'self.button_frame' frame
        set_button = Button(self.window, text = 'Set', font=('Helvetica',12), bd='4', bg = 'antique white', command=self.get_time).place(x=160,y=150)
    
    #this will destroy the window
    def cancel(self):
        self.pause=True
        self.window.destroy()
    #when set button is pressed,
    #this fn gets called
    def get_time(self):
        self.time_display = Label(self.time_frame,font=('Helvetica', 20 , "bold"), 
        bg = 'gray35', fg = 'yellow')
        self.time_display.place(x=130,y=210)

        try:
            # total amount of time in seconds
            h = (int(self.hour_combobox.get())*3600)
            m = (int(self.minute_combobox.get())*60)
            s = (int(self.second_combobox.get()))
            self.time_left = h+m+s

            #if user tries to set time (0:0:0) 
            # a warning message will display
            if s == 0 and m == 0 and h == 0:
                messagebox.showwarning('Warning!',
                'Please select a right time to set')
            else:
                # Start Button
                start_button = Button(self.button_frame, text='Start', font=('Helvetica',12), bg="green", fg="white",
                command=self.Threading)
                start_button.place(x=20, y=0)

                #Pause Button
                pause_button = Button(self.button_frame, text='Pause', 
                font=('Helvetica',12), bg='red', fg='white', 
                command=self.pause_time)
                pause_button.place(x=100,y=0)
        except Exception as es:
            messagebox.showerror("Error!",
            f"Error due to {es}")

    #creating a thread to run the show_time function
    def Threading(self):
        #killing a thread through "daemon=True" isn't a good idea
        self.x = Thread(target=self.start_time, daemon=True)
        self.x.start()

    #it will clear all the widgets inside the
    #'self.button_frame' frame(start and pause buttons)
    def clear_screen(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()
    def pause_time(self):
        self.pause=True
        
        mins, secs = divmod(self.time_left,60)
        hours=0
        if mins>60:
            #hour minute
            hours, mins = divmod(mins,60)

        self.time_display.config(text=f"Time Left: {hours}: {mins}: {secs}")
        self.time_display.update()

    #when the start button will be pressed then,
    #this "show_time" fn will get called.
    def start_time(self):
        self.pause=False
        while self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)

            hours = 0
            if mins >60:
                #hour minute
                hours, mins = divmod(mins,60)
            
            self.time_display.config(text=f"Time Left: {hours}: {mins}: {secs}")
            self.time_display.update()
            #sleep fn: for 1 second
            time.sleep(1)
            self.time_left = self.time_left-1
            #when the time is over, a piece of music 
            #will play in the background

            if self.time_left<=0:
                process = multiprocessing.Process(target=playsound,
                args=('C:\\Users\\PlayerUNKNOWN\\Music\\Haggstrom2.wav'))
                process.start()
                messagebox.showinfo("Time over","Please Enter to stop playing")
                process.terminate()
                #clearing the 'self.button_frame' frame
                self.clear_screen()
            #if the pause button is pressed
            #the while loop will break
            if self.pause == True:
                break

if __name__ == "__main__":
    timer = Tk()
    obj = countdown(timer)
    timer.mainloop()
