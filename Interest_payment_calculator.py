#collect the nessecary input: principal, apr, years
#calculate the monthly payment and show it to the user
def main():
    print("this is the monthly payment loan calculator")
    print("")
    principal=float(input("Enter the loan amount : "))
    apr=float(input("Enter the annual intrest rate : "))
    years= int(input("Enter the amount of years : "))
    monthly_intrest_rate=apr/1200
    months=years*12
    monthly_payment=principal*monthly_intrest_rate  / (1-(1+monthly_intrest_rate)**(-months))

    print("The monthly payment for {} is : {:.2f}".format(principal,monthly_payment))
main()


