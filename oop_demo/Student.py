
class StudentInfo:

    # class constructor
    def __init__(self,fname,lname,age,yearlevel):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.yearlevel = yearlevel

    # setter values / functions
    def set_firstname(self,firstname):
        self.firstname = firstname

    def set_lastname(self,lastname):
        self.lastname = lastname
    
    def set_age(self,age):
        self.age = age

    def set_yearlevel(self,yearlevel):
        self.yearlevel = yearlevel

    # getter values / functions

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_age(self):
        return self.age

    def get_yearlevel(self):
        return self.yearlevel