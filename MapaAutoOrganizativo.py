import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom

# Generar datos de entrenamiento
num_points = 10
m, b = 0.5, 2.5
data = np.random.rand(num_points, 2) * 10
labels = np.where(data[:, 1] > m * data[:, 0] + b, 1, -1)

# Función para visualizar los resultados del SOM
def plot_som(data, som, labels):
    plt.figure(figsize=(8, 8))
    plt.pcolor(som.distance_map().T, cmap='bone_r', alpha=0.6)
    plt.colorbar()

    for i, x in enumerate(data):
        w = som.winner(x)
        plt.plot(w[0] + 0.5, w[1] + 0.5, 'o', markerfacecolor='None', markeredgecolor='blue', markersize=12,
                 markeredgewidth=2)
        plt.text(w[0] + 0.5, w[1] + 0.5, str(labels[i]), color='black', fontsize=12, ha='center', va='center')

    plt.xticks(np.arange(0.5, som.get_weights().shape[0], 1), np.arange(0, som.get_weights().shape[0], 1))
    plt.yticks(np.arange(0.5, som.get_weights().shape[1], 1), np.arange(0, som.get_weights().shape[1], 1))
    plt.xlim([0, som.get_weights().shape[0]])
    plt.ylim([0, som.get_weights().shape[1]])
    plt.grid(True)

    # Agregar títulos
    plt.title('Mapa Auto Organizativo (SOM)')
    plt.xlabel('Neuronas en el eje x')
    plt.ylabel('Neuronas en el eje y')

    plt.show()

# Crear el SOM y entrenarlo
som = MiniSom(5, 5, 2, sigma=2.0, learning_rate=1.0, random_seed=42)
som.random_weights_init(data)
som.train_random(data, 1000)

# Visualizar los resultados del SOM
plot_som(data, som, labels)
