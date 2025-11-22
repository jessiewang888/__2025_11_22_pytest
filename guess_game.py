# guess_game.py
def guess_number(user_guess, target_number):
    #print("我有跑")
    if not isinstance(user_guess, int):
        return "請輸入整數"
    if user_guess < target_number:
        return "低了"
    elif user_guess > target_number:
        return "高了"
    else:
        return "猜對了"


#guess_number(100, 3)