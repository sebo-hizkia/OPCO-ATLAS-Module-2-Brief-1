import pandas as pd
import seaborn as sns
import missingno as msno
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Qt5Agg")

# Charger le CSV
df = pd.read_csv("fichier-de-donnees-numeriques.csv")

# Description du fichier
print(f"Description : {df.describe}")

# Affichage de la distribution des données (les données sont toutes numériques)
plt.figure(figsize=(15, 12))

for i, col in enumerate(df.columns, 1):
    plt.subplot(3, 3, i)     # 3x3 pour 9 colonnes
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f"Distribution de {col}")
    plt.xlabel(col)
    plt.ylabel("Fréquence")

plt.tight_layout()
plt.show()

# Heatmap de corrélation
plt.figure(figsize=(10, 8))
corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matrice de corrélation")
plt.show()

# Visualiser la matrice des valeurs manquantes
msno.matrix(df)
plt.show()

# Visualiser le barplot des colonnes manquantes
msno.bar(df)
plt.show()

# Nombre de lignes avec au moins une valeur manquante
missing_line = df.isna().any(axis=1).sum()
total_line = df.shape[0]
print(f"Nb lignes manquantes : {missing_line} / {total_line}")

# Boxplot pour détecter les outliers dans les revenus
sns.boxplot(x=df['revenu_estime_mois'])
plt.show()


