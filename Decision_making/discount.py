#In the below example, discount is calculated on the input amount. Rate of discount is 5%,
#if the amount is less than 1000, and 10% if it is above 10000. When the above code is
#executed, it produces the following result
input_amount = int(input("Enter the amount you shopped for: "))
if input_amount < 1000:
	discount = input_amount*0.05
	pay_amount = input_amount - discount
	print(f"You have shopped for {input_amount} but have to pay {pay_amount} since you got a discount of {discount}")
else:
	discount = input_amount*0.1
	pay_amount = input_amount - discount
	print(f"You have shopped for {input_amount} but have to pay {pay_amount} since you got a discount of {discount}")