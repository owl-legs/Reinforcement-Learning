#Action-Method w Epsilon parameter for K Bandits

def simulate_bandits_v2(k, T, epsilon):
    
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

        Qt_A[action] = Qt_A[action] + (1/action_count[action])*(rwd - Qt_A[action])
        
        #(sum_rewards[action] / action_count[action])

        if np.random.uniform(size = 1) <= epsilon:

            #explore:

            max_index = np.argmax(Qt_A)

            action = int(np.random.choice(list(set(range(k)) - {max_index})))

        else:

            #exploit:

            action = np.argmax(Qt_A)
                        
    return(rewards)
  
y = simulate_bandits_v2(k = 10, T = 100, epsilon = 0.01)
x = range(len(y))

x = np.asarray(x).reshape(-1,1)
y = np.asarray(y).reshape(-1,1)

lr = linear_model.LinearRegression()
fitted = lr.fit(x, y)

y_pred = fitted.coef_[0]*x

plt.plot(y)
plt.plot(y_pred)
plt.ylabel('Reward')
plt.xlabel('Time')
