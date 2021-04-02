# coding: utf-8

import csv
from pathlib import Path

"""Part 1: Automate the Calculations for the loan portfolio summaries.

Starts with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# 1. Show number of loans the list.
number_of_loans = len(loan_costs)
print("There are", number_of_loans, "loans in the portfolio.")

# 2. Show the total of all loans.
total_of_all_loans = sum(loan_costs)
print(f"The total of all loans is ${total_of_all_loans: .2f}.")

# 3. Show the average loan amount from the list.
average_loan_amount = total_of_all_loans / number_of_loans
print(f"The average loan amount is ${average_loan_amount: .2f}.")

"""Part 2: Analyze Loan Data to determine the investment evaluation.

1. Extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.
2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement to decide if the present value represents the loan's fair value and print the conclusions.
"""

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# 1. Show the future value and reminaing months on the loan.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"Future value of the loan is ${future_value: .2f}.")
print("Remaining months on the loan is ",remaining_months,".")


# 2. Use a minimum required return of 20% as the discount rate to determine the fair value of the loan.
annual_discount_rate = 0.2
# To be DRY, do the first part of Part 3 here:
def fair_value(future_value, remaining_months, annual_discount_rate):
    """ Part 3.1. Define a function to calculate present value.
    
    Args:
        future_value(int): The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
        remaining_months(int): The remaining maturity (in months) before the loan needs to be fully repaid.
        annual_discount_rate(float): annual cost of capital
    
    Returns:
        fair_value(float): the present value of the loan
    """
    fair_value = future_value / (1+annual_discount_rate/12)**remaining_months
    return fair_value
present_value = fair_value(future_value,remaining_months,annual_discount_rate)
print(f"Present value of the loan is $ {present_value: .2f}.")

# 3. Determine if the loan is worth the cost.
if present_value > loan.get("loan_price"):
    print("The loan is at least worth the cost.")
elif present_value < loan.get("loan_price"):
    print("The loan is not worth the cost.")
else:
    print("The loan is at the cost.")


"""Part 3: Perform Financial Calculations.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# 2. calculate the present value of the new loan using the annual discount rate of 0.2
annual_discount_rate = 0.2
present_value = fair_value(new_loan["future_value"], new_loan["remaining_months"],annual_discount_rate)
print(f"The present value of the new loan is ${present_value: .2f}.")


"""Part 4: Conditionally filter lists of loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to filter loans priced at or below 500 to be included in "inexpensive_loans".
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# 1. Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# 2. Filter the loan portfolio for all the loans that cost $500 or less to the `inexpensive_loans` list
for item in loans:
    loan_price = item.get("loan_price")
    if loan_price <= 500:
        inexpensive_loans.append(item)

# 3. Print the `inexpensive_loans` list
print(inexpensive_loans)


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# 1.a. Create a `csv.writer` using the csv library 
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # b. write the header row
    csvwriter.writerow(header)
    # c. write each row of `loan.values()` from the `inexpensive_loans` list to the csv file.
    for row in inexpensive_loans:
        csvwriter.writerow(row.values()) 



