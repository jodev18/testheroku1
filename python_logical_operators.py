
# and = ^
# or = v
# not = ~
a = 20
b = 10
c = 50
d = 100
e = 68
f = 69
print("---AND---")
print(int(False)) # type casting
print ((a > b) and (((a+b) > (c+d)) < d) and (e < f))
print (False and True and True)
print (True and False and True)
print (False and False and True)
print("---OR---")
print (True or True or False)
print (False or True or False)
print (True or False or False)
print (False or False or False)
print("---NOT---")
print(not True)
print(not False)