#first certain assets need to be imported to pyscripter
#numpy for arrays and matrix manipulation
#matplotlib to graph results
#random to be able to generate random numbers required for a random walk
#math to be able to use pi and sin and cos functions required for a random direction

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random
import math

#create global variable n, also used as the number of steps
n = 10000

#define a function randomwalk that can be called later in code
def randomwalk():
        # define number of steps - local variable
        n = 10000

        # create two arrays for x and y co-ordinates equal to n
        x = np.zeros(n)
        y = np.zeros(n)

        # theta changes with every step to give a different direction
        # creates a random step in each possible direction
        for i in range(1,n):
            theta = 2*math.pi*random.random()

            x[i] = x[i-1] + math.cos(theta)
            y[i] = y[i-1] + math.sin(theta)

        r2 = x**2 + y**2
        return r2

#set the number of repetitions
N = 100

#initialise numpy array for mean square displacement of the walk
mat = np.zeros((N,n))

#take the r2 values and set them as the squared distance (SqDi for short)
#Save the SqDi in an array
for i in range(1,N):
    Sqdi = randomwalk()
    mat[i,:] = Sqdi

#calculate the mean square displacement and save them in an array
MSD = np.zeros(n)
for j in range(n):
    MSD[j] = np.mean(mat[:,j])

#add a title and axis labels to the graph
plt.title('Displacement against n')
plt.xlabel(" n (steps) ")
plt.ylabel(" Squared displacement (X squared + Y squared) ")

#add a legend to highlight the average mean square displacement on the graph
#and each run plotted
black_patch = mpatches.Patch(color = 'black', label = 'Mean square displacement over all runs')
palevioletred_patch = mpatches.Patch(color = 'palevioletred', label = 'run 5')
pink_patch = mpatches.Patch(color = 'pink', label = 'run 10')
hotpink_patch = mpatches.Patch(color = 'hotpink', label = 'run 25')
cornflowerblue_patch=mpatches.Patch(color = 'cornflowerblue', label = 'linear regression')
plt.legend(handles=[black_patch] + [palevioletred_patch] + [pink_patch] + [hotpink_patch] + [cornflowerblue_patch] , loc = 2)

#plot of the SqDi of the 5th, 10th and 25th run
plt.plot(range(n),mat[5,:], color = 'palevioletred')
plt.plot(range(n),mat[10,:], color = 'pink')
plt.plot(range(n),mat[25,:], color = 'hotpink')

#plot of the average mean square displacement over all runs in a color
#that doesn't clash so it is easy to identify
plt.plot(range(n),MSD, color = 'black')

#plot the errorbars in the MSD, setting an error bar to every 1000 n
plt.errorbar(range(n), MSD, (np.std(MSD)/np.sqrt(N)), color = 'blue', errorevery=1000)

#compute the line of best fit of the MSD and plot it
fit = np.polyfit(range(n), MSD, 1)
fit_fn = np.poly1d(fit)
gradient, Yint = np.poly1d(fit)

#this line of code works intermittently, PyScripter wants x and y to be in the
#same dimentions despite it already working. Adding or removing brackets around 'range(n)'
#solves 'x and y must have same first dimention' error message
plt.plot(range(n), ((range(n)*gradient)+Yint), color = 'cornflowerblue')

#print the line of best fit, giving the gradient and the Y intercept
print(fit_fn)
#add the equation of the line of best fit to a fixed location on the graph
plt.text(500, 10000, fit_fn, color = 'cornflowerblue')

#show the plot
plt.show()



