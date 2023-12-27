from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import datetime
from tkinter.colorchooser import askcolor
from tkinter.ttk import Scale

#_________________________________________________________________________________________________________________

MyDb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="web_page"
)
database = MyDb.cursor()

#_________________________________________________________________________________________________________________

window = Tk()
window.title("My Program")
window.geometry("770x490")
window.resizable(False, False)


title = Label(
    window,
    text="Signup Page",
    background="blue",
    foreground="white",
    font=("Tahoma", 13),
)
title.place(x=140, y=10)

app_time = Label(window, text="", foreground="black")
app_time.place(x=690, y=460)


def showtime():
    time = datetime.datetime.now().strftime("%X")
    app_time.config(text=time, font=("Tahoma", 13))
    app_time.after(1000, showtime)
showtime()


#_________________________________________________________________________________________________________________



label_firstname = Label(window, text="First Name :")
label_firstname.place(x=10, y=50)
label_lastname = Label(window, text="Last Name :")
label_lastname.place(x=10, y=80)
label_email = Label(window, text="Email : ")
label_email.place(x=10, y=110)
label_phone = Label(window, text="Phone :")
label_phone.place(x=10, y=140)
label_age = Label(window, text="Age:")
label_age.place(x=10, y=170)
label_ctstats = Label(window, text="")
label_ctstats.place(x=20, y=330)
label_sustats = Label(window, text="")
label_sustats.place(x=240, y=330)
label_destats = Label(window, text="")
label_destats.place(x=130, y=330)
label_address = Label(window, text="Address")
label_address.place(x=10, y=200)
label_list = Label(window, text="Users List :")
label_list.place(x=350, y=10)



#_________________________________________________________________________________________________________________


en_firstname = Entry(window)
en_firstname.place(x=100, y=50)
en_lastname = Entry(window)
en_lastname.place(x=100, y=80)
en_email = Entry(window)
en_email.place(x=100, y=110)
en_phone = Entry(window)
en_phone.place(x=100, y=140)
en_address = Text(window, width=25, height=4)
en_address.place(x=100, y=200)


#_________________________________________________________________________________________________________________


age_numbers = []
for x in range(1, 101):
    age_numbers.append(x)

combo_age = ttk.Combobox(window, width=5, values=age_numbers)
combo_age.place(x=100, y=170)


#_________________________________________________________________________________________________________________


def savedata():
    try:
        sql = "INSERT INTO users11 (Fname , Lname , Age , Phone , Email , Address) VALUES (%s,%s,%s,%s,%s,%s)"
        data = (
            en_firstname.get(),
            en_lastname.get(),
            combo_age.get(),
            en_phone.get(),
            en_email.get(),
            en_address.get("1.0", END),
        )
        database.execute(sql, data)
        MyDb.commit()
        list_box.insert(END, data)

    except:
        label_sustats.config(text="Save Error", foreground="red")
        messagebox.showerror("Progress ", "OOPS!! Something Went Wrong")
    else:
        label_sustats.config(text="your information \n have saved", foreground="Green")
    messagebox.showinfo(
        "Progress ",
        f"Congrats !!! your information have been saved \n your information is : \n Fname :{en_firstname.get()} \n Lname:{en_lastname.get()}\n Age : {combo_age.get()}",
    )


def Create_Table():
    try:
        database.execute(
            "CREATE TABLE users11 (id INT AUTO_INCREMENT PRIMARY KEY  , FNAME VARCHAR (50), LNAME VARCHAR (50) , AGE INT (3) ,EMAIL VARCHAR (50), Phone INT (20) , Address VARCHAR (200) ) "
        )
    except:
        label_ctstats.config(
            text="create table error \n or its available", foreground="red"
        )
        messagebox.showerror("Progress ", "Am I joke to you @_@   ??!!")
    else:
        label_ctstats.config(text="Table has created", foreground="Green")
        messagebox.showinfo(
            "Progress ", "Your table created ! now its time to fill it "
        )


def showusers():
    showuser = "SELECT * FROM users11"
    database.execute(showuser)
    list_box.delete("0", END)
    for x in database:
        list_box.insert(END, x)


def delete():
    en_firstname.delete("0", END)
    en_lastname.delete("0", END)
    en_email.delete("0", END)
    combo_age.delete("0", END)
    en_phone.delete("0", END)
    en_address.delete("1.0", END)
    label_destats.config(text="Form cleared", foreground="Green")


def delete_all_list():
    if messagebox.askyesno("Warning", "you are clearing the list , are you sure?"):
        list_box.delete("0", END)
    else:
        pass


def delete_all_datas():
    if messagebox.askyesno(
        "may lost your all data",
        "you are removing data from database , wanna continue ??",
    ):
        delete_all_database = "TRUNCATE TABLE `web_page`.`users11`"
        database.execute(delete_all_database)


def delete_database():
    if messagebox.askyesno(
        "Warning", "you are deleting your database, you really want this ?"
    ):
        database.execute("DROP TABLE `web_page`.`users11`")


def delete_sel():
    sel = list_box.curselection()
    list_box.delete(sel)

#_________________________________________________________________________________________________________________
def setting():
    app_setting_bt = Toplevel()
    app_setting_bt.title("My Program Setting")
    app_setting_bt.geometry("200x200")
    app_setting_bt.resizable(False, False)
    def backgroundbt():
        color = askcolor(title="Chose background color")
        window.config(background=(color[1]))
        label_address.config(background=(color[1]))
        label_age.config(background=(color[1]))
        label_ctstats.config(background=(color[1]))
        label_destats.config(background=(color[1]))
        label_age.config(background=(color[1]))
        label_email.config(background=(color[1]))
        label_firstname.config(background=(color[1]))
        label_lastname.config(background=(color[1]))
        label_list.config(background=(color[1]))
        label_phone.config(background=(color[1]))
        label_sustats.config(background=(color[1]))
        app_time.config(background=(color[1]))
    

    

    def scale_change(event):
        list_box.config(font=("Tahoma",int(font.get())))

    font_change = DoubleVar()
    font = Scale(
        app_setting_bt,
        from_=0,
        to=100,
        orient="horizontal",
        variable= font_change,  
        command= scale_change)
    font.place(x=50,y=50)

    back_bt = Button(
        app_setting_bt,
        width=14,
        text="Background Color",
        command=backgroundbt,
        foreground="white",
        background="green",
        activebackground="black",
        activeforeground="white",
        font=("tahoma", 9),
    )
    back_bt.place(x=10, y=10)
    app_setting_bt.mainloop()
#_________________________________________________________________________________________________________________

def search():
    searchwin = Toplevel()
    searchwin.title("My Program Search")
    searchwin.geometry("500x200")
    searchwin.resizable(False, False)

    label_Search = Label(searchwin, text="Search Box :")
    label_Search.place(x=10,y=10)

    listbox2= Listbox(searchwin, width=45, height=2, font=("Tahoma ", 12))
    listbox2.place(x=50, y=35)

    search_bt = Button(
    searchwin,
    text="Search",
    command=savedata,
    foreground="white",
    background="Red",
    activebackground="black",
    activeforeground="white",
    font=("tahoma", 10),)
    search_bt.place(x=50,y=100)



#_________________________________________________________________________________________________________________

list_box = Listbox(window, width=45, height=17, font=("Tahoma ", 12))
list_box.place(x=350, y=35)

img = PhotoImage(file="C:/Users/Farsian/Desktop/newpy/png.png")

#_________________________________________________________________________________________________________________
CT_bt = Button(
    window,
    width=10,
    text="CreateTable",
    command=Create_Table,
    foreground="white",
    background="green",
    activebackground="black",
    activeforeground="white",
    font=("tahoma", 13),
)
CT_bt.place(x=20, y=290)
save_bt = Button(
    window,
    width=10,
    text="Sign up",
    command=savedata,
    foreground="white",
    background="green",
    activebackground="black",
    activeforeground="white",
    font=("tahoma", 13),
)
save_bt.place(x=240, y=290)
delete_bt = Button(
    window,
    width=10,
    text="Clear",
    command=delete,
    foreground="white",
    background="red",
    activebackground="black",
    activeforeground="white",
    font=("tahoma", 13),
)
delete_bt.place(x=130, y=290)
list_box_bt = Button(
    window,
    width=10,
    text="Show User",
    command=showusers,
    foreground="white",
    background="blue",
    activebackground="black",
    activeforeground="white",
    font=("tahoma", 13),
)
list_box_bt.place(x=350, y=370)
list_box_delete_bt = Button(
    window,
    width=10,
    text="Clear List",
    command=delete_all_list,
    foreground="white",
    background="blue",
    activebackground="black",
    activeforeground="white",
    font=("tahoma", 13),
)
list_box_delete_bt.place(x=460, y=370)
delete_all_datas_bt = Button(
    window,
    width=15,
    text="Clear database",
    command=delete_all_datas,
    foreground="white",
    background="blue",
    activebackground="black",
    activeforeground="white",
    font=("tahoma", 13),
)
delete_all_datas_bt.place(x=570, y=370)
delete_database_bt = Button(
    window,
    width=15,
    text="Delete database",
    command=delete_database,
    foreground="white",
    background="blue",
    activebackground="black",
    activeforeground="white",
    font=("tahoma", 13),
)
delete_database_bt.place(x=540, y=420)
delete_database_bt = Button(
    window,
    width=15,
    text="Delete Selected",
    command=delete_sel,
    foreground="white",
    background="blue",
    activebackground="black",
    activeforeground="white",
    font=("tahoma", 13),
)
delete_database_bt.place(x=380, y=420)
setting_bt = Button(
    window,
    width=10,
    text="Setting",
    command=setting,
    foreground="black",
    background="yellow",
    activebackground="black",
    activeforeground="white",
    font=("tahoma", 9),
)
setting_bt.place(x=680, y=5)
exit_bt = Button(
    window,
    image=img,
    command=window.quit,
)
exit_bt.place(x=10, y=425)
search_bt = Button(
    window,
    width=10,
    text="search",
    command= search ,
    foreground="black",
    background="yellow",
    activebackground="black",
    activeforeground="white",
    font=("tahoma", 9),
)
search_bt.place(x=580, y=5)

#_________________________________________________________________________________________________________________


window.mainloop()
