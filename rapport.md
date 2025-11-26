# OPCO-ATLAS-Module-1-Brief-2 - Rapport de Synthèse – Nettoyage de Données Numériques (FastIA)

## 1. Description générale du jeu de données

Le dataset contient **10 000 lignes et 9 colonnes**, exclusivement numériques.  
Colonnes initiales :

- age  
- taille  
- poids  
- revenu_estime_mois  
- historique_credits  
- risque_personnel  
- score_credit  
- loyer_mensuel  
- montant_pret  

Une première analyse a révélé :

- de nombreuses valeurs manquantes (jusqu'à 53 % dans certaines colonnes)  
- des outliers sur plusieurs variables  
- des asymétries dans certaines distributions

---

## 2. Analyse Exploratoire

### 2.1 Distribution  
Les histogrammes montrent :

- `revenu_estime_mois` très asymétriques
- `loyer_mensuel` présente une forte dispersion
- `taille` et `poids` contiennent des valeurs extrêmes  

### 2.2 Matrice de corrélation  
La heatmap révèle :

- Corrélation modérée entre `revenu_estime_mois` et `montant_pret`
-
- Faible valeur analytique des colonnes très incomplètes  

### 2.3 Valeurs manquantes  
Via missingno :

- 3 colonnes fortement incomplètes :
  - `historique_credits` : 52.9 %
  - `score_credit` : 53.0 %
  - `loyer_mensuel` : 29 %
- 8 446 lignes comportent au moins une valeur manquante

Conclusion : **supprimer les lignes manquantes détruirait 84 % du dataset**, donc suppression des colonnes préférée.

---

## 3. Nettoyage du Dataset

### 3.1 Suppression des colonnes très incomplètes  
Seuil retenu : 20 % de valeurs manquantes.

Colonnes supprimées :

- `historique_credits`
- `score_credit`
- `loyer_mensuel`

Passage de **9 → 6 colonnes**.

### 3.2 Gestion des valeurs manquantes restantes  
Après suppression :  
✔ **aucune valeur NaN** dans le dataset — aucune imputation nécessaire.

### 3.3 Filtrage des outliers  
Méthode appliquée : **IQR sur toutes les colonnes**.

Résultat :

- Avant : 10 000 lignes  
- Après : 9 751 lignes  
→ **249 outliers supprimés (2.49 %)**

---

## 4. Standardisation des données

Méthode utilisée : **StandardScaler()**

Objectifs :

- moyenne = 0  
- écart-type = 1  
- préparation au Machine Learning

Dataset final sauvegardé dans :

```
data/dataset_standardized.csv
```

---

## 5. Résultat final

| Étape | Résultat |
|-------|----------|
| Colonnes initiales | 9 |
| Colonnes finales | 6 |
| Lignes initiales | 10 000 |
| Lignes après nettoyage | 9 751 |
| Valeurs manquantes | 0 |
| Outliers | filtrés |
| Standardisation | effectuée |

Le dataset final est donc :

- propre  
- normalisé  
- sans valeurs manquantes  
- sans colonnes inutiles  
- compatible avec un pipeline d’IA  

---

## 6. Justification des choix

| Décision | Justification |
|----------|---------------|
| Suppression colonnes >20% de nulls | Évite la perte de 8 446 lignes |
| Filtrage IQR | Simple et adapté au dataset |
| Pas d’imputation | Plus de null/NaN après suppression des colonnes |
| Standardisation | Nécessaire pour la plupart des modèles ML |
| Pipeline reproductible | Conforme au brief |

---

## 7. Conclusion

Le dataset fourni a été :

- exploré  
- nettoyé  
- standardisé  
- documenté  

Le fichier final a été sauvegardé dans __data/dataset_standardized.csv__.

