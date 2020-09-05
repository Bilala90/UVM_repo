from ctypes import * 
so = "/home/bilal/Desktop/cadence/python/my_functions.so"

my_functions = CDLL(so) 

cfun = CDLL("/home/bilal/Desktop/cadence/python/my_functions.so")

print("first instance is ",cfun.square(5))

print(my_functions.square(10))

print(my_functions.square(8))

print("DONE")

