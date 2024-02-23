# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Create histogram of co2_emission for food_category 'beef'
beef_consumption = food_consumption[food_consumption['food_category'] == 'beef']
plt.hist(beef_consumption['co2_emission'])
# Show plot
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
eggs_consumption = food_consumption[food_consumption['food_category'] == 'eggs']
plt.hist(eggs_consumption['co2_emission'])
# Show plot
plt.show()