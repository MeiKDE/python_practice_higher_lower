# Follower Comparison Game

Welcome to the Follower Comparison Game! This interactive game challenges players to guess which of two public figures has more followers based on their social media presence.

## Features

- **Random Record Selection**: Each round presents two public figures, ensuring no duplicates.
- **User Interaction**: Players guess which figure has more followers, receiving immediate feedback on their choices.
- **Score Tracking**: The game keeps track of the player's score throughout the rounds.

## How It Works

1. **Data Format**: The game utilizes a dataset containing public figures, including their names, descriptions, countries, and follower counts.
2. **Game Logic**:
   - Players are prompted to guess whether figure A or figure B has more followers.
   - The game ensures that the same figure is not presented twice in a single round.
   - The current score is updated based on the player's guesses.
3. **Game Loop**: The game runs continuously until the player makes an incorrect guess or provides invalid input.

## Code Overview

- **Functions**:
  - `get_record(data)`: Randomly selects a record from the dataset.
  - `avoid_same_record(record_a, record_b)`: Checks for duplicate records and retrieves a new record if necessary.

- **Main Loop**: The game operates within a `while` loop, presenting figures and capturing user input.

## Dependencies

- `art`: For displaying the game logo and visual elements.
- `random`: For selecting random figures from the dataset.

