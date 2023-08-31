# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:35:29 2023

@author: kevin.wu
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import datasets
from sklearn import manifold
data = datasets.fetch_openml(
'mnist_784',
version=1,
return_X_y=True
)
pixel_values, targets = data
targets = targets.astype(int)
single_image = pixel_values.values[1, :].reshape(28, 28)
plt.imshow(single_image, cmap='gray')
tsne = manifold.TSNE(n_components=2, random_state=42)
transformed_data = tsne.fit_transform(pixel_values.values[:7000, :])
tsne_df = pd.DataFrame(
np.column_stack((transformed_data, targets[:7000])),
columns=["x", "y", "targets"]
)
tsne_df.loc[:, "targets"] = tsne_df.targets.astype(int)
grid = sns.FacetGrid(tsne_df, hue="targets", size=8)
grid.map(plt.scatter, "x", "y").add_legend()
