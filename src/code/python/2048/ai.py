
from __future__ import absolute_import, division, print_function
import copy, random
from game import Game

MOVES = {0: 'up', 1: 'left', 2: 'down', 3: 'right'}
MAX_PLAYER, CHANCE_PLAYER = 0, 1 

# Tree node. To be used to construct a game tree. 
class Node: 
    # Recommended: do not modify this __init__ function
    def __init__(self, state, player_type):
        self.state = (copy.deepcopy(state[0]), state[1])
        # to store a list of (direction, node) tuples
        self.children = []
        self.player_type = player_type

    # returns whether this is a terminal state (i.e., no children)
    def is_terminal(self):
        if self.player_type == -1:
            #print("is termianl: " , self.state[0])
            return True

        return False

# AI agent. Determine the next move.
class AI:
    # Recommended: do not modify this __init__ function
    def __init__(self, root_state, search_depth=3): 
        self.root = Node(root_state, MAX_PLAYER)
        self.search_depth = search_depth
        self.simulator = Game(*root_state)
        
    
    

    # (Hint) Useful functions: 
    # self.simulator.current_state, self.simulator.set_state, self.simulator.move

    # how to use function? 
    # current_matrix, current_score = self.simulator.current_state()
    # self.simulator.set_state
    # self.simulator.set_state(current_matrix, current_score)
#   self.state = (copy.deepcopy(state[0]), state[1])

#         # to store a list of (direction, node) tuples
#         self.children = []

#         self.player_type = player_type
#  root: player
# - level 1: computer 
# - level 2: player
# - level 3: terminal with payoff 

    # TODO: build a game tree from the current node up to the given depth
    def build_tree(self, node = None, depth = 0):

        
        if depth == 3:
            for i in range(0,4):
                
                self.simulator.set_state(self.root.state[0], self.root.state[1])
                if  self.simulator.move(i):
                    newNode = Node(self.simulator.current_state(), CHANCE_PLAYER)
                    self.root.children.append((i,newNode))

            for i in range(len(self.root.children)):
                (direction,newNode) = self.root.children[i]
                self.build_tree(newNode, depth - 1)
        
        elif depth == 2:
            self.simulator.set_state(node.state[0], node.state[1])
            openTiles = self.simulator.get_open_tiles()
            current_tile = self.simulator.tile_matrix
            for i in openTiles:
                (x,y) = i
                self.simulator.tile_matrix = current_tile
                if  self.simulator.tile_matrix[x][y] == 0:
                    self.simulator.tile_matrix[x][y] = 2
                    newNode = Node(self.simulator.current_state(), MAX_PLAYER)
                    node.children.append((None,newNode))
                    self.simulator.tile_matrix[x][y] = 0
                

            for i in node.children:
                ( _ , newNode) = i
                self.build_tree(newNode, depth - 1)
        elif depth == 1:
            for i in range(0,4):
                self.simulator.set_state(node.state[0], node.state[1])
                if self.simulator.move(i):
                    newNode = Node(self.simulator.current_state(), -1)
                    node.children.append((i,newNode))

    # TODO: expectimax calculation.
    # Return a (best direction, expectimax value) tuple if node is a MAX_PLAYER
    # Return a (None, expectimax value) tuple if node is a CHANCE_PLAYER

    def expectimax(self, node = None):
        # TODO: delete this random choice but make sure the return type of the function is the same
        # print("EM root is : " , self.root.state[0])

        if node.is_terminal():
            (currState, currScore) = node.state
            return  (None, currScore)

        # max player
        elif node.player_type == 0:
            (currState, currScore) = self.simulator.current_state()

            value = float('-inf')
            new_direction = None
    
            for i in node.children: 
                (temp_direction , temp_node) = i
                
                (D , score) = self.expectimax(temp_node)
                temp_value = max(value , score)

                

                if value < temp_value or new_direction == None:
                    new_direction = temp_direction
                    value = temp_value

            return (new_direction,value)
        

        #Chance player 
        elif node.player_type == 1:
            value = 0
            chance = 1 / len(node.children) 

            for i in node.children: 
                (temp_direction , temp_node) = i
                value = value + self.expectimax(temp_node)[1] * chance
            return (None , value)

   

    # Return decision at the root
    def compute_decision(self):
        self.build_tree(self.root, self.search_depth)     
        direction, _ = self.expectimax(self.root)
        #print("Direction is " , direction )
        return direction