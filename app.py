from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import os

#import db_utils
import score_calculation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('index.html')

@app.route('/getscore', methods=['POST'])
def get_score():
    username = request.form['username']
    github_id = request.form['github_id']
    stackoverflow_id = request.form['stackoverflow_id']
    hackernews_id = request.form['hackernews_id']
    score = score_calculation.calculate_score(github_id, stackoverflow_id, hackernews_id)
    user_dict = {
        'username': username,
        'github_id': github_id,
        'stackoverflow_id': stackoverflow_id,
        'hackernews_id': hackernews_id,
        'score': score
    }
    #db_utils.insert_into_db(user_dict)

    return render_template('getscore.html', user_dict=user_dict, score=score)

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port, debug=True)
