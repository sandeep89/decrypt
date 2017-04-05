import os
import csv
import json
from helper import setup_config
from aes_encyption import decrypt

CONFIG_FILENAME = 'decrypt.cfg'
DATA_CONFIG_SECTION = 'data'

config = setup_config(CONFIG_FILENAME)

