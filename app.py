from botting_nigga import ask, update_training_questions
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, session
app = Flask(__name__)
# if for some reason your conversation with Botting Nigga gets weird, change the secret key
app.config['SECRET_KEY'] = '24005770.848dfgb2531039'


@app.route('/bottn_nigga', methods=['POST'])
def bottn_nigga():
    incoming_msg = request.values['Body']

    answer = ask(incoming_msg)

    update_training_questions(incoming_msg, answer)

    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)


if __name__ == '__main__':
    app.run(debug=True)
