# Reinforcement Learning Part 2

<p>Part 2 of my Reinforcement Learning (RL) series. During this series, I dwell into the field of RL by applying various methods to video games to learn and understand how an algorthm can learn to play by itself. The motivation for doing this series is simply by pure interest and to gain knowledge and experience in the field of Machine Learning.

The litterature follow throughout this series is <em>Reinforcement Learning</em> "An Introduction" by Ricard S. Button and Andrew G. Barto. 
ISBN: 9780262039246
</p>

## Gambler's Problem
The Gambler's Problem is a straight forward problem which can be solved by applying Valute Iteration described in [part 1](https://github.com/AdamOlsson/rl_policy_iteration) of this series. A gambler has the opportunity to make bets on the outcome of a sequence of coin flips. If the coin comes up *heads* he wins as much money as he put on stake and loses otherwise. The game ends when the gambler reaches 100EUR or when the gambler run out of money. The rewards are 1 if the gambler wins and 0 on all other state transitions. Some restrictions are: the gambler can't stake more than money than he has and (2) all stakes are positive integers.

## Value Iteration
We define the state <em>s</em> of the environment as the current capital for gambler and the set of actions is defined as <em> a ∈ {0, 1, ...,</em> min<em>(s, 100 - s)}</em>. Here we've also set the probability of *heads* <em>p<sub>h</sub></em> as 0.4.

Below is the final value function and the policy for the environmet.

<p align="center"><img src=https://github.com/AdamOlsson/rl_gamblers_problem/blob/master/plots.png></p>

There are some things that can be said about the strange policy. When selecting what action to take, the action that returns the highest reward will be the one chosen. This is simply done by the max() function. However, when multiple action have the same expected rewards, the max() function will select the first action that rewards max expected value because of how it is implemented. Turns out that one of the actions that often returns the max expected reward is the action to stake 0 which also happens to be the first action in the list of action. In these cases, the algorithm would stake 0 which explains the almost noisy looking policy. According to James Teow, [here](https://medium.com/@jaems33/gamblers-problem-b4e91040e58a), the policy would be a lot smoother if the max() function chose the last index for the cases when the maximum estimated return can be found on multiple actions. 
