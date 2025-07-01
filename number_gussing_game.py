import random
a=random.randint(1,50)
c=0
# for i in range (1,6):
while c<5:
    try:
        b=int(input("Guess the number from 1-50 : "))
        if(b<1 or b>50):
            raise ValueError
    except ValueError:
        print('Plz guess the no. from 1-50.')
    else:
        c+=1
        if(b==a):
            print(f"You got it in {c} tries!")
            break
        elif(b>a):
            print('Your guess is high')
        else:
            print('Your guess is low')
        if(c==5):
            print(f'Better luck next time, (the no. is {a})')