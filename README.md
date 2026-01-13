# Spotify Ranking : an analysis

[![Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=googlecolab)](https://colab.research.google.com/github/theophile-bb/Spotify-ranking-an-analysis/blob/main/Spotify%20Analysis.ipynb)
[![Kaggle Dataset](https://img.shields.io/badge/Kaggle-Dataset-blue?logo=kaggle)](https://www.kaggle.com/datasets/yelexa/spotify200)
[![Website](https://img.shields.io/badge/Website-GitHub%20Pages-blue?logo=github)](https://theophile-bb.github.io/Spotify-ranking-an-analysis/Spotify_Analysis.html)

This project contains a comprehensive analysis of **Spotify’s regional Top 200 song charts** to uncover trends and characteristics of modern popular music and provides a simple Gradio webapp for interactive visualization of track rankings by region.

---

## Project Structure

Spotify-ranking-an-analysis/ <br>
├── Spotify Analysis.ipynb # Main data analysis notebook <br>
├── Spotify webapp.ipynb <br>
├── requirements.txt <br>
├── .gitignore <br>
└── README.md <br>

---

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.7+
- A Python environment (venv, conda, etc.)
- All dependencies installed via `requirements.txt`

---

## ⚙️ Installation

Clone the repository and install dependencies:

```
$ git clone https://github.com/theophile-bb/Spotify-ranking-an-analysis.git
$ cd Spotify-ranking-an-analysis
$ pip install -r requirements.txt
```

---

## Getting the data

Dataset : https://www.kaggle.com/datasets/yelexa/spotify200

This dataset includes:

- Track name

- Artist

- Weekly ranking

- Streams

- Release information

- Country and region metadata

- Music features (e.g., danceability, tempo, valence)

---

## Notebook

The main analysis is in: energy_forecasting.ipynb


It includes:

- Data loading and preprocessing

- Cleaning and feature engineering

- Genre distribution analysis

- Streams by region and country breakdowns

- Top artists, collaborations, and popularity metrics

- Insights into trends affecting popular songs

---

## Visualizations

Example of visualizations made :

*Word map of streams density*
<img width="1904" height="910" alt="map_plot" src="https://github.com/user-attachments/assets/fb620a32-5420-4c84-a068-187a2722c63e" />

*Music genre repartition*
<img width="1904" height="910" alt="pie_plot" src="https://github.com/user-attachments/assets/709737d5-0ac7-42f9-be56-9b352086ab5c" />

*Countries with the most streams*
<img width="1904" height="910" alt="bar_plot" src="https://github.com/user-attachments/assets/ffc3aa7d-667a-4f64-8f8b-10c09349efa5" />

