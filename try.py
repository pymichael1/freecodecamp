# this a defined function for calculating gross, tax and net pay. the program expects the user to input hour and rate and then does the other computing by itself.
def pay (hour, rate) :
    payroll = float(hour) * float(rate)
    tax = payroll // 100 * 15
    net_pay = payroll - tax 
    print("GrossPay: USD",payroll)
    print("IncomeTax (15%): USD", tax)
    print("NetPay: USD",net_pay)
    
# Below code is meant for user input and then call the pay function to do the math.

hour = input("Hours Worked: ")
rate = input("Rate per hour: ")
pay(hour, rate)

