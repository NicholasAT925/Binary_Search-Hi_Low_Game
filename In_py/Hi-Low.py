from asyncio.windows_events import NULL


Hi = 1000
Low = 1
NumOfGuess = 10
guess = NULL

print(f"Enter a number between {Low} and {Hi}")
num = input("Enter Number: ")
print("The computer will guess a number and you have to tell it to go Higher or Lower to guess correctly")
print("The computer is given 10 tries to guess your inputed number")
print("Input 'Correct' if the computer guessed right, 'H' to go higher and 'L' to go lower")

while True:
    guess = Low + (Hi -Low)//2
    Response = input(f"My guess is {guess}, is it correct or should i go Higher or Lower?".casefold())
    if NumOfGuess == 0:
        print("I have ran out of guesses, I guess you win")
        break
    elif Response == "h":
        # guess higher
        --NumOfGuess
        Low = guess + 1
    elif Response == "l":
        # guess lower
        --NumOfGuess
        Hi = guess - 1
    elif Response == "correct":
        NumOfGuess = 0
        print("Yay")
        break 
    else:
        print("Wrong Responce, input a new Responce")
        continue