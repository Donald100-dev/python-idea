def plus2Vector(a, b, step) -> tuple:
    return (a[0] + b[0] * step, a[1] + b[1] * step)

def copyMaze(maze):
    new_maze = []
    for arr in maze:
        new_maze.append(arr.copy())
    return new_maze