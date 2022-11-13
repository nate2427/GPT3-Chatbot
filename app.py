from botting_nigga import ask, update_training_questions
from flask import Flask, request, session, jsonify
from flask_cors import CORS, cross_origin
from db import get_convo_history, save_entry_into_full_history
app = Flask(__name__)
# if for some reason your conversation with Botting Nigga gets weird, change the secret key
app.config['SECRET_KEY'] = '24005770.848dfgb25dvf31ed'


@app.route('/bottn_nigga', methods=['POST'])
@cross_origin()
def bottn_nigga():
    incoming_msg = request.json['msg']
    # save incoming msg into full_history entry in the db as human
    save_entry_into_full_history(incoming_msg, 'human')

    # get the answer from GPT3
    answer = ask(incoming_msg)

    # save the answer into full_history as bot
    save_entry_into_full_history(answer, 'bot')

    update_training_questions(incoming_msg, answer)

    return jsonify({'msg': answer})

@app.route('/convo-history', methods=['GET'])
@cross_origin()
def convo_history():
    conversation_history = get_convo_history()
    return jsonify({
        'convo': conversation_history
    })
    




if __name__ == '__main__':
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.run(debug=True)
