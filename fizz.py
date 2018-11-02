fizz = 5
buzz = 7

counter = 1
while counter <= 60:
    fizz_num = counter % fizz
    buzz_num = counter % buzz
    if fizz_num == 0:
        print("Fizz")
    elif buzz_num == 0:
        print("Buzz") 
    else: 
        print(counter)
    counter += 1
    