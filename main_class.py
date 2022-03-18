
class Student:

    def __init__(self,name,section,yearlevel,gender):
        self.name = name #NULL
        self.section = section
        self.yearlevel = yearlevel
        self.gender = gender

    # Setter functions
    def set_name(self,stud_name):
        self.name = stud_name

    def set_section(self,stud_section):
        self.section = stud_section
    
    def set_yearlevel(self,stud_yr):
        self.yearlevel = stud_yr

    def set_gender(self,stud_gender):
        self.gender = stud_gender

    # Getter functions
    def get_name(self):
        return self.name

    def get_section(self):
        return self.section
    
    def get_yrlevel(self):
        return self.yearlevel

    def get_gender(self):
        return self.gender