from utils import get_zen_quote


def main():
    print("Добро пожаловать в генератор цитат!")
    print("Ваша цитата на сегодня:")
    print("-------------------------")
    print(get_zen_quote())
    print("-------------------------")


if __name__ == "__main__":
    main()
