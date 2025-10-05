import numpy as np
import matplotlib.pyplot as plt
def histograph(rolls):
       ticks=range(1,7)
       labels=["1","2","3","4","5","6"]
       plt.hist(rolls,bins=np.arange(0.5,7.5),edgecolor='black',color='skyblue')
       plt.xticks(ticks,labels)
       plt.xlabel("Dice Face")
       plt.ylabel("frequency")
       plt.title("Histogram of Dicerolls")
       plt.show()
def rollthedice(n,type):
    if(type==1):
       rolls=np.random.randint(1,7,n)
       print("dice rolls:")
       for roll in rolls:
         print(roll)
       histograph(rolls)
    elif(type==2):
       randarray=np.random.randint(1,7,n*2)
       sumpairs=randarray.reshape(n,2)
       rolls=sumpairs.sum(axis=1)
       print("dice rolls:")
       for roll in rolls:
          print(roll)
       histograph(randarray)
   
n=int(input("how many times you want to roll"))
type=int(input("1 for 1 dice roll and 2 for 2 dice roll"))
rollthedice(n,type)