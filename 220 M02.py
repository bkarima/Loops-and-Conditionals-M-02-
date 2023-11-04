#4.1
secret = 1
guess = 2
if guess < secret:
    print ('too low')
elif guess > secret:
    print ('too high')
elif guess == secret:
    print ('just right')

 #4.2
small = True
green = False

if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")

  #6.1
numberList = [3, 2, 1, 0]
for number in numberList:
    print(number)


  #6.2
guess_me = 7
number = 1
while number > 0:
    if number < guess_me:
        print ('too low')
    elif number == guess_me:
        print ('found it!')
        break
    elif number > guess_me:
        print ('oops')
        break
    number += 1

   #6.3
guess_me = 5
for number in range (10):
    if number < guess_me:
        print ('too low')
    elif number == guess_me:
        print ('found it!')
        break
    elif number > guess_me:
        print ('oops')
        break
    number += 1            