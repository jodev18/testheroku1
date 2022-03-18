
from reservation import RestaurantReservation

list_of_reservations = []

while True:

    choice = input("Please enter choice:\n1)Add\n2)Cancel\n"\
                "3)Update\n4)View\nEnter choice(1-4):")

    if choice == "1":
        client_name = input("Enter client's name:")
        reserve_date = input("Enter reservation date (dd-mm-yyyy):")
        table_name = input("Enter table number: ")

        if len(list_of_reservations) > 0:
            has_found = False
            has_found_index = -1
            
            for x in range(len(list_of_reservations)):

                if list_of_reservations[x].get_res_date() == reserve_date \
                        and list_of_reservations[x].get_table_name() == table_name:
                        has_found = True
                        has_found_index = x
                        break
            
            if has_found:
                print("Reservation for the table for the date already overlaps with: ")
                print("Client: " + list_of_reservations[has_found_index].get_client_name())
                print("Date: " + list_of_reservations[has_found_index].get_res_date())
                print("Table: " + list_of_reservations[has_found_index].get_table_name())
            else:
                res_info  = RestaurantReservation(client_name,reserve_date,table_name)
                list_of_reservations.append(res_info)  
        else:
            res_info  = RestaurantReservation(client_name,reserve_date,table_name)
            list_of_reservations.append(res_info)
    
    elif choice=="2":
        
        print("-"*10,"Cancelling Reservation","-"*10)
        for x in range(len(list_of_reservations)):
            current_item = list_of_reservations[x]

            print(x,current_item.get_client_name(),"\t" \
            ,current_item.get_res_date(),"\t",current_item.get_table_name())
        
        remove_choice = int(input("Enter the index of the item you want to remove (number only): "))

        list_of_reservations.remove(list_of_reservations[remove_choice])

    elif choice=="4":

        for item in list_of_reservations:
            print(item.get_client_name(),"\t",item.get_res_date(),"\t",item.get_table_name())

