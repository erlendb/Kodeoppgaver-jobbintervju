import article
import bottle
from bottle import request, response
from bottle import get
import json

app = bottle.default_app()

# enable_cors() is stolen from from https://stackoverflow.com/questions/17262170/bottle-py-enabling-cors-for-jquery-ajax-requests
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@get('/string_count_in_article/<title>/<string>')
@enable_cors
def handler(title, string):
    a = article.Article(title)
    a.fetch()
    
    if a.has_error():
        response.status = 400;
        return;
        
    count = a.get_string_count_in_text(string)
    
    response.headers['Content-Type'] = 'application/json'
    response.status = 200;
    return json.dumps({'count': count});
    
if __name__ == '__main__':
    bottle.run(host = '127.0.0.1', port = 8000)