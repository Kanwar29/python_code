n = 18
nog = 9
nol = 0
total = 0
while True:
    print("Guess the number :- ")
    num = int(input())
    nog = nog-1
    total += 1
    print(f"No of Guesses left :{nog}\n")
    if num > n:
        print("Number entered is greater. Guess a lower number\n")
    elif num < n:
        print("Number entered is lower .Guess a higher number\n")
    else:
        print(f"Your guess is right. You took {total} guesses")
        break
    if nog == 0:
        print("Total chances to guess is finished. Game Over")
        break
    else:
        continue