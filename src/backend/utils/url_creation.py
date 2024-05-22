def make_url_query_string(track: str, artist: str, album: str, search_type: str, limit: int, offset: int) -> str:
    track = track.strip().replace(' ', '+')
    artist = artist.strip().replace(' ', '+')
    album = album.strip().replace(' ', '+')
    search_type = search_type.strip()

    return f'?q={artist}-{track}+({album})&type={search_type}&limit={limit}&offset={offset}'