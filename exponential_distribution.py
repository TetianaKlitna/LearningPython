# Exponential distribution - probability of time between 
# lambda - average number of events per time interval Poisson events - continious(time)
# lambda(rate) - expected value of Exponential distribution 1/lambda
# avarage 1 ticket created every 2 min, lambda = 0.5

# On average, he responds to 1 request every 2.5 hours. 
# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes < 1 hour
print(expon.cdf(1, scale=2.5))

# Print probability response takes > 4 hours
print(1- expon.cdf(4, scale=2.5))

# Print probability response takes 3-4 hours
print(expon.cdf(4, scale = 2.5) - expon.cdf(3, scale = 2.5))

# t-distribution - like shape normal, but tails thicker
#degree of freedom(df) affects how tails thicker
# lower df - thiker tails
# high df - t-distribution closer to normal distribution

#log_normal - distribution -variable, wthich log normally distrubuted
# examples : length of chess games; blood pressure of adults