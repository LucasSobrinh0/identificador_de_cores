import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Dados de treino
data = {
    'Color': ['Red', 'Green', 'Blue', 'Yellow', 'Magenta', 'Cyan', 'White', 'Black', 'Orange', 'Purple'],
    'R': [255, 0, 0, 255, 255, 0, 255, 0, 255, 128],
    'G': [0, 255, 0, 255, 0, 255, 255, 0, 165, 0],
    'B': [0, 0, 255, 0, 255, 255, 255, 0, 0, 128]
}

df_colors = pd.DataFrame(data)
X_train = df_colors[['R', 'G', 'B']]
y_train = df_colors['Color']

# Modelo KNN
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)

def predict_color(r, g, b):
    # Criar um DataFrame para a entrada com nomes de colunas apropriados
    input_features = pd.DataFrame([[r, g, b]], columns=['R', 'G', 'B'])
    predicted_color = model.predict(input_features)
    return predicted_color[0]
