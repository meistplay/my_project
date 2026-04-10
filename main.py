from utils import get_zen_quote

# Главный исполняемый файл проекта


def main():
    print("Добро пожаловать в генератор цитат!")
    print("Ваша цитата на сегодня:")
    print("-------------------------")
    print(get_zen_quote())
    print("-------------------------")


if __name__ == "__main__":
    main()
