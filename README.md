# Détecteur d'Anomalies Boursières – Isolation Forest

## 📌 Description du projet

Ce projet consiste à développer une **application de Data Mining non supervisée** destinée à la **détection d’anomalies dans les cours de clôture boursiers**.

L’algorithme principal utilisé est **Isolation Forest**, une méthode adaptée aux données réelles et non étiquetées.  
Une anomalie peut représenter :
- un **pic anormal**
- une **chute brutale du prix**
- une valeur aberrante liée à une erreur ou à un événement exceptionnel

Le projet combine **analyse de données**, **apprentissage automatique**, **API backend** et **visualisation web interactive**.

---

## 🎯 Problématique

Les séries temporelles financières contiennent souvent des valeurs atypiques susceptibles de :
- fausser les analyses statistiques
- perturber les modèles prédictifs
- induire de mauvaises décisions

L’objectif du projet est donc de :
- détecter automatiquement ces anomalies
- les rendre interprétables via une visualisation graphique
- fournir des résultats exploitables pour l’analyse

---
### 🧠 Apprentissage non supervisé

Le projet repose sur un **apprentissage non supervisé**, ce qui signifie :
- Absence de jeu de données annoté
- Découverte automatique de la structure des données
- Identification des comportements normaux sans connaissance préalable des anomalies

Isolation Forest isole les points atypiques en construisant des arbres aléatoires.  
Les observations qui sont isolées rapidement sont considérées comme des anomalies.

## 🧠 Approche Data Mining

Le projet repose sur une **approche de Data Mining non supervisée** :

- Aucune donnée annotée n’est disponible
- Le modèle apprend uniquement à partir des données historiques
- Les observations rares et isolées sont identifiées comme anomalies

L’algorithme **Isolation Forest** isole progressivement les points atypiques à l’aide de partitions aléatoires.  
Les points isolés rapidement sont considérés comme des anomalies.

Bien qu’il ne s’agisse pas d’un algorithme de clustering classique, le modèle effectue :
- un **regroupement implicite** des données normales
- une **classification binaire implicite** :
  - `1` : observation normale  
  - `-1` : anomalie  

Les mêmes données historiques sont utilisées pour :
- l’apprentissage du modèle
- la détection des anomalies  

Ce choix est cohérent avec les scénarios réels de **détection d’anomalies non supervisée**.

---

## 🧠 Méthodologie

### 1. Collecte des données
- Récupération des cours de clôture boursiers via l’API `yfinance`
- Période configurable (ex : 2018 – 2025)

### 2. Prétraitement
- Suppression des valeurs manquantes
- Conversion des dates et des prix
- Sélection de la variable `Close`
- Standardisation des données avec `StandardScaler`

### 3. Modélisation – Isolation Forest
- Entraînement d’un modèle Isolation Forest par symbole boursier
- Détection des anomalies (`-1`) et des valeurs normales (`1`)
- Sauvegarde du modèle et du scaler pour chaque symbole

### 4. Visualisation et restitution
- Génération de graphiques avec `matplotlib`
- Affichage des anomalies sous forme de points rouges
- Interface web React permettant :
  - la sélection du symbole
  - le choix de la période
  - le téléchargement des graphiques

---
Résultats

Courbe du cours de clôture

Anomalies affichées sous forme de points rouges

Nombre total d’anomalies détectées

Export des données :

Images PNG

## ✅ Valeur ajoutée du projet

Ce projet illustre :
- l’application concrète du **Data Mining non supervisé**
- l’intégration complète du pipeline de données
- l’exploitation de données financières réelles
- la mise en valeur des résultats via une interface interactive

Il constitue un exemple complet et pédagogique d’utilisation du Data Mining dans le domaine financier.


## 🛠️ Technologies utilisées

### Backend
- Python
- FastAPI
- Pandas
- scikit-learn
- yfinance
- joblib
- matplotlib

### Frontend
- React
- Tailwind CSS
- Lucide Icons

### Stockage & Export
- Modèles sauvegardés (`.pkl`)
- Données CSV
- Export Excel (`.xlsx`)
- Images PNG

---

## 🚀 Installation

### Prérequis
- Python **3.10+**
- Node.js **18+**
- npm ou yarn

---
### 🔹 Backend (FastAPI)

#### 1. Cloner le projet

git clone <lien-du-repo>
cd fastapi-anomaly
---

### 2.installer les dépendances

pip install -r requirements.txt


### 3.Lancer le serveur
uvicorn app.main:app --reload

### 🔹 Frontend (React)
### 1. Accéder au dossier frontend
cd frontend

### 2.installer les dépendances
npm install

### 3.Lancer l'application
npm start



## 🎥 Démonstration vidéo
<video width="600" controls>
  <source src="demo.mp4" type="video/mp4">
  Votre navigateur ne supporte pas la lecture de vidéos.
</video>




