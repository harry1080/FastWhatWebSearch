# encoding:utf-8
import pymongo
from config.config import config


class MyMongodb:

    def __init__(self):
        self._client = pymongo.MongoClient(config['mongodb_uri'])
        self._coll = None
        self.database = None

    def set_database(self,database):
        self.database = database

    def set_table(self,table_name):
        self._coll = self._client[self.database][table_name]

    def find_all(self,condition=None):
        if(condition == None):
            return self._coll.find()
        else:
            return self._coll.find(condition)

    def __del__(self):
        self._client.close()