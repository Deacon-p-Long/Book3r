
# calculates the average rating of a book.
# if there are no ratings, returns 0
def average_rating (rating_list):
    if not rating_list:
        return 0
    return round (sum (rating_list) / len (rating_list))