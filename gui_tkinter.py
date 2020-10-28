import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import ttk,messagebox
from tkinter.scrolledtext import ScrolledText
class tk_project: #creating class
    def __init__(self,root):
        self.root=root
        self.root.title("PostJob.com")
        self.root.geometry("1080x700+0+0")
        #frame defiation for registration frame
        def register_frame():
            register_data.pack(fill="both",expand="yes")
            frame_home.pack_forget()
        
        #home frame function
        def home_frame():
            if self.txt_company.get()=="" or self.txt_role.get()=="" or self.txt_salary.get()=="" or self.txt_salary1.get()=="" or self.txt_addr.get()=="" or self.txt_email.get()=="" or self.txt_loc.get()=="" or self.txt_requirement.get()=="" or self.txt_edu.get()=="" or self.txt_skill.get()=="" or self.txt_about.get()=="":
            	messagebox.showerror("Error","All Fields Are Required")
            	
            else:
            	try:
            		mycon= mysql.connector.connect(host='localhost',user='root',password='H@ckmeifyoucan1',database='job_portal')
            		mycurs= mycon.cursor()
            		command_mysql=("insert into jobpost(role,company_name,min_salary,max_salary,compan_address,email_address,work_location,about_us,min_requirement,min_education,key_skills) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            		vartouple=(self.txt_role.get(),self.txt_company.get(),self.txt_salary.get(),self.txt_salary1.get(),self.txt_addr.get(),self.txt_email.get(),self.txt_loc.get(),self.txt_about.get(),self.txt_requirement.get(),self.txt_edu.get(),self.txt_skill.get())
            		mycurs.execute(command_mysql,vartouple)
            		mycon.commit()
            		mycurs.close()
            		register_data.pack_forget()
            		messagebox.showinfo("Success","Your Job Post Is Online")

            		frame_home.pack(fill="both",expand="yes")
            	except Error as err:
            		messagebox.showerror("Error",f"Error due to: {str(err)}")
           
	
            
            

            
        #hide frames function
        def hide_frames():
            frame_home.pack_forget()
            register_data.pack_forget()
        #Data fetch
        def fetch_data():
        	self.txt_company.get()
        	print(inputValue)




        #frame_1 necessary contents of company
        frame_home=LabelFrame(root)
        frame_home.pack(fill="both",expand="yes")
        #button for post jobs
        post_job_button=Button(frame_home,text="Post Job",fg='#b7f731',relief='flat',bg='black',command=register_frame)
        post_job_button.place(x=400,y=200,width=250,height=250)


        #frame_2 necessary for registeration form
        register_data=LabelFrame(root,bg="white")

        #button for registration form
        register_button=Button(register_data,text="Publish Jobs",fg='#b7f731',relief='flat',bg='black',command=home_frame)
        register_button.pack(side = BOTTOM, fill = BOTH)


        #_______All inputs for registration frame_______
        title_reg=Label(register_data,text="Enter Jobs Description",font=("times new roman",20,"bold"),bg="white",fg="#b380ff").place(x=30,y=30)


        #___________Entry Field for registration frame________
        #company name
        company_name=Label(register_data,text="Commpany Name",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=30,y=90)
        self.txt_company=Entry(register_data,font=("times new roman",13),bg="light gray")
        self.txt_company.place(x=31,y=120,width=250)
        #company Role
        company_role=Label(register_data,text="Role",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=600,y=90)
        self.txt_role=Entry(register_data,font=("times new roman",13),bg="light gray")
        self.txt_role.place(x=601,y=120,width=250)
        #compnay salary
        company_salary=Label(register_data,text="MIN-MAX salary",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=30,y=180)
        company_salary=Label(register_data,text="-",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=120,y=210)
        self.txt_salary=Entry(register_data,font=("times new roman",13),bg="light gray")
        self.txt_salary.place(x=30,y=210,width=80)
        self.txt_salary1=Entry(register_data,font=("times new roman",13),bg="light gray")
        self.txt_salary1.place(x=150,y=210,width=80)
        #company address
        company_addr=Label(register_data,text="Company Address",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=600,y=180)
        self.txt_addr=Entry(register_data,font=("times new roman",13),bg="light gray")
        self.txt_addr.place(x=601,y=210,width=250)

        #company email
        company_email=Label(register_data,text="Company Email",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=30,y=260)
        self.txt_email=Entry(register_data,font=("times new roman",13),bg="light gray")
        self.txt_email.place(x=30,y=290,width=250)
        #work location
        work_loc=Label(register_data,text="Work Location",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=600,y=260)
        self.txt_loc=Entry(register_data,font=("times new roman",13),bg="light gray")
        self.txt_loc.place(x=600,y=290,width=250)


        #about us
        company_about=Label(register_data,text="About Us",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=30,y=340)
        self.txt_about=Entry(register_data,font=("times new roman",13),bg="light gray")
        self.txt_about.place(x=30,y=370,width=850,height="40")

        #Minimum requirement
        company_requirement=Label(register_data,text="Minimum requirement",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=30,y=420)
        self.txt_requirement=Entry(register_data,font=("times new roman",13),bg="light gray")
        self.txt_requirement.place(x=30,y=450,width=850,height="40")

        #Minimum Education
        company_edu=Label(register_data,text="Minimum Education",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=30,y=500)
        self.txt_edu=Entry(register_data,font=("times new roman",13),bg="light gray")
        self.txt_edu.place(x=30,y=530,width=850,height="40")

        #Skills Required
        company_skill=Label(register_data,text="Key Skills",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=30,y=580)
        self.txt_skill=Entry(register_data,font=("times new roman",13),bg="light gray")
        self.txt_skill.place(x=30,y=610,width=850,height="40")


        



      

      	
      	
        

        





        

root=Tk()
obj=tk_project(root)
root.mainloop()
