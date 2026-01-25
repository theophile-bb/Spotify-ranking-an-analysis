import gradio as gr
import pandas as pd
import os
import kagglehub
import plotly.express as px
from datetime import datetime
from typing import List, Tuple, Optional, Any, Union
import plotly.graph_objects as go

def save_figs(figs: List[go.Figure], folder: str = "plots") -> None:
    os.makedirs(folder, exist_ok=True)
    timestamp: str = datetime.now().strftime("%Y%m%d_%H%M%S")

    for i, fig in enumerate(figs, 1):
        fig.write_image(f"{folder}/plot_{i}_{timestamp}.png")

    print(f"✅ Saved {len(figs)} figures to {folder}/")


def get_df(link: str) -> pd.DataFrame:
    dataset_path: str = kagglehub.dataset_download(link)
    csv_files: List[str] = [f for f in os.listdir(dataset_path) if f.endswith(".csv")]
    if csv_files:
        csv_path: str = os.path.join(dataset_path, csv_files[0])
        df: pd.DataFrame = pd.read_csv(csv_path)
    else:
        raise FileNotFoundError("No CSV file found in the dataset folder.")
    return df


def load_countries(link: str) -> Tuple[pd.DataFrame, Dict[str, Any], None, None]:
    df: pd.DataFrame = get_df(link)
    countries: List[str] = sorted(df['country'].dropna().unique().tolist())
    return (
        df, 
        gr.update(choices=countries, value=countries[0] if countries else None), 
        None, 
        None
    )


def process_songs(df: pd.DataFrame, country: str) -> List[str]:
    df["full_track"] = df["artist_names"] + " - " + df["track_name"]
    songs: List[str] = sorted(df[df['country'] == country]['full_track'].dropna().unique().tolist())
    return songs


def load_songs(df: Optional[pd.DataFrame], country: Optional[str]) -> Tuple[Dict[str, Any], None]:
    if df is None or country is None:
        return gr.update(choices=[], value=None), None
    
    df["full_track"] = df["artist_names"] + " - " + df["track_name"]
    songs: List[str] = sorted(df[df['country'] == country]['full_track'].dropna().unique().tolist())
    return gr.update(choices=songs, value=songs[0] if songs else None), None


def plot_song(df: Optional[pd.DataFrame], country: Optional[str], song: Optional[str]) -> Optional[go.Figure]:
    if df is None or country is None or song is None:
        return None

    song_df: pd.DataFrame = df[(df['country'] == country) & (df['full_track'] == song)].copy()
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
    fig.update_yaxes(autorange="reversed", tickmode='linear', dtick=10)
    return fig


def load_dataset_and_countries(link: str) -> Tuple[pd.DataFrame, Dict[str, Any], None, None]:
    df, country_update, song_update, plot_update = load_countries(link)
    return df, country_update, song_update, plot_update


def update_songs(df: Optional[pd.DataFrame], country: Optional[str]) -> Tuple[Dict[str, Any], None]:
    return load_songs(df, country)


def update_plot(df: Optional[pd.DataFrame], country: Optional[str], song: Optional[str]) -> Optional[go.Figure]:
    return plot_song(df, country, song)
