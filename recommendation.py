def recommend_books(user_prefs, books):
    recommended_books = []
    for title, details in books.items():
        if details["genre"] in user_prefs[0] or details["author"] in user_prefs[1] or title in user_prefs[2]:
            recommended_books.append((title, details["description"]))
    return recommended_books