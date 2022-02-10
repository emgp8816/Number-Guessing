import random
a = random.randint(0,9999)
number=str(a)
print(number)

if len(number)==4:
	number=number
elif len(number)==3:
		number='0' + number
elif len(number)==2:
	number='00' + number
elif len(number)==1:
	number='000' + number

print(number)	
# for i in numbers:
# 	digits[i]=numbers[i]
# print(digits)
print("_ _ _ _")