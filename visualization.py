# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())


# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

print(nb_sold_by_size)

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(x= "size", y = "nb_sold", kind = "bar")
# Show the plot
plt.show()