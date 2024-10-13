import pandas as pd
import matplotlib.pyplot as plt

# Input Data
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group by 'school_code' and calculate mean, min, and max for 'age'
age_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

# Plot a horizontal bar chart for the mean age
plt.figure(figsize=(8,6))
age_stats['mean'].plot(kind='barh', color='lightgreen')
plt.title('Mean Age by School Code')
plt.xlabel('Mean Age')
plt.ylabel('School Code')
plt.show()

# Displaying the result
print(age_stats)
