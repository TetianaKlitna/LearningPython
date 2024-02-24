# corr koef - relation between 2 variables [-1; 1] - strength of relationship
# 1- strong relationship, 0.75 data more spread out, but also good corr, 0.56 - moderate corr(medium)
# 0.21 (week corr), 0.04 - no relationship
# + - x increases and y increases
# - x increases and y decreases
# x corr y = y corr x 
# corr cannot be 0 !
# diffrenet variation to calc corr, example  Pearson product-moment corr (r)
# visual scatter plot, or bar distribution data - - can apply log when  corr!!! corr only for linear relations
#Transformations help to do relation more linear:
# log , sqrt, 1/x
# Combination: log(x) and log(y); sqrt(x) and 1/y
# Correlation  is not imply  Causation x corr y NOT x causes y
# spurious corr!

import seaborn as sns

# Create a scatterplot of happiness_score vs. life_exp and show
sns.scatterplot(x = 'life_exp', y = 'happiness_score', data = world_happiness)
# Show plot
plt.show()

# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x = 'life_exp', y = 'happiness_score', data = world_happiness, ci = None)

# Show plot
plt.show()

# Correlation between life_exp and happiness_score
cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])
print(cor)

sns.scatterplot(x = 'gdp_per_cap', y = 'life_exp', data = world_happiness)

# Show plot
plt.show()

# Correlation between gdp_per_cap and life_exp
cor = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])
print(cor)

# Scatterplot of happiness_score vs. gdp_per_cap
sns.scatterplot(x = 'gdp_per_cap', y = 'happiness_score', data = world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['happiness_score'].corr(world_happiness['gdp_per_cap'])
print(cor)

# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Scatterplot of happiness_score vs. log_gdp_per_cap
sns.scatterplot(x = 'log_gdp_per_cap', y = 'happiness_score', data = world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)

# Scatterplot of grams_sugar_per_day and happiness_score
sns.scatterplot(x = 'grams_sugar_per_day', y = 'happiness_score', data = world_happiness)
plt.show()

# Correlation between grams_sugar_per_day and happiness_score
# Increased sugar consumption is associated with a higher happiness score.
cor = world_happiness['grams_sugar_per_day'].corr(world_happiness['happiness_score'])
print(cor)
#Controlled(random) and observational(smoke or not smoke)

#Cross-sectional studies are observational studies that analyze data from a population at a single point in time.
#Longitudinal studies employ continuous or repeated measures to follow particular individuals over prolonged periods of time—often years or decades.