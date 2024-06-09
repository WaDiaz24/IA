# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Cargar el conjunto de datos de iris
iris = load_iris()
X = iris.data  # características

# Aplicar el algoritmo K-means
kmeans = KMeans(n_clusters=3, random_state=42)  # Queremos agrupar en 3 clusters
kmeans.fit(X)

# Obtener las etiquetas de los clusters
labels = kmeans.labels_

# Evaluar los resultados visualmente usando PCA para reducir la dimensionalidad a 2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Crear un DataFrame con los resultados para una visualización más sencilla
df = pd.DataFrame(data=X_pca, columns=['PCA1', 'PCA2'])
df['Cluster'] = labels

# Visualizar los clusters
plt.figure(figsize=(8, 6))
colors = ['r', 'g', 'b']
for cluster in range(3):
    cluster_data = df[df['Cluster'] == cluster]
    plt.scatter(cluster_data['PCA1'], cluster_data['PCA2'], c=colors[cluster], label=f'Cluster {cluster}')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title('Clusters de Iris usando K-means')
plt.legend()
plt.show()
