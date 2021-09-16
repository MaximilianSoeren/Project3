#
#%%
import pickle
import spotipy
import pandas as pd
import streamlit as st
import webbrowser

from time import sleep
from random import sample
from sklearn.preprocessing import StandardScaler
from config import client_id, client_secret
from spotipy import SpotifyClientCredentials
from websraping import hot_100_df
# %%
# make Spotipy work
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = client_id,
                                                           client_secret = client_secret))
# %%
def load(filename = "filename.pickle"): 
    try: 
        with open(filename, "rb") as f: 
            return pickle.load(f) 
    except FileNotFoundError: 
        print("File not found!")
# %%
# %%
def import_clean_songs():
    songs_df = pd.read_csv("tracks.csv")
    songs_df_ml = songs_df.copy()
    songs_sorted = songs_df_ml.sort_values(by="release_date", ascending=False)
    songs_sorted= songs_sorted.drop(["id", "name", "popularity", "artists", "id_artists", "release_date", "explicit", "mode", "time_signature"], axis=1)
    songs_cor = songs_sorted[:100000]
    return songs_cor
# %%
def put_cluster_col():
    songs_big_df = pd.read_csv("/Users/m.soren/Downloads/tracks.csv")
    songs_big_df = songs_big_df[["name","artists", "id"]][0:100000]
    songs_big_df_clean = import_clean_songs()   
    scaler = StandardScaler()
    kmeans = load("/Users/m.soren/Desktop/Ironhack/Project3/cluster16.pickle")
    big_df_scaled = pd.DataFrame(scaler.fit_transform(songs_big_df_clean),columns =songs_big_df_clean.columns)
    big_df_cluster = kmeans.predict(big_df_scaled)
    songs_big_df["Cluster"] = big_df_cluster
    return songs_big_df
# %%
songs_big_df = put_cluster_col()
# %%
def get_audio_feat_hot_100():
    uri = []
    list_of_col = ['Song', 'Artist', 'uri','danceability', 'energy', 'key', 'loudness', 'mode',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'duration_ms',]
    top_100_songs = hot_100_df["Song"].to_list()
    for i in top_100_songs:
        search = sp.search(q=i, limit=1)
        uri.append(search["tracks"]["items"][0]["uri"])
    top_100_audio = pd.DataFrame(sp.audio_features(uri))
    top_100_full_df = pd.concat([hot_100_df,top_100_audio], axis=1)
    top_100_full_df = top_100_full_df[list_of_col]
    return top_100_full_df
 # %%
    
# %%
def search_song(song,artist):
    query = song + " " + artist
    search = sp.search(q=query, type="track")
    uri = search["tracks"]["items"][0]["uri"]
    return uri
# %% 
def get_audio_feat(uri):
    audio_dict = sp.audio_features(uri)
    df_audio = pd.DataFrame(audio_dict)
    return df_audio
# %%
def get_cluster_top_100():
    top_100 = get_audio_feat_hot_100()
    scaler = StandardScaler()
    kmeans = load("/Users/m.soren/Desktop/Ironhack/Project3/cluster16.pickle")
    top_100_audio = top_100[['danceability', 'energy', 'key', 'loudness',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'duration_ms']]
    top_100_scaled = pd.DataFrame(scaler.fit_transform(top_100_audio),columns =top_100_audio.columns)
    top_100_cluster = kmeans.predict(top_100_scaled)
    hot_100_df_final = hot_100_df
    hot_100_df_final["Cluster"] = top_100_cluster
    return hot_100_df_final
# %%
# %%
def get_searched_song_cluster(a,b):
    song_uri = search_song(a,b)
    song_audio = get_audio_feat(song_uri)
    hot_100_df_final = get_cluster_top_100()
    song_audio = song_audio[['danceability', 'energy', 'key', 'loudness',
    'speechiness', 'acousticness', 'instrumentalness', 'liveness',
    'valence', 'tempo', 'duration_ms']]
    scaler = StandardScaler()
    kmeans = load("/Users/m.soren/Desktop/Ironhack/Project3/cluster16.pickle")
    song_scaled = pd.DataFrame(scaler.fit_transform(song_audio),columns =song_audio.columns)
    song_cluster = kmeans.predict(song_scaled)
    song_final = song_scaled    
    song_final["Cluster"] = song_cluster
    top_100_songs = hot_100_df_final["Song"].to_list()
    top_100_songs = [i.lower() for i in top_100_songs]
    hot_100_df_lower = hot_100_df_final.copy()
    hot_100_df_lower["Song"] = top_100_songs
    if a.lower() in top_100_songs:
        user_song_df = hot_100_df_lower.loc[hot_100_df_lower["Song"] == a.lower()]
        cluster = user_song_df["Cluster"][0]
        track_sug_df = hot_100_df_final[hot_100_df_final["Cluster"]==cluster]
        new_track = track_sug_df.sample()
        song_name = new_track.iloc[0]["Song"]
        song_artist = new_track.iloc[0]["Artist"]
        song_rec_print = "If you like that song, then how about: {} by {}".format(song_name, song_artist)
        searched_song_uri = search_song(song_name, song_artist).split(":")[-1]
        return song_rec_print, searched_song_uri
    else:
        track_sug_df = songs_big_df[songs_big_df["Cluster"]==song_cluster[0]]
        new_track = track_sug_df.sample()
        song_name = new_track.iloc[0]["name"]
        song_artist = new_track.iloc[0]["artists"].replace("[", "").replace("]", "").replace("'","")
        song_rec_print = "If you like that song, then how about: {} by {}".format(song_name, song_artist)
        searched_song_uri = search_song(song_name, song_artist).split(":")[-1]
        return song_rec_print, searched_song_uri
# %%
# %%
st.title("Song Reccomender")
st.subheader("This application will reccomend you a song based on a song you enter. Try it")
st.write("---")
col1, col2, col3 = st.beta_columns(3)
with col1:
    song_input = st.text_input(label="Type the Song")
with col2:
    artist_input = st.text_input(label="Type the Artist")
with col3:
    search_button = st.button("Search")
if search_button:
    with st.spinner(text="We're looking through 100.000 Songs to find one that is right for you."):
        song_rec, song_uri = get_searched_song_cluster(song_input, artist_input)
        sleep(3)
st.write("---")
st.write(song_rec)
st.write("---")
st.write("[Check out the Song](https://open.spotify.com/track/%s)" % song_uri)




# # %%
# scaler = StandardScaler() 
# scaler.fit(df_full_ready_test) 
# Full_scaled = scaler.transform(df_full_ready_test) 
# Full_scaled_df = pd.DataFrame(Full_scaled, columns = df_full_ready_test.columns) 
# display(df_full_ready_test.head())
# print() 
# display(Full_scaled_df.head())
# %%
# %%
