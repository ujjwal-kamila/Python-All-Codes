# Day-39 Exercise-3 KBC Game Solution in Python

# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game
# Create a lit data type to store questions and their correct answers
# Display the final amount the persn is taking home after playing the game


print(" Welcome to KBC Game 🙏️🙏️ 🎮️  👉️👉️👉️👉️ Created By Ujjwal Kamila 😎️ ")

Questions = [
    "Light Year is a unit of (A)Time (B)Speed (C)Distance (D)Acceleration",
    "Which Planet in our Solar System is the hottest: (A)Mercury (B) Earth (C)Venus (D)Mars",
    "Which of the following is the second Brightest star as viewed from Earth: (A)Sun (B)Siruis A (C)Sirius B (D)Vega",
    "Which Chemical Element has the notation Ir :(A)Iron (B)Irinanium (C)Iridium (D)Irvinium",
    "How Far is the Moon on average: (A)732000 (B)834000 (C)295000 (D)384000",
    "Which of the Following element has the symbol Rh:(A)Rhenium (B)Rhodium (C)Ruthernium (D)Ruthefordium",
    "Due to Which Force does a Magnetic Duster not fall of a Magnetic Board: (A)Frictional Force (B)Magnetic Force (C)Gravitational Force (D)Normal Force",
    "Which of the folllowing is true about Quantum Mechanics: (A)Linear Theory (B)Non Linear Theory (C)Not Veirifed (D)Non Probablistic",
    "Barry's Point is also known as the: (A)Center of Mass (B)Center Of gravity (C)Center of Torque (D)Center of Physical State",
    "Which of the following theory is still correct: (A)Maxwell's Theory (B)Newton's Theory (C)Plato's Theory (D)Bohr's Theory",
    "Who predicted the existence of White Holes:(A)Stephen Hawkings (B)Einstien (C)Newton (D)Schrodinger",
    "Who Proposed that the universe is Expanding:(A)Einstien (B)Newton (C) MaxWell (D)Hubble",
    "Which of the following is Radioactive: (A)Rhodium (B)Radon (C)Arsenic (D)Titanium",
    "Due to which discovery Einsien win the Nobel Prize: (A)Special Relativity (B)general Relativity (C)Photoelectric Effect (D)Quantum Mechanics",
    "Moon is formed due to the collision of the Earth with :(A)Bennu (B)Asteroid C-57723 (C)Phobos (D)Demos",
    "Why are you not Out yet: (A)Cheating (B)Very high IQ (C)Random Geuss (D)Dont Know"
]

# Sample answers of all Questions 
Answers = [
    "C", "C", "C", "C", "D", "B", "A", "A", "B", "A", "B", "D", "B", "C", "A",
    "C"
]


def KBC(Questions, Answers):
  a = 16
  money = 0
  print(" " * 30, "KBC")
  for i in range(a):
    print(Questions[i])
    Answer = input("What is the Answer  the clock is ticking:")



    if (Answer == Answers[i]):
      if (i != 15):
        money = money + i * i * 70000
        print("The Answer is Correct")
        print("You are currently standing at", money, "rupees")
        continue
      elif (i == 15):
        print("Congratulations! You have won the KBC and you win", money,
              "rupees!")
        break


    elif (Answer != Answers[i]):
      print("The Answer is incorrect")
      print("the correct answer is ", Answers[i])
      print("You have won", money, "rupees Congratulations!")
      print(
          "To get your Money, Your age must be above 80 and below 20 at the same time without using time Dilation! :)"
      )
      break


KBC(Questions, Answers)
again = input(
    "Thank You for playing this Game! if you want to play again Press 'P'! else press 'N':"
)

if (again == "P"):
  KBC(Questions, Answers)
elif (again == "N"):
  print("Thank You for devoting your time!")

#sample solution of kbc game by tutorial 

# questions = [
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
# ]

# levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
# money = 0
# for i in range(0, len(questions)):
  
#   question = questions[i]
#   print(f"\n\nQuestion for Rs. {levels[i]}")
#   print(f"a. {question[1]}          b. {question[2]} ")
#   print(f"c. {question[3]}          d. {question[4]} ")
#   reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
#   if (reply == 0):
#     money = levels[i-1]
#     break
#   if(reply == question[-1]):
#     print(f"Correct answer, you have won Rs. {levels[i]}")
#     if(i == 4):
#       money = 10000
#     elif(i == 9):
#       money = 320000
#     elif(i == 14):
#       money = 10000000
#   else:
#     print("Wrong answer!")
#     break 

# print(f"Your take home money is {money}")
