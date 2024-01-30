#Star Wars character template: 
# [Name, rebellion/empire, human/alien, personality trait, 
# character flaw, force sensitive y/n]

personalities = {
  "Luke Skywalker": ["A", "A", "A", "A", "A"],
  "Leia Organa": ["A", "A", "B", "B", "A"],
  "Han Solo": ["A", "A", "C", "C", "B"], 
  "Jabba the Hutt": ["B", "B", "D", "D", "B"],
  "Yoda": ["A", "B", "E", "E", "A"], 
  "Darth Vader": ["B", "A", "F", "F", "A"]
}

questions = [
  "\nWhich trait do you value most in a leader?",
  "\nWhere do you find your sense of belonging?",
  "\nWhich is your strongest character trait?",
  "\nWhich is your weakest character trait?", 
  "\nAre you drawn to the mysteries of the universe?"
]

options = [
  "A: Freedom and individual rights \nB: Order and authority", 
  "A: Among familiar life forms \nB: Among diverse life forms", 
  "A: idealist \nB: kind \nC: loyal \nD: ambitious \nE: wise \nF: powerful",
  "A: whiny \nB: stubborn \nC: reckless \nD: greedy \nE: unpredictable \nF: ruthless",
  "A: Yes, I seek to understand the unknown \nB: No, I prefer to focus on the tangible"
]

player_characteristics = []

def ask_question(question, options):
  print(question)
  print(options)
  answer = input("Your answer (A, B, etc): ").upper()
  while answer not in ("A","B","C","D","E","F"):
    print("Please enter the letter only (A, B, etc)")
    answer = input("Your answer (A, B, etc): ").upper()
  return answer

def find_best_match(personalities, player_characteristics):
  best_match = []
  highest_score = 0
  for name, traits in personalities.items():
    score = 0
    for i in range(len(player_characteristics)):
       if traits[i] == player_characteristics[i]:
         score += 1
    if score > highest_score:
      highest_score = score
      best_match = name
  if highest_score > 0: 
    print("\nCongratulations, you are " + best_match + "!")
  else: 
    print("Error! You don't match any of the personalities.")

print("Hello there!")
print("Let's find out which Star Wars character you are!")

for i in range(len(questions)):
  player_characteristics.append(ask_question(questions[i], options[i]))

find_best_match(personalities, player_characteristics)