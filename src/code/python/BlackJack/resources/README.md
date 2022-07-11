This is BlackJack game
==============

How to run progrsm
---------

1. Please download **ai.py , game.py, main.py, and resources folder** 
2. In the terminal, type **python main.py** to run the blackjack game
3. There are three choices for you, MC value, TQ value, and QL value. 
4. You need to turn QL value on first and can click auto play to see how the ai algorithm worksd.


Note 
--------
game.py and main.py were given to me. I designed ai.py file based the expectimax algorithm I leanred from the class. 

Monte Carlo Policy Evaluation
--------
Evaluate the policy "Hit (ask for a new card) if sum of cards is below 14, and Stand (switch to dealer) otherwise" using the Monte Carlo method. Namely, learn the values for each state under the policy.


Temporal-Difference Policy Evaluation
--------
Evaluate the policy "Hit (ask for a new card) if sum of cards is below 14, and Stand (switch to dealer) otherwise" using the Temporal-Difference method.


Q-Learning
--------
Implement the Q-learning algorithm. Use epsilon=0.4 in the epsilon-strategy in your final submission, but you are encouraged to check the behavior difference for various choices of epsilon. After learning, AutoPlay will follow the Q-learning values to make decisions.
