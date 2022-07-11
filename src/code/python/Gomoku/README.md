This is GOMOKU game
==============

How to run progrsm
---------

1. Please download **ai.py , game.py, and main.py** 
2. In the terminal, type **python main.py** to run gomoku game
3. You are a black stone player. Once you place a stone on the board, ai would start to think!


In MCTS, the search exits when the "computation budget" is reached. The current default value is 1000, which will be used for testing. You can increase or decrease it to see the different behaviors of AI. For instance, with a budget over 6000, a correctly implemented MCTS AI should be able to play a fairly interesting game against you (although it may still make some obvious mistakes when the number of next actions to consider gets larger). 