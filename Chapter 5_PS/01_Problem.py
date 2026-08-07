# Urdu to English dictionary
urdu_to_english = {
    "Namak": "Salt",
    "Pani": "Water",
    "Roti": "Bread",
    "Doodh": "Milk",
    "Kitab": "Book",
    "Ghar": "House",
    "Kursi": "Chair",
    "Meetha": "Sweet",
    "Dost": "Friend",
    "Phool": "Flower"
}
word = input("Enter a Urdu language word:\n").strip().title() #Taking input from the user
if word in urdu_to_english:
    print(f"\n\t{word} means \"{urdu_to_english[word]}\"")
else:
    print(f"\nSorry! The translation of the word \"{word}\" does not found.")
print(f"""\n\nWe have the translation of these words:
    {urdu_to_english} """)