from tkinter import*
def ftoc():
 t1=float(input_t1.get())
 res=(t1-32)*(5/9)
 lbl_res.config(text=str(res)+"°c")
def ctof():
 t1=float(input_t1.get())
 res=t1*(9/5)+32
 lbl_res.config(text=str(res)+"°f")
root=Tk()
root.configure(background="red")
root.title("Temperature_converter")
root.geometry("500x500+500+100")
root.resizable(False,False)
lbl_title=Label(root,text="Temperature Convertor",fg="Black",font=("Arial 20 bold"))
lbl_title.place(x=100,y=50)
input_t1=Entry(root,font=("Arial 15"))
input_t1.place(x=150,y=100)
lbl_res=Label(root,text="",fg="Blue",font=("Arial 15 bold"),bg="red")
lbl_res.place(x=200,y=150)
btn_f=Button(root,text="FtoC",font=("Arial 15 bold"),fg="black",relief=SUNKEN,command=ftoc)
btn_f.place(x=200,y=200)
btn_c=Button(root,text="CtoF",font=("Arial 15 bold"),fg="black",relief=SUNKEN,command=ctof)
btn_c.place(x=200,y=300)
root.mainloop()