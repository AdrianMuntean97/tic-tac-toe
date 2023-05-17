# Tic-Tac-Toe

Tic-Tac-Toe is a Python terminal game, which runs in Code Institute mock terminal on Heroku.

Users can try to beat the computer by filling an entire row, column or diagonal with X before the computer do it with O.

The live link can be found here - https://tic-tac-toe-adrian.herokuapp.com/

![Am i Responsive](https://github.com/AdrianMuntean97/tic-tac-toe/blob/main/media/am-i-responsive.png?raw=true)

## How to Play

Tic-Tac-Toe is based on a pen and paper game.
In this version, the player enters their name and board size.
The player is playing against a computer. The player is playing as X and the computer as O.
The player and computer each take a turn to try and fill a space.
The winner is the one that fills an entire row, column, or diagonal.

## Features

# Existing Features

- The player ability to choose his name

![Player Name](https://github.com/AdrianMuntean97/tic-tac-toe/blob/main/media/player-name.png?raw=true)

- Player ability to choose the board size

![Board Size](https://github.com/AdrianMuntean97/tic-tac-toe/blob/main/media/board-size.png?raw=true)

- Play against the computer
- User choice is colored in green
- Computer making random moves

![Main Game](https://github.com/AdrianMuntean97/tic-tac-toe/blob/main/media/main-game.png?raw=true)

- The player cannot enter the same row and column again
- The input player provided must be valid

![Invalid Input](https://github.com/AdrianMuntean97/tic-tac-toe/blob/main/media/invalid-input.png?raw=true)

- Computer is trying to block the player when it detects the player will win in the next turn

![Computer Block](https://github.com/AdrianMuntean97/tic-tac-toe/blob/main/media/computer-block.png?raw=true)

- Computer is trying to win by detecting if it can win in the next turn

![Computer Win](https://github.com/AdrianMuntean97/tic-tac-toe/blob/main/media/computer-win.png?raw=true)

## Testing

- I have tested the game and it works on all 3 board sizes.
- The computer is making random moves until it detects it can win then is going for the win.
- In the current state there are no known bugs.
- All the features are working as intended.
- I have tested the app on PEP8 Python Validator and no there was no error.

## Bugs

- Old version gave the player the choice to whatever board size he wanted.
The old version could break the game if for example, the user selected a board size like 100x100
making the game impossible to win (fixed by making the board size available between 3x3 to 5x5)

## Deployment

The project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment:
    - Clone this repository
    - Create a new Heroku app
    - Set the buildpacks to Python and NodeJS in that order
    - Link the Heroku app to the repository
    - Click on Deploy

## Credits

- Code Institute for the deployment terminal

   

