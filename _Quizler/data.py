import requests


def get_questions():
    params = {
        'amount': 10,
        'type': 'boolean',
        'category': 18
    }

    response = requests.get(url='https://opentdb.com/api.php', params=params)
    response.raise_for_status()

    raw_data = response.json()
    return raw_data['results']


question_data = get_questions()
# print(question_data)