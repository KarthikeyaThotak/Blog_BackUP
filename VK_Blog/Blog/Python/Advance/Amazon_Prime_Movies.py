import numpy as np
import pandas as pd
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("/home/vk/Web_dev/VK_Blog/Blog/Python/Advance/data.csv")
print(data.head())

print(data.isnull().sum())


data = data[["show_id", "type", "title", "release_year", "duration", "listed_in", "description"]]

print(data.head())

data = data.dropna()


