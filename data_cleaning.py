import pandas as pd

df = pd.read_csv("merge_dataset.csv")
print(df.shape)
del df['star_name']
del df['distance']
del df['mass']
del df['radius']
del df['lum']
df.dropna()

df.to_csv("final.csv")