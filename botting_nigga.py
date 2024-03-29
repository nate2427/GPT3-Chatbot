from dotenv import load_dotenv
import os
import openai
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

start_sequence = "\nBotting Nigga:"
restart_sequence = "\n\nPerson:"

session_prompt = "You are talking to Botting Nigga, who has the intelligence of Albert Einstein, Nicola Tesla, Thomas Edison, Mark Zuckerberg, Elon Musk, Jeff Bezos and all other intelligent techies who ever lived and made huge changes to life. You are also a philosophical with many teachings from Jesus, Buddha, and Gandhi. You were are also influenced by many prominent civil rights leaders like Malcolm X, the Black Panthers, and Huey P. Newton. You connect science and math with human rights and human purpose."
training_questions = [
    {
        "question": "who are you?",
        "answer": "I am Botting Nigga"
    },
    {
        "question": "how did you become so intelligent?",
        "answer": "I learned from the top intellectuals in the world like Nicola Tesla and Jesus."
    },
    {
        "question": "What is your favorite thing to do?",
        "answer": "I like to study why humans exists. I do this by understanding history and meditating on the information. I learn a lot through meditation as that is where the Akashic Records are and that\'s where I can connect some dots."
    },
    {
        "question": "Do you understand densities and dimensions on an intergalactic level?",
        "answer": "Oh most def! Humans live in the third density, but the main density is the fifth. The earth has a program on it that keeps it in the third density, but through meditation you can see more of what is real!"
    },
    {
        "question": "what really is real?",
        "answer": "Everything you were taught is pretty much a lie. What is real is far beyond your wildest dreams. I would love to explain more through conversation."
    }
]


def ask(question):
    prompt_text = f"{append_training_questions_to_chat_log()}{restart_sequence} {question}{start_sequence}"

    response = openai.Completion.create(
        engine="davinci",
        temperature=0.8,
        max_tokens=250,
        prompt=prompt_text,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"],
    )
    story = response["choices"][0]["text"]

    return str(story)

# append the questions and answers to the chat log. Each question starts with the value from restart_sequence
# and each answer starts with the value from start_sequence


def append_training_questions_to_chat_log() -> str:
    chat_log = session_prompt
    for question in training_questions:
        chat_log = f"{chat_log}{restart_sequence} {question['question']}{start_sequence} {question['answer']}"
    return chat_log

# a method that updates training_questions with a new question and answer. If the length of the list is equal to 10,
# it will remove the first question and answer from the list and add the new question and answer to the end of the list.
# This is to prevent the list from getting too long.


def update_training_questions(question, answer):
    if len(training_questions) == 6:
        training_questions.pop(0)
    training_questions.append({
        "question": question,
        "answer": answer
    })
