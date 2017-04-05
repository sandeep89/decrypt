import base64
import hashlib
import zlib
from Crypto import Random
from Crypto.Cipher import AES
from helper import setup_config

CONFIG_FILENAME = '../decrypt.cfg'
GRAYLOG_CONFIG_SECTION = 'graylog'

bs = 16


def get_key(key):
    if key is None:
        config = setup_config(CONFIG_FILENAME)
        key = config.get(GRAYLOG_CONFIG_SECTION, 'key')
    return key


def encrypt(raw, key=None):
    key = get_key(key)
    raw = ':$;' + zlib.compress(raw)
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))


def decrypt(enc, key=None):
    key = get_key(key)
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(enc[AES.block_size:]))
    if ':$;' in data:
        return zlib.decompress(data[3:])
    else:
        return data


def pad(s):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)


def unpad(s):
    return s[:-ord(s[len(s)-1:])]
