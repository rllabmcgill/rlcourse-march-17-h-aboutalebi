# Here we show actions of bandit corresponds to the indices in our Q list...
# ... So q_i in List Q is the value corresponding to doing action i


import random
import time
import numpy as np
from Graph2 import *
import math

def main():
    start_time = time.time()
    print("Started...")
    Result2=[]
    Result1=[]
    File2 = "result.txt"  # for storing results
    Q_Ground=[5,10,6,-1,9]
    varience=1
    epsilon=0.01
    epsilon2=0.1
    c=0.0001
    c2=0.001
    Average_V_UCB = []
    Average_V_UCB2 = []
    Average_V_epsilon_Greedy2 = []
    Average_V_epsilon_Greedy=[]
    Average_V_Greedy = []
    for j in range(5):
        Q_UCB = []
        Q_UCB2 = []
        Q_epsilon_Greedy2 = []
        Q_epsilon_Greedy = []
        Counter_epsilon_Greedy = []  # for memorizing how many actions of particular type we have done
        Counter_epsilon_Greedy2 = []  # for memorizing how many actions of particular type we have done
        Counter_Greedy = []  # for memorizing how many actions of particular type we have done
        Counter_UCB = []  # for memorizing how many actions of particular type we have done
        Counter_UCB2 = []  # for memorizing how many actions of particular type we have done
        Q_Greedy = []
        for i in range(5):
            Q_UCB.append(3)
            Q_UCB2.append(3)
            Q_epsilon_Greedy.append(3)
            Q_epsilon_Greedy2.append(3)
            Counter_epsilon_Greedy.append(0)
            Counter_UCB.append(0)
            Counter_UCB2.append(0)
            Counter_epsilon_Greedy2.append(0)
            Counter_Greedy.append(0)
            Q_Greedy.append(3)
        Value_UCB = [0]
        Value_UCB2= [0]
        Value_Epsilon_Greedy = [0]
        Value_Epsilon_Greedy2 = [0]
        Value_Greedy = [0]
        for i in range(1,1000):
            i4 = UCB(Q_UCB2, i, Counter_UCB2, c2)
            Counter_UCB2[i4] += 1
            i3 = UCB(Q_UCB, i,Counter_UCB, c)
            Counter_UCB[i3] += 1
            i1 = epsilon_Greedy(Q_epsilon_Greedy, i, epsilon)
            Counter_epsilon_Greedy[i1] += 1
            i0=epsilon_Greedy(Q_epsilon_Greedy2, i, epsilon2)
            Counter_epsilon_Greedy2[i0]+=1
            i2=epsilon_Greedy(Q_Greedy, i, 0)
            Counter_Greedy[i2]+=1
            r_UCB = implement_action(Q_Ground[i3], varience)
            r_UCB2 = implement_action(Q_Ground[i4], varience)
            r_epsilon_Greedy=implement_action(Q_Ground[i1],varience)
            r_epsilon_Greedy2 = implement_action(Q_Ground[i0], varience)
            New_Value_UCB2 = Value_UCB2[i - 1] + (1 / i) * (r_UCB2 - Value_UCB2[i - 1])
            New_Value_UCB = Value_UCB[i - 1] + (1 / i) * (r_UCB - Value_UCB[i - 1])
            New_Value_epsilon_Greedy=Value_Epsilon_Greedy[i-1]+(1/i)*(r_epsilon_Greedy-Value_Epsilon_Greedy[i-1])
            New_Value_epsilon_Greedy2=Value_Epsilon_Greedy2[i-1]+(1/i)*(r_epsilon_Greedy2-Value_Epsilon_Greedy2[i-1])
            Value_Epsilon_Greedy.append(New_Value_epsilon_Greedy)
            Value_Epsilon_Greedy2.append(New_Value_epsilon_Greedy2)
            Value_UCB2.append(New_Value_UCB2)
            Value_UCB.append(New_Value_UCB)
            update_epsilon_Greedy(Q_UCB2, i4, r_UCB2, Counter_UCB2[i4], 0)
            update_epsilon_Greedy(Q_UCB, i3, r_UCB, Counter_UCB[i3], 0)
            update_epsilon_Greedy(Q_epsilon_Greedy,i1,r_epsilon_Greedy,Counter_epsilon_Greedy[i1],0)
            update_epsilon_Greedy(Q_epsilon_Greedy2,i0,r_epsilon_Greedy2,Counter_epsilon_Greedy2[i0],0)
            r_Greedy = implement_action(Q_Ground[i2], varience)
            New_Value_Greedy = Value_Greedy[i - 1] + (1 / i) * (r_Greedy - Value_Greedy[i - 1])
            Value_Greedy.append(New_Value_Greedy)
            update_epsilon_Greedy(Q_Greedy, i2, r_Greedy, Counter_Greedy[i2], 0)
        Average_V_UCB2.append(Value_UCB2)
        Average_V_UCB.append(Value_UCB)
        Average_V_epsilon_Greedy.append(Value_Epsilon_Greedy)
        Average_V_epsilon_Greedy2.append(Value_Epsilon_Greedy2)
        Average_V_Greedy.append(Value_Greedy)
    Value_Epsilon_Greedy=Average(Average_V_epsilon_Greedy)
    Value_Epsilon_Greedy2 = Average(Average_V_epsilon_Greedy2)
    Value_Greedy=Average(Average_V_Greedy)
    Value_UCB = Average(Average_V_UCB)
    Value_UCB2 = Average(Average_V_UCB2)
    Graph("Comparision Of different Bandit Algorithms with Variance: "+str(varience), Value_Greedy, Value_Epsilon_Greedy,Value_Epsilon_Greedy2, Value_UCB,Value_UCB2, [x for x in range(0,1000)])
    print(Value_UCB)
    print(Value_UCB2)





# Implements the epsilon greedy alg
def epsilon_Greedy(Q_list,n,epsilon):
    i=np.random.uniform(0,1)
    bool=False
    if(i<=epsilon):
        bool=True
    j=0
    if(bool==False):
        j=Max_index_List(Q_list)
    else:
        j=np.random.randint(0,len(Q_list))
    return j

# This update the value list for epsilon Greedy and non epsilon greedy
def update_epsilon_Greedy(Q,i,new_target,n,alpha):
    Q[i]=Q[i]+(1/n)*(new_target-Q[i])


def deleteContent(fName):
    with open(fName, "w"):
        pass

# return the index of the maximum element in the list.
def Max_index_List(Q):
    max=-10
    i=-1
    j=0
    for q in Q:
        if(q>max):
            max=q
            i=j
        j+=1
    return i

# implements upper bound confidence method
def UCB(Q,n,counter,c):
    New_Q=[]
    i=0
    for q in Q:
        if(counter[i]==0):
            return i
        else:
            New_Q.append(q+c*math.sqrt(math.log(n)/counter[i]))
            i+=1
    return Max_index_List(New_Q)

def Average(List):
    Output=[]
    for i in range(len(List[0])):
        Sum=0
        for j in range(len(List)):
            Sum+=List[j][i]
        Output.append(Sum/(j+1))
    return Output

#implements the action of bandit and returns the value
def implement_action(mean,variance):
    return np.random.normal(mean,variance)

if __name__ == '__main__':
    main()
