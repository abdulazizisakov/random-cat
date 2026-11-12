import requests

from config import TOKEN, TG_BASE_URL, CAT_BASE_URL

def send_message(chat_id: int | str, text: str) -> None:
    url = f'{TG_BASE_URL}{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url, json=payload)

def send_photo(chat_id: int | str, photo: str, caption: str = '') -> None:
    url = f'{TG_BASE_URL}{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': photo,
        'caption': caption
    }
    requests.post(url, json=payload)

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
    url = CAT_BASE_URL
    response = requests.get(url)

    if response.status_code == 200:
        # Agar javob JSON formatida kelsa
        try:
            data = response.json()
            image_path = data.get('url', '')
            if image_path:
                return f'https://cataas.com{image_path}'
        except:
            pass
        
        # Agar to'g'ri kelmasa, rasmning o'zining URL manzilini qaytaradi
        return response.url
        
    return ''