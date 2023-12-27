# #1
# import pizza

# pizza.making_pizza("large" , "soda")


# #2
# from pizza import making_pizza,mohit
# # making_pizza("small")
# print(mohit(45,63))


# #3
# from pizza import *

# print(mydata)


# #4
# from pizza import making_pizza as mk
# mk("large" , "soda")


# #5
# import pizza as pz
# pz.making_pizza("large" , "soda")




################################################


# import re
# import math
# import calendar
# import time
# import datetime
# import json
# import random
# import tkinter
# import os
# import zipapp
# import csv


# /www.w3schools.com/



# data = '{"name": "mahdi" , "age" : 25 , "city" : "mashhad"}'

# # result = json.loads(data)
# # print(result["age"])


# x = ["name", 3427234 , True , False , None , ("php", "perl" , "java")]
# print(json.dumps(x))





################################################


# x = lambda a : a * 10

# # print(x(5))


# x1 = lambda a, b : a * b

# # print(x1(7,9))


# def mohasebe(n):
#     return lambda a : a * n


# duble = mohasebe(10)


# print(duble(3))




################################################

# OOP 

# class mobile:
#     def __init__(self , brand , model , ram , price , color):
#         self.brand = brand
#         self.model = model
#         self.ram = ram
#         self.price = price
#         self.color = color
        



# mb1 = mobile("Apple" , "iPhone" , 2 , 800 , "white")
# mb2 = mobile("samsung" , "s24" , 4 , 500 , "red")
# mb3 = mobile("htc" , "sd3" , 1 , 300 , "black")

# mb1.brand = ""
# mb1.price = 700
# del mb1.ram
# del mb2
# # print(mb1.ram)
# print(mb2.brand,mb2.ram,mb2.model,mb2.price )



# class person:
#     def __init__(self , name, family , age ):
#         self.name = name
#         self.family = family
#         self.age = age
        

#     def intro(self):
#         print("Hello my name is:",self.name  , "and my family name is:" , self.family)





# class teacher(person):
#     def __init__(self, name , family ,age , code_Ostad):
#         super().__init__(name, family , age )
#         self.code_Ostad = code_Ostad


#     def about_teacher(self):
#         print("Teacher name:" , self.name , "Teacher Code:" , self.code_Ostad)



# # t1 = teacher("kamran" ,"mosavi" , 47 , 3247348734)
# # t1.intro()


# p1 = person("mahdi" , "mohammadi" , 25)
# p1.intro()




# x = 50
# def about():
#     global x
#     x = 46
# print(x)
# about()




# try:
#     print(10/0)
    


# except NameError:
#     print("Error !")


# except ImportError:
#     print("Error import !")


# except ValueError:
#     print("Error !")


# except ZeroDivisionError:
#     print("adad taghsim bar sefr nemishe !!")



# else:
#     print("END")



# finally:
#     print("THE END")




#1 
# price = 54.5674854748
# number = 74334
# brand = "Samsung"

# text = "Product brand is {}. Serial number is {} The price is {:.2f} dollars."

# print(text.format(brand, number, price))



#2
# name = "ali"
# age = 36
# text = "His name is {1} , {1} is {0} years old."
# print(text.format(age , name))



# #3
# text = "His name is {name} , {name} is {age} years old."
# print(text.format(age = 66 , name = "mahdi"))



#4
# name = "rahman"
# age =43
# print(f"His name is {name} , {name} is {age} years old.")







# f = open("C:/Users/Farsian-Teacher/Desktop/users.txt", "a")

# # print(f.read(50))
# # print(f.readline(10))



# f.write("Kamran")
# f.write("\t")
# f.write("alizadeh")
# f.write("\n")

# f.close()




# number = int(input("Enter a number:"))

# str_number = str(number)

# max_number = str_number[0]




# for x in str_number:
#     if int(max_number) < int(x):
#         max_number = int(x)


# print(max_number)




# import os


# os.remove("C:/Users/Farsian-Teacher/Desktop/users.txt")

# os.rmdir("C:/Users/Farsian-Teacher/Desktop/3692")
# os.mkdir("C:/Users/Farsian-Teacher/Desktop/3692")

# print(os.listdir("D:/"))






from tkinter import *
import datetime
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import time


myconnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "myapplication"
)

mycursor = myconnection.cursor()



win = Tk()
win.title("برنامه من")
win.geometry("800x500")
win.resizable(False,False)

lb_text = Label(win,text="به نام خدا" ,font=("Tahoma" , 12) , foreground="red" )
lb_text.place(x=10 , y=10)


def showtime():
    ti = datetime.datetime.now().strftime("%X")
    lb_text.config(text=ti)
    lb_text.after(1000,showtime)


showtime()



lb_name = Label(win,text="Name:",font=("Tahoma" , 13) )
lb_name.place(x=10 , y=50)


lb_family = Label(win,text="Family:",font=("Tahoma" , 13) )
lb_family.place(x=10 , y=80)


en_name = Entry(win,font=("Tahoma" , 13))
en_name.place(x=100 , y=50)

en_family = Entry(win,font=("Tahoma" , 13))
en_family.place(x=100 , y=80)



lb_age = Label(win,text="Age:",font=("Tahoma" , 13) )
lb_age.place(x=10 , y=110)


lb_sex = Label(win,text="Sex:",font=("Tahoma" , 13) )
lb_sex.place(x=10 , y=145)

lb_sex = Label(win,text="Address:",font=("Tahoma" , 13) )
lb_sex.place(x=10 , y=180)


text_address = Text(win, width=20, height=4,font=("Tahoma" , 12))
text_address.place(x=100 , y=180)



lb_title = Label(win,text="Users list & Results:",font=("Tahoma" , 9) )
lb_title.place(x=300 , y=2)


lb_state = Label(win,text="State !",font=("Tahoma" , 9) )
lb_state.place(x=20 , y=460)

list_age=[]
for x in range(1,121):
    list_age.append(x)

combo_age = ttk.Combobox(win,width=28, values=list_age)
combo_age.place(x=100 , y=115)



var = IntVar()

r1 = Radiobutton(win, text="Woman",value=0 , variable=var )
r1.place(x=100 , y=145)

r2 = Radiobutton(win, text="Man",value=1 , variable=var )
r2.place(x=180 , y=145)

def clear():
    en_name.delete("0" ,END)
    en_family.delete("0" ,END)
    text_address.delete("1.0" ,END)


def savedata():
    # f = open("c:/Users/Farsian-Teacher/Desktop/users.txt","a")
    # f.write(en_name.get())
    # f.write("\t")
    # f.write(en_family.get())
    # f.write("\n")
    # f.close()
    try:
        sql = "INSERT INTO users (name,family,age,sex,address) VALUES (%s,%s,%s,%s,%s)"
        if var.get() == 0 :      
            data = (en_name.get(),en_family.get(), combo_age.get() , "Woman" , text_address.get("1.0" ,END))
            list_box_users.insert(END,data )
        else:
            data = (en_name.get(),en_family.get(), combo_age.get() , "Man" , text_address.get("1.0" ,END))
            list_box_users.insert(END,data )

        mycursor.execute(sql, data)
        myconnection.commit()
        messagebox.showinfo("User saved !" , f"User {en_name.get()} saved.")
        
        
        
        time.sleep(3)
        clear()
    
    except:
        lb_state.config(text="!خطای درج در جدول")
    
    else:
        lb_state.config(text="User saved.")
    


def create_table():
    try:
        mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),family VARCHAR(50), age INT(3), sex VARCHAR(10), address VARCHAR(100) )")
    except:
        lb_state.config(text="!خطا در ساخت جدول")
    else:
        lb_state.config(text="!جدول ساخته شد")


bt_save = Button(win,text="ذخیره",font=("Tahoma" , 9) ,background="green" , foreground="white" , width=18, command=savedata)
bt_save.place(x=10 , y=280)



def showusers():
    sql = "SELECT * FROM users"
    mycursor.execute(sql)
    list_box_users.delete("0" ,END)
    for x in mycursor:
        list_box_users.insert(END,x)






bt_showusers = Button(win,text="نمایش کاربران",font=("Tahoma" , 9) ,background="green" , foreground="white" , width=18, command=showusers)
bt_showusers.place(x=10 , y=310)


bt_create_table = Button(win,text="ساخت جدول",font=("Tahoma" , 9) ,background="green" , foreground="white" , width=18, command=create_table)
bt_create_table.place(x=150 , y=280)







list_box_users = Listbox(win,width=70,font=("Tahoma" , 9))
list_box_users.place(x=300 , y=20)













win.mainloop()





