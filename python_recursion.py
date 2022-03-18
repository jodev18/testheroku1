
def recursion_demo(counter):

    print("This is a function for recursion")
    if counter < 2:
        counter += 3
        recursion_demo(counter)

recursion_demo(0)