import pymongo
import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), 'env')
load_dotenv(dotenv_path)


client = pymongo.MongoClient(os.getenv('MONGO_DB'))
db = client.XMYCHAN
col = db.pipin_admina


def create_user(user):
    find_ = col.find_one({
        'user': str(user)
    })
    if not find_:

        col.insert_one({
            "user": str(user),
            'state': False
        })


def change_state(user, set_=False):
    find_ = col.find_one({
        'user': str(user)
    })
    if set_:
        col.update(
            {'_id': find_['_id']},
            {'$set': {'state': True}}
        )
    else:
        col.update_one(
            {'_id': find_['_id']},
            {'$set': {'state': False}}
        )


def give_state(user):
    find_ = col.find_one(
        {'user': str(user)}
    )
    return find_['state']
