import os
import csv
import json
from helper import setup_config
from aes_encyption import decrypt

CONFIG_FILENAME = 'decrypt.cfg'
DATA_CONFIG_SECTION = 'data'

config = setup_config(CONFIG_FILENAME)


def get_csv_reader(filename, delimiter, quotechar):
    """Return CSV reader object, given csv filename, delimiter and quotechar

    :param filename: CSV filename.
    :type filename: str
    :param delimiter: CSV delimiter, single character python string.
    :type delimiter: str
    :param quotechar: CSV quote character, single character python string.
    :type quotechar: str

    :return: CSV reader object that can be used to read CSV file content.
    :rtype: CSV reader object

    """
    return csv.reader(open(filename), delimiter=delimiter, quotechar=quotechar)


def get_headers_and_data(reader):
    """Return CSV headers and data as tuple.

    :param reader: CSV reader.
    :type reader: CSV reader object.

    :return: Tuple of CSV headers and data.
    :rtype: tuple

    """
    raw_data = []
    headers = reader.next()
    for data in reader:
        elem = {}
        for idx, col in enumerate(data):
            elem[headers[idx]] = col
        raw_data.append(elem)
    return (headers, raw_data)


def get_decrypted_data(raw_data, decrypt_fields):
    """Returns decrypted data, given a list of fields to be decrypted.

    :param raw_data: List of raw data, contains encrypted data.
    :type raw_data: list
    :param decrypt_fields: List of fields to be decrypted.
    :type decrypt_fields: list

    :return: List of decrypted data.
    :rtype: list

    """
    dec_data = []
    for data in raw_data:
        for field in decrypt_fields:
            try:
                if data[field] != '':
                    data[field] = decrypt(data[field])
            except:
                # For data that can't be decrypted, put as it is
                data[field] = data[field]

        dec_data.append(data)
    return dec_data


if __name__ == '__main__':
    reader = get_csv_reader(
        config.get(DATA_CONFIG_SECTION, 'data_file'),
        config.get(DATA_CONFIG_SECTION, 'delimiter'),
        config.get(DATA_CONFIG_SECTION, 'quotechar')
    )
    decrypt_fields = config.get(
        DATA_CONFIG_SECTION,
        'decrypt_fields'
    ).split(',')
    headers, raw_data = get_headers_and_data(reader)
    dec_data = get_decrypted_data(raw_data, decrypt_fields)
    # Print the decrypted data
    # ensure_ascii characters are not escaped. This is to avoid dump failures
    # due to special symbols.
    print json.dumps(dec_data, indent=2, ensure_ascii=False)
