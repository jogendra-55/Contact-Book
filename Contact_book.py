import sqlite3
from tkinter import *                  # This and 2 line  is to be there in every program below
root = Tk()
from PIL import ImageTk, Image
root.iconbitmap('pistol.ico')
root.title("Contacts Book")

# Adding Frames to Program
# frame=LabelFrame(root,padx=50,pady=50)
# frame.pack(padx=100,pady=100)

# b=Button(frame,text="Don't Click Here")
# b2=Button(frame,text='or here..')
# b.grid(row=0,column=0)
# b2.grid(row=1,column=1)

# root.mainloop()


# Radio Buttons
# r=IntVar()
# r.set("2")
# def clicked(a):
#     mylabel=Label(root,text=a)
#     mylabel.pack()

# Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:clicked(r.get()) ).pack()
# Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda:clicked(r.get())).pack()

# mylabel=Label(root,text=r.get())
# mylabel.pack()
# mybutton=Button(root,text="Clicke me!",command=lambda :clicked(r.get()))
# mybutton.pack()

# # Using List to create RadioButtons For n Number of options
# pizza = StringVar()
# pizza.set("jii")

# def clicked(a):
#     mylabel = Label(root, text=a)
#     mylabel.pack()


# modes = [
#     ("Pepperoni", "Jogi"),
#     ("Onion", "Onion"),
#     ("Cheese", "Cheese"),
#     ("Mushroom", "Mushroom")
# ]

# for text,mode in modes:
#     Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)


# mybutton=Button(root,text='Click Me!',command=lambda :clicked(pizza.get()))
# mybutton.pack()

# root.mainloop()


# Message Box
# from tkinter import messagebox

# # showinfo,showwarning,showerror,askquestion,askokcancel,askyesno -Different types of message boxes
# def popup():
#    # messagebox.askyesno("This is my popup","Hello World!")
#    r=messagebox.askyesno("This is my popup","Hello World!")
#    Label(root,text=r).pack()
#    if r==1:
#        Label(root, text="You Click Yes!").pack()
#    else:
#        Label(root, text="You Click No!").pack()

# Button(root,text='Popup',command=popup).pack()

# root.mainloop()


# Creating New Windows
# from PIL import Image,ImageTk

# def buttonopen():
#     global my_img
#     top = Toplevel()  # it create's a window
#     top.title('MY SECOND WINDOW')
#     l = Label(top, text='Hello World!').pack()
#     my_img = ImageTk.PhotoImage(Image.open('Img3.png'))
#     lbl = Label(top, image=my_img).pack()
#     btn2=Button(top,text='Close Window',command=top.destroy).pack()

# btn=Button(root,text='Open Second Window',command=buttonopen).pack()
# root.mainloop()


#Open Files,Dialog Boxes               root.filenmame -it returns the location of file n then we can open it through any mtd
# from tkinter import filedialog
# from PIL import ImageTk,Image

# def open():
#     global my_img
#     root.filename = filedialog.askopenfilename(initialdir="C/Projects", title='Select A file',
#                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))
#     my_label = Label(root, text=root.filename).pack()
#     my_img = ImageTk.PhotoImage(Image.open(root.filename))
#     my_im_label = Label(root, image=my_img).pack()

# btn=Button(root,text='Open File',command=open).pack()

# root.mainloop()


#Sliders
# root.geometry("400x400")               #size of window
#
# vertical=Scale(root,from_=0,to=100)
# vertical.pack()
#
# def slide():
#     lbl=Label(root,text=horizontal.get() ).pack()
#     root.geometry(str(horizontal.get())+"x"+str(vertical.get()))
#
# horizontal=Scale(root,from_=0,to=220,orient=HORIZONTAL)
# horizontal.pack()
# btn=Button(root,text='Click me!',command=slide).pack()
# lbl = Label(root, text=horizontal.get()).pack()
# root.mainloop()


#Checkboxes
# var=StringVar()
# def click():
#     lbl=Label(root,text=var.get()).pack()
#
# c=Checkbutton(root,text='Check This Button,I dare You!',variable=var,onvalue='Yes',offvalue='No')
# c.deselect()
# c.pack()
#
# btn= Button(root, text='Click me!', command=click)
# btn.pack()
#
# root.mainloop()


# DropDown Menus
# root.geometry("200x200")
# def show():
#     lbl=Label(root,text=clicked.get()).pack()
#
# clicked=StringVar()
# clicked.set("CHOOSE A OPTION")
#
# # drop=OptionMenu(root,clicked,"Monday","Tuesday","Wednesday","Thursday","Friday").pack()
# #OR
# options=[ "Monday","Tuesday","Wednesday","Thursday","Friday" ]
# drop=OptionMenu(root,clicked,*options).pack()
#
# btn=Button(root,text='Show Selection',command=show).pack()
#
# root.mainloop()


#Using Databases
root.geometry("400x600")

#create a database or connect to one
conn=sqlite3.connect('Address_Book.db')

#create cursor
c=conn.cursor()


# #create table i.e in which the data is to be stored
# c.execute("""CREATE TABLE addresses(
#         first name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         pincode integer)""")
# 
def update():
    # create a database or connect to one
    conn = sqlite3.connect('Address_Book.db')

    # create cursor
    c = conn.cursor()

    record_id=delete_box.get()
    c.execute("""UPDATE addresses SET
       first=:first,
       last_name=:last,
       address=:address,
       city=:city,
       state=:state,
       pincode=:pincode
       
       WHERE oid=:oid""",
         {'first':f_name_editor.get(),
           'last':l_name_editor.get(),
           'address':address_name_editor.get(),
           'city':city_name_editor.get(),
           'state':state_name_editor.get(),
           'pincode':pc_name_editor.get(),

           'oid':record_id



        } )

    # Commit changes
    conn.commit()

    # close connection
    conn.close()

    editor.destroy()



def edit():
    global editor
    editor=Tk()
    editor.title('Update a Record')
    editor.iconbitmap('pistol.ico')
    editor.geometry("400x600")

    # create a database or connect to one
    conn = sqlite3.connect('Address_Book.db')

    # create cursor
    c = conn.cursor()

    record_id=delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid= "+record_id)
    records = c.fetchall()

    #Craete Global variables for text boxes names
    global f_name_editor
    global l_name_editor
    global address_name_editor
    global city_name_editor
    global state_name_editor
    global pc_name_editor


    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_name_editor = Entry(editor, width=30)
    address_name_editor.grid(row=2, column=1)
    city_name_editor = Entry(editor, width=30)
    city_name_editor.grid(row=3, column=1)
    state_name_editor = Entry(editor, width=30)
    state_name_editor.grid(row=4, column=1)
    pc_name_editor = Entry(editor, width=30)
    pc_name_editor.grid(row=5, column=1)

    # Create Text Box labels
    fl = Label(editor, text="FIRST NAME")
    fl.grid(row=0, column=0, pady=(10, 0))
    ll = Label(editor, text="LAST NAME")
    ll.grid(row=1, column=0)
    al = Label(editor, text="ADDRESS")
    al.grid(row=2, column=0)
    cl = Label(editor, text="CITY")
    cl.grid(row=3, column=0)
    sl = Label(editor, text="STATE")
    sl.grid(row=4, column=0)
    pnl = Label(editor, text="PINCODE")
    pnl.grid(row=5, column=0)

    save_bn = Button(editor, text='Save Records', command=update)
    save_bn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=140)

    # display record through loop
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_name_editor.insert(0, record[2])
        city_name_editor.insert(0, record[3])
        state_name_editor.insert(0, record[4])
        pc_name_editor.insert(0, record[5])

def delete():
    # create a database or connect to one
    conn = sqlite3.connect('Address_Book.db')

    # create cursor
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid= "+delete_box.get())

    # Commit chnages
    conn.commit()

    # close connection
    conn.close()



def submit():
    # create a database or connect to one
    conn = sqlite3.connect('Address_Book.db')

    # create cursor
    c = conn.cursor()

    #INSERT into Table
    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address_name,:city_name,:state_name,:pc_name)",
              { 'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address_name':address_name.get(),
                'city_name':city_name.get(),
                'state_name':state_name.get(),
                'pc_name':pc_name.get()
              })

    # Commit chnages
    conn.commit()

    # close connection
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    address_name.delete(0,END)
    city_name.delete(0,END)
    state_name.delete(0,END)
    pc_name.delete(0,END)

def query():
    # create a database or connect to one
    conn = sqlite3.connect('Address_Book.db')

    # create cursor
    c = conn.cursor()

    c.execute("SELECT *,oid FROM addresses")
    records=c.fetchall()
    # print(records)

    #display record through loop
    print_record=''
    for record in records:
        print_record += str(record[0])+" "+str(record[1])+"\t"+str(record[6]) +"\n"
    lbl=Label(root,text=print_record)
    lbl.grid(row=12,column=0,columnspan=2)

    # Commit chnages
    conn.commit()

    # close connection
    conn.close()



#Create Text Boxes
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,pady=(10,0) )
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)
address_name=Entry(root,width=30)
address_name.grid(row=2,column=1)
city_name=Entry(root,width=30)
city_name.grid(row=3,column=1)
state_name=Entry(root,width=30)
state_name.grid(row=4,column=1)
pc_name=Entry(root,width=30)
pc_name.grid(row=5,column=1)
delete_box=Entry(root,width=35)
delete_box.grid(row=9,column=1)

#Create Text Box labels
fl=Label(root,text="FIRST NAME")
fl.grid(row=0,column=0,pady=(10,0))
ll=Label(root,text="LAST NAME")
ll.grid(row=1,column=0)
al=Label(root,text="ADDRESS")
al.grid(row=2,column=0)
cl=Label(root,text="CITY")
cl.grid(row=3,column=0)
sl=Label(root,text="STATE")
sl.grid(row=4,column=0)
pnl=Label(root,text="PINCODE")
pnl.grid(row=5,column=0)
delete_box_lb=Label(root,text='SELECT ID')
delete_box_lb.grid(row=9,column=0)


#Create Submit Button
submit_btn=Button(root,text='Add Record To Databse',command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

#Craete a Query Button i.e to show the data on screen
q_btn=Button(root,text='Show Records',command=query)
q_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

#Create a delete button
d_btn=Button(root,text='Delete Records',command=delete)
d_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=135)

#Craete update button
edit_bn=Button(root,text='Edit Records',command=edit)
edit_bn.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=140)


#Commit chnages
conn.commit()

#close connection
conn.close()

root.mainloop()