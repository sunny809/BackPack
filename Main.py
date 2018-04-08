import Main
from Player import Player

# backpack issue

class Main:
    def __init__(self):
        print("init")

        # random data


        print(self.playerList)

    def get_data(self):
        player1 = Player(1, 'yaochen', 8, 7);
        player2 = Player(2, 'xiaolin', 9, 5);
        player3 = Player(3, 'haoyang', 6, 7);
        player4 = Player(4, 'jiahao', 7, 8);
        player5 = Player(5, 'chengkun', 11, 10);
        player6 = Player(6, 'ziye', 7, 11);
        self.playerList = [player1, player2, player3, player4, player5, player6];

    def process(self):
        print("process")


if __name__ == "__main__":
    main = Main()
    main.process()

# https://www.cnblogs.com/William-xh/p/7305877.html