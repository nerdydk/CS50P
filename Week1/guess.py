def get_guess():
    guess = int(input("Enter ur guess : "))
    return guess

def main():
    guess = (get_guess())
    if guess == 50:
        print("Wohoooo, Its Correct !")
    else:
        print("Nah, Its wrong")

main()
