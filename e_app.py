import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data import data

df = data()

flag = True
years = [
    "1987", "1991", "1994", "1998", "1999", "2000", "2001", "2002", "2003",
    "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
    "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021",
    "2022", "2023", "2024"
]

st.set_page_config(
    page_title="Global Statistics Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded"
)

left, middle, right = st.columns(3)

with left:
    start, end = st.select_slider(
        "Select a year",
        options=years,
        value=('1987', '2024'),
    )

with middle:
    platform = st.selectbox(
        "Please choose a company you want to analyse",
        [
            "YouTube",
            "TikTok",
            "Amazon Music",
            "Spotify",
            "SoundCloud",
            "Deezer",
            "Apple Music",
            "AirPlay",
            "Shazam",
        ],
        index=0
    )

with right:
    explicit = st.selectbox(
        "Explicitly or No choose an option",
        ["Yes", "No","All"],
        index=0
    )

range_of_years = []
start_of_y_views = years.index(start)
end_of_y_views = years.index(end)
if start == end:
    st.error("Please select a range where the start year is different from the end year.")
    flag = False

i = start_of_y_views
while i <= end_of_y_views:
    range_of_years.append(years[i])
    i += 1

if explicit == "All":
    df = df
elif explicit == "Yes":
    df = df[df['Explicit Track'] == 1]
elif explicit == "No":
    df = df[df['Explicit Track'] == 0]


if flag:
    if platform == "YouTube":
        y_left, y_middle, y_right = st.columns(3)
        with y_left:
            st.write(f"YouTube Views from {start} to {end}")
            filtered_df = df[df['Release Date'].isin(range_of_years)]
            filtered_df = filtered_df[['Release Date', 'YouTube Views']]
            st.line_chart(filtered_df.set_index('Release Date'), color=["#FF0000"])

        with y_middle:
            st.write(f"YouTube Likes from {start} to {end}")
            filtered_df = df[df['Release Date'].isin(range_of_years)]
            filtered_df = filtered_df[['Release Date', 'YouTube Likes']]
            st.line_chart(filtered_df.set_index('Release Date'), color=["#00CC00"])

        with y_right:
            st.write(f"YouTube Playlist Reach from {start} to {end}")
            filtered_df = df[df['Release Date'].isin(range_of_years)]
            filtered_df = filtered_df[['Release Date', 'YouTube Playlist Reach']]
            st.line_chart(filtered_df.set_index('Release Date'), color=["#0000CC"])

        md = st.text_area('  ',
                          "Here, I can provide some explanation for these line graphs. They actually represent the number of views or likes on the YouTube platform for music released in a certain year.")


    elif platform == "Amazon Music":

        st.write(f"Amazon Playlist Counts from  {start} to {end}")

        filtered_df = df[df['Release Date'].isin(range_of_years)]

        filtered_df = filtered_df[['Release Date', 'Amazon Playlist Count']]

        st.line_chart(filtered_df.set_index('Release Date'), color=["#FF0000"])

        md = st.text_area('  ',
                          "Here, I can provide some explanation for these line graph. This is actually represent the number of streams  on the Amazon Music platform for music released in a certain year.")


    elif platform == "Apple Music":

        st.write(f"Apple Music Playlist Count from  {start} to {end}")

        filtered_df = df[df['Release Date'].isin(range_of_years)]

        filtered_df = filtered_df[['Release Date', 'Apple Music Playlist Count']]

        st.line_chart(filtered_df.set_index('Release Date'), color=["#FF0000"])

        md = st.text_area('  ',
                          "Here, I can provide some explanation for these line graph. This is actually represent the number of streams  on the Apple Music platform for music released in a certain year.")

    elif platform == "AirPlay":

        st.write(f"AirPlay Spins from  {start} to {end}")
        filtered_df = df[df['Release Date'].isin(range_of_years)]
        filtered_df = filtered_df[['Release Date', 'AirPlay Spins']]
        st.line_chart(filtered_df.set_index('Release Date'), color=["#FF0000"])

        md = st.text_area('  ',
                          "Here, I can provide some explanation for these line graph. This is actually represent the number of streams  on the AirPlay platform for music released in a certain year.")
    elif platform == "Deezer":
        y_left, y_middle = st.columns(2)
        with y_left:
            st.write(f"Deezer Playlist Count from {start} to {end}")
            filtered_df = df[df['Release Date'].isin(range_of_years)]
            filtered_df = filtered_df[['Release Date', 'Deezer Playlist Count']]
            st.line_chart(filtered_df.set_index('Release Date'), color=["#FF0000"])

        with y_middle:
            st.write(f"Deezer Playlist Reach from {start} to {end}")
            filtered_df = df[df['Release Date'].isin(range_of_years)]
            filtered_df = filtered_df[['Release Date', 'Deezer Playlist Reach']]
            st.line_chart(filtered_df.set_index('Release Date'), color=["#00CC00"])

        md = st.text_area('  ',
                          "Here, I can provide some explanation for these line graphs. They actually represent the number of playlist reach or playlist count on the Deezer platform for music released in a certain year.")


    elif platform == "Shazam":

        st.write(f"Shazam Counts from  {start} to {end}")

        filtered_df = df[df['Release Date'].isin(range_of_years)]

        filtered_df = filtered_df[['Release Date', 'Shazam Counts']]

        st.line_chart(filtered_df.set_index('Release Date'), color=["#FF0000"])

        md = st.text_area('  ',

                          "Here, I can provide some explanation for these line graph. This is actually represent the number of Shazam Counts  on the Shazam platform for music released in a certain year.")


    elif platform == "SiriusXM":

        st.write(f"SiriusXM Spins from  {start} to {end}")

        filtered_df = df[df['Release Date'].isin(range_of_years)]

        filtered_df = filtered_df[['Release Date', 'SiriusXM Spins']]

        st.line_chart(filtered_df.set_index('Release Date'), color=["#FF0000"])

        md = st.text_area('  ',

                          "Here, I can provide some explanation for these line graph. This is actually represent the number of SiriusXM Spins on the SiriusXM platform for music released in a certain year.")

    elif platform == "SoundCloud":

        st.write(f"Soundcloud Streams from  {start} to {end}")
        filtered_df = df[df['Release Date'].isin(range_of_years)]
        filtered_df = filtered_df[['Release Date', 'Soundcloud Streams']]
        st.line_chart(filtered_df.set_index('Release Date'), color=["#FF0000"])

        md = st.text_area('  ',
                          "Here, I can provide some explanation for these line graph. This is actually represent the number of Soundcloud Streams on the Soundcloud platform for music released in a certain year.")

    if platform == "Spotify":
        y_left, y_middle, y_right,very_right = st.columns(4)
        with y_left:
            st.write(f"Spotify Popularity from {start} to {end}")
            filtered_df = df[df['Release Date'].isin(range_of_years)]
            filtered_df = filtered_df[['Release Date', 'Spotify Popularity']]
            st.line_chart(filtered_df.set_index('Release Date'), color=["#FF0000"])

        with y_middle:
            st.write(f"Spotify Streams from {start} to {end}")
            filtered_df = df[df['Release Date'].isin(range_of_years)]
            filtered_df = filtered_df[['Release Date', 'Spotify Streams']]
            st.line_chart(filtered_df.set_index('Release Date'), color=["#00CC00"])

        with y_right:
            st.write(f"Spotify Playlist Count from {start} to {end}")
            filtered_df = df[df['Release Date'].isin(range_of_years)]
            filtered_df = filtered_df[['Release Date', 'Spotify Playlist Count']]
            st.line_chart(filtered_df.set_index('Release Date'), color=["#0000CC"])

        with very_right:
            st.write(f"Spotify Playlist Reach from {start} to {end}")
            filtered_df = df[df['Release Date'].isin(range_of_years)]
            filtered_df = filtered_df[['Release Date', 'Spotify Playlist Reach']]
            st.line_chart(filtered_df.set_index('Release Date'), color=["#0000CC"])



        md = st.text_area('  ',
                          "Here, I can provide some explanation for these line graphs. They actually represent the numbers about Spotify platform for music released in a certain year.")

    if platform == "TikTok":
        y_left, y_middle, y_right = st.columns(3)
        with y_left:
            st.write(f"TikTok Posts from {start} to {end}")
            filtered_df = df[df['Release Date'].isin(range_of_years)]
            filtered_df = filtered_df[['Release Date', 'TikTok Posts']]
            st.line_chart(filtered_df.set_index('Release Date'), color=["#FF0000"])

        with y_middle:
            st.write(f"TikTok Views from {start} to {end}")
            filtered_df = df[df['Release Date'].isin(range_of_years)]
            filtered_df = filtered_df[['Release Date', 'TikTok Views']]
            st.line_chart(filtered_df.set_index('Release Date'), color=["#00CC00"])

        with y_right:
            st.write(f"TikTok Views from {start} to {end}")
            filtered_df = df[df['Release Date'].isin(range_of_years)]
            filtered_df = filtered_df[['Release Date', 'TikTok Views']]
            st.line_chart(filtered_df.set_index('Release Date'), color=["#0000CC"])

        md = st.text_area('  ',
                          "Here, I can provide some explanation for these line graphs. They actually represent the numbers about TikTok platform for music released in a certain year.")

