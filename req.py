
from flask import Flask, request
from bard import MyBard
from bard import BARD_CLI_DICT


app = Flask(__name__)


@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    token = data.get('token', 'no_exist')
    if token == 'no_exist':
        return 'token can not be empty', 500
    print(token)
    if BARD_CLI_DICT.exist(token):
        bard = BARD_CLI_DICT.get(token)
    else:
        bard = MyBard(usr_token=token)
    aws = bard.send(data.get('words', 'hello'))
    return aws, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
