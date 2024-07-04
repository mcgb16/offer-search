import requests

def get_response(url) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text
        return content
    else:
        error_message = f"Falha na requisição. Status code: {response.status_code}"
        return error_message
