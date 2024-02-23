# Binomial distribution - probability distribution of the number of success in seq od independent trials
# n - total number of trials
# p - probability of success
# binom.rvs(, p, n)
# Expected value n * p

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate 52 weeks of 3 deals
deals = binom.rvs(n=3,p=0.3,size = 52)
print(np.mean(deals))

#What is propability to close all 3 deals per week?

# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3, 3, 0.3)
print(prob_3)

# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1, 3, 0.3)
print(prob_less_than_or_equal_1)

# Probability of closing > 1 deal out of 3 deals
prob_greater_than_1 = 1 - binom.cdf(1, 3, 0.3)
print(prob_greater_than_1)
