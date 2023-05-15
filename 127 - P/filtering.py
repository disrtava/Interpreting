import pandas as pd
import matplotlib.pyplot as plt

x
stars_df = pd.read_csv('stars.csv')


stars_within_100_ly = stars_df[stars_df['distance'] <= 100]


selected_stars = stars_within_100_ly[(stars_within_100_ly['gravity'] >= 150) & (stars_within_100_ly['gravity'] <= 350)]


selected_stars.to_csv('selected_stars.csv', index=False)
