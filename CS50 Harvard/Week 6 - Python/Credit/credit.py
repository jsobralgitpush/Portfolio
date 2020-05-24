import cs50
import sys

#1-Checking the validation of the card

#a) Asks for user input
card_number = cs50.get_int("Number: ")

#b) Counters
j = 1
i = 2
sum_by_two = 0
sum_by_one = 0
answer = ''


#c) Checking the sum of the number from card
while i <= len(str(card_number)):
    number_sum = int(str(card_number)[-i])*2
    
    for k in range(len(str(number_sum))):
        sum_by_two = sum_by_two + int(str(number_sum)[k]) 
        
    i+=2

while j <= len(str(card_number)):
    number_sum = int(str(card_number)[-j])
    
    for k in range(len(str(number_sum))):
        sum_by_one = sum_by_one + int(str(number_sum)[k]) 
        
    j+=2

validation = sum_by_two + sum_by_one

#d) Checking if the card is valid
if validation % 10 != 0:
    print('INVALID')
    exit(0)

    
#2-Checking the flag of the card
n_to_string = str(card_number)

#a) Mastercard
if int(n_to_string[0]) == 5 and int(n_to_string[1]) in [1,2,3,4,5] and len(n_to_string) == 16:
    print("MASTERCARD")
    exit(1)
elif int(n_to_string[0]) == 4 and len(n_to_string) in [13,16]:
    print("VISA")
    exit(1)
elif int(n_to_string[0]) == 3 and int(n_to_string[1]) in [4,7]:
    print("AMEX")
    exit(1)
