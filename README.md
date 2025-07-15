Python assignment #3
Hangman.py code to include the following:
Adding level of easiness
The game allows for 8 trails (eight lives) before the user loses the game. Also, there is only one set of secret words (animal :ant baboon badger bat bear beaver camel cat clam cobra) from which the code randomly selects one. It is requested to add three more sets of secret words:
Shapes: square triangle rectangle circle ellipse rhombus trapezoid Place: Cairo London Paris Baghdad Istanbul Riyadh
You should advance the game by allowing the user to select from three levels: Easy, Moderate, and Hard.
Easy: the user will be given a chance to select the set from which the random word will be chosen (Animal, Shap, Place). This will make it easier to guess the secret word. .
Moderate: similar to Easy, the user will be given a chance to select the set from which the random word will be selected (Animal, Plant, Place), but the number of trail will be reduced to 6. The last two graphics will not be used or displayed
Hard: The code will randomly select a set and randomly select a word from this set. The uses will have no clue about the secret word. Also, the number of trails will remain at 6.


Adding tracking of winners and records
Adding a database, using QSlite, to track the highest record (number of remaining life) for each level. The database will keep the following items: Player Name (to be provided by the user), Level (Easy, Moderate, Hard), Remaining lives. The winner's name and remaining lives will be updated once a new record ( guessing the secret word with the highest number of remaining lives ) is achieved.

HALL OF FAME
Level
Winner name
Remaining lives
Easy
John
6
Moderate
Nancy
5
Hard
Ahmed
3


Menus
Introductory menu: When running the code the user will be asked to provide his name. Then an introductory menu appears from which the user can select the level of challenge, explore the list of winners, and read instructions about the game. This menu will also appear at the end of the game if the user selects to play again.


Hi “player name”.
Welcome to HANGMAN
PLAY THE GAME
Easy level 1	Moderate level 2	Hard level  3
Hall of fame	4
About the game 5


Sets of secret words: If the user choses to play either Esay or Hard level, a menu will appear from which the user can select the set of secret words


About the game: This menu includes an explanation/ instruction about the game, the level of challenges, and the hall of fame.


NOTE: The menus should be very well formatted using any table library such as Table
