
import gradio as gr

import pandas as pd
import os
import kagglehub

import plotly.express as px

#--------------------- Save Images ------------------------

def save_figs(figs, folder="plots"):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    for i, fig in enumerate(figs, 1):
        fig.savefig(
            f"{folder}/plot_{i}_{timestamp}.png",
            dpi=300,
            bbox_inches="tight"
        )

    print(f"✅ Saved {len(figs)} figures to {folder}/")

#--------------------- Webapp ------------------------


def get_df(link):
    dataset_path = kagglehub.dataset_download(link)
    csv_files = [f for f in os.listdir(dataset_path) if f.endswith(".csv")]
    if csv_files:
        csv_path = os.path.join(dataset_path, csv_files[0])
        df = pd.read_csv(csv_path)
    else:
        raise FileNotFoundError("No CSV file found in the dataset folder.")
    return df


def load_countries(link):
    df = get_df(link)
    countries = sorted(df['country'].dropna().unique().tolist())
    return df, gr.update(choices=countries, value=countries[0] if countries else None), None, None


def process_songs(df, country):
    df["full_track"] = df["artist_names"] + " - " + df["track_name"]
    songs = sorted(df[df['country'] == country]['full_track'].dropna().unique().tolist())
    return songs


def load_songs(df, country):
    if df is None or country is None:
        return [], None
    df["full_track"] = df["artist_names"] + " - " + df["track_name"]
    songs = sorted(df[df['country'] == country]['full_track'].dropna().unique().tolist())
    return gr.update(choices=songs, value=songs[0] if songs else None), None


def plot_song(df, country, song):
    if df is None or country is None or song is None:
        return None

    song_df = df[(df['country'] == country) & (df['full_track'] == song)]
    if song_df.empty:
        return None

    song_df['week'] = pd.to_datetime(song_df['week'])
    song_df = song_df.sort_values(by="week")

    fig = px.line(
        song_df,
        x='week',
        y='rank',
        title=f'{song} ranking over weeks in {country}',
        labels={'rank': 'Rank', 'week': 'Week'},
        markers=True
    )
    fig.update_yaxes(autorange="reversed",tickmode='linear', dtick=10)
    return fig


def load_dataset_and_countries(link):
        df, country_update, song_update, plot_update = load_countries(link)
        return df, country_update, song_update, plot_update


def update_songs(df, country):
        return load_songs(df, country)


def update_plot(df, country, song):
        return plot_song(df, country, song)

