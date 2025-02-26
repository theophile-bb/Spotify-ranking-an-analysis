# Spotify Ranking : an analysis

This repository contains a comprehensive analysis of Spotify's regional Top 200 song charts, aiming to uncover trends and insights surrounding the music streaming industry.

![image](https://github.com/user-attachments/assets/eda1d039-0e91-48a5-8089-7eda3bf2ccdd)

## Project Overview
This project is divided into 2 parts :

• Data Analysis: An in-depth exploration of Spotify's streaming data to identify key insights.

• Web Application: An interactive Gradio webapp that plots the ranking of a song in the selected region.

## Data

Dataset : https://www.kaggle.com/datasets/yelexa/spotify200

The dataset for this project is sourced from Spotify Charts, which provides publicly available rankings of the most streamed songs on the platform. The dataset includes attributes such as:

• Track Name

• Artist

• Ranking data (peak rank, previous rank, number of week on chart)

• Number of streams

• Release date

• Collab

• Country

• Music features (danceability, loudness, tempo, valence, liveness, loudness,...)

The dataset has a total of 36 columns.

## Repository Structure
• Spotify Analysis.ipynb: This notebook is divided in 2 parts : the data cleaning and processing, and the analysis analysis process of Spotify's Top 200 charts
to identify trends, such as the most streamed songs, artists, and genres over specific periods.

• Spotify webapp.ipynb: This other notebook is dedicated to the Gradio webapp to visualize songs by country.
