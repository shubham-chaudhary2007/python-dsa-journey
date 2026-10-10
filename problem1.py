#Take input of the price of 3 products and calculate the total bill, average price, and total after adding 18% GST



produc_1=input("Enter product price 1:-")

produc_2=input("Enter product price 2:-")

produc_3=input("Enter product price 3:-")


Total = float(produc_1)+float(produc_2)+float(produc_3)

print("Total Amount:-",Total)


Average_price= float(Total)/3

print("Average bill:-", Average_price)


Gst=Total*18/100

Total_Amount= Total+Gst


print("Total Amount to pay", str(Total_Amount) + ".rs"+" ( With 18% GST)")
