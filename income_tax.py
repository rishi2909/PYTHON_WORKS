class CalTax:
    income = int(input("Enter your income:"))
    def op_income(self,income):
        if income>=0 and income<=250000:
            Tax = income*0
            print(f"Tax of {income} is {Tax}")
        elif income>250000 and income<=500000:
            Tax = income*0.05
            print(f"Tax of {income} is {Tax}")
        elif income>500000 and income<=750000:
            Tax = income*0.1
            print(f"Tax of {income} is {Tax}")
        elif income>750000 and income<=1000000:
            Tax = income*0.15
            print(f"Tax of {income} is {Tax}")
        elif income>1000000 and income<=1500000:
            Tax = income*0.2
            print(f"Tax of {income} is {Tax}")
        elif income>1500000:
            Tax = income*0.25
            print(f"Tax of {income} is {Tax}")
        else:
            print("Invalid Income")
    
object1 = CalTax()
print(object1)
print(object1.op_income(object1.income))