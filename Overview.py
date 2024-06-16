import requests


def fetch_api_data(url, params=None):
    """
    Функция для запроса данных из API.

    Args:
        url (str): URL API-endpoint, к которому нужно обратиться.
        params (dict, optional): Словарь с параметрами запроса. Defaults to None.

    Returns:
        dict or None: Словарь с данными, полученными из API, или None в случае ошибки.
    """
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None
    except ValueError as e:
        print(f"Ошибка при обработке ответа API: {e}")
        return None


# Пример использования функции:
api_url = "https://api.github.com"
params = {"q": "search_term", "limit": 10}
data = fetch_api_data(api_url, params)
if data:
    print(data)
else:
    print("Не удалось получить данные из API.")


import numpy as np
c = np.random.randint(1, 10, size=(4,4))
d = np.random.randint(1, 10, size=(4,4))
print(c)
print(d)
print(c**d)


import pandas as pd

data = {
    'Name': ['Tom', 'Nick', 'John', 'Tom', 'John'],
    'Score': [90, 85, 88, 92, 89]
}

df = pd.DataFrame(data)

print(df)