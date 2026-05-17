""" 
RISK CALCULATOR

Ce programme permet d'analyser un portefeuille composé d'actifs selectionnés

Fonctionnalités du programme :
- Télécharge les données historiques grâce à yfinance
- Calcul le rendement annualisé, la volatilité annualisée et le ratio de Sharpe de chaque actifs selectionnés
- Calcul le rendement, la volatilité et le ratio de Sharpe du portefeuille composé des actifs selectionnés et de leurs allocation
- Analyse la corrélation entre les actifs du portefeuille
- Permet de visualiser les performances et corrélations sur graphiques grâce à matplotlib

Auteur : Kylian BEAUDINOT
Date : Mai 2026
"""

# On importe les différentes bibliothèques dont nous avons besoins

import yfinance as yf # yfinance afin de récupérer les différentes valeurs des actifs en temps réel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # matplotlib pour illustrer graphiquement les différents exemples

# Création de la variable TICKERS, qui contient les symboles des actifs que nous allons étudier
# Possibilité de modifier la liste des actifs selectionnés selon vos préférences

TICKERS = ["NVDA" , "AAPL" , "AMZN" , "GOOGL" , "MC.PA" , "ASML.AS" , "TSM"]

# Création de la variable PERIOD, nous allons utiliser 1 an afin d'obtenir des données simples et fiables

PERIOD = "1y"

# Création de la variable WEIGHTS, qui permet de définir la répartition des actifs dans le portefeuille
# Possibilité de modifier l'allocation des actifs selectionnés selon vos préférences, mais le total doit être égal à 1

WEIGHTS = [0.15, 0.1, 0.1, 0.15, 0.15, 0.15, 0.2]

# Téléchargement de toutes les données nécessaires pour notre étude

print()
print("Téléchargement des données")
print()

# Définition d'une nouvelle variable data, qui contiendra toutes les données correspondantes aux actifs selectionnés

data = yf.download(TICKERS, period=PERIOD, progress = False)
data = data["Close"]
print(f"Données téléchargées sur {len(data)} jours")
print(f"Période allant du {data.index[0].date()} au {data.index[-1].date()}")
print()

# Calcul des rendements journaliers des actifs choisis
# Pour cela, on utilise pct_change qui est une fonction de pandas qui permet de calculer directement le rendement journalier de chaque actif
# Utilisation de dropna() qui permet de supprimer les valeurs manquantes
# Définition d'une variable returns qui contient tous les rendements des actifs étudiés

returns = data.pct_change(fill_method=None).dropna()

# ANALYSE PAR ACTION

print("Analyse par action :")
print()

# Création de la variable risk_free_rate, on utilise 4% comme référence

risk_free_rate = 0.04

# Création de la boucle pour calculer et afficher le rendement annualisé, la volatilité annualisée, et le ratio de Sharpe de chaque actifs selectionnés

for ticker in TICKERS:
    #Rendement annualisé
    annual_return = returns[ticker].mean()*252
    #Volatilité annualisée
    volatility = returns[ticker].std()*np.sqrt(252)
    #Ratio de Sharpe
    sharpe_ratio = (annual_return-risk_free_rate)/volatility
    print(f"{ticker}:")
    print(f"Le rendement annualisé de {ticker} est de {round(annual_return*100, 2)}%")
    print(f"La volatilité annualisée de {ticker} est de {round(volatility*100, 2)}%")
    print(f"Le ratio de Sharpe de {ticker} est de {round(sharpe_ratio, 2)}")
print()

# Création du portefeuille composé des actions et allocation choisies

print(f"Portefeuille composé des actifs selectionnés : {TICKERS}")
print()

# Allocation des actifs au sein du portefeuille
print("Allocation :")
for ticker, weight in zip(TICKERS, WEIGHTS):
    print(f"{ticker} : {round(weight*100, 1)}%")
print()
# Calcul du rendement du portefeuille

portfolio_return = sum(returns[ticker].mean()*252*w for ticker, w in zip(TICKERS, WEIGHTS))

# Calcul de la volatilité du portefeuille

portfolio_variance = 0
for i, ticker_i in enumerate(TICKERS):
    for j, ticker_j in enumerate(TICKERS):
        cov = returns[ticker_i].cov(returns[ticker_j])*252
        portfolio_variance += WEIGHTS[i]*WEIGHTS[j]*cov

portfolio_volatility = np.sqrt(portfolio_variance)

# Calcul du ratio de Sharpe du portefeuille

portfolio_sharpe = (portfolio_return-risk_free_rate)/portfolio_volatility

# Affichage des résultats du portefeuille

print("Analyse du portefeuille :")
print(f"Le rendement annualisé du portefeuille est de {round(portfolio_return*100, 2)}%")
print(f"La volatilité annualisée du portefeuille est de {round(portfolio_volatility*100, 2)}%")
print(f"Le ratio de Sharpe du portefeuille est de {round(portfolio_sharpe, 2)}")
print()

# Matrice de corrélation des actifs selectionnés

correlation = returns.corr()
print("La matrice de corrélation des actifs est :")
print(round(correlation, 2))
print()
# Illustration des résultats par des graphiques

print("Génération des graphiques")
print()
# Graphique de la performance relative de chaque actifs

plt.figure(figsize=(14, 5)) # Création de la zone d'affichage des graphiques

plt.subplot(1, 2, 1)

data_clean = data.dropna()
normalized_data = ((data_clean/data_clean.iloc[0])-1)*100

for ticker in TICKERS:
    plt.plot(normalized_data.index, normalized_data[ticker], label=ticker)

plt.title("Performance relative de chaque actifs sur 1 an ")
plt.xlabel("Date")
plt.ylabel("Évolution en %")
plt.legend()

# Graphique de la matrice de corrélation

plt.subplot(1, 2, 2)

im = plt.imshow(correlation, cmap = "coolwarm", vmin = -1, vmax = 1)
plt.colorbar(im)
plt.xticks(range(len(TICKERS)), TICKERS)
plt.yticks(range(len(TICKERS)), TICKERS)
plt.title("Matrice de corrélation des actifs")

# Ajout des valeurs dans les cases du graphique des corrélation pour plus de compréhension

for i in range(len(TICKERS)):
    for j in range(len(TICKERS)):
        plt.text(j, i, f"{round(correlation.iloc[i, j], 2)}", ha="center", va="center")

plt.show()

print("Analyse terminée !")
print()