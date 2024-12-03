from tkinter import *
from tkinter.messagebox import *
font = ("raised", 12, "bold",)
padx = 0
pady = 0
width = 7
# Important Function
def clear():
    ex =textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0, END)
    textField.insert(0, ex)

def all_clear():
    textField.delete(0, END)

def click_btn_function(event):
    print("btn clicked")
    b=event.widget
    text = b['text']
    print(text)
    if text == "X":
        textField.insert(END, "*")
        return

    if text == "=":
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)
        except Exception as e:
            print("Error",e)
            showerror("Error",e)


        return
    textField.insert(END, text)




# creating a window

window = Tk()
window.title("Kavira Calculator")
window.geometry("340x240")
# Heading Label
heading = Label(window, text="Kavira Calculator", font=font)


# Text Field

textField = Entry(window,font = font,justify=CENTER, width=7, borderwidth=7)
textField.pack(side=TOP, fill=X,padx=padx, pady=pady)
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)
Temp = 1
for i in range(0,3):
    for j in range(0,3):
        btn =Button(buttonFrame, text=str(Temp),font=font,width = width ,relief = "raised",activebackground='red', activeforeground='black')
        btn.grid(row=i, column=j,padx = padx, pady =pady)
        Temp = Temp+1
        btn.bind("<Button-1>", click_btn_function)




zero_btn = btn =Button(buttonFrame, text=0,font=font,width = width,relief = "raised",activebackground='red', activeforeground='black')
zero_btn.grid(row=3, column=1,padx = padx, pady =pady)

dot_btn = btn =Button(buttonFrame, text='.',font=font,width = width,relief = "raised",activebackground='red', activeforeground='black')
dot_btn.grid(row=3, column=0,padx = padx, pady =pady)

all_clear_btn = Button(buttonFrame, text='AC', font=font, width=width, relief="raised", activebackground='red', activeforeground='black', command=all_clear)
all_clear_btn.grid(row=0, column=3, padx=padx, pady=pady)

Clear_btn = btn =Button(buttonFrame, text='c',font=font,width = 15,relief = "raised",activebackground='red', activeforeground='black',command = clear)
Clear_btn.grid(row=4, column=1,padx = padx, pady =pady, columnspan=2)


Add_btn = btn =Button(buttonFrame, text='+',font=font,width = width,relief = "raised",activebackground='red', activeforeground='black')
Add_btn.grid(row=1, column=3,padx = padx, pady =pady)

Sub_btn = btn =Button(buttonFrame, text='-',font=font,width = width,relief = "raised",activebackground='red', activeforeground='black')
Sub_btn.grid(row=2, column=3,padx = padx, pady =pady)

MULTIPLE_btn = btn =Button(buttonFrame, text='X',font=font,width = width,relief = "raised",activebackground='red', activeforeground='black')
MULTIPLE_btn.grid(row=3, column=3,padx = 5, pady =pady)

Divide_btn = btn =Button(buttonFrame, text='/',font=font,width = width,relief = "raised",activebackground='red', activeforeground='black')
Divide_btn.grid(row=4, column=3,padx = padx, pady =pady,columnspan=2)

Equal_btn = btn =Button(buttonFrame, text='=',font=font,width = width,relief = "raised",activebackground='red', activeforeground='black')
Equal_btn.grid(row=3, column=2,padx = padx, pady =pady)


Percent_btn = btn =Button(buttonFrame, text='%',font=font,width = width,relief = "raised",activebackground='red', activeforeground='black')
Percent_btn.grid(row=4, column=0,padx = padx, pady =pady)



# Binding all btns

Add_btn.bind("<Button-1>", click_btn_function)


MULTIPLE_btn.bind("<Button-1>", click_btn_function)


Sub_btn.bind("<Button-1>", click_btn_function)


Divide_btn.bind("<Button-1>", click_btn_function)


Percent_btn.bind("<Button-1>", click_btn_function)


Equal_btn.bind("<Button-1>", click_btn_function)

dot_btn.bind("<Button-1>", click_btn_function)

zero_btn.bind("<Button-1>", click_btn_function)




all_clear_btn.bind("<Button-1>", click_btn_function)




window.mainloop()