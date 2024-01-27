# Star Wars Personality Quiz

This is a "just for fun" beginner level project in Python, which asks a series of questions in order to determine which Star Wars character you are, based on your answers. It can be adapted for different themes by changing the questions, responses, and list of characters.

## How It Works

The quiz contains a predefined list of Star Wars characters along with their traits/personality types.

- It asks the user 5 multiple choice questions.
- Their answers are compared against the traits of each predefined character.
- A scoring system calculates which character's traits most closely match the user's answers.
- The character with the highest score is displayed as the user's match.

## Code Overview

### Lists
- Personalities - A 2D list containing the character name, Rebellion/Empire alignment, human/alien species, main personality trait, main flaw, and force sensitivity of each character
- Questions - A list of personality quiz questions to ask the user
- Options - A list of multiple choice answers for each question, with answers corresponding with a different character
- PlayerCharacteristics - A list to store the players's answers

### Functions
- AskQuestion() - Function to prompt user with a question and input options
- FindBestMatch() - Function to score user answers against each character and return best match

## Customising the Quiz

To customize the quiz with different characters/questions/traits, modify the lists at the top of the main.py file. The structure is fairly flexible - new questions and options can be added as long as the index positions match up.

## Contributing

Contributions to improve or expand the quiz are welcome! Some ideas:

- Add more characters from Star Wars or other franchises
- Improve the answer matching/scoring algorithm (handling ties, etc)
- Add a user interface

## License

This project is open source and available under the MIT License. Let me know if you would like any changes or have additional sections to add!
