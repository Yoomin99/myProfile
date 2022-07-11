from __future__ import print_function
from heapq import * #Hint: Use heappop and heappush

ACTIONS = [(0,1),(1,0),(0,-1),(-1,0)]

class AI:
    def __init__(self, grid, type):
        self.grid = grid
        self.set_type(type)
        self.set_search()

    def set_type(self, type):
        self.final_cost = 0
        self.type = type

    def set_search(self):
        self.final_cost = 0
        self.grid.reset()
        self.finished = False
        self.failed = False
        self.previous = {}

        # Initialization of algorithms goes here
        if self.type == "dfs":
            self.frontier = [self.grid.start]
            self.explored = []
        elif self.type == "bfs":
            self.frontier = [self.grid.start]
            self.explored = []
        elif self.type == "ucs":
            self.frontier = [ (0,self.grid.start) ]
            self.explored = []
        elif self.type == "astar":
            #(G+H value, real cost, previous H value, Node)
            w = abs(self.grid.start[0] - self.grid.goal[0]) + abs(self.grid.start[1] - self.grid.goal[1])
            self.frontier = [ (w,0,self.grid.start) ]
            self.explored = []
            

    def get_result(self):
        total_cost = 0
        current = self.grid.goal
        while not current == self.grid.start:
            total_cost += self.grid.nodes[current].cost()
            current = self.previous[current]
            self.grid.nodes[current].color_in_path = True #This turns the color of the node to red
        total_cost += self.grid.nodes[current].cost()
        self.final_cost = total_cost

    def make_step(self):
        if self.type == "dfs":
            self.dfs_step()
        elif self.type == "bfs":
            self.bfs_step()
        elif self.type == "ucs":
            self.ucs_step()
        elif self.type == "astar":
            self.astar_step()

    #DFS: BUGGY, fix it first
    def dfs_step(self):
        if not self.frontier:
            self.failed = True
            self.finished = True
            print("no path")
            return
        current = self.frontier.pop() #getting the newest block

        # Finishes search if we've found the goal.
        if current == self.grid.goal:
            self.finished = True
            return
        children = [(current[0]+a[0], current[1]+a[1]) for a in ACTIONS]
        self.grid.nodes[current].color_checked = True
        self.grid.nodes[current].color_frontier = False

        if current not in self.explored:
            self.explored.append(current)
            for n in children:
                if n[0] in range(self.grid.row_range) and n[1] in range(self.grid.col_range):
                    if not self.grid.nodes[n].puddle and n not in self.explored and n not in self.frontier:
                        self.previous[n] = current
                        self.frontier.append(n)
                        #Now n becomes the member of frontier
                        self.grid.nodes[n].color_frontier = True
                        self.grid.nodes[n].color_checked = True

    #Implement BFS here (Don't forget to implement initialization at line 23)
    def bfs_step(self):
        if not self.frontier:
            self.failed = True
            self.finished = True
            print("no path")
            return
        current = self.frontier.pop(0) #getting the newest block

        # Finishes search if we've found the goal.
        if current == self.grid.goal:
            self.finished = True
            return
        children = [(current[0]+a[0], current[1]+a[1]) for a in ACTIONS]
        self.grid.nodes[current].color_checked = True
        self.grid.nodes[current].color_frontier = False

        if current not in self.explored:
            self.explored.append(current)
            for n in children:
                if n[0] in range(self.grid.row_range) and n[1] in range(self.grid.col_range):
                    if not self.grid.nodes[n].puddle and n not in self.explored and n not in self.frontier:
                        self.previous[n] = current
                        self.frontier.append(n)
                        #Now n becomes the member of frontier
                        self.grid.nodes[n].color_frontier = True
                        self.grid.nodes[n].color_checked = True

    #Implement UCS here (Don't forget to implement initialization at line 23)
    def ucs_step(self):
        if not self.frontier:
            self.failed = True
            self.finished = True
            print("no path")
            return
        self.frontier.sort(reverse = False)
        current = self.frontier.pop(0) #getting the least cost block
        currentCost = current[0]
        currentNode = current[1]

        # Finishes search if we've found the goal.
        if currentNode == self.grid.goal:
            self.finished = True
            return
        children = [(currentNode[0]+a[0], currentNode[1]+a[1]) for a in ACTIONS]
        self.grid.nodes[currentNode].color_checked = True
        self.grid.nodes[currentNode].color_frontier = False
        self.explored.append(currentNode)
  
        for n in children:
            if n[0] in range(self.grid.row_range) and n[1] in range(self.grid.col_range):
                if not self.grid.nodes[n].puddle:
                    newCost = currentCost + self.grid.nodes[n].cost()

                    #Meaning that else if child.state is in frontier?  It will causes the error when n is not in frontier.
                    try: 
                        index = [x[1] for x in self.frontier].index(n)
                        indexCost = self.frontier[index][0]
                        if indexCost > newCost:
                            self.frotier.pop(index)
                            self.frotier.append((newCost,n))
                            self.previous[n] = currentNode
                            
                    except:
                        # not explored && not in frontier
                        if n not in self.explored:
                            self.previous[n] = currentNode
                            self.frontier.append((newCost,n))
                            self.grid.nodes[n].color_frontier = True
                            self.grid.nodes[n].color_checked = True




    
    #Implement Astar here (Don't forget to implement initialization at line 23)
    #(G+H value, real cost, previous H value, Node)
    def astar_step(self):
        if not self.frontier:
            self.failed = True
            self.finished = True
            print("no path")
            return
        self.frontier.sort(reverse = False)
        current = self.frontier.pop(0) #getting the least cost block
        currentCost = current[1]
        currentNode = current[2]
        CurrentGH = current[0]

        # Finishes search if we've found the goal.
        if currentNode == self.grid.goal:
            self.finished = True
            return
        children = [(currentNode[0]+a[0], currentNode[1]+a[1]) for a in ACTIONS]
        self.grid.nodes[currentNode].color_checked = True
        self.grid.nodes[currentNode].color_frontier = False
        self.explored.append(currentNode)
  
        for n in children:
            if n[0] in range(self.grid.row_range) and n[1] in range(self.grid.col_range):
                if not self.grid.nodes[n].puddle:
                    H = abs(n[0] - self.grid.goal[0]) + abs(n[1] - self.grid.goal[1])
                    G = currentCost + self.grid.nodes[n].cost()
                    F = G + H
                    newCost = currentCost + self.grid.nodes[n].cost()

                    #Meaning that else if child.state is in frontier?  It will causes the error when n is not in frontier. 
                    try: 
                        index = [x[2] for x in self.frontier].index(n)
                        indexCost = self.frontier[index][0]
                        if indexCost > F:
                            self.frotier.pop(index)
                            self.frotier.append((F,newCost,n))
                            self.previous[n] = currentNode
                            
                    except:
                        # not explored && not in frontier
                        if n not in self.explored:
                            self.previous[n] = currentNode
                            self.frontier.append((F,newCost,n))
                            self.grid.nodes[n].color_frontier = True
                            self.grid.nodes[n].color_checked = True