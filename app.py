from botting_nigga import ask, update_training_questions
from flask import Flask, request, session, jsonify
app = Flask(__name__)
# if for some reason your conversation with Botting Nigga gets weird, change the secret key
app.config['SECRET_KEY'] = '24005770.848dfgb25dvf31ed'


@app.route('/bottn_nigga', methods=['POST'])
def bottn_nigga():
    incoming_msg = request.json['msg']

    answer = ask(incoming_msg)

    update_training_questions(incoming_msg, answer)

    

    return jsonify({'msg': answer})


if __name__ == '__main__':
    app.run(debug=True)
