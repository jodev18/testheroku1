
class Plant:

    def __init__(self):
        self.size = 0
    
    def water_plant(self):
        # put something here
        self.size += 1

    def wilt_plant(self):
        # put something here
        self.size -= 1

    def get_fruit(self,date):

        if date == "02-14-2022":
            return "Kiwi"

    def get_flower(self,date):

        if date == "02-14-2022":
            return "Rose"
