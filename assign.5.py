print("welcome to the Multiplication/Exponent Table Program")
name=input("Hello,what is your name:").title().strip()
num=float(input("What number would you like to work with:"))
message=f"{name},Math is cool!"
#multiplication table
print("Multiplication Table for" + str(num))
print(f"\t1.0*{num}={round(1*num,4)}")
print(f"\t2.0*{num}={round(2*num,4)}")
print(f"\t3.0*{num}={round(3*num,4)}")
print(f"\t4.0*{num}={round(4*num,4)}")
print(f"\t5.0*{num}={round(5*num,4)}")
print(f"\t6.0*{num}={round(6*num,4)}")
print(f"\t7.0*{num}={round(7*num,4)}")
print(f"\t8.0*{num}={round(8*num,4)}")
print(f"\t9.0*{num}={round(9*num,4)}")

print(f"\n\t1.0*{num}={round(1*num,4)}")
print(f"\t2.0*{num}={round(2*num,4)}")
print(f"\t3.0*{num}={round(3*num,4)}")
print(f"\t4.0*{num}={round(4*num,4)}")
print(f"\t5.0*{num}={round(5*num,4)}")
print(f"\t6.0*{num}={round(6*num,4)}")
print(f"\t7.0*{num}={round(7*num,4)}")
print(f"\t8.0*{num}={round(8*num,4)}")
print(f"\t9.0*{num}={round(9*num,4)}")
#Exponent table
print("\nExponent Table for " +str(num))
print(f"\t{num}** 1={round(num**1,4)}")
print(f"\t{num}** 2={round(num**2,4)}")
print(f"\t{num}** 3={round(num**3,4)}")
print(f"\t{num}** 4={round(num**4,4)}")
print(f"\t{num}** 5={round(num**5,4)}")
print(f"\t{num}** 6={round(num**6,4)}")
print(f"\t{num}** 7={round(num**7,4)}")
print(f"\t{num}** 8={round(num**8,4)}")
print(f"\t{num}** 9={round(num**9,4)}")
#math is cool!
print("\n"+ message)
print("\t" + message.lower())
print("\t\t"+ message.title())
print("\t\t\t" + message.upper())
