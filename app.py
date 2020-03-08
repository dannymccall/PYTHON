from tkinter import messagebox
import random
import tkinter as tk

def password_generator(): 

	#Opening a try block
	try:  	
		#declaring a variable pw as a string without initialising
			pw = str()
			#Getting the input from the text box
			length = text_field_1.get()
			if length == '':
				messagebox.showerror('error', 'Enter your length of characters')
			#declaring a variable called characters to hold the password characters
			charactors = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@%!"
			#Converting the length to an integer 
			number = int(length)
			#Looping through length 
			for i in range(number):
			
				#Generating the password
				pw = pw + random.choice(charactors) 

				
			return pw
		#Catching a value error
	except ValueError:
		messagebox.showerror('error', 'Inputs should be numbers only')

#Displaying the password
def pass_display():

	password = password_generator() 
	# display the password in a new window
	password_dislay = tk.Text(master=window, height=10, width=30)

	password_dislay.grid(column=0, row=3)
	password_dislay.insert(tk.END, password)

def clear_button():
	text_field_1.delete(0)

#--Master window--
window = tk.Tk()
window.title("Welcome to my app")
size = "400x400"
window.geometry(size)

#---Labels---
label_1 = tk.Label(text="Welcome to my Random Password Generator")
label_1.grid(column=0, row=0)

label_2 = tk.Label(text="Enter your number of characters")
label_2.grid(column=0, row=1)

#---Text fields ----
text_field_1 = tk.Entry()
text_field_1.grid(column=1, row=1)

#---Buttons----
button_1 = tk.Button(text="CLEAR", command=clear_button)
button_1.grid(column=1, row=2)

button = tk.Button(text="Get Your Password", bg="red", command=pass_display)
button.grid(column=0, row=2)
window.mainloop()
