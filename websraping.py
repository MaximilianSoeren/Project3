#%%
import requests
import pandas as pd

from bs4 import BeautifulSoup

# %%
# Get artist
# Get songname

url = "https://www.billboard.com/charts/hot-100"
response = requests.get(url)
print(response.status_code)
# %%
soup = BeautifulSoup(response.text, 'html.parser')

# %%
#This gets us all song titles
def get_song_titles():
    song_titles = soup.find_all("span", class_="chart-element__information__song text--truncate color--primary")
    song_titles_list = []
    for i in song_titles:
        song_titles_list.append(i.get_text())
    return song_titles_list
# %%
def get_artist():
    artists = soup.find_all("span", class_="chart-element__information__artist text--truncate color--secondary")
    artist_list = []
    for i in artists:
        artist_list.append(i.get_text())
    return artist_list
# %%
list = [1, 2, 3]
list.pop
# %%
# ugly cleaning dataframe
def make_dataframe():
    artists_list = get_artist()
    song_title_list = get_song_titles()
    test_dict = {"Song": song_title_list, "Artist": artists_list}
    songs_df = pd.DataFrame.from_dict(test_dict)
    return songs_df
# %%
hot_100_df = make_dataframe()

# %%
hot_100_df["Song"]
# %%
