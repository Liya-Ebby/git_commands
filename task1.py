'''wap to check whether the given number is prime or not'''

num = int(input("Enter a number : "))

if num == 1:

    print(f"The {num} is not prime")

else:

    for i in range(2,num):

        if num % i == 0 :

            print(f"The {num} is not prime")

            break

    else:

        print(f"The {num} is prime")    

