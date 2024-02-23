import requests
from bs4 import BeautifulSoup
import random

def fetch_bubble_sort_implementation_randomly():
    url = "https://api.stackexchange.com/2.2/search/advanced"
    params = {
        "order": "desc",
        "sort": "relevance",
        "accepted": "True",
        "tagged": "python;bubble-sort",
        "site": "stackoverflow",
        "filter": "withbody",
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch questions. Status code: {response.status_code}, Response: {response.text}")
            return []

        data = response.json()
        if not data['items']:
            print("No questions found.")
            return []

        question = random.choice(data['items'])
        if 'accepted_answer_id' not in question:
            print("Selected question does not have an accepted answer.")
            return []

        answer_id = question['accepted_answer_id']
        answer_url = f"https://api.stackexchange.com/2.2/answers/{answer_id}?site=stackoverflow&filter=withbody"
        answer_response = requests.get(answer_url)
        if answer_response.status_code != 200:
            print(f"Failed to fetch the accepted answer. Status code: {answer_response.status_code}, Response: {answer_response.text}")
            return []

        answer_data = answer_response.json()
        if not answer_data['items']:
            print("No answer data found.")
            return []

        print(f"Sourced from: {question['link']}")
        answer_body = answer_data['items'][0]['body']
        soup = BeautifulSoup(answer_body, 'html.parser')
        code_blocks = [code.text for code in soup.find_all('code')]
        print(code_blocks)
        if not code_blocks:
            print("No code blocks found in the answer.")
            return []

        print("Found code blocks from the randomly selected accepted answer.")
        for code_block in code_blocks:
            print(code_block)
        
        return code_blocks

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
