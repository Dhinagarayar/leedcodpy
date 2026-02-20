"""Apple_fRuite123=10
print(Apple_fRuite123)
# data type
#integer
#float
#string
#boolean
#list
#tuple
#dictionary
1
current_year=int(input("Enter the current year: "))21
birth_year=int(input("Enter birth year: "))
age=current_year-birth_year
print(age)
2
current_age=int(input("Enter the current age: "))
max_age=int(input("Enter the maximum age: "))
amount_per_day=int(input("Enter the amount of money you spend per day: "))
total_amount=(max_age-current_age)*365.1/42*amount_per_day
print("You will need Rs.", total_amount, "to last until your old age", max_age)
3
current_age=int(input("Enter the current age: "))
max_age=int(input("Enter the maximum age: "))
drinking_water_per_day=int(input("Enter the amount of water you drink per day : "))
total_water=(max_age-current_age)*365.1/4*drinking_water_per_day
print("You will need", total_water, "liters of water to last until your old age", max_age)
4
trip_distance=int(input("Enter the trip distance"))
milage=int(input("Enter the vehicle milage"))
fuel_price=int(input("Enter th fuel price"))
fuel_need=trip_distance/milage
total_cost=fuel_need*fuel_price
print("the fuel need is" ,fuel_need, "litres")
print("The total fuel cost for the trip is Rs.",total_cost)
5
data_useage=int(input("Enter the daily data"))
month=int(input("Enter the number of months"))
total_data=data_useage*30*month
print("You will need", total_data, "GB of data for", month, "months")
6
current_age=int(input("Enter the current age: "))
year=current_age*365.1/4
print("You have lived for", year, "days")
7
orginal_price=int(input("Enter the orginal price :"))
discount_percentage=int(input("enter the discount percetage :"))
discount_amount=orginal_price-((discount_percentage/100)*orginal_price)
print("the final price is", discount_amount)
x=int(input("Enter the number :"))
y=int(input("Enter the number :"))
if x<y:
    print(x," less than ",y)
elif x==y:
    print("x and y is equal :",x)
else:
    print(x," greater than ",y)

x=input("Enter the alphabet ;")
if x in ['a','e','i','o','u']:
    print(x," is a vowel")
else:    
    print(x," is a consonant")
8
student_marks=int(input("Enter the marks of the student :"))
if student_marks==100:
    print("Grade S")
elif student_marks>=90:
    print("Grade A")
elif student_marks>=80:
    print("Grade B")    
elif student_marks>=70:
    print("Grade C")
elif student_marks>=60:
    print("Grade D")
elif student_marks>=50:
    print("Grade E")       
else:
    print("Grade F")  
9
buy_price=int(input("Enter the buying price :"))      
selling_price=int(input("Enter the selling price :"))
if selling_price>buy_price:
    print("profit of Rs.",(selling_price-buy_price)*12)
elif selling_price<buy_price:
    print("loss of Rs.",(buy_price-selling_price)*12)
else:
    print("no profit or loss")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

#day 2
#1
students=["DS : Days Scholar    ","H : Hosteller   ","MSH : Management Seat days Scholar  ","MSH : Management Seat hosteller"]
print(students)
student_type=str(input("Enter the student type DS,H,MSDS OR MSH :"))
stution_fees=int(input("Enter the stution fees :"))
if student_type=="MSH":
    hostal_fees=int(input("Enter the hostal fees :"))
    print("the student paid the fees is Rs.",1.5*(stution_fees+hostal_fees))
elif student_type=="MSDS":
    bus_fees=int(input("Enter the bus fees Rs."))
    print("the student paid the fees is Rs.",1.5*(stution_fees+bus_fees))
elif student_type=="DS":
    bus_fees=int(input("Enter the bus fees Rs."))
    print("the student paid the fees is Rs.",(stution_fees+bus_fees))
elif student_type=="H":
    hostal_fees=int(input("Enter the hostal fees :"))
    print("the student paid the fees is Rs.",stution_fees+hostal_fees)
else:
    print("Invalid student type")
#2
account_balance=int(input("Enter the account balance :"))
withdrawal_amount=int(input("Enter the withdrawal amount :"))
if withdrawal_amount>account_balance:
    print("Insufficient balance")
elif withdrawal_amount>10000:
    print("you get money only for Rs.10000")
else:
    balance=(account_balance-withdrawal_amount)
    print("withdrawal amount is Rs.",withdrawal_amount)
    print("your balance is Rs.",balance)
#3
account_balance=100000
stored_pin=6385
user_id=int(input("Enter your user ID pin :"))
if stored_pin==user_id:
    withdrawal_amount=int(input("Enter the withdrawal amount :"))

    if withdrawal_amount>account_balance:
        print("Insufficient balance")
    elif withdrawal_amount>10000:
        print("you get money only for Rs.10000")
    else:
        print("Your pin is valid")
        print("your balance is Rs.",account_balance)
        balance=(account_balance-withdrawal_amount)
        print("withdrawal amount is Rs.",withdrawal_amount)
        print("your current balance is Rs.",balance)

else:
    print("Your pin is wrong")

#4


age = int(input("Enter your age: "))
show_time = input("Enter your show time (Morning or Evening): ")

if show_time=="Morning":
    if age<=5:
        print("Entry is free")
    elif age<=17:
        print("You get child ticket")
        ticket_price = 150-50
        print("Your ticket price is Rs.", ticket_price)
    elif age<59:
        print("You get adult ticket")
        ticket_price = 250 - 50   
        print("Your ticket price is Rs.", ticket_price)
    else:
        print("You get senior citizen ticket with discount")
        ticket_price = 200 - 50  
        print("Your ticket price is Rs.", ticket_price)

elif show_time=="Evening":
    if age<=5:
        print("Entry is free")
    elif age<17:
        print("You get child ticket")
        ticket_price = 150
        print("Your ticket price is Rs.", ticket_price)
    elif age<59:
        print("You get adult ticket")
        ticket_price = 250
        print("Your ticket price is Rs.", ticket_price)
    else:
        print("You get senior citizen ticket")
        ticket_price = 200
        print("Your ticket price is Rs.", ticket_price)

else:
    print("Invalid show time entered.")"""

