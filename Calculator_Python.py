from tkinter import *
#Basic Window
r=Tk()
r.geometry("300x324")
#Prevents resizing of window in future 
r.resizable(0,0)
#Titile of the Window
r.title("My_Simple_Calculator")
#Helps to get input as a clicked button
def button_click(item):
    global exp
    exp=exp+str(item)
    input_t.set(exp)
#Helps to clears the entered expression
def btn_clean():
    global exp
    exp=""
    input_t.set("")
#Evaluates the entered expression
def btn_eval():
    global exp
    result=str(eval(exp))
    input_t.set(result)
    exp=""
#starts the program here
#At first the expression in empty
exp=""
input_t=StringVar()#Evaluates the string as it is
#Expression Field where the evaluation takes place
input_frame=Frame(r,width=300,height=50,bd=0,highlightbackground="black",highlightthickness=2)
input_frame.pack(side=TOP)#Packs at the top of the frame

input_field=Entry(input_frame,font=('arial',18,'bold'),textvariable=input_t,width=50,bg='#eee',bd=0,justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)
#ipady increases the height of input field
btn_frame=Frame(r,width=300,height=272.5,bg="black")
btn_frame.pack()
#Buttons
clear=Button(btn_frame,text="Clear",fg="black",width=30,height=4,bg='yellow',cursor="hand2",command=lambda:btn_clean()).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide=Button(btn_frame,text="/",fg="black",width=10,height=3,bd=0,bg='palegreen',cursor="hand2",command=lambda:button_click("/")).grid(row=0,column=3,padx=1,pady=1)
seven=Button(btn_frame,text="7",fg="black",width=10,height=3,bd=0,bg='pink',cursor="hand2",command=lambda:button_click(7)).grid(row=1,column=0,padx=1,pady=1)
eight=Button(btn_frame,text="8",fg="black",width=10,height=3,bd=0,bg='pink',cursor="hand2",command=lambda:button_click(8)).grid(row=1,column=1,padx=1,pady=1)
nine=Button(btn_frame,text="9",fg="black",width=10,height=3,bd=0,bg='pink',cursor="hand2",command=lambda:button_click(9)).grid(row=1,column=2,padx=1,pady=1)
multiply=Button(btn_frame,text="*",fg="black",width=10,height=3,bd=0,bg='palegreen',cursor="hand2",command=lambda:button_click("*")).grid(row=1,column=3,padx=1,pady=1)

four = Button(btn_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = 'pink', cursor = "hand2", command = lambda: button_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btn_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = 'pink', cursor = "hand2", command = lambda: button_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btn_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = 'pink', cursor = "hand2", command = lambda: button_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btn_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = 'palegreen', cursor = "hand2", command = lambda: button_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)


one = Button(btn_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = 'pink', cursor = "hand2", command = lambda: button_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btn_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = 'pink', cursor = "hand2", command = lambda: button_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btn_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = 'pink', cursor = "hand2", command = lambda: button_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btn_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = 'palegreen', cursor = "hand2", command = lambda: button_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

zero = Button(btn_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = 'pink', cursor = "hand2", command = lambda: button_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btn_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = 'pink', cursor = "hand2", command = lambda: button_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btn_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "palegreen", cursor = "hand2", command = lambda: btn_eval()).grid(row = 4, column = 3, padx = 1, pady = 1)
r.mainloop()





