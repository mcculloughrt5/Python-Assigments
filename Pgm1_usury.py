# Richard McCullough
# Program that will compute monthly payment amount, total amount paid, and total interest rate paid for loan.


def main():

    # Ask  user for initial loan amount, months on the loan, and interest rate on the loan
    principal = float(input("How much is the initial loan amount?: "))
    months = int(input("How many months of the loan?: "))
    interest = float(input("What is the interest rate?: "))
    rate = interest / 1200

# Compute monthly payment for the loan, total amount paid and total interest paid
    monthly_payment = (principal * rate) / (1 - ((1 + rate) ** -months))
    total_amt = monthly_payment * months
    total_rate = total_amt - principal

# Print the Result
    print("The principal/loan Amount is: $", principal)
    print("The number of months on the loan", months)
    print("The interest rate on the loan:", interest, "%")
    print("The monthly payment is: $", monthly_payment)
    print("The total amount paid: $", total_amt)
    print("The total interest paid: $", total_rate)


main()
