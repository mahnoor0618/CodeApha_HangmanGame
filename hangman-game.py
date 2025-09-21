import random
words_1=["laptop","program","python","jupiter","compiler","liabraries","comment","iteration","logic",""]
words_2=["chowmein","chilli","cheese","ketchup","biryani","zinger","fries"]
words_3=["cricket","padel","over","review","goal","keeper","squad","wicket"]
words_4=["projectile","derivation","gravity","capacitor","equilibrium","torque","force","vector"]
words_5=["derivative","limit","integration","function","sequence","series","sets","Hyperbola"]


print("From which category do you want to guess the word?\n\nTHE CATEGORIES ARE:\n1.Programming\n2.Food\n3.Sports\n4.Physics\n5.Mathematics")
Choice=int(input("Enter category number: "))
if Choice == 1:
    word=random.choice(words_1)
elif Choice == 2:
    word=random.choice(words_2)
elif Choice == 3:
    word=random.choice(words_3)
elif Choice == 4:
    word=random.choice(words_4)
elif Choice == 5:
    word=random.choice(words_5)
else:
    print("Invalid choice!\n\n")


len=len(word)
list=[]
for letter in word:
    list.append(letter)
    continue
print("\nSTART guessing the word!\n\nYou have only 6 chances of wrong guesses.")
blanks=["_"]*len 
print("secret word:"+" ".join(blanks))
wrong_guess=0
while wrong_guess < 6 and "".join(blanks) != word:
    if wrong_guess==5:
        print("\nLAST CHANCE!")
    guess=str(input("\nGuess 1 character:\n")).lower()
    found=False
    for index,letter in enumerate(word):
        if letter == guess:
            blanks[index]=guess
            found=True
            continue
    if found:        
        print("\nupdated secret word:"+"".join(blanks))
    else:
        wrong_guess+=1
        print(f"Wrong guess! Chances left: {6 - wrong_guess}")

    
if ("".join(blanks)) == (word):
    print("\nYou won!\n")
else:
    print("\nYou lose!\n")


