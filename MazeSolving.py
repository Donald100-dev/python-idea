import json, keyboard, os
from func import *

with open("M.json", "r") as f:
    MAZE = json.load(f)

SIZEMAZE = (len(MAZE[0]), len(MAZE))

moving = {
    'up'   : (0, -1),
    'down' : (0, 1),
    'left' : (-1, 0),
    'right': (1, 0),
    'pass' : (0, 0),
}

class Player:
    def __init__(self, name):
        self.name = name[0].upper()
        self.speed = 1
        self.pos = (1, 1)
        
    def playerMove(self) -> None:
        while True:
            direc = self.getDirec()
            if direc == 'exit': return
            if direc == 'pass': continue
            new_pos = plus2Vector(self.pos, moving[direc], self.speed)
            if self.canMoving(new_pos): 
                self.pos = new_pos
                self.printPlayer()
        

    def getDirec(self) -> str:
        key = keyboard.read_key()
        if key == 'w': return 'up'
        if key == 's': return 'down'
        if key == 'a': return 'left'
        if key == 'd': return 'right'
        if key == 'esc': return 'exit'
        return 'pass'

    def canMoving(self, pos):
        x, y = pos[0], pos[1]
        if not(0 <= x < SIZEMAZE[0]): return False
        if not(0 <= y < SIZEMAZE[1]): return False
        if MAZE[y][x] == "███": return False
        return True

    def printPlayer(self):
        maze_show = copyMaze(MAZE)
        maze_show[self.pos[1]][self.pos[0]] = ' ' + self.name + ' '
        os.system('cls')
        for arr in maze_show:
            print(''.join(arr))


def main():
    name_player = input("nhap ten nguoi choi:")
    p = Player(name_player)
    p.printPlayer()
    p.playerMove()

if __name__ == '__main__':
    main()