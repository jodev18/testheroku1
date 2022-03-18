
from datetime import date


class RestaurantReservation:

    def __init__(self,reserve_date,client_name,table_name):
        self.res_date = reserve_date
        self.res_name = client_name
        self.res_table_name = table_name

    def get_date(self):
        return self.res_date

    def get_client(self):
        return self.res_name

    def get_table(self):
        return self.res_table_name