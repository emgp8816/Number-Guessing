#Number Guessing
import random
a = random.randint(0,9999)
number=str(a)
def coincidences(user_number, number):
    cont_num=0;
    cont_pos=0;
    
    #Positions
    for i in range(0,len(user_number)):
        for j in range(0,len(number)):
            if user_number[i] == number[j] and j==i:
                    cont_pos+=1;
    
    #Digits
    for i in range(0,len(user_number)):
        for j in range(0,len(number)):
            if user_number[i] == number[j]:
                user_number = user_number.replace(user_number[i],'-')
                number = number.replace(number[j],'o')
                cont_num+=1;
                break
                
    
    if cont_pos==4:
        print('Congrants, u win:)')
    else:
        print('Correct digits:',cont_num)
        print('Correct positions:',cont_pos)
    
            

if len(number)==4:
    number=number
elif len(number)==3:
    number='0' + number
elif len(number)==2:
    number='00' + number
elif len(number)==1:
    number='000' + number

print(number)
user_number=''

while user_number !=number:
    user_number = str(input("Introduce a possible number: "))
    
    if len(user_number )==4:
        user_number =user_number 
    elif len(user_number )==3:
        user_number='0' + user_number 
    elif len(number)==2:
        user_number ='00' + user_number 
    elif len(number)==1:
        user_number ='000' + user_number
    
    coincidences(user_number, number)
    a=user_number
    #user_number= number
