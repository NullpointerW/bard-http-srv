from bardapi import Bard
import bardapi
import threading
import datetime
import time

from typing import Dict


class ThreadSafeDict(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.dict = {}

    def set(self, key, value):
        with self.lock:
            self.dict[key] = value

    def get(self, key):
        with self.lock:
            return self.dict.get(key)

    def in_(self, key):
        with self.lock:
            if key in self.dict:
                return True
            else:
                return False

    def exist(self, key):
        with self.lock:
            if key in self.dict:
                return True
            else:
                return False

    def clear(self):
        with self.lock:
            self.dict.clear()

    def sacn_and_clean(self):
        with self.lock:
            del_list = []
            now_time = datetime.datetime.now()
            for key, bard in self.dict.items():
                specified_time_plus_5 = bard.time + \
                    datetime.timedelta(minutes=5)
                if specified_time_plus_5 <= now_time:
                    del_list.append(key)
            for it in del_list:
                self.dict.pop('d', None)


BARD_CLI_DICT: Dict[str, Bard] = ThreadSafeDict()


def clear():
    while True:
        time.sleep(60*5)
        BARD_CLI_DICT.clear()


threading.Thread(target=clear).start()


class MyBard:
    ___token___ = 'ZA***********************************IX5cowUrykdy7g.'

    @classmethod
    def change_token(cls, token):
        cls.___token___ = token
        print("bard key has been changed, all clients will be removed")
        BARD_CLI_DICT.clear()

    def __init__(self, usr_token):
        print("new bard")
        self.usr_token = usr_token
        self.bard = bardapi.Bard(token=self.__class__.___token___)
        self.time = datetime.datetime.now()
        BARD_CLI_DICT.set(usr_token,self)

    def send(self, words):
        self.time = datetime.datetime.now()
        return self.bard.get_answer(words)['content']
