import pymongo
import os
from dotenv import load_dotenv
load_dotenv()
MONGO_DB_PWD= os.getenv('MONGO_DB_PWD')
client = pymongo.MongoClient("mongodb+srv://streetcodernate:" + MONGO_DB_PWD + "@maincluster.0bemjlv.mongodb.net/?retryWrites=true&w=majority")
db = client.AI_CONVOS
def get_db_collection(collection):
    return db.get_collection(collection)


def get_convo_history():
    convos_collection = get_db_collection('convos')
    training_questions = get_training_questions(convos_collection)
    convo = convert_training_questions_to_convo(training_questions)
    convo.extend(get_full_history(convos_collection))
    return convo

def get_full_history(collection):
    # check if history exists, if not create the list and store it, otherwise grab it and return it
    convo_history = collection.find_one(
        {
            'full_history': {
                '$exists': True
            }
        }
    )
    if convo_history == None:
        convo_history = []
        collection.insert_one({
            'full_history': convo_history
        })
    else:
        convo_history = convo_history['full_history']
    return convo_history
         


def get_training_questions(collection):
    # grab the questions from the training set
    training_questions = collection.find_one(
        {
            "bot_training_set":{
                '$exists': True
            }
        }
    )
    training_questions = training_questions['bot_training_set']['questions']
    return training_questions

def convert_training_questions_to_convo(questions):
    convo = []
    for question in questions:
        convo.append({
            'human': question['question'],
            'bot': question['answer']
        })
    return convo
