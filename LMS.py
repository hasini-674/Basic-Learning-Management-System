class LMS:

    def __init__(self):
        self.students=[]
        
    def register_student(self):
        username=input("enter username:")
        for val in self.students:
            if val.username== username:
                print("username already taken")
                username= input("enter username")
            else:
                break
        password=input("enter password:")
        name= input("enter name:")
        rollno=input("enter rollno")
        new_student= Student(username,password,name,rollno)
        self.students.append(new_student)
        print("student registered successfully")
        
    def login_student(self):
        username=input("enter username:")
        password=input("enter password:")
        for val in self.students:
            if val.username== username:
                val.login(usename,password)
                return
        print("student not found")
        
    def display_details(self):
        username= input("enter username:")
        for val in self.students:
            if val.username== username:
                val.display()
                return
        print("student not found")
        
    def logout_student(self):
        username= input("enter username:")
        for val in self.students:
            if val.username== username:
                val.logout()
                return
        print("student not found")

obj= LMS()
print("Enter 1 for Registering")
print("Enter 2 for Login")
print("Enter 3 for Display details")
print("Enter 4 for logout")
n= int(input("enter your choice: "))
if(n==1):
    obj.register_student()
elif(n==2):
    obj.login_student()
elif(n==3):
    obj.display_details()
elif(n==4):
    obj.logout_student()
else:
    print("enter valid choice")
