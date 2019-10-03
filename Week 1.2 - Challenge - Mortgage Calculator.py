#Let's make this thing personal
print("Welcome to the Awesome Mortgage Calculator. To make me work, I will first need to know a few things.")
name=(input("Let's start by telling me what I should call you: "))
print("Nice to meet you", name)
print("I will now need some details of the mortgage you are considering.")

#We get the necessary input.
total=int(input("The total value of the house is: "))
down=int(input("The downpayment is: "))
int_annual=float(input("The annual interest rate in % (e.g. enter 5% as 5) is: "))
freq=int(input("The number of annual payments (e.g. 12 for monthly payments) is: "))
amort=int(input("Amortisation period in years is: "))

#Then convert the annual interest rate into periodic interest rate
intr=int_annual/100/freq

#Then determine the value of the loan
loan=total-down

#Then calculate the total number of payments
num=freq*amort

#Now the monthly payment using formula: periodic payment = loan value*[periodic interest rate(1 + periodic interest rate)^total number of payments]/[(1 + periodic interest rate)^total number of payments - 1]
pay=loan*(intr*(1+intr)**num)/((1+intr)**num-1)

#Now to spit out the answer in a convenient to read formula
print("Thanks", name)
print("Your periodic payments will amount to:")
print("%.2f" % pay)




