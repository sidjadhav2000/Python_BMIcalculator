from tkinter import * 
from tkinter.messagebox import*


root = Tk()
root.title("BMI CALCULATOR")
root.configure(bg = "lightgreen")
root.geometry("600x600+100+100")
f = ("Arial", 20, "bold")

def bmi_cal():
	try:
		try:
			a = int(ent_age.get())
			if (a<1) or (a>120):
				showerror("Issue","AGE should be between 1 to 120")
				return
		except ValueError:
			showerror("Issue", "Enter Number")
			return
		try:	
			h = float(ent_height.get())
			if h<0:
				showerror("Issue","Enter Valid Height")
				return
		except ValueError:
			showerror("Issue","Enter Number")
			return
		try:
			w = float(ent_weight.get())
			if w<0:
				showerror("Issue","Enter Postive Weight")
				return
		except ValueError:
			showerror("Issue","Enter Number")
			return

		h1 = h / 100
		h2 = h1 * h1
		w1 = w / h2
		res = round(w1,2)
		
		if res < 18.5 :
			showinfo(res,"Underweight")
		
		elif res < 25 :
			showinfo(res,"Normal")
		
		elif res < 30 :
			showinfo(res,"Overweight")
		else :
			showinfo(res,"Obasity")

		ent_age.delete(0,END)
		ent_height.delete(0,END)
		ent_weight.delete(0,END)

		ent_age.focus()
		rb.set(1)

	except Exception as e:
		showerror("Issue",e)		
		
lab_header = Label(root, text = "BODY MASS INDEX CALCULATOR(BMI)", font=f , bg = "lightgreen" )
lab_header.pack(pady=20)

rb = IntVar()
rb.set(1)
rb_male = Radiobutton(root, text = "MALE", font=f, bg = "lightblue",variable=rb, value=1)
rb_female = Radiobutton(root, text = "FEMALE", font =f, bg = "lightblue",variable=rb, value=2)
rb_male.place (x =100, y=100)
rb_female.place(x=300, y=100)


lab_age = Label(root, text = "AGE", font = f, bg = "lightblue")
ent_age = Entry(root, font=f, width=5)
lab_age.place(x=150, y=200)
ent_age.place(x=250, y=200)

lab_height = Label(root, text = "HEIGHT(cm)", font=f, bg="lightblue")
ent_height = Entry(root, font=f, width=5)
lab_height.place(x=50, y=300)
ent_height.place(x=250,y=300)

lab_weight = Label(root, text="WEIGHT(Kg)", font=f, bg="lightblue")
ent_weight = Entry(root, font=f, width=5)
lab_weight.place(x=50, y=400)
ent_weight.place(x=250,y=400)

but_cal = Button(root,text="CALCULATE", font=f, bg="lightblue",command = bmi_cal)
but_cal.place(x=200,y=480)


root.mainloop() 