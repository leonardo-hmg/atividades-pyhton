import numpy as np
import pandas as pd

# 1. Vetor com as idades fornecidas
idades = np.array([18, 21, 19, 22, 20])

# 2. Matriz 2x3 qualquer, imprimindo o shape e o elemento [1, 2]
matriz = np.array([[10, 20, 30], [40, 50, 60]])
print("Shape da matriz:", matriz.shape)
print("Elemento [1, 2]:", matriz[1, 2])

# 3. Transformação das idades numa Series com os nomes no índice
idades_serie = pd.Series(idades, index=["Ana", "Bruno", "Carla", "Diego", "Eva"])

# 4. Impressão da idade da Carla com loc
print("Idade da Carla:", idades_serie.loc["Carla"])

# 5. Filtro para idades iguais ou superiores a 21 anos
filtro_maiores_21 = idades_serie[idades_serie >= 21]
print("\nPessoas com 21 anos ou mais:")
print(filtro_maiores_21)