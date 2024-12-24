class User:
    def __init__(self):
        self.history = []

    def send_message(self, message, character):
        self.history.append(f"使用者: {message}")
        response = character.respond(message)
        self.history.append(f"虛擬人物: {response}")

    def view_history(self):
        for record in self.history:
            print(record)

class VirtualCharacter:
    def respond(self, message):
        if message == "讀書":
            return "記得休息"
        elif message == "健康":
            return "多喝水"
        else:
            return "我不知道你在說甚麼"

# 測試程式
user = User()
character = VirtualCharacter()

user.send_message("讀書", character)
user.send_message("健康", character)
user.send_message("測試文字", character)

user.view_history()
