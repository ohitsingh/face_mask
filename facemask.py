from tkinter import *
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("incognitobilling")
        bg_colour="#074463"
        title=Label(self.root, text="Billing Desk",bd=12, relief=GROOVE,bg=bg_colour,fg="white", font=("times new roman",30,"bold"), pady =2).pack(fill=X)
        #==========student details========frame=======
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Student Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_colour)
        F1.place(x=0,y=70,relwidth=1)

        sname_lbl=Label( F1,text="Student Name",bg=bg_colour,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        sname_txt=Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        sphone_lbl = Label(F1, text="contact no.", bg=bg_colour, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        sphone_txt = Entry(F1, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        sid_lbl = Label(F1, text="unique id", bg=bg_colour, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        sid_txt = Entry(F1, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=5,pady=10)


        #===================semester wise payment details+++++++++++++++++++++
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Semester Payment",font=("times new roman",15,"bold"),fg="gold",bg=bg_colour)
        F2.place(x=0,y=160,width=325,height=380)

        sem1=Label(F2,text="sem1",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        sem1_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        sem2=Label(F2,text="sem2",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        sem2_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        sem3=Label(F2,text="sem3",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        sem3_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        sem4=Label(F2,text="sem4",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        sem4_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        sem5=Label(F2,text="sem5",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sem5_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        sem6=Label(F2,text="sem6",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        sem6_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #+++++++++++++++++++Bus payment+++++++++++++++++++++++++++++++++++

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bus Payment",font=("times new roman",15,"bold"),fg="gold",bg=bg_colour)
        F3.place(x=326,y=160,width=325,height=380)

        sem1=Label(F3,text="sem1",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        sem1_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        sem2=Label(F3,text="sem2",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        sem2_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        sem3=Label(F3,text="sem3",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        sem3_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        sem4=Label(F3,text="sem4",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        sem4_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        sem5=Label(F3,text="sem5",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sem5_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        sem6=Label(F3,text="sem6",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        sem6_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #***********fine+++++++++++++++++++++++

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Fine",font=("times new roman",15,"bold"),fg="gold",bg=bg_colour)
        F4.place(x=650,y=160,width=325,height=380)

        payment=Label(F4,text="Late payment",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        payment_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        lib=Label(F4,text="Library",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        lib2_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        distruct=Label(F4,text="Distruction",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        distruct_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        #*********Bill area++++++++++++++++++++++++++++

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=975,y=160,width=325,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #*******Button Frame **********

        F6=LabelFrame(self.root, bd=10, relief=GROOVE, text="Billing Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_colour)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1_lbl=Label(F6,text="Total semester payment",bg=bg_colour,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,font="arial 10 bold ",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Bus payment",bg=bg_colour,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,font="arial 10 bold ",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)


        m3_lbl=Label(F6,text="Total Fine",bg=bg_colour,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,font="arial 10 bold ",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=400,width=585,height=105)

        total_btn=Button(btn_F,text="total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        gen_btn=Button(btn_F,text="generate bill",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="clear",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="exit",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)

root = Tk()
obj = Bill_App(root)
root.mainloop()
