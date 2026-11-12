import requests

from config import TOKEN, TG_BASE_URL, CAT_BASE_URL


def send_message(chat_id: int | str, text: str) -> None:
    url = f'{TG_BASE_URL}{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url, json=payload)


def send_photo(chat_id, photo: str, caption: str = '') -> None:
    url = f'{TG_BASE_URL}{TOKEN}/sendPhoto'
    payload = {'chat_id': chat_id, 'photo': photo, 'caption': caption}
    response = requests.post(url, json=payload, timeout=30)
    if response.status_code != 200:
        print('sendPhoto xato:', response.status_code, response.text)


def get_updates(offset: int | None = None) -> list[dict]:
    url = f'{TG_BASE_URL}{TOKEN}/getUpdates'
    payload = {
        'offset': offset
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data['result']

    return []


def get_randomcat_image() -> str:
    try:
        response = requests.get(CAT_BASE_URL, timeout=10)
        response.raise_for_status()
        image_url = response.json().get('url', '')
    except requests.RequestException as e:
        print('cataas xato:', e)
        return ''

    print('cataas javobi:', image_url)  # tekshirish uchun
    if image_url.startswith('http'):
        return image_url
    return f'https://cataas.com/{image_url.lstrip("/")}'