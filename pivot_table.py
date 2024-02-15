# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(index = "type", values = "weekly_sales")

# Print mean_sales_by_type
print(mean_sales_by_type)

# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(index = "type", values = "weekly_sales", aggfunc = [np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(index = "type", values = "weekly_sales", columns = "is_holiday")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value = 0, margins = True))