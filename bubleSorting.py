#!/usr/bin/env python3.9
import matplotlib.pyplot as plt
import random
from datetime import datetime
import time

def buble_sort(unsorted):    
    for a in range(len(unsorted)):
        for b in range(len(unsorted)):
            if(unsorted[a]<unsorted[b]):
                tmp=unsorted[a]
                unsorted[a]=unsorted[b]
                unsorted[b]=tmp
        print ('sorting..')
        ax.clear()
        ax.plot(subjects, lista)       
        plt.draw()
        plt.pause(1)
    return unsorted

def selection_sort(unsorted):        
    for x in range(len(unsorted)-1):        
        if(unsorted[x]>unsorted[x+1]):
            unsorted[x],unsorted[x+1]=unsorted[x+1],unsorted[x]        
    return unsorted

if __name__ == "__main__":    
    maxvalue=10
    lista=[]
    subjects = []
    for l in range(0,maxvalue):
        valor=random.randint(0,maxvalue)
        lista.append(valor)    
        subjects.append(str(l))
    print(lista)
    print('----------------------------------------')
    fig, ax = plt.subplots()
    ax.plot(subjects, lista)
    plt.show(block=False)
    plt.draw()    
    print(buble_sort(lista))
    print(input('press key to continue'))