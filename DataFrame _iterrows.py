# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# 1.)Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))
    cars.loc[label, "COUNTRY"] = row["country"].upper()

# 2.) Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print cars
print(cars)
