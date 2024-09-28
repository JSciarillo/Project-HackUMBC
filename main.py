# Take name of book as input
book_name = input("Enter book name: ")
temp = ""
# Convert spaces to underscores
for c in book_name:
    if c == " ":
        c = "_"
    temp += c
# Append converted name of book to "en.wikipedia.org/wiki/"
book_name = "en.wikipedia.org/wiki/" + temp;
print(book_name)
# Check if article exists on Wikipedia. If not, try appending "_(novel)" to the string and try again
# Otherwise say not found
# Get book properties from fields on the article's infobox card
