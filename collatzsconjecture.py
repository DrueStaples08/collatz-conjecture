# -*- coding: utf-8 -*-
"""CollatzsConjecture.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m708yUN9D3BYYLGS9gRKGKdpw7mIQhRu

#Collatz Conjecture

###-Any positive integer fed into the Collatz's Conjecture will always end up in a 4-2-1 infinite loop

###-When the integer is even, divide by two
###-When the integer is odd, multiply by 3 and then add 1

###-Feed the results back into the function until....
###a.) you reach the 4-2-1 trap
###b.) or you disprove Collatz's Conjecture by reaching 0 or a negative number



#####Example:     5 -> 16 -> 8 -> 4 -> 2 -> 1
"""

import matplotlib.pyplot as plt

class CollatzConjecture:




    def __init__(self):
        self.cc_results = []




    def collatz_conjecture(self, start): 
        cc_results = self.cc_results
        i = float(start) 
        trap = []

        if i > 0:
            while i > 0 and len(trap) != 2:
                if i == 2 or i == 4:
                    trap.append(i)
                    cc_results.append(i)
                    i = i / 2
                    #print(i)
                
                elif i % 2 == 0:
                    cc_results.append(i)
                    i = i / 2
                    #print(i)

                elif i == 1:
                    trap.append(i)
                    cc_results.append(i)
                    i = (3 * i) + 1
                    #print(i)
      
                else:
                    cc_results.append(i)
                    i = (3 * i) + 1
                    #print(i)

            else:
                cc_results.append(i)
                #print('Reached 4-2-1 Conjecture Trap')
                print('\n')

            return cc_results




    def plot_collatz_conjecture(self, start):
        y_values = self.collatz_conjecture(start)
        x_values = range(len(y_values))
        x_val = len(y_values) - 1
        print(f'Reached 4-2-1 Conjecture Trap in {x_val} steps starting from {y_values[0]}')
        print('\n')
        plt.figure(figsize=(10,7))
        plt.rcParams['axes.facecolor'] = 'black'
        plt.title('Collatz Conjecture', fontsize=20)
        plt.plot(x_values, y_values, 'r', label=f'{y_values[0]}')
        plt.xlabel('Steps Towards Conjecture Trap', fontsize=20)
        plt.ylabel('Conjecture Output from Each Step', fontsize=20)
        plt.legend(facecolor='white')
        plt.grid(color='cyan')
        plt.show()

'''
RUN EXAMPLE

#cc_example = CollatzConjecture()

#cc_example.plot_collatz_conjecture(100)


for a in range(1,10):
    #fig, ax = plt.subplots()
    #ax.plot(x, y)
    #ax.set_title('A single plot')
    cc_example_1 = CollatzConjecture()
    cc_example_1.plot_collatz_conjecture(a)
    #ax.plot(xyu.plot_collatz_conjecture(xyu.collatz_conjecture, a))
'''