
import os
from flask import Flask, request, Response

app = Flask(__name__)

SLACKPEDIA_BOT_DEBUG = False

@app.route('/contact', methods=['post'])
def contact():
    query = request.values.get('text')
    result = get_query_result(query)

    return 'Hello' + name
    #Response(result, content_type='charset=utf-8; text/plain')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=SLACKPEDIA_BOT_DEBUG)