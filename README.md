# collatz-conjecture
#### Based off of Collatz's Conjecture, try your own positive input to disprove the conjecture by reaching zero or less 


# Collatz Conjecture

#### -Any positive integer fed into the Collatz's Conjecture will always end up in a 4-2-1 infinite loop

#### -When the integer is even, divide by two
#### -When the integer is odd, multiply by 3 and then add 1

#### -Feed the results back into the function until....
##### a.) you reach the 4-2-1 trap
##### b.) or you disprove Collatz's Conjecture by reaching 0 or a negative number



##### Example:     5 -> 16 -> 8 -> 4 -> 2 -> 1




# View cc_demo.pynb for demonstration on how to run class:

### 1.) pip install matplotlib if you don't already have it
### 2.) git clone this repo

### 3,) Start a new blank python file, jupyter notebook, or colab notebook 
### 4.) Whatever file or notebook your working on, make sure this clone repo lies in the same directory
### 5.) Type the following and run

##### from collatzsconjecture import CollatzConjecture
##### plot_1e6 = CollatzConjecture()
##### plot_1e6.plot_collatz_conjecture(16.5)
