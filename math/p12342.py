from math import ceil

num_cases = int(input())
for i in range(num_cases):
  money = int(input())
  taxable = money - 180000

  tax = 0
  if taxable > 0:
    if taxable >= 300000:
      tax += 30000
      taxable -= 300000
      if taxable >= 400000:
        tax += 60000
        taxable -= 400000
        if taxable >= 300000:
          tax += 60000 
          taxable -= 300000
          if taxable > 0:
            tax += 0.25*taxable
        else:
          tax += 0.2*taxable
      else:
        tax += 0.15*taxable
    else:
      tax += 0.1*taxable

    tax = int(ceil(tax))
    tax = max(tax, 2000)
  print("Case {}: {}".format(i+1, tax))
