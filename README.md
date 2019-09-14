# Reinforcement Learning Part 2

<p>Part 2 of my Reinforcement Learning (RL) series. During this series, I dwell into the field of RL by applying various methods to video games to learn and understand how an algorthm can learn to play by itself. The motivation for doing this series is simply by pure interest and to gain knowledge and experience in the field of Machine Learning.

The litterature follow throughout this series is <em>Reinforcement Learning</em> "An Introduction" by Ricard S. Button and Andrew G. Barto. 
ISBN: 9780262039246
</p>
## Gambler's Problem
The Gambler's Problem is a straight forward problem which can be solved by applying Valute Iteration described in [part 1](https://github.com/AdamOlsson/rl_policy_iteration) of this series. A gambler has the opportunity to make bets on the outcome of a sequence of coin flips. If the coin comes up *heads* he wins as much money as he put on stake and loses otherwise. The game ends when the gambler reaches 100EUR or when the gambler run out of money. Some restrictions are: the gambler can't stake more than money than he has and (2) all stakes are positive integers.

## Value Iteration
We define the state <em>s</em> of the environment as the current capital for gambler and the set of actions is defined as <em> a ∈ {0, 1, ...,</em> min<em>(s, 100 - s)}</em>. Here we've also set the probability of *heads* <em>p<sub>h</sub></em> as 0.4.

Below is the final value function and the policy for the environmet.

<p align="center"><img src=https://github.com/AdamOlsson/rl_gamblers_problem/blob/master/plots.png></p>

