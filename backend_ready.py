from transliterate import translit

# Define the Pushkin poem
poem = """Духовной жаждою томим,
В пустыне мрачной я влачился, - 
И шестикрылый серафим
На перепутьи мне явился.
Перстами легкими как сон
Моих зениц коснулся он.
Отверзлись вещие зеницы,
Как у испуганной орлицы.
Моих ушей коснулся он, - 
И их наполнил шум и звон:
И внял я неба содроганье,
И горний ангелов полет,
И гад морских подводный ход.
И дольней лозы прозябанье.
И он к устам моим приник,
И вырвал грешный мой язык,
И празднословный, и лукавый,
И жало мудрыя змеи
В уста замершие мои
Вложил десницею кровавой.
И он мне грудь рассек мечом,
И сердце трепетное вынул
И угль, пылающий огнем,
Во грудь отверстую водвинул.
Как труп в пустыне я лежал,
И бога глас ко мне воззвал:
"Восстань, пророк, и виждь, и внемли,
Исполнись волею моей,
И, обходя моря и земли,
Глаголом жги сердца людей"."""

# Split the poem into lines
lines = poem.split('\n')

def find_word(word):
    # Transliterate the word to Cyrillic if it is in Latin script
    cyrillic_word = translit(word, 'ru') if word.isascii() else word
    print(f"Searching for word: {word} (transliterated: {cyrillic_word})")  # Debug print
    found = False
    # Loop through each line in the poem
    for i, line in enumerate(lines):
        # Check if the word (in lowercase) is in the line (also converted to lowercase)
        if cyrillic_word.lower() in line.lower():
            print(f"Line {i + 1}: {line}")
            found = True
    if not found:
        print("Слово не найдено" if not word.isascii() else f"Word not found: {word}")

def print_full_poem():
    print(poem)

# Define the current line number
current_line = 0

def main():
    global current_line
    while True:
        action = input(
            "Enter 'word' to search for a word, 'next' for the next line, 'start' for the beginning, 'full' for the full poem, or 'play' to restart: ").strip().lower()

        if action == 'word':
            search_word = input("Enter the word you want to search for: ").strip().lower()
            find_word(search_word)
        elif action == 'next':
            if current_line < len(lines) - 1:
                print(f"Line {current_line + 1}: {lines[current_line]}")
                current_line += 1
            else:
                print("End of poem reached.")
        elif action == 'start':
            current_line = 0
            print("Beginning of the poem:")
            print(lines[current_line])
        elif action == 'full':
            print_full_poem()
        elif action == 'play':
            current_line = 0
            print("Restarting...")
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
