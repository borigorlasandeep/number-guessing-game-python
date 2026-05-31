import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target (1-100) or type Quit: ")

    if userChoice.lower() == "quit":
        break

    userChoice = int(userChoice)

    if userChoice == target:
        print("🎉 Success: Correct Guess!")
        break
    elif userChoice < target:
        print("📉 Your number was too small. Try a bigger guess...")
    else:
        print("📈 Your number was too big. Try a smaller guess...")

print("------- GAME OVER -------")