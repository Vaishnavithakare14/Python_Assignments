print("Welcome to the Grade Sorter App")
grades=[]
grade=int(input("what is your first grade(0-100):"))
grades.append(grade)
grade=int(input("what is your second grade(0-100):"))
grades.append(grade)
grade=int(input("what is your third grade(0-100):"))
grades.append(grade)
grade=int(input("what is your fourth grade(0-100):"))
grades.append(grade)

print(f"\n Your grades are:{grades}]")

grades.sort(reverse=True)

print(f"\nYour grades from highest to lowest are:{grades}.")
print("The lowest two grades will now be droped")
      

print(f"\nremove grade :{grades[3]}")
grades.pop()

print(f"\nremove grade :{grades[2]}")
grades.pop()
print(f"\n Your remaining grades :{grades}.")
print(f"Nice work! Your highest grade is a {grades[0]}")
