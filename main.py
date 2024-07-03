import random
AI = random.randint(1,5000)
I = int(input("Enter a Number: "))
if(I==AI):
    print("You Guessed it right")
else:
    if(I>AI):
        print("Lower Number Please")
    else:
        print("Higher Number PLease")
    print(f"AI's choice is: {AI}.\n Your Choice is {I}")
