def get_user_preferences():
    print("Welcome to the Book Recommendation System!")
    print("Please answer the following questions to receive personalized book recommendations.")
    
    favorite_genres = input("Enter your favorite genres (comma-separated): ").split(",")
    favorite_authors = input("Enter your favorite authors (comma-separated): ").split(",")
    favorite_books = input("Enter the titles of books you've enjoyed (comma-separated): ").split(",")
    
    return favorite_genres, favorite_authors, favorite_books
