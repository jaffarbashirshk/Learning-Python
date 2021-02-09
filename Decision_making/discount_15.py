# example programon if elif 
input_amount = int(input("Enter the amount you shopped for: "))
if input_amount < 1000:
	discount = input_amount*0.05
	pay_amount = input_amount - discount
	print(f"You have shopped for {input_amount} but have to pay {pay_amount} since you got a discount of {discount}")
elif input_amount < 10000:
	discount = input_amount*0.1
	pay_amount = input_amount - discount
	print(f"You have shopped for {input_amount} but have to pay {pay_amount} since you got a discount of {discount}")
else:
	discount = input_amount*0.15
	pay_amount = input_amount - discount
	print(f"You have shopped for {input_amount} but have to pay {pay_amount} since you got a discount of {discount}")
