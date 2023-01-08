import random
Shoot = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if Shoot == "0":
    print( '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif Shoot == "1":
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
else:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
computer = random.randint(0, 2)
if computer == 0:
    print('''
Computer chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    if computer == 0 and Shoot == "0":
        print("it's a Draw.")
    elif computer == 0 and Shoot == "1":
        print("You lose.")
    else:
        print("You win.")
elif computer == 1:
    print('''
Computer chose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    if computer == 1 and Shoot == "0":
        print("You Lose.")
    elif computer == 1 and Shoot == "1":
        print("It's a Draw")
    else:
        print("You Win.")
else:
    print('''
Computer chose:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    if computer == 2 and Shoot == "0":
        print("You Win.")
    elif computer == 2 and Shoot == "1":
        print("You Lose.")
    else:
        print("It's a Draw.")