# converting celsius into fahrenheit
Celsius = float(input("Enter The tempreture in Celsius : "))
convertC= Celsius * 1.8 - 32
print("Celsius to fahrenheit : ",convertC)

# converting fahrenheit into celsius
Fahrenheit = float(input("Enter The tempreture in fahrenheit : "))
convertF = (Fahrenheit + 32) /1.8
print("fahrenheit to celsius : ",convertF)


# Login
print("Login  :) ")
name = str(input("Enter name : "))
reg = str(input("Enter Registration ID : "))
pas = int(input("enter pin : "))
admin = reg == 65217 and pas == 123
print(admin)


#Price of an item 

orignal_price = int(input("Enter the price of item : "))
discount = orignal_price/10
final_price = orignal_price-discount
print("Orignal Price : ",orignal_price)
print("After Discount Price : ",final_price)
print("Discount You get : ", discount)


#book reading time

num_pages = int(input("Number of pages in book : "))
reading_time = num_pages * 2
print("Number pages", num_pages)
print("Reading time : ",reading_time,"Minutes")

# Area of rectangle

lenght = int(input("Enter lenght  : "))
width = int(input("Enter width : "))
area = lenght*width
print("Area OF Rectangle is : ",area)


#Flag

name = str(input("Enter name : "))
reg = str(input("Enter Registration ID : "))
age = int(input("Enter age : "))
Flag = reg ==65217
print("The student is completed the assigment : ",Flag)
