import os, json, random, time, func

class Maze:
    def __init__(self, X, Y, pos_start = (1, 1), pos_end = None):
        self.size: tuple(int) = (X, Y)
        self.pos_start: tuple(int) = min(pos_start[0], X), min(pos_start[1], Y)
        self.pos_end: tuple(int) = None
        if pos_end is not None:
            self.pos_end =  min(pos_end[0], X), min(pos_end[1], Y)  
        else:
            self.pos_end = (X - 2, Y - 2)
        self.maze: list[list[str]] = [['███' for _ in range(X)] for _ in range(Y)]
        self.exit_Road = None
        self.maze[self.pos_start[1]][self.pos_start[0]] = '[s]'
        self.maze[self.pos_end[1]][self.pos_end[0]] = '[e]'

    def createPathway(self) -> None:
        def direcInMaze(x, y) -> list[tuple]:
            return [(x + 2, y), (x - 2, y), (x, y - 2), (x, y + 2)]

        def rightDirec(x, y) -> bool:
            if not(0 <= x < self.size[0]): return False
            if not(0 <= y < self.size[1]): return False
            if self.maze[y][x] == '[e]': return True
            if self.maze[y][x] != '███': return False
            return True
        
        def choseDirec(direcs: list[tuple]) -> tuple:
            return random.choice(direcs)

        def BreakWall(pos, new_pos) -> None:
            self.maze[(pos[1] + new_pos[1]) // 2][(pos[0] + new_pos[0]) // 2] = "▒▒▒"
            self.maze[new_pos[1]][new_pos[0]] = "▒▒▒"
        
        def createdRoad(old_pos: tuple[int]):
            if pathway == []: return
            old_pos2 = pathway[-1]
            self.maze[(old_pos2[1] + old_pos[1]) // 2][(old_pos2[0] + old_pos[0]) // 2] = "   "
            self.maze[old_pos[1]][old_pos[0]] = "   "

        pathway = [self.pos_start]

        while True:
            self.printMaze()
            if pathway == []: break

            last_pos = pathway[-1]
            direcs: list[tuple] = direcInMaze(last_pos[0], last_pos[1])
            direcs = [direc for direc in direcs if rightDirec(direc[0], direc[1])]

            if direcs == []:
                old_pos: tuple(x,y) = pathway.pop()
                createdRoad(old_pos)
                continue

            new_pos = choseDirec(direcs)
            BreakWall(last_pos, new_pos)
            pathway.append(new_pos)

            if new_pos == self.pos_end:
                self.FindingExitRoad(pathway)
        
        self.maze[self.pos_end[1]][self.pos_end[0]] = '[e]'

    def FindingExitRoad(self, pathway):
            self.exit_Road = pathway.copy()

    def printExitRoad(self):
        maze_show: list[list[str]] = func.copyMaze(self.maze)
        l_exit_road: int = len(self.exit_Road)
        for pos in range(1, l_exit_road):
            oldPathway = self.exit_Road[pos - 1]
            newPathway = self.exit_Road[pos]
            maze_show[(oldPathway[1] + newPathway[1]) // 2][(oldPathway[0] + newPathway[0]) // 2] = " . "
            self.printMaze(maze_show)
            maze_show[newPathway[1]][newPathway[0]] = " . "
            self.printMaze(maze_show)
        maze_show[self.pos_end[1]][self.pos_end[0]] = '[e]'
        self.printMaze(maze_show)

    def printMaze(self, maze = None) -> None:
        if maze is None: maze = self.maze
        os.system('cls')
        for arr in maze:
            print(''.join(arr)) 
        time.sleep(0.05)

    def saveMaze(self, namef = 'maze') -> None:
        with open(namef + ".json", "w") as f:
            json.dump(self.maze, f)

os.system('cls')
X = int(input("nhap X: "))
Y = int(input("nhap Y: "))
namef = input("nhap ten: ")

if X % 2 == 0: X += 1
if Y % 2 == 0: Y += 1

def main():
    maze = Maze(X, Y)
    maze.createPathway()
    maze.printMaze()
    maze.saveMaze(namef)
    maze.printExitRoad()

if __name__ == '__main__':
    main()



#> tạo mê cung bằng tay
    # s = ' '

    # direc = {'w':(-1, 0), 'a':(0, -1), 's':(1, 0), 'd':(0, 1)}

    # pos = [0, 0]

    # while s != '':
    #     s = input()
    #     if s in direc:
    #         pos[0] += direc[s][0]
    #         pos[1] += direc[s][1]
    #     maze[pos[0]][pos[1]] = '   '
    #     os.system('cls')
    #     for arr in maze:
    #         print(''.join(arr))