

maze = []
with open ("programs/mazes/first.txt", "r", encoding="UTF-8") as file:
    for line in file:
        line_ = line.rstrip("\n")
        maze.append(line_)


#Other way to do it:
# from pathlib import Path

# maze = Path("mazes/first.txt").read_text(encoding="utf-8").splitlines()

#We have to search the start and the end of the maze
start = None #firstly, start has no value; in the future, it'll turn into a tuple
end = None
queue = []
for r, row in enumerate(maze):
    for c, cell in enumerate(row):
        if cell == "S":
            start = (r, c)
            queue.append((r,c))
        if cell == "E":
            end = (r,c)




set_of_explored_sites = set() #a set; no duplicates
set_of_explored_sites.add(start)#we add the first coords explored (start)

actual_cord = None

came_from = {start: None} #a dictionary with all the way (cord : origin)

def add_to_queue(row, col):
    if row >=0 and col >= 0:
        try:
            dir = maze[row][col] #up, down, right or left
            if (dir != "#" and (row, col) not in set_of_explored_sites): 
                #if its not a wall and it's not in the set of explored sites
                set_of_explored_sites.add((row,col))
                queue.append((row, col))
                came_from[(row, col)] = actual_cord
        except IndexError as e:
            return


#while queue is True (not null) and the tuple is not the end one. 
while queue and actual_cord != end:
    actual_cord = queue.pop(0) #removes it and returns the first cell
    add_to_queue(actual_cord[0] - 1, actual_cord[1]) 
    add_to_queue(actual_cord[0] + 1, actual_cord[1])
    add_to_queue(actual_cord[0], actual_cord[1] + 1)
    add_to_queue(actual_cord[0], actual_cord[1] - 1)
    #coords are only added if they pass the restrictions


path = []
cell = end #(r,c) -> a tuple

while cell != None:
    path.append(cell) #adds the cord to the path, then it's origin
    try:
        cell = came_from[cell]
    except KeyError:
        print("unreachable path")
        break
if len(path) > 1:
    path.reverse()
    print(path)


    

    



