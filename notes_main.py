import requests
from bs4 import BeautifulSoup

url = "https://randomword.com/"

response = requests.get(url)

# print(response.content)

def get_english_words_and_meanings():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        word = soup.find("div", id="random_word").text.strip()
        meaning = soup.find("div", id="random_word_definition").text.strip()

        return {"word": word,
                "meaning": meaning}

    except requests.exceptions.RequestException as e:
        print("Произошла ошибка при получении данных:", e)
        return None

    except Exception as e:
        print("Произошла ошибка:", e)


def guess_word_game():
    print("Добро пожаловать в игру 'Угадай слово'!")
    while True:
        word_dict = get_english_words_and_meanings()
        word = word_dict.get("word")
        meaning = word_dict.get("meaning")

        print(f"\nЗначение слова: {meaning}")
        user_guess = input("Введите английское слово: ").strip().lower()

        if user_guess == word:
            print("Правильно! Вы угадали слово.")
        else:
            print(f"Неверно. Правильное слово: {word}")

        play_again = input("Хотите сыграть еще раз? (y/n): ").strip().lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break


guess_word_game()
