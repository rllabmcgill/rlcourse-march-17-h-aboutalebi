#we plot the results here

import numpy as np
import matplotlib.pyplot as plt

class Graph:

    def __init__(self,title,List1,List2,List3,List4,List5,xAxis):
        self.graphic( title,List1, List2,List3,List4, List5,xAxis)


    def graphic(self,title,List1,List2,List3,List4,List5,xAxis):
        plt.axis(xmax=1000,xmin= -50)
        plt.title(title)
        plt.xlabel("Number Of Step")
        plt.ylabel("Average Reward")
        firstLine=plt.plot(xAxis,List1,label="Greedy")
        SecondLine=plt.plot(xAxis,List2,label="epsilon=0.01")
        ThirdLine = plt.plot(xAxis, List3, label="epsilon=0.1")
        FourthLine = plt.plot(xAxis, List4, label="UCB with c=0.01")
        FifthLine = plt.errorbar(xAxis, List5,  label="UCB with c=0.1")
        # FourthLine = plt.errorbar(xAxis, Mean4, STD4, fmt='--o', label="Fourth",color='y')
        plt.legend(loc='lower right')
        plt.show()

