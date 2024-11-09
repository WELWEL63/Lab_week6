def net_annual_income(gross_salary):
    # Determine the tax rate based on the salary brackets
    if gross_salary >= 45000:
        tax_rate = 0.50  # 50% tax rate for salaries of £45,000 or more
    elif gross_salary >= 30000:
        tax_rate = 0.30  # 30% tax rate for salaries between £30,000 and £44,999
    else:
        tax_rate = 0.15  # 15% tax rate for salaries less than £30,000
    
    # Calculate the net salary after tax
    net_salary = gross_salary * (1 - tax_rate)
    return net_salary

# Test the function with the provided gross income values
test_values = [60000, 30000, 30000, 21000, 20000, 17000,100000]

# Output the results for each gross income
for gross_income in test_values:
    net_income = net_annual_income(gross_income)
    print(f"Gross income: £{gross_income} --> Net income: £{net_income:.2f}")

        




