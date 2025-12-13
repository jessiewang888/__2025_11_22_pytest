from unittest import mock
import pytest
from itertools import chain, combinations, product
from collections import Counter
from game import Board, RED_TEAM, BLACK_TEAM, Game, EMPTY


def test_board_init():
    board = Board()
    assert Counter(chain.from_iterable(board._hiden_chesses)) == Counter(board.CHESSES)

    assert isinstance(board._hiden_chesses[0], list)


def test_chess_up():
    board = Board()
    up = board.up(0, 0)
    assert up in board.CHESSES
    assert up == board._hiden_chesses[0][0]
    assert board[0, 0] == up


def test_chess_cannot_up_again():
    board = Board()
    up = board.up(0, 0)
    with pytest.raises(ValueError):
        board.up(0, 0)


def test_move_to_empty():
    source = (0, 0)
    target = (0, 1)

    board = Board()
    source_chess = board.up(*source)
    board.player = "red" if source_chess in RED_TEAM else "black"
    board.current[target[0]][target[1]] = EMPTY

    board.move(source, target)
    assert board.current[target[0]][target[1]] == source_chess
    assert board[source] == EMPTY


def test_cannot_move_to_hidden():
    board = Board()
    up = board.up(0, 0)
    board.player = "red"
    with pytest.raises(ValueError):
        board.move((0, 0), (0, 1))


@pytest.mark.parametrize(
    "source_chess, target_chess",
    list(combinations(BLACK_TEAM, 2)) + list(combinations(RED_TEAM, 2))
)
def test_cannot_move_to_same_team(source_chess, target_chess):
    source = (0, 0)
    target = (0, 1)

    board = Board()
    board.player = "red" if source_chess in RED_TEAM else "black"
    board.current[source[0]][source[1]] = source_chess
    board.current[target[0]][target[1]] = target_chess
    with pytest.raises(ValueError):
        board.move(source, target)


@pytest.mark.parametrize(
    "source_chess, target_chess",
    list(product(RED_TEAM, BLACK_TEAM)) + list(product(BLACK_TEAM, RED_TEAM)),
)
def test_move_to_diff_team(source_chess, target_chess):
    source = (0, 0)
    target = (0, 1)

    board = Board()
    board.player = "red" if source_chess in RED_TEAM else "black"
    board.current[source[0]][source[1]] = source_chess
    board.current[target[0]][target[1]] = target_chess

    board.move(source, target)
    assert board.current[target[0]][target[1]] == source_chess
    assert board[source] == EMPTY


@pytest.mark.parametrize(
    "player, source_chess, target_chess",
    [
        ("black", *it) for it in product(RED_TEAM, BLACK_TEAM)
    ] + [
        ("red", *it) for it in product(BLACK_TEAM, RED_TEAM)
    ]
)
def test_cannot_move_diff_team_source(player, source_chess, target_chess):
    source = (0, 0)
    target = (0, 1)

    board = Board()
    board.player = player
    board.current[source[0]][source[1]] = source_chess
    board.current[target[0]][target[1]] = target_chess
    with pytest.raises(ValueError):
        board.move(source, target)


def test_board_up_will_init_player():
    board = Board()
    board.up(0, 0)
    assert board.player in {"red", "black"}


def test_board_up_will_switch_player():
    board = Board()
    board.player = "red"
    board.up(0, 0)
    assert board.player == "black"


@pytest.mark.parametrize(
    "player, source_chess, target_chess",
    [
        ("red", "帥", EMPTY),
        ("black", "將", EMPTY),
    ]
)
def test_move_will_switch_player(player, source_chess, target_chess):
    source = (0, 0)
    target = (0, 1)

    board = Board()
    board.player = player
    board.current[source[0]][source[1]] = source_chess
    board.current[target[0]][target[1]] = target_chess
    board.move(source, target)

    assert board.player
    assert board.player != player


def test_win_game():
    board = Board()
    game = Game(board)
    board.current = [
        [EMPTY] * 8
        for _ in range(4)
    ]
    board.current[0][0] = "帥"
    board.scoring()
    assert board.finished
    assert board.winner == "red"


def test_peace_game():
    board = Board()
    game = Game(board)
    board.current = [
        [EMPTY] * 8
        for _ in range(4)
    ]
    board.current[0][0] = "帥"
    board.current[1][1] = "將"
    board.scoring()
    assert board.finished
    assert board.winner is None


def test_game_will_be_stop_while_finished():
    board = Board()
    game = Game(board)
    board.finished = True

    with mock.patch("builtins.input") as input_:
        game.start()
        input_.assert_not_called()


def test_game_call_up_by_input():
    board = Board()
    game = Game(board)
    up = mock.Mock()
    stop = mock.Mock(side_effect=[True])
    board.up = up
    game.stop = stop

    with mock.patch("builtins.input", side_effect=["(0, 0) -> (0, 0)"]) as input_:
        game.start()
        up.assert_called_once_with(0, 0)


def test_game_call_move_by_input():
    board = Board()
    game = Game(board)
    move = mock.Mock()
    stop = mock.Mock(side_effect=[True])
    board.move = move
    game.stop = stop

    with mock.patch("builtins.input", side_effect=["(0, 0) -> (0, 1)"]) as input_:
        game.start()
        move.assert_called_once_with((0, 0), (0, 1))


def test_game_call_game_info_before_input():
    board = Board()
    game = Game(board)
    up = mock.Mock()
    stop = mock.Mock(side_effect=[True])
    board.up = up
    game.stop = stop

    with mock.patch("builtins.input", side_effect=["(0, 0) -> (0, 0)"]) as input_:
        def assert_input_not_called():
            nonlocal input_
            input_.assert_not_called()

        game.info = mock.Mock(side_effect=assert_input_not_called)
        game.start()
        game.info.assert_called_once()
        up.assert_called_once_with(0, 0)


def test_game_info_will_print_board_info():
    board = Board()
    game = Game(board)

    with mock.patch("builtins.print") as print_:
        game.info()

    print_.assert_called_once_with(
        "Player: None\n"
        "ＯＯＯＯＯＯＯＯ\n"
        "ＯＯＯＯＯＯＯＯ\n"
        "ＯＯＯＯＯＯＯＯ\n"
        "ＯＯＯＯＯＯＯＯ"
    )

def test_game_action_failed_will_keep_player_and_continue():
    board = Board()
    game = Game(board)
    move = mock.Mock()
    board.player = "red"
    stop = mock.Mock(side_effect=[False, True])
    game.stop = stop
    info = mock.Mock(side_effect=[None, None])
    game.info = info

    with mock.patch("builtins.print") as print_:
        with mock.patch("builtins.input", side_effect=[
            "(0, 0) -> (0, 0)",     # red do it
            "(0, 0) -> (0, 0)",     # black do: will raise error
        ]) as input_:
            game.start()

    print_.assert_has_calls([mock.call("Cannot up again")])

    assert board.player == "black"
    assert info.call_count == 2