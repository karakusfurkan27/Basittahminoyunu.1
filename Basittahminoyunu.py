import random

print("Welcome to the Simple Guessing Game!")

sayi = random.randint(1, 100)
tahmin_hakki = 5

while True:
    tahmin = int(input("Enter your prediction: "))
    if tahmin == sayi:
        print("Congratulations! You guessed it right.")
        break
    elif tahmin < sayi:
        print("Enter a larger number.")
    else:
        print("Enter a smaller number.")
    
    tahmin_hakki -= 1
    
    if tahmin_hakki == 0:
        print("Your right to guess is over! Correct answer", sayi, "idi.")
        break