#A Python program that asks the user to enter the following data:

#An initial stock level for a product
#The number of month(s) to plan
#The planned sales quantity for each month
#Based on this data, calculate the required production quantity as follows:

#If the sales quantity is smaller than the stock level of the previous month, the production quantity is 0
#If the sales quantity is larger than the stock level of the previous month, the production quantity is this difference

initial_stock_level = int(input("Please enter an initial stock level: "))
month_number = int(input("Please enter the number of month to plan: "))

list_production = []
list_month = []
list_quantity = []
production_quantity = 500
need_production = 0


for element in range(month_number):
    planned_sales_quantity = int(input("Please enter the planned sales quantity: "))
    
    list_quantity.append(planned_sales_quantity)
    list_month.append(element+1)
    
    production_quantity = abs(production_quantity) - planned_sales_quantity
    
    if production_quantity < 0:
        need_production = abs(production_quantity)
        production_quantity = 0
    else:
        need_production = 0

    list_production.append(need_production)
    
    
print("The resulting production quantities are:")
for element in (list_month):
    text = ("Production quantity month " + str(element) + "-" + str(list_production[element-1])) 
    print(text)
    