# The dictionary of books, with publication dates and ratings

books = {
    "The Linux Command Line by William Shotts": {
        "publication_date": 2012,
        "rating": 4.5
    },
    "Linux Bible by Christopher Negus": {
        "publication_date": 2015,
        "rating": 4.3
    },
    "How Linux Works: What Every Superuser Should Know by Brian Ward": {
        "publication_date": 2014,
        "rating": 4.6
    },
    "UNIX and Linux System Administration Handbook by Evi Nemeth, Garth Snyder, Trent Hein, and Ben Whaley": {
        "publication_date": 2010,
        "rating": 4.8
    },
    "Linux Pocket Guide by Daniel J. Barrett": {
        "publication_date": 2016,
        "rating": 4.2
    },
    "Linux Kernel Development by Robert Love": {
        "publication_date": 2010,
        "rating": 4.7
    },
    "The Linux Programming Interface by Michael Kerrisk": {
        "publication_date": 2010,
        "rating": 4.9
    },
    "Linux in Action by David Clinton": {
        "publication_date": 2018,
        "rating": 4.4
    },
    "Advanced Programming in the UNIX Environment by W. Richard Stevens, Stephen A. Rago": {
        "publication_date": 2013,
        "rating": 4.9
    },
    "Linux Essentials by Roderick W. Smith": {
        "publication_date": 2012,
        "rating": 4.1
    }
}

# Function to sort books by publication date, least to greatest
def sort_by_publication_date(books_dict):
    return dict(sorted(books_dict.items(), key=lambda x: x[1]["publication_date"]))

# Function to sort books by publication date, greatest to least
def sort_by_publication_date_descending(books_dict):
    return dict(sorted(books_dict.items(), key=lambda x: x[1]["publication_date"], reverse=True))

# Function to sort books by rating, least to greatetst
def sort_by_rating_ascending(books_dict):
    return dict(sorted(books_dict.items(), key=lambda x: x[1]["rating"]))

# Function to sort books by rating, greatest to least
def sort_by_rating(books_dict):
    return dict(sorted(books_dict.items(), key=lambda x: x[1]["rating"], reverse=True))

# Prints the books sorted from least to greatest
print("Books sorted by publication date (least to greatest):")
for book, details in sort_by_publication_date(books).items():
    print(f"{book}: {details['publication_date']}")

print("\nBooks sorted by publication date (greatest to least)")
for book, details in sort_by_publication_date_descending(books).items():
    print(f"{book}: {details['publication_date']}")

print("\nBooks sorted by rating (lowest to highest):")
for book, details in sort_by_rating_ascending(books).items():
    print(f"{book}: {details['rating']} stars")

# Prints the books sorted by rating
sorted_by_rating = sort_by_rating(books)
print("\nBooks sorted by rating (highest to lowest):")
for book, details in sorted_by_rating.items():
    print(f"{book}: {details['rating']} stars")
