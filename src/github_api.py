import requests
from config import GITHUB_TOKEN

def get_repo_contents(owner, repo, path=''):
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_file_content(url):
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json()['content']

def repo_to_text(owner, repo):
    contents = get_repo_contents(owner, repo)
    text = ''
    for item in contents:
        if item['type'] == 'file':
            content = get_file_content(item['download_url'])
            text += f"File: {item['name']}\n{content}\n\n"
    return text
