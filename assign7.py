num_strings=["15","100","55","42"]
print("The variable num_strings is a" ,type(num_strings))
print(f"It contains the elements:{num_strings}")
print(f"The element {num_strings[0]} is a", type(num_strings[0]))

num_ints=[15,100,55,42]
print("\nThe variable num_ints is a",type(num_ints))
print(f"It contains an elements:{num_ints}")
print(f"The element {num_ints[0]} is a" ,type(num_ints[0]))
num_floats=[22.3,34.6,4.6,8.7]
print("\nThe variable num_floats is a ", type(num_floats))
print("It  contains  the element:{num_floats}")
print("The element{num_floats[0]} is", type(num_floats[0]))
num_list=[[1,2,3],[4,5,6],[7,8,9]]
print("\nThe variable num_list is a", type(num_list))
print(f"It contains the element {num_list}")
print(f"It contains element {num_list[0]}",type(num_list[0]))
print("\n Now sorting num_strings and num_ints...")


num_strings.sort()
num_ints.sort()

print(f"Sorted num_strings:{num_strings}")
print(f"sorted num_ints:{num_ints}")
print("\nStrings are sorted alphabetically while integers are sorted numerically!")


