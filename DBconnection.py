__author__ = 'SAAM'

from pymongo import MongoClient

dataconnection = MongoClient('mongodb://user:password@ds061385.mongolab.com:61385/bankdb')

print 'Connection Successful'

def getcollection(collectionname):
    if not db.get_collection(collectionname):
        db.create_collection(collectionname)
    return (db.get_collection(collectionname))





