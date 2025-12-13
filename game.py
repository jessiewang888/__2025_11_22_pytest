import random

EMPTY = "Ｘ"
HIDDEN = "Ｏ"
RED_TEAM = {
    "帥",
    "仕",
    "相",
    "俥",
    "傌",
    "炮",
    "兵",
}
BLACK_TEAM = {
    "將",
    "士",
    "象",
    "車",
    "馬",
    "砲",
    "卒",
}
assert not RED_TEAM & BLACK_TEAM
SWITCH = {"red": "black", "black": "red"}


class Board():
    CHESSES = [
        "帥", "將",
        *["仕", "士"] * 2,
        *["相", "象"] * 2,
        *["俥", "車"] * 2,
        *["傌", "馬"] * 2,
        *["炮", "砲"] * 2,
        *["兵", "卒"] * 5,
    ]

    def __init__(self):
        chesses = self.CHESSES.copy()
        random.shuffle(chesses)

        self._hiden_chesses = []
        self.finished = False
        self.winner = None

        for _ in range(4):
            row = []
            for _ in range(8):
                row.append(chesses.pop())
            self._hiden_chesses.append(row)

        self.current = [
            [HIDDEN] * 8
            for _ in range(4)
        ]
        self.player = None

    def up(self, x, y):
        if self.current[x][y] != HIDDEN:
            raise ValueError("Cannot up again")
        self.current[x][y] = self._hiden_chesses[x][y]
        if not self.player:
            self.player = "red" if self.current[x][y] in RED_TEAM else "black"

        self.player = SWITCH[self.player]
        return self.current[x][y]

    def __getitem__(self, idx):
        return self.current[idx[0]][idx[1]]

    def move(self, source, target):
        source_chess = self.current[source[0]][source[1]]
        target_chess = self.current[target[0]][target[1]]
        if self.player == "red" and source_chess not in RED_TEAM:
            raise ValueError("Cannot move diff team")
        if self.player == "black" and source_chess not in BLACK_TEAM:
            raise ValueError("Cannot move diff team")

        if target_chess == HIDDEN:
            raise ValueError("Cannot move to hidden")
        if (
            target_chess in RED_TEAM
            and source_chess in RED_TEAM
        ) or (
            target_chess in BLACK_TEAM
            and source_chess in BLACK_TEAM
        ):
            raise ValueError("Cannot move to same team")
        self.current[target[0]][target[1]] = self.current[source[0]][source[1]]
        self.current[source[0]][source[1]] = EMPTY
        self.player = SWITCH[self.player]

    def scoring(self):
        curr = {
            chess: (row_idx, col_idx)
            for row_idx, row in enumerate(self.current)
            for col_idx, chess in enumerate(row)
        }
        if HIDDEN in curr:
            return

        curr_without_empty = (set(curr) - {EMPTY})
        if curr_without_empty & RED_TEAM == curr_without_empty:
            self.winner = "red"
            self.finished = True
        elif curr_without_empty & BLACK_TEAM == curr_without_empty:
            self.winner = "black"
            self.finished = True

        if len(curr_without_empty) == 2:
            first = curr_without_empty.pop()
            second = curr_without_empty.pop()
            if (abs(curr[first][0] - curr[second][0]) + abs(curr[first][1] - curr[second][1])) == 2:
                self.finished = True


def extract_to_location(maybe_location_string: str):
    import re

    matching = re.compile(r"\((\d+),\s*(\d+)\)")
    x, y = map(int, matching.findall(maybe_location_string)[0])
    return x, y


class Game:
    def __init__(self, board):
        self.board = board

    def start(self):
        while not self.board.finished:
            self.info()
            action = input()
            source, target = [extract_to_location(it) for it in action.split("->")]
            try:
                if source != target:
                    self.board.move(source, target)
                else:
                    self.board.up(*source)
            except ValueError as e:
                print(str(e))
            if self.stop():
                break

    def info(self):
        print(f'''Player: {self.board.player}\n{"\n".join("".join([it for it in row]) for row in self.board.current)}''')

    def stop(self):
        return False


if __name__ == "__main__":
    board = Board()
    game = Game(board)
    game.start()