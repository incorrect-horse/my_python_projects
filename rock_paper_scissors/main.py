import random
import os

class Game:
    def __init__(self):
        self.player_1 = HumanPlayer(0)
        self.player_2 = ComputerPlayer(0)
        self.tied = 0

    def validate_rounds(self):
        greet = '\n--- Rock Paper Scissors Game ---\
                 \nHow many rounds would you like to play? '

        while True:
            try:
                self.rounds = int(input(greet))

                if self.rounds < 1:
                    input('\nno...\ncontinue...')
                    clear_screen()
                    self.rounds = 0
                    return
                elif self.rounds > 99:
                    input('\nseriously, no...\ntoo many rounds, limit is 99\ncontinue...')
                    clear_screen()
                    self.rounds = 0
                    return
                elif self.rounds > 50:
                    print("\nthat's a lot of games,\nbut okay...")
                    return self.rounds
                else:
                    return self.rounds
            except ValueError as e:
                if 'invalid literal for int() with base 10' in str(e):
                    input('\nsorry, input must be a number\ncontinue...')
                    clear_screen()
                    self.rounds = 0
                    return

    def play(self):
        self.game_round = 0
        self.rounds = 0
        while self.rounds == 0:
            self.validate_rounds()

        while self.game_round < self.rounds:
            self.game_round += 1
            self.round()
        
        print(f'\n{self.summary()}')
        return 'Game Over'

    def show_hand(self, hand1, hand2):
        print(f'\nYou: {hand1}  | Computer: {hand2}')

    def round(self):
        if clear_screen_setting == True:
            clear_screen()
        print('\nRound >>', self.game_round)

        self.player_1.play()
        hand1 = self.player_1.turn

        self.player_2.play()
        hand2 = self.player_2.turn

        self.show_hand(hand1, hand2)

        result = self.r_p_s(hand1, hand2)
        if result == 'win':
            self.player_1.score += 1
            print('\nYou won this round!')
        elif result == 'lose':
            self.player_2.score += 1
            print('\nYou lost this round!')
        elif result == 'tie':
            self.tied += 1
            print('\nIt was a tie.')

        if clear_screen_setting == True:
            input('\nPress Enter to continue.')
    
    def r_p_s(self, play1, play2):
        # print('\nr_p_s/function', type(play1), play1)
        while play1 not in ['r', 'p', 's']:
            print('\nloop/you entered:', type(play1), play1)
            play1 = input('\noops, input not valid\ntry again [r/p/s]? ').strip().lower()

        if play1 == play2:
            return 'tie'

        if play1 == 'r' and play2 == 'p':
            if verbose_feedback_setting == True:
                print('\npaper covers rock, player 1 lose / player 2 win')
            return 'lose'
        elif play1 == 'r' and play2 == 's':
            if verbose_feedback_setting == True:
                print('\nrock dulls scissors, player 1 win / player 2 lose')
            return 'win'

        if play1 == 'p' and play2 == 'r':
            if verbose_feedback_setting == True:
                print('\npaper covers rock, player 1 win / player 2 lose')
            return 'win'
        elif play1 == 'p' and play2 == 's':
            if verbose_feedback_setting == True:
                print('\nscissors cut paper, player 1 lose / player 2 win')
            return 'lose'

        if play1 == 's' and play2 == 'r':
            if verbose_feedback_setting == True:
                print('\nrock dulls scissors, player 1 lose / player 2 win')
            return 'lose'
        elif play1 == 's' and play2 == 'p':
            if verbose_feedback_setting == True:
                print('\nscissors cut paper, player 1 win / player 2 lose')
            return 'win'

    def summary(self):
        score1 = self.player_1.score
        score2 = self.player_2.score
        score0 = self.tied

        if clear_screen_setting == True:
            clear_screen()

        print(f'\n[Game Summary] Your points: {score1}  |  '
              f'Computer points: {score2}  |  '
              f'Tied rounds: {score0}')

        if tournament_scoring == False:
            self.player_1.score = 0
            self.player_2.score = 0
            self.tied = 0

        if score1 == score2:
            return 'It was a tie.'
        elif score1 > score2:
            return 'You won.'
        elif score1 < score2:
            return 'Computer won.'

class Player:
    def __init__(self, score):
        self.score = score

    def score(self):
        pass

class HumanPlayer(Player):
    def __init__(self, score):
        super().__init__(score)

    def play(self):
        self.turn = input('\nRock, Paper, or Scissor [r/p/s]? ').strip().lower()

class ComputerPlayer(Player):
    def __init__(self, score):
        super().__init__(score)

    def play(self):
        self.turn = random.choice(['r', 'p', 's'])


def clear_screen():
    os.system("clear")

def settings():
    global clear_screen_setting
    global verbose_feedback_setting
    global tournament_scoring

    try:
        while True:
            settings = ("\n\nWelcome\n\n"
                        f"1) clear screen after every move [{clear_screen_setting}]\n"
                        f"2) provide verbose feedback during game play [{verbose_feedback_setting}]\n"
                        f"3) use tournament scoring [{tournament_scoring}]\n"
                        "\n"
                        "S) SAVE SETTINGS & PLAY\n"
                        ">>  ")
            clear_screen()
            usr_input = input(settings).strip().lower()
            if usr_input == '1':
                if clear_screen_setting == False:
                    clear_screen_setting = True
                elif clear_screen_setting == True:
                    clear_screen_setting = False
                print('clear_screen_setting:', clear_screen_setting)
            elif usr_input == '2':
                if verbose_feedback_setting == False:
                    verbose_feedback_setting = True
                elif verbose_feedback_setting == True:
                    verbose_feedback_setting = False
                print('verbose_feedback_setting:', verbose_feedback_setting)
            elif usr_input == '3':
                if tournament_scoring == False:
                    tournament_scoring = True
                elif tournament_scoring == True:
                    tournament_scoring = False
                print('tournament_scoring:', tournament_scoring)
            elif usr_input == 's':
                break
            else:
                print('\ninput not valid')
            input('\npress enter to continue')
    except KeyboardInterrupt:
        print('\nctrl+c detected, exiting...')
    clear_screen()

def run():
    global clear_screen_setting
    global verbose_feedback_setting
    global tournament_scoring
    clear_screen_setting = False
    verbose_feedback_setting = False
    tournament_scoring = False

    try:
        while True:
            if clear_screen_setting == True or verbose_feedback_setting == True or tournament_scoring == True:
                play_settings = 'CuStOm'
            else:
                play_settings = 'default'

            greet = ("\n\nWelcome\n\n"
                    f"1) Play with {play_settings} settings\n"
                    "2) Customize settings\n"
                    "\n"
                    "X) EXIT\n"
                    ">>  ")

            clear_screen()
            usr_input = input(greet).strip().lower()

            if usr_input == '1':
                print('\ndefault play')
                clear_screen()
                my_game.play()
                input('\npress enter to continue')
            elif usr_input == '2':
                print('\customize settings')
                settings()

            elif usr_input == 'x':
                print('\nThanks for playing!')
                break
            else:
                print('\ncommand not recognized')
    except KeyboardInterrupt:
        print('\nctrl+c detected, exiting...')

if __name__ == '__main__':
    my_game = Game()
    run()

input('\nGoodbye!')
clear_screen()
