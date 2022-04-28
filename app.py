from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.kqpab.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Eom')
def Eom():
    return render_template('Eom.html')

@app.route('/Lee')
def Lee():
    return render_template('Lee.html')

@app.route('/Choi')
def Choi():
    return render_template('Choi.html')

@app.route('/Han')
def Han():
    return render_template('Han.html')

@app.route("/team_comment", methods=["POST"])
def team_comment_post():
    nicname_receive = request.form['nicname_give']
    comment_receive = request.form['comment_give']

    doc = {
        'nicname':nicname_receive,
        'comment':comment_receive
    }
    db.team_comment.insert_one(doc)
    return jsonify({'msg':'소중한 코멘트 감사합니다'})

@app.route("/team_comment", methods=["GET"])
def team_comment_get():
    all_comment = list(db.team_comment.find({}, {'_id': False}))
    return jsonify({'comments':all_comment})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)