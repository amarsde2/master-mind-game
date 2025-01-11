## Master Mind Game
## This is a Master mind game implementation in which user has to guess 4 digits of a number.

##  Author Details 

## Name  :  Er. Amar kumar 
## Email :  amarkumar9685079691@gmail.com 

## Start of a Game ##

import random 

class MasterMindGame: 
    
    _number = 0
    _guess_number = 0
    _attempts = 0

    # function to reset game state on lose or win
    def _resetGameState(self):
        self._guess_number = 0
        self._number = random.randint(1000, 10000)

    # function to show game starting status 
    def _showStartMessage(self):

        print("Hi, You're welcome to play Master Mind Game! ")
        print("Guess a secret 4 digit number... ")
        print()
        print("Best of luck! ")

    def _guessNumberFun(self):
        self._guess_number = int(input("Enter 4 digit number: "))

        while self._guess_number < 999 or self._guess_number > 10000:
            self._guess_number = int(input("Please a enter 4 digit number: "))

    def _winnerMessage(self):
            print("\nConfiguration!")
            print(f"Great you are mastermind you have guessed number in {self._attempts} attempt ")
            should_play = int(input("Do you want to play again? Type 1 for play or 2 for exit "))
            
            if should_play == 1:
               self.play()
            else:
               print("See, You again!")
               exit(0)

    # logic for playing game
    def play(self):

        self._resetGameState()
        self._showStartMessage()
       
        try:
            self._guessNumberFun()
            if self._number == self._guess_number:
                self._winnerMessage()
            else:
                while self._number != self._guess_number:
                    self._attempts += 1

                    correct = 0
                    correct_digit = ['x'] * 4
                    numstr = str(self._number)
                    guess_num_str = str(self._guess_number)
                
                    for i in range(4):
                        if numstr[i] == guess_num_str[i]:
                           correct += 1
                           correct_digit[i] = numstr[i] 
                        else:
                            continue 

                    
                    if correct > 0 and correct < 4:
                        print(f"Not quite! but you have guess {correct} correct digits of number")
                        
                        for x in correct_digit:
                            print(x, end =" ")
                    else:
                        print("None of your guessed digit match the number")

                    print("Please guess next correct number")
                    self._guessNumberFun()

            self._winnerMessage()
        
        except KeyboardInterrupt:
           print()
           print("Bye, see you again !")
           exit()

if __name__ == '__main__':
    game = MasterMindGame()
    game.play()
## End of a Game ## 