import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('EDGE_GEOCODE_PUBLICLEA_1718.csv')

categories = data['NAME']
values = data['CNTY']

plt.bar(categories, values)
plt.xlabel('School Districts')
plt.ylabel('Number of Students')
plt.title('Number of Students per School District')
plt.xticks(rotation=90)

# Show the graph
plt.show()

print("The graph indicates the number of students per school district.")
