#defining a simple function
def greet_user():
    print("wellcome on board")
#call the function
greet_user()

#calculating VAT
def calculate_vat(amount):
    vat = amount * 0.15
    return vat

print(f"VAT for R100 is R{round(calculate_vat(100), 2)}")
calculate_vat(100)

def total(*nums):
 return sum(nums)
print(total(1, 2, 3))