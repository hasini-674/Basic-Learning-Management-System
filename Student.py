class Student:
    def __init__(self,username,password,name,rollno):
        self.username= username
        self.password= password
        self.name= name
        self.rollno= rollno
        self.logged_in= False
    def login(self,username,password):
        if username==self.username and password== self.password:
            print("login successful")
            self.logged_in= True
        elif username in self.username and password!= self.password:
            print("Incorrect details")
        else:
            print("User not Registered")
    def display(self,name,rollno):
        if self.logged_in:
            print("Name: ",self.name)
            print("Roll Number: ",self.rollno)
        else:
            print("please login")
    def logout(self):
        if self.logged_in:
            self.logged_in= False
            print("logged out successfully")
