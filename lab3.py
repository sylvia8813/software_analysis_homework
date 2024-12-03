class Player:
    def __init__(self, name, position, number):
        """
        初始化 Player 類別的屬性
        :param name: 玩家名稱
        :param position: 玩家位置
        :param number: 球衣號碼
        """
        self.name = name
        self.position = position
        self.number = number


class Team:
    def __init__(self, name):
        """
        初始化 Team 類別的屬性
        :param name: 球隊名稱
        """
        self.name = name
        self.players = []  # 用來存放 Player 實例的清單

    def add_player(self, player):
        """
        將 Player 實例加入球隊
        :param player: Player 實例
        """
        self.players.append(player)

    def get_player_info(self, number):
        """
        根據球衣號碼尋找玩家資訊
        :param number: 球衣號碼
        :return: 格式化後的玩家資訊或 "Player not found."
        """
        for player in self.players:
            if player.number == number:
                return f"{player.name} ({player.position}) - {player.number}"
        return "Player not found."


# 測試程式碼
player1 = Player("Chen Jie-Xian", "Outfielders", 24)
player2 = Player("Lin Yu-Min", "Pitchers", 45)
player3 = Player("Lin Chia-Cheng", "Catchers", 27)

team1 = Team("Team Taiwan")
team1.add_player(player1)
team1.add_player(player2)

print(team1.get_player_info(24))  # 輸出: "Chen Jie-Xian (Outfielders) - 24"
print(team1.get_player_info(45))  # 輸出: "Lin Yu-Min (Pitchers) - 45"
print(team1.get_player_info(27))  # 輸出: "Player not found."
