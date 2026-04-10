import requests
from config import API_URL


def get_zen_quote():
    """Получает случайную цитату с GitHub Zen API"""
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.text
        return "Не удалось получить цитату."
    except requests.exceptions.RequestException:
        return "Ошибка сети."