from tkinter import *

root = Tk()
root.geometry("800x530")
root.title("BBQ Olive Chicken")
root.config(bg = "lemonchiffon")

val1 = IntVar()
val2 = IntVar()
val3 = BooleanVar()
val4 = BooleanVar()
val5 = BooleanVar()

def fried():
    if val1.get() == 1:
        label_item = Label(right_frame, text=" ", bg = "white")
        label_item = Label(right_frame, text="Golden Tenders   $10.99", bg = "white")
        label_item.grid(row=3, column=2)
    if val1.get() == 2:
        label_item = Label(right_frame, text=" ", bg = "white")
        label_item = Label(right_frame, text="Golden Wings   $9.99", bg = "white")
        label_item.grid(row=3, column=2)
    if val1.get() == 3:
        label_item = Label(right_frame, text=" ", bg = "white")
        label_item = Label(right_frame, text="Golden Whole   $19.99", bg="white")
        label_item.grid(row=3, column=2)
def spicy():
    if val2.get() == 1:
        label_item = Label(right_frame, text="Spicy Tenders  $11.99", bg="white")
        label_item.grid(row=4, column=2)
    elif val2.get() == 2:
        label_item2 = Label(right_frame, text="Spicy Wings  $10.99", bg="white")
        label_item2.grid(row=4, column=2)
    elif val2.get() == 3:
        label_item3 = Label(right_frame, text="Spicy Whole  $20.99", bg="white")
        label_item3.grid(row=4, column=2)
def side():
    if (val3.get() == 1):
        label_item4 = Label(right_frame, text = "Fries  $3.99", bg = "white")
        label_item4.grid(row = 5, column = 2)
    if (val4.get() == 1):
        label_item5 = Label(right_frame, text = "Coleslaw  $3.99", bg = "white")
        label_item5.grid(row = 6, column = 2)
    if (val5.get() == 1):
        label_item6 = Label(right_frame, text = "Calamari  $7.99", bg ="white")
        label_item6.grid(row = 7, column = 2)

top_frame = Frame(root, width = 400, height = 70, bg = "white")
top_frame.grid(row = 0, column = 0, padx = 5, pady = 10)
# must be a .png file. 'r' to convert to raw
icon = PhotoImage(file = r"C:\Users\lytph\PycharmProjects\orderApp\app_pictures\logo.png")
iconlabel = Label(top_frame, image = icon, bg = "white")
iconlabel.grid(row = 1, column = 0, padx = 5, pady = 5)

left_frame = Frame(root, width = 400, height = 400, bg = "white")
left_frame.grid(row = 1, column = 0, padx = 5, pady = 5)

entree_frame = Frame(left_frame, width = 370, height = 390, bg = "white")
entree_frame.grid(row = 1, column = 0, padx = 5, pady = 5)

label_entree = Label(entree_frame, text = "Menu", width = 50, bg = "white")
label_entree.grid(row = 2, column = 0, padx = 5, pady = 5)

label_entree1 = Label(entree_frame, text = "Golden Olive Chicken", width = 50, bg ="white")
label_entree1.grid(row = 3, column = 0, padx = 5, pady = 5)

radio1 = Radiobutton(entree_frame, text = "Tenders", value = 1, variable = val1,  bg = "white", anchor = "w", command = fried)
radio1.grid(row = 4, column = 0, padx = 10)
radio2 = Radiobutton(entree_frame, text = "Wings", value = 2, variable = val1,  bg ="white", anchor = "w", command = fried)
radio2.grid(row = 5, column = 0, padx = 10)
radio3 = Radiobutton(entree_frame, text = "Whole", value =3, variable = val1, bg = "white", anchor = "w", command = fried)
radio3.grid(row = 6, column = 0, padx = 10)

label_price = Label(entree_frame, text = "$10.99", bg = "white")
label_price.grid(row = 4, column = 1, padx = 5)
label_price2 = Label(entree_frame, text = "$9.99", bg = "white")
label_price2.grid(row = 5, column = 1, padx = 5)
label_price3 = Label(entree_frame, text = "$19.99", bg = "white")
label_price3.grid(row = 6, column = 1, padx = 5)

label_entree2 = Label(entree_frame, text = "Secret Spicy Chicken", width = 50, bg ="white")
label_entree2.grid(row = 7, column = 0, padx = 5, pady =5)

radio1 = Radiobutton(entree_frame, text = "Tenders", value = 1, variable = val2, bg = "white", command = spicy)
radio1.grid(row = 8, column = 0, padx = 10)
radio2 = Radiobutton(entree_frame, text = "Wings", value = 2, variable = val2,  bg ="white", command = spicy)
radio2.grid(row = 9, column = 0, padx = 10)
radio3 = Radiobutton(entree_frame, text = "Whole", value = 3, variable = val2, bg = "white", command = spicy)
radio3.grid(row = 10, column = 0, padx = 10)

label_price4 = Label(entree_frame, text = "$11.99", bg = "white")
label_price4.grid(row = 8, column = 1, padx = 5)
label_price5 = Label(entree_frame, text = "$10.99", bg = "white")
label_price5.grid(row = 9, column = 1, padx = 5)
label_price6 = Label(entree_frame, text = "$20.99", bg = "white")
label_price6.grid(row = 10, column = 1, padx = 5)

label_side = Label(entree_frame, text = "Sides", width = 50, bg = "white")
label_side.grid(row = 11, column = 0, padx =5, pady =5)

check1 = Checkbutton(entree_frame, text = "Fries", variable = val3, bg = "white", anchor = "w", command = side)
check1.grid(row = 12, column = 0, padx = 10)
check2 = Checkbutton(entree_frame, text = "Coleslaw", variable = val4, bg = "white", anchor = "w", command = side)
check2.grid(row = 13, column = 0, padx = 10)
check3 = Checkbutton(entree_frame, text = "Calamari", variable = val5, bg = "white", anchor = "w", command = side)
check3.grid(row = 14, column = 0, padx = 10)

label_price7 = Label(entree_frame, text = "$3.99", bg = "white")
label_price7.grid(row = 12, column = 1, padx = 5)
label_price8 = Label(entree_frame, text = "$3.99", bg = "white")
label_price8.grid(row = 13, column = 1, padx = 5)
label_price9 = Label(entree_frame, text = "$7.99", bg = "white")
label_price9.grid(row = 14, column = 1, padx = 5)

right_frame = Frame(root, width = 200, height = 200, bg = "white")
right_frame.grid(row = 1, column = 2, padx = 5, pady = 5)
label_order = Label(right_frame, text = "Order", width = 30, bg = "white")
label_order.grid(row = 2, column = 2, padx = 5, pady =5)

button = Button(root, text = "Place Order", bg = "red3", fg = "white", relief = "flat")
button.config(width = 12, height = 2)
button.grid(row = 6, column = 2, padx = 5, pady = 5)

spicy()
fried()
side()
root.mainloop()