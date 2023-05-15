import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("star_data.csv")

star_name = df['Star name'].tolist()
mass = df['Mass'].tolist()
radius = df['Radius'].tolist()
distance = df['Distance'].tolist()
gravity = df['Gravity'].tolist()

plt.bar(star_name, mass)
plt.xticks(rotation=90)
plt.xlabel("Star Name")
plt.ylabel("Mass (Solar Mass)")
plt.title("Star Name vs Mass")
plt.show()

plt.bar(star_name, radius)
plt.xticks(rotation=90)
plt.xlabel("Star Name")
plt.ylabel("Radius (Solar Radius)")
plt.title("Star Name vs Radius")
plt.show()

plt.bar(star_name, distance)
plt.xticks(rotation=90)
plt.xlabel("Star Name")
plt.ylabel("Distance (Parsecs)")
plt.title("Star Name vs Distance")
plt.show()

plt.bar(star_name, gravity)
plt.xticks(rotation=90)
plt.xlabel("Star Name")
plt.ylabel("Gravity (m/s^2)")
plt.title("Star Name vs Gravity")
plt.show()
