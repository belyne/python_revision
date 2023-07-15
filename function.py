bill = 175.00

tax_rate = 15

total_tax = (bill * tax_rate) / 100.00

print("Total tax :", total_tax)


def calculate_tax(bill2, tax_rate2):
    return (bill2 * tax_rate2) / 100.00
print("Total tax:", calculate_tax(100, 12))
print("Total tax:", calculate_tax(156.89, 2))
print("Total tax:", calculate_tax(100.57, 42))
print("Total tax:", calculate_tax(123.50, 20))
