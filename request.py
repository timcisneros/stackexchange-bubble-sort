import requests
from bs4 import BeautifulSoup
import random

def fetch_bubble_sort_implementation_randomly():
    """
    Fetches a random bubble sort implementation from Stack Overflow.
    """
    url = "https://api.stackexchange.com/2.2/search/advanced"
    params = {
        "order": "desc",
        "sort": "relevance",
        "accepted": "True",
        "tagged": "python;bubble-sort",
        "site": "stackoverflow",
        "filter": "withbody",
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch questions. Status code: {response.status_code}")

    data = response.json()
    if not data['items']:
        raise Exception("No questions found.")

    question = random.choice(data['items'])
    print("Sourced from:", question["link"])
    answer_id = question['accepted_answer_id']
    answer_url = f"https://api.stackexchange.com/2.2/answers/{answer_id}?site=stackoverflow&filter=withbody"
    answer_response = requests.get(answer_url)
    if answer_response.status_code != 200:
        raise Exception(f"Failed to fetch the accepted answer. Status code: {answer_response.status_code}")

    answer_data = answer_response.json()
    if not answer_data['items']:
        raise Exception("No answer data found.")

    answer_body = answer_data['items'][0]['body']
    soup = BeautifulSoup(answer_body, 'html.parser')
    code_blocks = [code.text for code in soup.find_all('code')]
    if not code_blocks:
        raise Exception("No code blocks found in the answer.")

    return code_blocks