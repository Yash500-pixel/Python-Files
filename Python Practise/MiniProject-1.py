#Guess the Number
import random
random_num = random.randint(1,100)
n = int(input("Let's Play Guess the number:"))
if(random_num == n):
    print("You Have guessed the right number")
    print("The correct number is :",random_num)
elif(random_num>n):
    print("You have guessed the number which is smaller than the target number")
    print("The correct number is :",random_num)
elif(random_num<n):
    print("You have guessed the number which is bigger than the target number")
    

    print("The correct number is :",random_num)