import random
from tkinter import *
from tkinter import messagebox

import mysql.connector

root = Tk()
# width x height
root.geometry("700x500")
# width,height
root.minsize(700, 500)
# width,height
root.maxsize(900, 900)


def page2():
    root.destroy()
    root2 = Tk()
    root2.title("Main Project")
    p2 = PhotoImage(file="plane.png")
    Label(root2, image=p2).grid(row=0, column=0, columnspan=4)
    Label(root2, text="WELCOME TO AIRLINE BOOKING PORTAL", bg="white", fg="red", font=("Bauhaus 93", 22)).grid(row=0,
                                                                                                               column=0,
                                                                                                               columnspan=4)
    Label(root2, text="Flights Availability", font=("Bauhaus 93", 17), fg="White", width=46, bg="red").grid(row=1,
                                                                                                            column=0,
                                                                                                            columnspan=4)
    Label(root2, text="FROM", font=("Berlin Sans FB", 14), fg="Blue").grid(row=2, column=1)
    Label(root2, text="TO", font=("Berlin Sans FB", 14), fg="Blue").grid(row=7, column=1)
    board = StringVar()
    arr = StringVar()
    board.set("Select Current location")
    boardentry1 = OptionMenu(root2, board, "Ahmedabad", "Bangalore", "Chennai", "Delhi")
    boardentry1.grid(row=2, column=2)
    arr.set("Select Destination location")
    reentry = OptionMenu(root2, arr, "Ahmedabad", "Bangalore", "Chennai", "Delhi")
    reentry.grid(row=7, column=2)
    Button(root2, text="Show Availability", fg="white", bg="red", font=("Arial Black", 10, "bold"),
           command=lambda: page2_1()).grid(row=10, column=0)

    # Frame(root2,border width=3).grid(row=15,column=0)
    def page2_1():

        def signup():
            root3.destroy()

            def insert():
                username1 = v5.get()
                password1 = v6.get()
                email1 = v7.get()
                phone1 = v8.get()
                print(username1)
                if username1 == " " or password1 == " " or email1 == " " or phone1 == " ":
                    messagebox.showinfo("Error", "All fields are required")
                else:

                    con = mysql.connector.connect(host="localhost", user="root", password="root", database="saurabh")
                    cursor = con.cursor()
                    lan = (username1, password1, email1, phone1)
                    # cursor.execute("EXISTS(SELECT * from Lambdaaa WHERE username1=%s)", username1)
                    # print(cursor)
                    # if cursor:
                    #     messagebox.showinfo("Status", "username already exist so enter another")
                    cursor.execute("INSERT INTO Lambdaaa (username1,password1,email1,phone1) VALUES(%s,%s,%s,%s)", lan)
                    cursor.execute("commit")
                    messagebox.showinfo("Status", "Sign Up Successful")
                    con.close()
                    signin()
                # else:
                #     messagebox.showinfo("successfully register", " please sigin below")

            def signin():
                root5.destroy()

                def insert2():

                    username1 = v10.get()
                    password1 = v20.get()
                    if not username1:
                        messagebox.showinfo("Error", "All fields are required")
                    if not password1:
                        messagebox.showinfo("Error", "All fields are required")
                    else:
                        con = mysql.connector.connect(host="localhost", user="root", password="root", database="saurabh"
                                                      )
                        cursor = con.cursor()
                        lan = (username1, password1)
                        d = """SELECT * FROM Lambdaaa WHERE username1= %s AND password1= %s"""
                        cursor.execute(d, lan)
                        data = cursor.fetchall()
                        con.close()
                        if not data:
                            messagebox.showinfo("Error", "Invalid username or password")
                            exit()

                        def page3():
                            root7 = Tk()
                            root7.title("Ticket Details")
                            Label(root7, text="Thanks For Choosing Airplane Booking System", font=("Bauhaus 93", 17),
                                  fg="White", bg="red", width=46).grid(row=0, column=0, columnspan=4)
                            Label(root7, text="Ticket Details", font=("Bauhaus 93", 17), fg="Blue", width=46).grid(
                                row=1, column=0, columnspan=4)
                            Label(root7, text="Passenger Name", font=("Arial", 14), fg="Blue").grid(row=2, column=1)
                            q = name.get()
                            Label(root7, text=q, font=("Arial", 14), fg="Blue").grid(row=2, column=2)
                            Label(root7, text="Age", font=("Arial", 14), fg="Blue").grid(row=3, column=1)
                            Label(root7, text=age.get(), font=("Arial", 14), fg="Blue").grid(row=3, column=2)
                            Label(root7, text="Gender", font=("Arial", 14), fg="Blue").grid(row=4, column=1)
                            if a.get() == 0:
                                Label(root7, text="Male", font=("Arial", 14), fg="Blue").grid(row=4, column=2)
                            else:
                                Label(root7, text="Female", font=("Arial", 14), fg="Blue").grid(row=4, column=2)
                            Label(root7, text="Class", font=("Arial", 14), fg="Blue").grid(row=5, column=1)
                            Label(root7, text=v.get(), font=("Arial", 14), fg="Blue").grid(row=5, column=2)
                            Label(root7, text="Additional Passenger Details", font=("Bauhaus 93", 17), fg="Blue",
                                  width=46).grid(row=7, column=0, columnspan=4)
                            Label(root7, text="Passenger Name", font=("Arial", 14), fg="Blue").grid(row=8, column=1)
                            Label(root7, text=name1.get(), font=("Arial", 14), fg="Blue").grid(row=8, column=2)
                            Label(root7, text="Class", font=("Arial", 14), fg="Blue").grid(row=9, column=1)
                            Label(root7, text=v1.get(), font=("Arial", 14), fg="Blue").grid(row=9, column=2)
                            Label(root7, text="Passenger Name", font=("Arial", 14), fg="Blue").grid(row=10, column=1)
                            Label(root7, text=name2.get(), font=("Arial", 14), fg="Blue").grid(row=10, column=2)
                            Label(root7, text="Class", font=("Arial", 14), fg="Blue").grid(row=11, column=1)
                            Label(root7, text=v2.get(), font=("Arial", 14), fg="Blue").grid(row=11, column=2)
                            Label(root7, text="Passenger Name", font=("Arial", 14), fg="Blue").grid(row=12, column=1)
                            Label(root7, text=name3.get(), font=("Arial", 14), fg="Blue").grid(row=12, column=2)
                            Label(root7, text="Class", font=("Arial", 14), fg="Blue").grid(row=13, column=1)
                            Label(root7, text=v3.get(), font=("Arial", 14), fg="Blue").grid(row=13, column=2)
                            Button(root7, text="PLEASE CLICK TO BOOK YOUR TICKETS", fg="white", font="algerian",
                                   bg="red",
                                   command=exit()).grid(row=19, columnspan=5)

                        root4.destroy()
                        root6 = Tk()
                        root6.title("Booking Portal")
                        Label(root6, text="Booking Portal", font=("Times New Roman 93", 17), fg="White", width=46,
                              bg="red").grid(row=1, column=0, columnspan=4)
                        Label(root6, text="Enter Your Details", font=("Times New Roman 93", 14), fg="Blue",
                              width=46).grid(row=2, column=0, columnspan=4)
                        Label(root6, text="Full Name", font=("Times New Roman 93", 14), fg="blue").grid(row=3, column=1)
                        name = Entry()
                        name.grid(row=3, column=2)
                        Label(root6, text="Enter Your age", font=("Times New Roman 93", 14), fg="Blue").grid(row=4,
                                                                                                             column=1)
                        age = Entry(width=4)
                        age.grid(row=4, column=2)
                        Label(root6, text="Select Gender", font=("Times New Roman 93", 14), fg="blue").grid(row=5,
                                                                                                            column=1)
                        a = IntVar()
                        Radiobutton(root6, text="Male", variable=a, value=0, fg="red").grid(row=5, column=2)
                        Radiobutton(root6, text="Female", variable=a, value=1, fg="red").grid(row=5, column=3)
                        Label(root6, text="Seat Class", font=("Times New Roman 93", 14), fg="blue").grid(row=6,
                                                                                                         column=1)
                        v = StringVar(root6)
                        v.set("Select class")
                        w = OptionMenu(root6, v, "First Class", "Business Class", "Economy Class")
                        w.grid(row=6, column=2)
                        Label(root6, text="Additional Passengers Details", font=("Times New Roman 93", 14), fg="Blue",
                              width=46).grid(row=7, column=0, columnspan=4)
                        Label(root6, text="Passenger 1", font=("Times New Roman 93", 14), fg="Blue").grid(row=8,
                                                                                                          column=1)
                        name1 = Entry()
                        name1.grid(row=8, column=2)
                        Label(root6, text="Enter age", font=("Times New Roman 93", 14), fg="Blue").grid(row=9, column=1)
                        age1 = Entry(width=4)
                        age1.grid(row=9, column=2)
                        Label(root6, text="Seat Class", font=("Times New Roman 93", 14), fg="blue").grid(row=10,
                                                                                                         column=1)
                        v1 = StringVar(root6)
                        v1.set("Select class")
                        w1 = OptionMenu(root6, v1, "First Class", "Business Class", "Economy Class")
                        w1.grid(row=10, column=2)
                        Label(root6, text="Passenger 2", font=("Times New Roman 93", 14), fg="Blue").grid(row=11,
                                                                                                          column=1)
                        name2 = Entry()
                        name2.grid(row=11, column=2)
                        Label(root6, text="Enter age", font=("Times New Roman 93", 14), fg="Blue").grid(row=12,
                                                                                                        column=1)
                        age2 = Entry(width=4)
                        age2.grid(row=12, column=2)
                        Label(root6, text="Seat Class", font=("Times New Roman 93", 14), fg="blue").grid(row=13,
                                                                                                         column=1)
                        v2 = StringVar(root6)
                        v2.set("Select class")
                        w2 = OptionMenu(root6, v2, "First Class", "Business Class", "Economy Class")
                        w2.grid(row=13, column=2)
                        Label(root6, text="Passenger 3", font=("Times New Roman 93", 14), fg="Blue").grid(row=14,
                                                                                                          column=1)
                        name3 = Entry()
                        name3.grid(row=14, column=2)
                        Label(root6, text="Enter age", font=("Times New Roman 93", 14), fg="Blue").grid(row=15,
                                                                                                        column=1)
                        age3 = Entry(width=4)
                        age3.grid(row=15, column=2)
                        Label(root6, text="Seat Class", font=("Times New Roman 93", 14), fg="blue").grid(row=16,
                                                                                                         column=1)
                        v3 = StringVar(root6)
                        v3.set("Select class")
                        w3 = OptionMenu(root6, v3, "First Class", "Business Class", "Economy Class")
                        w3.grid(row=16, column=2)
                        Label(root6, text="Number of Passengers", font=("Times New Roman 93", 14), fg="blue").grid(
                            row=18, column=1)
                        v4 = StringVar(root6)
                        v4.set("0")
                        w4 = OptionMenu(root6, v4, "1", "2", "3", "4")
                        w4.grid(row=18, column=2)
                        Button(root6, text="Confirm Booking", fg="white", font="algerian", bg="red",
                               command=lambda: page3()).grid(row=19, columnspan=5)

                # root3.destroy()
                root4 = Tk()
                root4.geometry("400x300")
                l1 = Label(root4, text="Signin Page", bg="black", fg="white", font=("Algerian", 20, "bold"),
                           borderwidth=1, width=10, relief=SUNKEN)
                l1.grid(row=1, column=3, padx=10, pady=10)
                v10 = StringVar()
                v20 = StringVar()
                Label(root4, text="Username", font=("Arial", 15, "bold"), fg="blue").grid(row=5, column=2, pady=10)
                Label(root4, text="Password", font=("Arial", 15, "bold"), fg="blue").grid(row=7, column=2, pady=10)
                Entry(root4, textvariable=v10).grid(row=5, column=3)
                Entry(root4, textvariable=v20, show="*").grid(row=7, column=3)
                Button(root4, text='Submit', command=lambda: insert2(), font='none 13 bold').grid(row=8, column=3,
                                                                                                  padx=5)

            root5 = Tk()
            root5.title("Sign-up page")
            root5.geometry("600x400")
            v5 = StringVar()
            v6 = StringVar()
            v7 = StringVar()
            v8 = StringVar()
            l11 = Label(root5, text="Sign-up Page", bg="black", fg="white", font=("Algerian", 20, "bold"),
                        borderwidth=1, width=10, relief=SUNKEN)
            l11.grid(row=1, column=0, padx=100, pady=10)
            Label(root5, text="Username *", font=("Arial", 14), fg="blue").grid(row=2, column=0)
            Label(root5, text="Password *", font=("Arial", 14), fg="blue").grid(row=3, column=0)
            Label(root5, text="Email *", font=("Arial", 14), fg="blue").grid(row=4, column=0)
            Label(root5, text="Phone *", font=("Arial", 14), fg="blue").grid(row=5, column=0)
            Entry(root5, textvariable=v5).grid(row=2, column=1)
            Entry(root5, textvariable=v6, show="*").grid(row=3, column=1)
            Entry(root5, textvariable=v7).grid(row=4, column=1)
            Entry(root5, textvariable=v8).grid(row=5, column=1)
            but = Button(root5, text='Submit', command=insert, font='none 13 bold')
            but.grid(row=7, column=1)
            Button(root5, text="Already have an account - Sign in", font=("Book Antique", 12), command=signin).grid(
                row=8, column=0, padx=20)

        if board.get() == "Ahmedabad" and arr.get() == "Bangalore":
            root2.destroy()
            root3 = Tk()
            root3.minsize(600, 400)
            Label(root3, text="You selected flight from Ahmedabad to Bangalore", font=("Book Antiqua", 15),
                  fg="blue").grid(row=1, column=0, padx=50, pady=10)
            Label(root3, text="Distance of flight is 1235km", font=("Book Antiqua", 15), fg="blue").grid(row=2,
                                                                                                         column=0,
                                                                                                         pady=10,
                                                                                                         padx=10)
            Label(root3, text="Time duration of flight is 2h 10min", font=("Book Antiqua", 15), fg="blue").grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10)
            Label(root3, text="Number of Seats Available are:", font=("Book Antiqua", 14), fg="white",
                  bg="orange").grid(row=4, column=0, padx=10)
            Label(root3, text=random.randint(100, 300), font=("Book Antiqua", 14), fg="white", bg="green").grid(row=4,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=15)
            Label(root3, text=" ").grid(row=5, column=0)
            Button(root3, text="Proceed for the next step", font=("Book Antiqua", 12), command=signup).grid(row=6,
                                                                                                            column=0,
                                                                                                            padx=20)
            Label(root3, text=" ").grid(row=7, column=0)
            root3.mainloop()
        elif board.get() == "Ahmedabad" and arr.get() == "Delhi":
            root2.destroy()
            root3 = Tk()
            Label(root3, text="You selected flight from Ahmedabad to Delhi", font=("Book Antique", 15), fg="blue").grid(
                row=1, column=0, padx=50, pady=10)
            Label(root3, text="Distance of flight is 755km", font=("Book Antique", 15), fg="blue").grid(row=2, column=0,
                                                                                                        pady=10,
                                                                                                        padx=10)
            Label(root3, text="Time duration of flight is 1h 30min", font=("Book Antique", 15), fg="blue").grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10)
            Label(root3, text="Number of Seats Available are:", font=("Book Antique", 14), fg="white",
                  bg="orange").grid(row=4, column=0, padx=10)
            Label(root3, text=random.randint(100, 300), font=("Book Antique", 14), fg="white", bg="green").grid(row=4,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=15)
            Label(root3, text=" ").grid(row=5, column=0)
            Button(root3, text="Proceed for the next step", font=("Book Antique", 12), command=signup).grid(row=6,
                                                                                                            column=0,
                                                                                                            padx=20)
            Label(root3, text=" ").grid(row=7, column=0)
            # Button(root3,text="Already have an account - Sign in",font=("Book Antiqua",12),command=signin).grid(
            # row=8,column=0,pads=20)
            root3.mainloop()
        elif board.get() == "Ahmedabad" and arr.get() == "Chennai":
            root2.destroy()
            root3 = Tk()
            Label(root3, text="You selected flight from Ahmedabad to Chennai", font=("Book Antiqua", 15),
                  fg="blue").grid(row=1, column=0, padx=50, pady=10)
            Label(root3, text="Distance of flight is 1374km", font=("Book Antique", 15), fg="blue").grid(row=2,
                                                                                                         column=0,
                                                                                                         pady=10,
                                                                                                         padx=10)
            Label(root3, text="Time duration of flight is 2h 15min", font=("Book Antique", 15), fg="blue").grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10)
            Label(root3, text="Number of Seats Available are:", font=("Book Antique", 14), fg="white",
                  bg="orange").grid(row=4, column=0, padx=10)
            Label(root3, text=random.randint(100, 300), font=("Book Antique", 14), fg="white", bg="green").grid(row=4,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=15)
            Label(root3, text=" ").grid(row=5, column=0)
            Button(root3, text="Proceed for the next step", font=("Book Antique", 12), command=signup).grid(row=6,
                                                                                                            column=0,
                                                                                                            padx=20)
            Label(root3, text=" ").grid(row=7, column=0)
            # Button(root3,text="Already have an account - Sign in",font=("Book Antiqua",12),command=signin).grid(
            # row=8,column=0,padx=20)
            root3.mainloop()
        elif board.get() == "Bangalore" and arr.get() == "Ahmedabad":
            root2.destroy()
            root3 = Tk()
            Label(root3, text="You selected flight from Bangalore to Ahmedabad", font=("Book Antique", 15),
                  fg="blue").grid(row=1, column=0, padx=50, pady=10)
            Label(root3, text="Distance of flight is 1235km", font=("Book Antique", 15), fg="blue").grid(row=2,
                                                                                                         column=0,
                                                                                                         pady=10,
                                                                                                         padx=10)
            Label(root3, text="Time duration of flight is 2h 10min", font=("Book Antique", 15), fg="blue").grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10)
            Label(root3, text="Number of Seats Available are:", font=("Book Antique", 14), fg="white",
                  bg="orange").grid(row=4, column=0, padx=10)
            Label(root3, text=random.randint(100, 300), font=("Book Antique", 14), fg="white", bg="green").grid(row=4,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=15)
            Label(root3, text=" ").grid(row=5, column=0)
            Button(root3, text="Proceed for the next step", font=("Book Antique", 12), command=signup).grid(row=6,
                                                                                                            column=0,
                                                                                                            padx=20)
            Label(root3, text=" ").grid(row=7, column=0)
            # Button(root3,text="Already have an account - Sign in",font=("Book Antiqua",12),command=signin).grid(
            # row=8,column=0,padx=20)
            root3.mainloop()
        elif board.get() == "Bangalore" and arr.get() == "Delhi":
            root2.destroy()
            root3 = Tk()
            Label(root3, text="You selected flight from Bangalore to Delhi", font=("Book Antiqua", 15), fg="blue").grid(
                row=1, column=0, padx=50, pady=10)
            Label(root3, text="Distance of flight is 1740km", font=("Book Antiqua", 15), fg="blue").grid(row=2,
                                                                                                         column=0,
                                                                                                         pady=10,
                                                                                                         padx=10)
            Label(root3, text="Time duration of flight is 2h 50min", font=("Book Antiqua", 15), fg="blue").grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10)
            Label(root3, text="Number of Seats Available are:", font=("Book Antiqua", 14), fg="white",
                  bg="orange").grid(row=4, column=0, padx=10)
            Label(root3, text=random.randint(100, 300), font=("Book Antiqua", 14), fg="white", bg="green").grid(row=4,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=15)
            Label(root3, text=" ").grid(row=5, column=0)
            Button(root3, text="Proceed for the next step", font=("Book Antiqua", 12), command=signup).grid(row=6,
                                                                                                            column=0,
                                                                                                            padx=20)
            Label(root3, text=" ").grid(row=7, column=0)
            # Button(root3,text="Already have an account - Sign in",font=("Book Antiqua",12),command=signin).grid(
            # row=8,column=0,padx=20)
            root3.mainloop()
        elif board.get() == "Bangalore" and arr.get() == "Chennai":
            root2.destroy()
            root3 = Tk()
            Label(root3, text="You selected flight from Bangalore to Chennai", font=("Book Antiqua", 15),
                  fg="blue").grid(row=1, column=0, padx=50, pady=10)
            Label(root3, text="Distance of flight is 260km", font=("Book Antiqua", 15), fg="blue").grid(row=2, column=0,
                                                                                                        pady=10,
                                                                                                        padx=10)
            Label(root3, text="Time duration of flight is 50min", font=("Book Antiqua", 15), fg="blue").grid(row=3,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=10)
            Label(root3, text="Number of Seats Available are:", font=("Book Antiqua", 14), fg="white",
                  bg="orange").grid(row=4, column=0, padx=10)
            Label(root3, text=random.randint(100, 300), font=("Book Antiqua", 14), fg="white", bg="green").grid(row=4,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=15)
            Label(root3, text=" ").grid(row=5, column=0)
            Button(root3, text="Proceed for the next step", font=("Book Antiqua", 12), command=signup).grid(row=6,
                                                                                                            column=0,
                                                                                                            padx=20)
            Label(root3, text=" ").grid(row=7, column=0)
            # Button(root3,text="Already have an account - Sign in",font=("Book Antiqua",12),command=signin).grid(
            # row=8,column=0,padx=20)
            root3.mainloop()
        elif board.get() == "Chennai" and arr.get() == "Ahmedabad":
            root2.destroy()
            root3 = Tk()
            Label(root3, text="You selected flight from Chennai to Ahmedabad ", font=("Book Antiqua", 15),
                  fg="blue").grid(row=1, column=0, padx=50, pady=10)
            Label(root3, text="Distance of flight is 1374km", font=("Book Antiqua", 15), fg="blue").grid(row=2,
                                                                                                         column=0,
                                                                                                         pady=10,
                                                                                                         padx=10)
            Label(root3, text="Time duration of flight is 2h 15min", font=("Book Antiqua", 15), fg="blue").grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10)
            Label(root3, text="Number of Seats Available are:", font=("Book Antiqua", 14), fg="white",
                  bg="orange").grid(row=4, column=0, padx=10)
            Label(root3, text=random.randint(100, 300), font=("Book Antiqua", 14), fg="white", bg="green").grid(row=4,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=15)
            Label(root3, text=" ").grid(row=5, column=0)
            Button(root3, text="Proceed for the next step", font=("Book Antiqua", 12), command=signup).grid(row=6,
                                                                                                            column=0,
                                                                                                            padx=20)
            Label(root3, text=" ").grid(row=7, column=0)
            # Button(root3,text="Already have an account - Sign in",font=("Book Antiqua",12),command=signin).grid(
            # row=8,column=0,padx=20)
            root3.mainloop()
        elif board.get() == "Chennai" and arr.get() == "Bangalore":
            root2.destroy()
            root3 = Tk()
            Label(root3, text="You selected flight from Chennai to Bangalore", font=("Book Antiqua", 15),
                  fg="blue").grid(row=1, column=0, padx=50, pady=10)
            Label(root3, text="Distance of flight is 260km", font=("Book Antiqua", 15), fg="blue").grid(row=2, column=0,
                                                                                                        pady=10,
                                                                                                        padx=10)
            Label(root3, text="Time duration of flight is 50min", font=("Book Antiqua", 15), fg="blue").grid(row=3,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=10)
            Label(root3, text="Number of Seats Available are:", font=("Book Antiqua", 14), fg="white",
                  bg="orange").grid(row=4, column=0, padx=10)
            Label(root3, text=random.randint(100, 300), font=("Book Antiqua", 14), fg="white", bg="green").grid(row=4,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=15)
            Label(root3, text=" ").grid(row=5, column=0)
            Button(root3, text="Proceed for the next step", font=("Book Antiqua", 12), command=signup).grid(row=6,
                                                                                                            column=0,
                                                                                                            padx=20)
            Label(root3, text=" ").grid(row=7, column=0)
            # Button(root3,text="Already have an account - Sign in",font=("Book Antiqua",12),command=signin).grid(
            # row=8,column=0,padx=20)
            root3.mainloop()
        elif board.get() == "Chennai" and arr.get() == "Delhi":
            root2.destroy()
            root3 = Tk()
            Label(root3, text="You selected flight from Chennai to Delhi", font=("Book Antiqua", 15), fg="blue").grid(
                row=1, column=0, padx=50, pady=10)
            Label(root3, text="Distance of flight is 1757km", font=("Book Antiqua", 15), fg="blue").grid(row=2,
                                                                                                         column=0,
                                                                                                         pady=10,
                                                                                                         padx=10)
            Label(root3, text="Time duration of flight is 3h", font=("Book Antiqua", 15), fg="blue").grid(row=3,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=10)
            Label(root3, text="Number of Seats Available are:", font=("Book Antiqua", 14), fg="white",
                  bg="orange").grid(row=4, column=0, padx=10)
            Label(root3, text=random.randint(100, 300), font=("Book Antiqua", 14), fg="white", bg="green").grid(row=4,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=15)
            Label(root3, text=" ").grid(row=5, column=0)
            Button(root3, text="Proceed for the next step", font=("Book Antiqua", 12), command=signup).grid(row=6,
                                                                                                            column=0,
                                                                                                            padx=20)
            Label(root3, text=" ").grid(row=7, column=0)
            # Button(root3,text="Already have an account - Sign in",font=("Book Antiqua",12),command=signin).grid(
            # row=8,column=0,padx=20)
            root3.mainloop()
        elif board.get() == "Delhi" and arr.get() == "Ahmedabad":
            root2.destroy()
            root3 = Tk()
            Label(root3, text="You selected flight from Delhi to Ahmedabad ", font=("Book Antiqua", 15),
                  fg="blue").grid(row=1, column=0, padx=50, pady=10)
            Label(root3, text="Distance of flight is 755km", font=("Book Antiqua", 15), fg="blue").grid(row=2, column=0,
                                                                                                        pady=10,
                                                                                                        padx=10)
            Label(root3, text="Time duration of flight is 1h 30min", font=("Book Antiqua", 15), fg="blue").grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10)
            Label(root3, text="Number of Seats Available are:", font=("Book Antiqua", 14), fg="white",
                  bg="orange").grid(row=4, column=0, padx=10)
            Label(root3, text=random.randint(100, 300), font=("Book Antiqua", 14), fg="white", bg="green").grid(row=4,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=15)
            Label(root3, text=" ").grid(row=5, column=0)
            Button(root3, text="Proceed for the next step", font=("Book Antiqua", 12), command=signup).grid(row=6,
                                                                                                            column=0,
                                                                                                            padx=20)
            Label(root3, text=" ").grid(row=7, column=0)
            # Button(root3,text="Already have an account - Sign in",font=("Book Antiqua",12),command=signin).grid(
            # row=8,column=0,padx=20)
            root3.mainloop()
        elif board.get() == "Delhi" and arr.get() == "Bangalore":
            root2.destroy()
            root3 = Tk()
            Label(root3, text="You selected flight from Delhi to Bangalore", font=("Book Antiqua", 15), fg="blue").grid(
                row=1, column=0, padx=50, pady=10)
            Label(root3, text="Distance of flight is 1740km", font=("Book Antiqua", 15), fg="blue").grid(row=2,
                                                                                                         column=0,
                                                                                                         pady=10,
                                                                                                         padx=10)
            Label(root3, text="Time duration of flight is 2h 50min", font=("Book Antiqua", 15), fg="blue").grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10)
            Label(root3, text="Number of Seats Available are:", font=("Book Antiqua", 14), fg="white",
                  bg="orange").grid(row=4, column=0, padx=10)
            Label(root3, text=random.randint(100, 300), font=("Book Antiqua", 14), fg="white", bg="green").grid(row=4,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=15)
            Label(root3, text=" ").grid(row=5, column=0)
            Button(root3, text="Proceed for the next step", font=("Book Antiqua", 12), command=signup).grid(row=6,
                                                                                                            column=0,
                                                                                                            padx=20)
            Label(root3, text=" ").grid(row=7, column=0)
            # Button(root3,text="Already have an account - Sign in",font=("Book Antiqua",12),command=signin).grid(
            # row=8,column=0,padx=20)
            root3.mainloop()
        elif board.get() == "Delhi" and arr.get() == "Chennai":
            root2.destroy()
            root3 = Tk()
            Label(root3, text="You selected flight from Delhi to Chennai", font=("Book Antiqua", 15), fg="blue").grid(
                row=1, column=0, padx=50, pady=10)
            Label(root3, text="Distance of flight is 1757km", font=("Book Antiqua", 15), fg="blue").grid(row=2,
                                                                                                         column=0,
                                                                                                         pady=10,
                                                                                                         padx=10)
            Label(root3, text="Time duration of flight is 3h", font=("Book Antiqua", 15), fg="blue").grid(row=3,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=10)
            Label(root3, text="Number of Seats Available are:", font=("Book Antiqua", 14), fg="white",
                  bg="orange").grid(row=4, column=0, padx=10)
            Label(root3, text=random.randint(100, 300), font=("Book Antiqua", 14), fg="white", bg="green").grid(row=4,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=15)
            Label(root3, text=" ").grid(row=5, column=0)
            Button(root3, text="Proceed for the next step", font=("Book Antiqua", 12), command=signup).grid(row=6,
                                                                                                            column=0,
                                                                                                            padx=20)
            Label(root3, text=" ").grid(row=7, column=0)
            # Button(root3,text="Already have an account - Sign in",font=("Book Antiqua",12),command=signin).grid(
            # row=8,column=0,padx=20)
            root3.mainloop()
        elif board.get() == "Ahmedabad" and arr.get() == "Ahmedabad":
            messagebox.showerror("ERROR", "Invalid Input")
        elif board.get() == "Bangalore" and arr.get() == "Bangalore":
            messagebox.showerror("ERROR", "Invalid Input")
        elif board.get() == "Chennai" and arr.get() == "Chennai":
            messagebox.showerror("ERROR", "Invalid Input")
        else:
            messagebox.showerror("ERROR", "Invalid Input")

    root2.mainloop()


p1 = PhotoImage(file="plane.png")
l2 = Label(image=p1)
l2.pack()
l1 = Label(text="AIRLINE BOOKING SYSTEM\nProject Lambda", bg="red", fg="yellow", padx=27, pady=27,
           font=("Algerian", 25, "bold"), borderwidth=8, relief=SUNKEN)
# l1.pack(side="bottom",anchor="s")
l1.pack(padx=30, pady=30)
root.title("AIRLINE BOOKING SYSTEM")
f1 = Frame(root, borderwidth=2, bg="pink")
f1.pack()
b1 = Button(f1, fg="green", text="PROCEED TO PROJECT", font=("Algerian", 12), command=page2)
b1.pack()
root.mainloop()
