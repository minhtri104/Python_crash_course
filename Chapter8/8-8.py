def make_album(artist, title, tracks=None):
    """Xây dựng một từ điển mô tả thông tin về album âm nhạc."""
    album = {
        'artist': artist.title(),
        'title': title.title()
    }
    
    # Nếu có truyền vào số lượng bài hát, thêm vào từ điển
    if tracks:
        album['tracks'] = tracks
        
    return album

while True:
    print("\nHãy cho tôi biết thông tin về album âm nhạc của bạn:")
    print("(nhập 'q' bất cứ lúc nào để thoát)")

    artist_input = input("Hãy nhập tên nghệ sĩ: ")
    if artist_input.lower() == 'q':
        break
    
    title_input = input("Hãy nhập tên album: ")
    if title_input.lower() == 'q':
        break
    
    user_album = make_album(artist_input, title_input)
    print(user_album)