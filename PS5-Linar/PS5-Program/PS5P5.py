name=str(input("Enter name: "))
incomeGross=float(input("Enter gross income: "))
dependent=int(input("Enter number of dependents: "))
incomeAdjusted=incomeGross-12000*dependent
incomeTaxRate = 0.2 if incomeAdjusted > 50000 else 0.1
incomeTax=incomeTaxRate*incomeAdjusted
incomeTax=100 if incomeTax<0 else incomeTax
print("Name: ",name,f"  Gross income: {incomeGross:.2f}",f"  Dependents: ",dependent,f"  Adjusted income: {incomeAdjusted:.2f}",f"  Income tax: {incomeTax:.2f}")