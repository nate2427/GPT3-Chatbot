from botting_nigga import ask, append_interaction_to_chat_log
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, session
app = Flask(__name__)
# if for some reason your conversation with Botting Nigga gets weird, change the secret key
app.config['SECRET_KEY'] = '0.848436602531039'


@app.route('/bottn_nigga', methods=['POST'])
def bottn_nigga():
    incoming_msg = request.values['Body']
    # chat_log = session.get('chat_log')
    answer = ask(incoming_msg)

    # session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
    #                                                      chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)


if __name__ == '__main__':
    app.run(debug=True)
