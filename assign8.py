print("Welcome to the Grocery List")
import datetime

time = datetime.datetime.now()
month=str(time.month)
day=str(time.day)
hour=str(time.hour)
minute =str(time.minute)
print("Current Date and time : ",time)
grocery=['Meat','cheese']
print(f"You currently have {grocery[0]} and {grocery[1]} in your list")
add=input("Type of food to add to the grocery list:")
grocery.append(add)
add=input("Type of food to add to the grocery list:")
grocery.append(add)
add=input("Type of food to add to the grocery list:")
grocery.append(add)

print("Here is your grocery list : ",grocery)
grocery.sort()
print("Here is your sorted list sorted :",grocery)
print("Simulating grocery shopping...\n")
print('Current grocery, list:', len(grocery))
print(grocery)
add=input("what food did you just buy:")
grocery.remove("Apples")
print("Removing Apples from list...",grocery)
print("Current grocery list:", len(grocery))
print(grocery)
add=input("What food did you just buy:")
grocery.remove("Cheese")
print("Removing Cheese from list...")
print("current grocery list:", len(grocery))
add=input("What food did you just buy:")
grocery.remove("Soup")
print("Removing Soup from list...")
print("Current grocery list:", len(grocery))
print(grocery)
print("Sorry,the store is out of Meal")
add=input("What food like instead:")
grocery.append(add)
print("Here is what remains on your grocery list:",grocery)


