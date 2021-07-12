from tkinter import *
root=Tk()
root.geometry("312x394")  # Size of the window
root.title("calculator")
root.iconbitmap('C:/Users/Dell/Desktop/calcu.ico') #changing image

########### Function ############

a=StringVar()

def clear():   # helps to clear the given value
    a.set(" ")

def setbtn(value):
    a.set(a.get() +value) #concentation

def answer():
    ans= eval(a.get())    # eval is a function in the python library which convert any kind of maths data in appropriate format float to int etc.
    a.set(ans)


############ main entry window ########################





entry=Entry (root,font=("",20),justify="right",textvariable=a ) #TO GIVE THE VALUE FROM RIGHT

entry.grid(row=0,column=0,columnspan=3,padx=5,pady=5)  #grid manage the gemotry ; like the size of the button


########################Button Start#############################

#### row 1#######################

b1=Button(root,text="clear" ,fg="white",width=10 ,height=2, bg="black", command= clear)
b1.grid(row=1,column=0,padx=5,pady=5)  #pad is used to increase the spacing in the button.

b2=Button(root,text="0",fg="white",width=10 ,height=2,bg="black" ,command= lambda : setbtn ("0"))
b2.grid(row=1,column=1,padx=5,pady=5)

b3=Button(root,text="." ,fg="white",width=10 ,height=2,bg="black" , command= lambda : setbtn (".") )
b3.grid(row=1,column=2,padx=5,pady=5)

########ROW 2##################

nine=Button(root,text="9",fg="white",width=10 ,height=2,bg="black", command= lambda : setbtn ("9"))
nine.grid(row=2,column=0,padx=5 ,pady=5)

eight=Button(root,text="8",fg="white",width=10 ,height=2, bg="black",command= lambda : setbtn ("8"))
eight.grid(row=2,column=1,padx=5 ,pady=5)

seven=Button(root,text="7",fg="white",width=10 ,height=2, bg="black" ,command= lambda : setbtn ("7"))
seven.grid(row=2,column=2,padx=5 ,pady=5)

############## ROW 3 ################

six=Button(root,text="6",fg="white",width=10 ,height=2, bg="black", command= lambda : setbtn ("6"))
six.grid(row=3,column=0,padx=5 ,pady=5)

five=Button(root,text="5", fg="white",width=10 ,height=2, bg="black", command= lambda : setbtn ("5"))
five.grid(row=3,column=1,padx=5 ,pady=5)

four=Button(root,text="4",fg="white",width=10 , height=2, bg="black",command= lambda : setbtn ("4"))
four.grid(row=3,column=2,padx=5 ,pady=5)

################## ROW 4 ################

three=Button(root,text="3",fg="white",width=10 ,height=2, bg="black",command= lambda : setbtn ("3"))
three.grid(row=4,column=0,padx=5 ,pady=5)

two=Button(root,text="2",fg="white",width=10 ,height=2,bg="black", command= lambda : setbtn ("2"))
two.grid(row=4,column=1,padx=5 ,pady=5)

one=Button(root,text="1",fg="white",width=10 ,height=2,bg="black", command= lambda : setbtn ("1"))
one.grid(row=4,column=2,padx=5 ,pady=5)

########### ROW 5 ##############

plus=Button(root,text="+",fg="white",width=10 ,height=2,bg="black", command= lambda : setbtn ("+"))
plus.grid(row=5,column=0,padx=5 ,pady=5)

minus=Button(root,text="-",fg="white",width=10 ,height=2,bg="black", command= lambda : setbtn ("-"))
minus.grid(row=5,column=1,padx=5 ,pady=5)

mul=Button(root,text="*",fg="white",width=10 ,height=2, bg="black",command= lambda : setbtn ("*"))
mul.grid(row=5,column=2,padx=5 ,pady=5)


########### ROW 6 ##############

divide=Button(root,text="/",fg="white",width=10 ,height=2,bg="black", command= lambda : setbtn ("/"))
divide.grid(row=6,column=0,padx=5 ,pady=5)

mod=Button(root,text="%",fg="white",width=10 ,height=2, bg="black",command= lambda : setbtn ("%"))
mod.grid(row=6,column=1,padx=5 ,pady=5)

equalto=Button(root,text="=",fg="white",width=10 ,height=2,bg="black", command = answer)
equalto.grid(row=6,column=2,padx=5 ,pady=5)



root=mainloop()
