
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇
import random
choice=[rock,paper,scissors]
choicep=['rock','paper','scissors']
your_choice=int(input("What do you choose?Type 0 for Rock,1 for Paper or 2 for Scissors\n "))
comp_out=random.randint(0,2)

win="You win"
lose="You lose"
tied="You tied"
if your_choice < 3 and your_choice>=0:
  print("You chose "+choicep[your_choice])
  print(choice[your_choice])
  print("Computer chose: "+choicep[comp_out])
  print(choice[comp_out])

  if your_choice==comp_out:
    print(tied)
  elif your_choice==0 and comp_out==2:
    print(win)
  elif your_choice==2 and comp_out==0:
    print(lose)
  elif your_choice<comp_out:
    print(lose)
  elif your_choice>comp_out:
    print(win)
else:
  print("Invaid entry!!!Computer wins by default")


