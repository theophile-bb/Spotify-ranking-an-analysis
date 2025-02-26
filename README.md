# Spotify Ranking : an analysis

This repository contains a comprehensive analysis of Spotify's regional Top 200 song charts, aiming to uncover trends and insights surrounding the music streaming industry.

![image](https://github.com/user-attachments/assets/eda1d039-0e91-48a5-8089-7eda3bf2ccdd)

This project is divided into 2 parts :

• **Case Study : What are the caracteristics of modern popular songs ?** : An in-depth exploration of Spotify's streaming data to identify key insights.

• Web Application: An interactive Gradio webapp that plots the ranking of a song in the selected region.

## Repository Structure
• Spotify Analysis.ipynb: This notebook is divided in 2 parts : the data cleaning and processing, and the analysis analysis process of Spotify's Top 200 charts
to identify trends, such as the most streamed songs, artists, and genres over specific periods.

• Spotify webapp.ipynb: This other notebook is dedicated to the Gradio webapp to visualize songs by country. It takes a kaggle link as input to get the dataset, and then 2 dropdowns - one for the country and one the song - are loaded. The functions then load the evolution of the ranking of the selected song.

## Data

Dataset : https://www.kaggle.com/datasets/yelexa/spotify200

The dataset for this project is sourced from Spotify Charts, which provides publicly available rankings of the most streamed songs on the platform. The dataset includes attributes such as:

• Track Name

• Artist

• Ranking data (peak rank, previous rank, number of weeks on chart)

• Number of streams

• Release date

• Collab

• Country

• Music features (danceability, loudness, tempo, valence, liveness, loudness,...)

The dataset has a total of 36 columns.

## Methodology
The analysis is structured as follows:

### Data Preprocessing:
➣ Converting columns to appropriate type

➣ Filling NaN values

➣ Replacing aberrant values.

### Data visualization and analysis:
➣ Genre distribution

➣ Streams by regions of the world : number of streams by region

➣ How many songs does an average user listens to ?

➣ Number of streams by country : visualization using a world map

➣ Who are the top artists based on the number of streams ?

➣ How do featurings influence the popularity of a song ? Which artists are more into solos and which are more into featurings ?

➣ Which artists have the most cumulated weeks in the top 200 ?
