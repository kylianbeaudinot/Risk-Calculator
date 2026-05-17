# Risk Calculator

---

## Présentation du projet

Ce projet constitue ma **première application concrète en programmation financière**. Réalisé de ma propre initiative en parallèle de ma deuxième année de Licence, il a pour objectif d'automatiser l'analyse quantitative et la gestion des risques d'un portefeuille multi-actifs. 

En s'appuyant sur les principes de la **Théorie Moderne du Portefeuille slon le Modèle de Markowitz**, ce script Python se connecte en temps réel à l'API Yahoo Finance pour extraire les données de marché, calculer les métriques de risque/rendement individuelles et modéliser l'impact de la diversification au sein d'un portefeuille composé d'actifs selectionnés.

---

## Fonctionnalités majeures

- **Collecte Dynamique de Données :** Extraction automatisée des cours de clôture ajustés via yfinance.
- **Analyse Quantitative par Actif :** Calcul du rendement annualisé, de la volatilité annualisée et du ratio de Sharpe pour chaque actifs.
- **Modélisation Matricielle du Portefeuille :** Calcul de la performance globale attendue, de la variance globale (via la matrice de covariance pondérée) et du score d'efficience (Sharpe) du portefeuille.
- **Visualisation Graphique :** Génération automatique d'un graphique de performance et d'une heatmap de la matrice de corrélation pour analyser le risque du portefeuille.

---

## Selections des actifs et des paramètres

Le portefeuille actuel est configuré pour analyser une allocation diversifiée de 7 actifs majeurs, comprenant de la Tech US, les semi-conducteurs et le luxe européen :
* **Actifs étudiés :** `NVDA`, `AAPL`, `AMZN`, `GOOGL`, `MC.PA`, `ASML.AS`, `TSM`.
* **Paramètre Macroéconomique :** Le taux sans risque (risk free rate) utilisé est de **4.0%**, reflétant les conditions actuelles des obligations d'État de référence.
**Possibilité de choisir les actifs de votre choix :** Il suffit de remplacer les actifs à l'intérieur de la variable TICKERS à la ligne 27 du fichier main.py par les actifs de votre choix.
**Possibilité de changer l'allocation des actifs du portefeuille :** Il suffit de remplacer les valeurs présentent dans la variable WEIGHTS à la ligne 36 par les valeurs de votre choix, mais la somme de ses valeurs doit être égale à 1, et il doit y avoir autant de valeurs que d'actifs selectionnés dans la variable TICKERS.

---

## Méthodologie & fondations financières

L'intégralité des calculs respecte les standards académiques et professionnels de la finance de marché :

1. **Annualisation des Données :** Les rendements moyens et les écarts-types journaliers sont extrapolés sur une base stricte de **252 jours de trading** par an.
2. **Volatilité Globale du Portefeuille :** Pour intégrer l'effet de diversification et les structures de dépendance, la variance est calculée de manière matricielle :
   $$\sigma_p = \sqrt{W^T \cdot \Sigma \cdot W}$$
   *Où $W$ représente le vecteur des poids d'allocation et $\Sigma$ la matrice de covariance annualisée.*
3. **Ratio de Sharpe :** Utilisé pour mesurer l'excès de rendement par unité de risque :
   $$\text{Sharpe} = \frac{R_p - R_f}{\sigma_p}$$

---

## Ressources utilisées

Ce projet a été développé sous environnement **Anaconda** (Python 3.13) et m'a permis de me familiariser avec les bibliothèques standards de la Data Science :
* **Pandas & NumPy :** Manipulation de structures de données financières et calculs matriciels vectorisés.
* **Matplotlib :** Modélisation et rendu graphique des données.
* **YFinance :** Intégration d'API tierces.

### Installation des prérequis
```bash
pip install yfinance pandas numpy matplotlib