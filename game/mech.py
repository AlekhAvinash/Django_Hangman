from string import ascii_lowercase as asl
from json import load
from random import choice


class cell:
    def __init__(self, val: str) -> None:
        self.val = val
        self.vis = True
        self.clr = "primary"

    def update(self, chk):
        self.vis = False
        self.clr = "success" if chk else "danger"

    def __str__(self) -> str:
        return f"{self.val}: {self.vis}"


class word:
    def __init__(self, dicv) -> None:
        self.dicv = dicv
        self.kfnd = lambda a: [j for j in self.keys if j.val == a][0]
        self.keys = [cell(i) for i in asl]
        self.start()

    def start(self, word: str = None):
        if not word:
            self.word, self.hint = choice(list(self.dicv.items()))
            self.hint = self.hint[0].split("; ")[0]
        self.word = self.word.lower()
        self.chLt = {i: True for i in set(self.word) if i in asl}
        self.ictr = 0
        self.cstr = ""
        self.winn = False
        self.ptrs = 6
        self.update()

    def update(self) -> None:
        self.cstr = "".join(
            ["_" if (i in asl) and (self.chLt[i]) else i for i in self.word]
        )

    def checkwin(self):
        self.winn = all(False == i for i in self.chLt.values())
        self.cstr = "Winner!!"

    def checklos(self):
        if self.ictr > 6:
            self.cstr = "Op! Try Again!"

    def calc(self, val):
        return (val * 2) - 1

    def inp(self, key: cell):
        res = key in self.chLt
        self.ptrs += self.calc(int(res))
        if res:
            self.chLt[key] = not res

        self.ictr += int(not res)
        self.checkwin()
        if not self.winn:
            self.update()
        self.checklos()

        key = self.kfnd(key)
        key.update(res)
        return key


ostr = word(load(open("game/static/out.txt")))
