# game rock_paper_scissor-TAMRIN 4-2
import random

list = ['rock', 'paper', 'scissor']
computer = list[random.randint(0, 2)]
print(computer)
user = input("((what is your choic ? rock   paper  scissor ))-------->")
if computer == 'rock' and user == 'scissor':
    print("computer is win")
elif computer == 'paper' and user == 'rock':
    print("computer is win")
elif computer == 'scissor' and user == 'paper':
    print("computer is win")
else: #سوالم اینجاست زمانیکه کامپیوتر سنگ می دهد و ما هم سنگ میاوریم چزا برنامه اجرا نمی شود از کجا تشخصیص داد مگر else به غیر از بالایی هر چی بزنیم اجرا نمی شود اینجا مقداری در فهم مشکل دارم
    print("user is win")
if computer == 'rock':
    print("computer :")
    print("""

        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)

            """)
elif computer == 'paper':
    print("computer :")
    print(""""


        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)



            """)
elif computer == 'scissor':
    print("computer :")
    print("""


         _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
            """)
if user == 'rock':
        print("user :")
        print("""

            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)

                """)
elif user == 'paper':
        print("user :")
        print(""""


            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)



                """)
elif user == 'scissor':
        print("computer :")
        print("""


             _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
                """)