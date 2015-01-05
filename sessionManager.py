__author__ = 'bernardo'
import cookieHandler
import config
import random
import pickle
import os

def get(self, key):
    return readSession(self)[key]


def set(self, key, value):
    _SESSION_ = readSession(self)
    _SESSION_[key] = value
    commitSession(self, _SESSION_)

def newSession(self):
    return startSession(self, True)

def startSession(self, forceStart = False):
    session = readSessionKey(self)
    if len(str(session)) < 10 or forceStart:
        hash = random.getrandbits(128)
        __SESSION__ = {}
        save_obj(__SESSION__, hash)
        key = hash
        try:
            __SESSION__2 = load_obj(key)
        except:
            key = startSession(self, True)
            __SESSION__2 = load_obj(key)

    else:
        key = readSessionKey(self)
        try:
            __SESSION__2 = load_obj(key)
        except:
            key = startSession(self, True)
            __SESSION__2 = load_obj(key)

        __SESSION__ = readSession(self, key)

    return key


def commitSession(self, __SESSION__, key = None):
    if key == None:
        key = readSessionKey(self)
    save_obj(__SESSION__, key)
    return


def readSessionKey(self):
    session = cookieHandler.ReadCookie(self, config.__SESSION_COOKIE_NAME__)
    return session


def readSession(self, key = None):
    if key == None:
        key = readSessionKey(self)
    __SESSION__ = {}
    try:
        __SESSION__2 = load_obj(key)
    except:
        key = startSession(self, True)
        __SESSION__2 = load_obj(key)

    return __SESSION__2


def save_obj(obj, name):
    with open(config.__SESSIONS_DIR__ + str(name) + '.session', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(config.__SESSIONS_DIR__ + str(name) + '.session', 'rb') as f:
        return pickle.load(f)


def delete_all_sessions():
    folder = config.__SESSIONS_DIR__
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e

def delete_session(key):
    folder = config.__SESSIONS_DIR__
    file_path = os.path.join(folder, str(key)+'.session' )
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception, e:
        print e