import requests

class Article():
    base_url = 'https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page='
    
    def __init__(self, title):
        self.title = title
        self.content = None
    
    def fetch(self):
        url = Article.base_url + self.title
        self.content = requests.get(url).json()
    
    def get_string_count_in_text(self, string):
        return self.content['parse']['text']['*'].count(string)
    
    def has_error(self):
        return 'error' in self.content

if __name__ == '__main__':
    title = 'KGB'
    string = title
    a = Article(title)
    a.fetch()
    print(f'{a.get_string_count_in_text(string)} occurances of {string} in article {title}')