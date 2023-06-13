#This is a program that calculates an employee's gross pay based on number of hours worked 
#deducts employee's income tax from gross pay and gives the net pay

print("EMPLOYEE PAYMENT PORTAL")
title = input("Title: ")
name = input("Please enter your full name: ")
print("Welcome to your payment portal, ",title, name)
try:
    hours = float(input("Service Hours: "))
except:
    print("WARNING!!! Invalid input, numeric only!")
    quit()
rate = float(22.5)
otr = float(0.50) 
print("fixed rate per hour: USD 22.5")
print("Overtime rate per hour: USD 0.50")
if hours < 40:
    print("PAY CLASS: REGULAR")
    pay = hours * rate
else:
    print("PAY CLASS: OVERTIME")
    reg = hours * rate
    otp = (hours - 40.0) * (rate * otr)
    pay = reg + otp
tax = pay // 100 * 15
net_income = float(pay) - float(tax)
print("Gross Wage: USD",pay)
print("Income Tax (15%): USD",tax)
print("Net Wage: USD",net_income)
print("Please contact Accounts Department for any question or clarification.")
print("Thank you for your service, ",title, name)