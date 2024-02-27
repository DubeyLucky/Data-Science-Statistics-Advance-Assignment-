#!/usr/bin/env python
# coding: utf-8

# Q1. What is the Probability density function?

# probability density function (PDF), in statistics, a function whose integral is calculated to find probabilities associated with a continuous random variable.

# Q2. What are the types of Probability distribution?

# There are 6 common Probability distribution:
#     1.Bernoulli
#     2.Uniform
#     3.Binomial
#     4.Normal
#     5.Poisson
#     6.Exponential Distribution

# Q3. Write a Python function to calculate the probability density function of a normal distribution with
# given mean and standard deviation at a given point.

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
 
# Creating a series of data of in range of 1-50.
x = np.linspace(1,50,200)
 
#Creating a Function.
def normal_dist(x , mean , sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density
 
#Calculate mean and Standard deviation.
mean = np.mean(x)
sd = np.std(x)
 
#Apply function to the data.
pdf = normal_dist(x,mean,sd)
 
#Plotting the Results
plt.plot(x,pdf , color = 'red')
plt.xlabel('Data points')
plt.ylabel('Probability Density')


# Q4. What are the properties of Binomial distribution? Give two examples of events where binomial
# distribution can be applied.

# the binomial distribution is the discrete probability distribution that gives only two possible results in an experiment, either Success or Failure. For example, if we toss a coin, there could be only two possible outcomes: heads or tails, and if any test is taken, then there could be only two results: pass or fail. 

# Q7. How Binomial distribution different from Poisson distribution?

# Binomial distribution is the one in which the number of outcomes are only two, that is success or failure. Example of binomial distribution: Coin toss.
#     
#     
# Poisson distribution is the one in which the number of possible outcomes has no limits.

# Q9. How mean and variance are related in Binomial distribution and Poisson distribution?

# The mean and variance of the Binomial Distribution are determined by the number of trials and the probability of success, while the mean and variance of the Poisson Distribution are both equal to the rate parameter

# Q10. In normal distribution with respect to mean position, where does the least frequent data appear?

# This means that most of the observed data is clustered near the mean, while the data become less frequent when farther away from the mean. The resultant graph appears as bell-shaped where the mean, median, and mode are of the same values and appear at the peak of the curve.

# In[ ]:




