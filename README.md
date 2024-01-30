# Star Wars Personality Quiz

This is a "just for fun" beginner level project in Python, which asks a series of questions in order to determine which Star Wars character you are, based on your answers. It can be adapted for different themes by changing the questions, responses, and list of characters.

## How It Works

The quiz contains a predefined list of Star Wars characters along with their traits/personality types.

- It asks the user 5 multiple choice questions.
- Their answers are compared against the traits of each predefined character.
- A scoring system calculates which character's traits most closely match the user's answers.
- The character with the highest score is displayed as the user's match.

## Code Explanation
The main functionality of the program is contained within the `main.py` file. Here's a breakdown of the key components:

### Data Representation
The Star Wars character traits and options are represented using the following data structures:
- personalities: A dictionary mapping character names to lists of traits, representing attributes such as allegiance, species, personality trait, character flaw, and Force sensitivity.
- questions: A list of questions presented to the user during the quiz.
- options: A list of options corresponding to each question to provide the user with multiple choice answers.

### Functions
- ask_question(question, option) - This function presents the user with a question and a set of options to choose from. It then validates and returns the user's input.
- find_best_match(personalities, player_characteristics) - This function matches the user's input with the predefined character traits to determine the best match. The character with the highest matching score is considered the best match.

## Customising the Quiz

To customize the quiz with different characters/questions/traits, modify the lists at the top of the main.py file. The structure is fairly flexible - new questions and options can be added as long as the index positions match up.

## Contributing

Contributions to improve or expand the quiz are welcome! Some ideas:

- Add more characters from Star Wars or other franchises
- Improve the answer matching/scoring algorithm (handling ties, etc)
- Add a user interface
