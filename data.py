def data():
    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.read_csv('11.csv', encoding='latin1')

    nulls = []
    cols = df.columns

    for i in cols:
        if df[i].isnull().sum():
            nulls.append(i)

    unique_dt = []
    cols = nulls
    for i in cols:
        dtype_ = df[i].dtypes
        if dtype_ not in unique_dt:
            unique_dt.append(dtype_)

    objects = []
    ints = []
    floats = []
    for i in cols:
        dtype_ = df[i].dtypes

        if dtype_ == 'O':
            objects.append(i)
        elif dtype_ == 'int':
            ints.append(i)
        else:
            floats.append(i)

    objects.remove('Pandora Track Stations')
    objects.remove('SiriusXM Spins')

    for i in objects:
        mode = df[i].mode()
        df[i] = df[i].fillna(mode[0])

    floats.remove('TIDAL Popularity')

    for i in floats:
        mode = df[i].mode()
        df[i] = df[i].fillna(mode[0])

    df['Release Date'] = pd.to_datetime(df['Release Date'])

    from_obj_to_int = [
        "Spotify Streams",
        "Spotify Playlist Count",
        "Spotify Playlist Reach",
        "YouTube Views",
        "YouTube Likes",
        "TikTok Posts",
        "TikTok Likes",
        "TikTok Views",
        "YouTube Playlist Reach",
        "AirPlay Spins",
        "Deezer Playlist Reach",
        "Pandora Streams",
        "Shazam Counts",
    ]

    for i in from_obj_to_int:
        df[i] = df[i].str.replace(',', '')
        df[i] = df[i].astype(float)
        df[i] = df[i].astype(int)

    del df['TIDAL Popularity']
    df['Pandora Track Stations'].fillna(df['Pandora Track Stations'].mode()[0])
    return df