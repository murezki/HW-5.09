numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
kvadrat_numbers = list(map(lambda x: x ** 2, even_numbers))
print(kvadrat_numbers)



words = ["Abubandit", "Chief Keef", "Ara", "Ashab Tamaev", "Rwanda"]
filtered_words = list(filter(lambda x: x[0] == 'A' and x[0].isupper(), words))
lowercase_words = list(map(lambda x: x.lower(), filtered_words))
print(lowercase_words)