# Poisson distribution - events happens in certain rate, but completely random - descrete distribution
# lambda - average number of events per time interval

# Import poisson from scipy.stats
from scipy.stats import poisson

# Probability of 5 responses
#average 4
prob_5 = poisson.pmf(5,4)
print(prob_5)

# Probability of 5 responses
#average 5.5
prob_coworker = poisson.pmf(5, 5.5)
print(prob_coworker)

# Probability of 2 or fewer responses
prob_2_or_less = poisson.cdf(2, 4)
print(prob_2_or_less)

# Probability of > 10 responses
prob_over_10 = 1 - poisson.cdf(10, 4)
print(prob_over_10)