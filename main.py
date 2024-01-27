#Simple Personality Quiz by Alaina Jensen
#This can be adapted for different themes

# Star Wars character template: 
# [Name, rebellion/empire, human/alien, personality trait, 
# character flaw, force sensitive y/n]

Personalities = [
  ["Luke Skywalker", "A", "A", "A", "A", "A"],
  ["Leia Organa", "A", "A", "B", "B", "A"],
  ["Han Solo", "A", "A", "C", "C", "B"],
  ["Jabba the Hutt", "B", "B", "D", "D", "B"],
  ["Yoda", "A", "B", "E", "E", "A"],
  ["Darth Vader", "B", "A", "F", "F", "A"]
]

Questions = [
  "\nWhich trait do you value most in a leader?",
  "\nWhere do you find your sense of belonging?",
  "\nWhich is your strongest character trait?",
  "\nWhich is your weakest character trait?", 
  "\nAre you drawn to the mysteries of the universe?"
]

Options = [
  "A: Freedom and individual rights \nB: Order and authority", 
  "A: Among familiar life forms \nB: Among diverse life forms", 
  "A: idealist \nB: kind \nC: loyal \nD: ambitious \nE: wise \nF: powerful",
  "A: whiny \nB: stubborn \nC: reckless \nD: greedy \nE: unpredictable \nF: ruthless",
  "A: Yes, I seek to understand the unknown \nB: No, I prefer to focus on the tangible"
]

PlayerCharacteristics = []

def ask_question(question, options):
  print(question)
  print(options)
  answer = input("Your answer (A, B, etc): ").upper()
  while answer not in ("A","B","C","D","E","F"):
    print("Please enter the letter only (A, B, etc)")
    answer = input("Your answer (A, B, etc): ").upper()
  return answer

print("Hello there!")
print("Let's find out which Star Wars character you are!")

for i in range(len(Questions)):
  PlayerCharacteristics.append(ask_question(Questions[i], Options[i]))

best_match = []
highest_score = 0
for Personality in Personalities:
  score = 0
  for i in range(1, len(PlayerCharacteristics)):
     if Personality[i] == PlayerCharacteristics[i-1]:
       score += 1
  if score > highest_score:
    highest_score = score
    best_match = Personality
if highest_score > 0:
  print("\nCongratulations, you are " + best_match[0] + "!")
else: 
  print("Error! You don't match any of the personalities.")