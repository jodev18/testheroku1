
from restaurant_data import RestaurantReservation

reservation_list = []

while True:
    reserve_name = input("Enter client name: ")
    reserve_table = input("Enter table name: ")
    reserve_date = input("Enter reservation date: ")
    
    has_duplicate = False

    for item in reservation_list:
        if reserve_date == item.get_date():
            has_duplicate = True
            break
    
    if has_duplicate:
        print("This date is already present in the list.")
    else:
        rr = RestaurantReservation(reserve_date,reserve_name,reserve_table)
        reservation_list.append(rr)

    
