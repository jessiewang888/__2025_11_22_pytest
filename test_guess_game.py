# test_guess_game.py
import pytest
from guess_game import guess_number  # 假設函數儲存在 guess_game.py 檔案中

def test_correct_guess():
    assert guess_number(5, 5) == "猜對了"

def test_guess_too_low():
    assert guess_number(3, 5) == "低了"

def test_guess_too_high():
    assert guess_number(7, 5) == "高了"

def test_guess_string_will_request_int():
    assert guess_number("5", 5) == "請輸入整數"
