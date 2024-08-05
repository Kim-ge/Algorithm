def solution(genres, plays):
    # 장르별로 노래를 분류하고 재생 횟수를 합산
    genre_play_dict = {}
    genre_song_dict = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_play_dict:
            genre_play_dict[genre] = 0
            genre_song_dict[genre] = []
        genre_play_dict[genre] += play
        genre_song_dict[genre].append((play, i))
    
    # 장르를 총 재생 횟수 기준으로 정렬
    sorted_genres = sorted(genre_play_dict.items(), key=lambda x: x[1], reverse=True)
    
    best_album = []
    
    #각 장르 내에서 노래를 정렬하고 베스트 앨범에 추가
    for genre, _ in sorted_genres:
        # 각 장르 내에서 노래를 재생 횟수 기준으로 정렬
        sorted_songs = sorted(genre_song_dict[genre], key=lambda x: (-x[0], x[1]))
        
        # 최대 두 개의 노래를 선택
        best_album.extend([song[1] for song in sorted_songs[:2]])
    
    return best_album