import tkinter
from tkinter import Button, Entry, Frame, Label, Scrollbar, Tk, XView, YView, messagebox, ttk
from tkinter.constants import BOTH, BOTTOM, END, HORIZONTAL, RIGHT, VERTICAL, X, Y
import pymysql, random, time

host = "localhost"
user = "root"
password = ""
database = "studentdb"

date = time.strftime("%m/$d /%Y")
etime = time.strftime("%H:%M:%S")

r_id = random.randint(10000, 99999)


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.leftbg = "#005A8D"
        self.leftfg = "white"

        r_id = random.randint(10000, 99999)
        self.topheading = Label(self.root, text="Student Management System", font=("oswald", 25, "bold"), bg="#022E57",
                                fg="white", pady=10)
        self.topheading.place(x=0, y=0, relwidth=1)

        # Left Frame
        self.LeftFrame = Frame(self.root, bg="#005A8D")
        self.LeftFrame.place(x=0, y=62, width=450, height=685)
        self.leftheadertitle = Label(self.LeftFrame, text="Student Form", fg="white", font=("oswald", 13, "bold"),
                                     bg="#005A8D")
        self.leftheadertitle.place(x=0, y=10, relwidth=1)

        # Form Area
        self.id = Label(self.LeftFrame, text="Student ID:", font=("oswald", 12, "bold"), bg="#005A8D", fg="white")
        self.id.place(x=30, y=80)
        self.id_e = Entry(self.LeftFrame, font=("oswald", 12, "bold"))
        self.id_e.place(x=150, y=80)
        self.id_e.insert(END, str(r_id))

        self.department = Label(self.LeftFrame, text="Department:", font=("oswald", 12, "bold"), bg="#005A8D",
                                fg="white")
        self.department.place(x=30, y=130)
        self.department_e = ttk.Combobox(self.LeftFrame, font=("oswald", 12, "bold"))
        self.department_e["values"] = (
        "Computer Science", "Engineering", "Arts and Design", "Statistics", "Hospitality", "Other...")
        self.department_e.config(width=18)
        self.department_e.current(0)
        self.department_e.place(x=150, y=130)

        self.name = Label(self.LeftFrame, text="Student Name:", font=("oswald", 12, "bold"), bg="#005A8D", fg="white")
        self.name.place(x=30, y=180)
        self.name_e = Entry(self.LeftFrame, font=("oswald", 12, "bold"))
        self.name_e.place(x=150, y=180)

        self.email = Label(self.LeftFrame, text="Email Address:", font=("oswald", 12, "bold"), bg="#005A8D", fg="white")
        self.email.place(x=30, y=230)
        self.email_e = Entry(self.LeftFrame, font=("oswald", 12, "bold"))
        self.email_e.place(x=150, y=230)

        self.phone = Label(self.LeftFrame, text="Phone Number:", font=("oswald", 12, "bold"), bg="#005A8D", fg="white")
        self.phone.place(x=30, y=280)
        self.phone_e = Entry(self.LeftFrame, font=("oswald", 12, "bold"))
        self.phone_e.place(x=150, y=280)

        self.gender = Label(self.LeftFrame, text="Gender:", font=("oswald", 12, "bold"), bg="#005A8D", fg="white")
        self.gender.place(x=30, y=330)
        self.gender_e = ttk.Combobox(self.LeftFrame, font=("oswald", 12, "bold"))
        self.gender_e["values"] = ("Male", "Female", "Other")
        self.gender_e.config(width=18)
        self.gender_e.current(0)
        self.gender_e.place(x=150, y=330)

        self.address = Label(self.LeftFrame, text="Address:", font=("oswald", 12, "bold"), bg="#005A8D", fg="white")
        self.address.place(x=30, y=380)
        self.address_e = Entry(self.LeftFrame, font=("oswald", 12, "bold"))
        self.address_e.place(x=150, y=380)

        self.Level = Label(self.LeftFrame, text="Level:", font=("oswald", 12, "bold"), bg="#005A8D", fg="white")
        self.Level.place(x=30, y=430)
        self.Level_e = ttk.Combobox(self.LeftFrame, font=("oswald", 12, "bold"))
        self.Level_e["values"] = ("100", "200", "300", "400")
        self.Level_e.config(width=18)
        self.Level_e.current(0)
        self.Level_e.place(x=150, y=430)

        # Button
        self.addbtn = Button(self.LeftFrame, command=self.insertdata, text="Add Student", font=("oswald", 12, "bold"),
                             bg="#DA0037", fg="white", padx=10, width=10, activebackground="black",
                             activeforeground="#D83A56")
        self.addbtn.place(x=30, y=500)
        self.updatebtn = Button(self.LeftFrame, command=self.updatedata, text="Update", font=("oswald", 12, "bold"),
                                bg="#DA0037", fg="white", padx=10, width=10, activebackground="black",
                                activeforeground="#D83A56")
        self.updatebtn.place(x=160, y=500)
        self.deletebtn = Button(self.LeftFrame, command=self.deletedata, text="Delete", font=("oswald", 12, "bold"),
                                bg="#DA0037", fg="white", padx=10, width=10, activebackground="black",
                                activeforeground="#D83A56")
        self.deletebtn.place(x=290, y=500)

        self.showallbtn = Button(self.LeftFrame, command=self.fetchdata, text="Show All", font=("oswald", 12, "bold"),
                                 bg="#DA0037", fg="white", padx=10, width=10, activebackground="black",
                                 activeforeground="#D83A56")
        self.showallbtn.place(x=30, y=565)
        self.clearbtn = Button(self.LeftFrame, command=self.cleardata, text="Clear", font=("oswald", 12, "bold"),
                               bg="#DA0037", fg="white", padx=10, width=10, activebackground="black",
                               activeforeground="#D83A56")
        self.clearbtn.place(x=160, y=565)
        self.exitbtn = Button(self.LeftFrame, command=self.exit, text="Exit", font=("oswald", 12, "bold"), bg="#DA0037",
                              fg="white", padx=10, width=10, activebackground="black", activeforeground="#D83A56")
        self.exitbtn.place(x=290, y=565)

        # Right Frame
        self.RightFrame = Frame(self.root, bg="#FFC947")
        self.RightFrame.place(x=450, y=62, width=920, height=680)

        self.righttopheading = Label(self.RightFrame, text="Student table", font=("oswald", 18, "bold"), bg="#FFC947",
                                     fg="white")
        self.righttopheading.place(x=0, y=10, relwidth=1)

        self.TableFrame = Frame(self.RightFrame)
        self.TableFrame.place(x=25, y=60, width=850, height=550)

        # Student Data Table
        self.scroll_x = Scrollbar(self.TableFrame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.TableFrame, orient=VERTICAL)
        self.StudentTable = ttk.Treeview(self.TableFrame, columns=(
        "id", "department", "name", "email", "phone", "gender", "address", "level", "edate", "etime"),
                                         xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.StudentTable.xview)
        self.scroll_y.config(command=self.StudentTable.yview)
        self.StudentTable.heading("id", text="Student ID")
        self.StudentTable.heading("department", text="Department")
        self.StudentTable.heading("name", text="Name")
        self.StudentTable.heading("email", text="Email")
        self.StudentTable.heading("phone", text="Phone")
        self.StudentTable.heading("gender", text="Gender")
        self.StudentTable.heading("address", text="Address")
        self.StudentTable.heading("level", text="Level")
        self.StudentTable.heading("edate", text="Entry Date")
        self.StudentTable.heading("etime", text="Entry Time")
        self.StudentTable.column("id", width=150)
        self.StudentTable.column("department", width=150)
        self.StudentTable.column("name", width=150)
        self.StudentTable.column("email", width=150)
        self.StudentTable.column("phone", width=150)
        self.StudentTable.column("gender", width=150)
        self.StudentTable.column("address", width=150)
        self.StudentTable.column("level", width=150)
        self.StudentTable.column("edate", width=150)
        self.StudentTable.column("etime", width=150)
        self.StudentTable["show"] = "headings"
        self.StudentTable.pack(fill=BOTH, expand=1)
        self.StudentTable.bind("<ButtonRelease>", self.get_cur)
        self.fetchdata()

    def insertdata(self):
        if self.department_e.get() == "" or self.name_e.get() == "" or self.phone_e.get() == "":
            messagebox.showerror("Error", "Some fields are required.")
        else:
            con = pymysql.connect(host=host, user=user, password=password, database=database)
            cur = con.cursor()
            q = "insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(q, (
            self.id_e.get(), self.department_e.get(), self.name_e.get(), self.email_e.get(), self.phone_e.get(),
            self.gender_e.get(), self.address_e.get(), self.Level_e.get(), date, etime))
            con.commit()
            self.id_e.delete(0, END)
            self.id_e.insert(END, str(r_id))
            self.department_e.delete(0, END)
            self.name_e.delete(0, END)
            self.email_e.delete(0, END)
            self.phone_e.delete(0, END)
            self.gender_e.delete(0, END)
            self.address_e.delete(0, END)
            self.Level_e.delete(0)
            self.fetchdata()

            con.close()
            messagebox.showinfo("Added", f"Student ID {self.id_e.get()} added successfully")

    def fetchdata(self):
        con = pymysql.connect(host=host, user=user, password=password, database=database)
        cur = con.cursor()
        q = "select * from students"
        cur.execute(q)
        rows = cur.fetchall()
        self.StudentTable.delete(*self.StudentTable.get_children())
        for row in rows:
            singlerow = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
            self.StudentTable.insert("", END, values=singlerow)
            print(singlerow)

    def get_cur(self, ev):
        copy = self.StudentTable.focus()
        content = self.StudentTable.item(copy)
        data = content["values"]
        if len(data) != 0:
            self.id_e.delete(0, END)
            self.id_e.insert(END, data[0])

            self.department_e.delete(0, END)
            self.department_e.insert(END, data[1])

            self.name_e.delete(0, END)
            self.name_e.insert(END, data[2])

            self.email_e.delete(0, END)
            self.email_e.insert(END, data[3])

            self.phone_e.delete(0, END)
            self.phone_e.insert(END, data[4])

            self.gender_e.delete(0, END)
            self.gender_e.insert(END, data[5])

            self.address_e.delete(0, END)
            self.address_e.insert(END, data[6])

            self.Level_e.delete(0, END)
            self.Level_e.insert(END, data[7])

    def cleardata(self):
        mess = messagebox.askyesnocancel("Clear", "Do you want to clear form")
        if mess > 0:
            self.id_e.delete(0, END)
            self.id_e.insert(END, str(r_id))
            self.department_e.delete(0, END)
            self.name_e.delete(0, END)
            self.email_e.delete(0, END)
            self.phone_e.delete(0, END)
            self.gender_e.delete(0, END)
            self.address_e.delete(0, END)
            self.Level_e.delete(0)
            self.fetchdata()

    def updatedata(self):
        mess = messagebox.askyesnocancel("Update", "Do you want to update form")
        if mess > 0:
            con = pymysql.connect(host=host, user=user, password=password, database=database)
            cur = con.cursor()
            q = "update students set department=%s, name=%s, email=%s, phone=%s, gender=%s, address=%s, Level=%s where id=%s"
            cur.execute(q, (
            self.department_e.get(), self.name_e.get(), self.email_e.get(), self.phone_e.get(), self.gender_e.get(),
            self.address_e.get(), self.Level_e.get(), self.id_e.get()))
            con.commit()
            self.id_e.delete(0, END)
            self.id_e.insert(END, str(r_id))
            self.department_e.delete(0, END)
            self.name_e.delete(0, END)
            self.email_e.delete(0, END)
            self.phone_e.delete(0, END)
            self.gender_e.delete(0, END)
            self.address_e.delete(0, END)
            self.Level_e.delete(0)
            self.fetchdata()

    def deletedata(self):
        mess = messagebox.askyesnocancel("Delete", "Do you want to delete form")
        if mess > 0:
            con = pymysql.connect(host=host, user=user, password=password, database=database)
            cur = con.cursor()
            q = "update students set department=%s, name=%s, email=%s, phone=%s, gender=%s, address=%s, Level=%s where id=%s"
            cur.execute(q, (
            self.department_e.get(), self.name_e.get(), self.email_e.get(), self.phone_e.get(), self.gender_e.get(),
            self.address_e.get(), self.Level_e.get(), self.id_e.get()))
            con.commit()
            self.id_e.delete(0, END)
            self.id_e.insert(END, str(r_id))
            self.department_e.delete(0, END)
            self.name_e.delete(0, END)
            self.email_e.delete(0, END)
            self.phone_e.delete(0, END)
            self.gender_e.delete(0, END)
            self.address_e.delete(0, END)
            self.Level_e.delete(0)
            self.fetchdata()

            con.close()
            messagebox.showinfo("Delete", f"Student ID {self.id_e.get()} deleted successfully")

    def exit(self):
        mess = messagebox.askyesnocancel("Exit", "Do you want to exit application")
        if mess > 0:
            self.root.destroy()


root = Tk()
obj = StudentManagementSystem(root)
root.mainloop()
