# Normal distribution - summetrical like bell
# robability never hits zero
# descibed by mean and std
#standart normal distribution: mean = 0 and std = 1
#[-1; 1] - 68%; [-2; 2] - 95%; [-3; 3] 99.7%

# Histogram of amount with 10 bins and show plot
amir_deals['amount'].hist(bins=10)
plt.show()

# Probability of deal < 7500 mean = 5000 std = 2000
prob_less_7500 = norm.cdf(7500, 5000, 2000)
print(prob_less_7500)

# Probability of deal > 1000
prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)
print(prob_over_1000)

# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)
print(prob_3000_to_7000)

# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25, 5000, 2000)
print(pct_25)