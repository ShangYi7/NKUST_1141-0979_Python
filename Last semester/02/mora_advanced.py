# 剪刀石頭布遊戲 - 高階語法版本
# Rock Paper Scissors Game - Advanced Syntax Version

class RockPaperScissors:
    """剪刀石頭布遊戲類別"""

    # 遊戲選項常數
    SCISSORS = 1  # 剪刀
    ROCK = 2      # 石頭
    PAPER = 3     # 布

    # 結果常數
    TIE = "A tie"
    FIRST_WINS = "The first man wins the game"
    SECOND_WINS = "The second man wins the game"

    def __init__(self):
        """初始化遊戲"""
        self.games = []

    def read_input(self):
        """讀取所有遊戲輸入"""
        print("請輸入 10 組遊戲數據，每組兩個數字（1=剪刀, 2=石頭, 3=布）:")
        for i in range(10):
            try:
                game_input = list(map(int, input().split()))
                if len(game_input) != 2:
                    raise ValueError("每組必須包含兩個數字")
                if not all(1 <= num <= 3 for num in game_input):
                    raise ValueError("數字必須在 1-3 範圍內")
                self.games.append(game_input)
            except ValueError as e:
                print(f"輸入錯誤: {e}")
                return False
        return True

    def determine_winner(self, player1, player2):
        """判斷單場遊戲的勝負

        Args:
            player1 (int): 第一個玩家的選擇
            player2 (int): 第二個玩家的選擇

        Returns:
            str: 遊戲結果
        """
        if player1 == player2:
            return self.TIE

        # 使用字典映射來判斷勝負關係
        win_conditions = {
            self.SCISSORS: self.PAPER,  # 剪刀勝布
            self.ROCK: self.SCISSORS,   # 石頭勝剪刀
            self.PAPER: self.ROCK       # 布勝石頭
        }

        if win_conditions[player1] == player2:
            return self.FIRST_WINS
        else:
            return self.SECOND_WINS

    def play_all_games(self):
        """執行所有遊戲並輸出結果"""
        if not self.games:
            print("沒有遊戲數據")
            return

        print("\n遊戲結果:")
        print("-" * 30)

        for i, game in enumerate(self.games, 1):
            result = self.determine_winner(game[0], game[1])
            print(f"第 {i} 場: {result}")

    def get_statistics(self):
        """計算遊戲統計數據"""
        if not self.games:
            return None

        first_wins = 0
        second_wins = 0
        ties = 0

        for game in self.games:
            result = self.determine_winner(game[0], game[1])
            if result == self.FIRST_WINS:
                first_wins += 1
            elif result == self.SECOND_WINS:
                second_wins += 1
            else:
                ties += 1

        return {
            'first_wins': first_wins,
            'second_wins': second_wins,
            'ties': ties,
            'total_games': len(self.games)
        }

    def print_statistics(self):
        """印出遊戲統計"""
        stats = self.get_statistics()
        if stats:
            print("\n遊戲統計:")
            print("-" * 30)
            print(f"第一個人獲勝: {stats['first_wins']} 場")
            print(f"第二個人獲勝: {stats['second_wins']} 場")
            print(f"平手: {stats['ties']} 場")
            print(f"總場數: {stats['total_games']} 場")


def main():
    """主程式入口點"""
    print("=" * 50)
    print("剪刀石頭布遊戲 - 高階語法版本")
    print("Rock Paper Scissors Game - Advanced Version")
    print("=" * 50)

    # 創建遊戲實例
    game = RockPaperScissors()

    # 讀取輸入
    if not game.read_input():
        print("輸入失敗，程式結束")
        return

    # 執行遊戲
    game.play_all_games()

    # 顯示統計
    game.print_statistics()

    print("\n遊戲結束！")


# 簡化版本 - 使用函數式程式設計
def simple_rock_paper_scissors():
    """簡化版本的剪刀石頭布遊戲"""

    def get_game_result(player1, player2):
        """判斷遊戲結果的函數"""
        if player1 == player2:
            return "A tie"

        # 使用元組和字典來簡化邏輯
        win_map = {1: 3, 2: 1, 3: 2}  # 1勝3, 2勝1, 3勝2

        if win_map[player1] == player2:
            return "The first man wins the game"
        else:
            return "The second man wins the game"

    # 讀取並處理所有遊戲
    games = []
    for _ in range(10):
        game_input = list(map(int, input().split()))
        games.append(game_input)

    # 輸出結果
    for game in games:
        result = get_game_result(game[0], game[1])
        print(result)


if __name__ == "__main__":
    # 選擇執行版本
    print("選擇執行版本:")
    print("1. 完整版本 (類別導向)")
    print("2. 簡化版本 (函數式)")

    choice = input("請輸入選擇 (1 或 2): ").strip()

    if choice == "1":
        main()
    elif choice == "2":
        simple_rock_paper_scissors()
    else:
        print("無效選擇，執行完整版本")
        main()

