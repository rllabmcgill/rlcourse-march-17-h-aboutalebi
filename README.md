# Comparision Of Different Algorithm in solving Bandit Arm Problem

Here I have tested different bandit arm algorithm including epsilon greedy, UCB by changing their parameters and then compared them with each other. To do so, I have set 5 actions correponding to 5 bandits, each have different mean reward and equal variance. The reaward has Guassian distribution. Then, I applied different Bandit Algorithms to see how they work. I also changed the variance to see its effect on performance. 

##Epsilon Greedy:

Here is the graph of greedy algorithm wih different epsilon. Note that the epsilon for Greedy line (blue line) is zero:

![b1](https://cloud.githubusercontent.com/assets/5707322/24042767/d59b7fd2-0ae9-11e7-8b86-8c97894b29da.png)

As it can be seen, pure greedy stays on its first choice, however, epsilon greedy eventualy reaches best action. If we set epsilon higher, then the learning curve is faster though it might have poor performance in the beggining. Here is a graph when variance of reward is 0.1:

![b2](https://cloud.githubusercontent.com/assets/5707322/24042991/d25bbba6-0aea-11e7-96ad-2daee176564e.png)

Here is for variance 0.01:


![b3](https://cloud.githubusercontent.com/assets/5707322/24043057/0db71858-0aeb-11e7-848a-a94c0989b153.png)

As it can be seen when varianc decreases, the gap between epsilon greedy with 0.1 and others become more noticeble.

Now Let's see the performance UBC on bandit by assigning different c values.

![b6](https://cloud.githubusercontent.com/assets/5707322/24043154/9e9216a2-0aeb-11e7-9a1f-5f7628b9e312.png)

So, the UCB with c=0.01 has the best performance. As it can be seen, when we change c to high value like 10 or low value like 0.0001 the performance drops. We have the poorest performnce with c=0.0001, as by using this parameter in UBC, UBC behaves like pure Greedy algorithm.

the last two figures are the comparison of UCB with epsilon greedy algorithms. It is obvious that UCB has much better learning curve with good choice of parameter compared with epsilon greedy.

![b5](https://cloud.githubusercontent.com/assets/5707322/24043264/34fc4126-0aec-11e7-87ac-49d3fcd325bd.png)
![b4](https://cloud.githubusercontent.com/assets/5707322/24043265/3506923e-0aec-11e7-9038-6f95439a9943.png)

