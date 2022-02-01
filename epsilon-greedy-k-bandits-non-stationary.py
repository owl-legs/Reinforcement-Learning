#Epsilon-greedy k bandits simulation

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn import linear_model

# `k` : number of bandits or actions
# `T` : how many actions taken (e.g. how long to simulate over)
# `epsilon` : with a probability of epsilon, we will choose to explore the available actions that do not have the highest reward/selection ratio [Qt_A] with equal probability.
  # Note that with a probability of 1 - epsilon, we will choose to exploit our current knowledge and greedily select the action having the highest reward/selection ratio [Qt_A]

def simulate_bandits(k, T, epsilon):
  
    reward_distribution_means = np.random.normal(loc = 0, scale = 1.0, size = k)
    
    rewards = []

    sum_rewards = [0] * k

    action_count = [0] * k

    Qt_A = [0] * k

    action = int(np.random.randint(0, k))

    for dt in range(T):

        rwd = np.random.normal(loc = reward_distribution_means[action], scale = 1.0, size = 1)

        rewards.append(rwd)

        sum_rewards[action] += rwd

        action_count[action] += 1

        Qt_A[action] = (sum_rewards[action] / action_count[action])

        if np.random.uniform(size = 1) <= epsilon:

            #explore:

            max_index = np.argmax(Qt_A)

            action = int(np.random.choice(list(set(range(k)) - {max_index})))

        else:

            #exploit:

            action = np.argmax(Qt_A)
            
        reward_distribution_means + list(np.random.normal(loc = 0.0, scale = 0.01, size = k))
            
    return(rewards)

y = simulate_bandits(k = 10, T = 100, epsilon = 0.01)
x = range(len(y))

x = np.asarray(x).reshape(-1,1)
y = np.asarray(y).reshape(-1,1)

lr = linear_model.LinearRegression()
fitted = lr.fit(x, y)

y_pred = fitted.coef_[0]*x

plt.plot(y)
plt.plot(y_pred, label = 'line of best fit')
plt.legend(loc = 'upper right')
plt.ylabel('Reward')
plt.xlabel('Time')
