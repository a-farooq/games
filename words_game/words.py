
class WordsGame:
    wordsList = []

    def __init__(self):
        pass

    def is_unique(self, word):
        if word in self.wordsList:
            return False
        self.wordsList.append(word)
        return True

    def print_list(self):
        print(self.wordsList)


class Player:
    def __init__(self, name=None):
        self.name = name
        self.wordList = []

    def get_name(self):
        return self.name

    def add_word(self, word):
        self.wordList.append(word)


def main():
    game = WordsGame()
    num = int(input("Input number of players: "))

    playersList = []

    for i in range(num):
        name = input("Input player name: ")
        pl = Player(name)
        playersList.append(pl)

    for player in playersList:
        print("My name is %s" % player.get_name())

    for i in range(2):
        for player in playersList:
            word = input("Input your word: ")
            while not game.is_unique(word):
                word = input("Input your word again: ")

            player.add_word(word)

    game.print_list()


if __name__ == '__main__':
    main()
