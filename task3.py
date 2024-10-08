sentence = input("Введіть речення: ")

words = sentence.split()

filtered_words = [word for word in words if word.lower() != "привіт"]

new_sentence = ' '.join(filtered_words)

if "привіт" in sentence.lower():
    print("Речення без слова 'привіт':", new_sentence)
else:
    print("Слово 'привіт' не знайдено у реченні.")
