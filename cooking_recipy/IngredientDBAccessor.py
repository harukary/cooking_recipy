import pandas as pd
from scipy.spatial import distance_matrix
import random

class IngredientDBAccessor:
    def __init__(self,file):
        self.df = pd.read_csv('database/'+file, index_col=0)
        df_n = self.df.drop(['ingredient'], axis=1)
        df_normalized = (df_n - df_n.min()) / (df_n.max() - df_n.min())
        self.distance_matrix = pd.DataFrame(distance_matrix(df_normalized.values, df_normalized.values), index=df_normalized.index, columns=df_normalized.index)
    def get_random_substitution(self,ingredient):
        candidates = self.distance_matrix[ingredient].sort_values()[1:11]
        weights = [1/c if c != 0 else 100000 for c in candidates.to_list() ]
        for w,name in zip(weights,candidates.index):
            print(name, w)
        id = random.choices(candidates.index.to_list(), k=1, weights=weights)[0]
        return id.replace('\u3000',' '), 1/candidates[id]