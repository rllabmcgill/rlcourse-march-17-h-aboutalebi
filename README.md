# Comparision Of Different Algorithm in solving Bandit Arm Problem

Here I have tested different bandit arm algorithm by changing their parameters and then compared them with each other. To do so, I have set 5 actions correponding to 5 bandits, each have different mean reward and equal variance. The reaward has Guassian distribution. Then, I applied different Bandit Algorithms to see how they work. I also changed the variance to see its effect on performance. 

##Epsilon Greedy:

Here is the graph of greedy algorithm wih different epsilon. Note that the epsilon for Greedy line (blue line) is zero:

![b1](https://cloud.githubusercontent.com/assets/5707322/24042767/d59b7fd2-0ae9-11e7-8b86-8c97894b29da.png)

As it can be seen, pure greedy stays on its first choice, however, epsilon greedy eventualy reaches best action. If we set epsilon higher, then the learning curve is faster though it might have poor performance in the beggining.
