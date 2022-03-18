
from datetime import date
from unicodedata import name


class RestaurantReservation:

    def __init__(self,resname,resdate,restable):
        self.client_name = resname
        self.reservation_date = resdate
        self.table_name = restable

    # Getter functions
    def get_client_name(self):
        return self.client_name

    def get_res_date(self):
        return self.reservation_date

    def get_table_name(self):
        return self.table_name