import os
import ConfigParser

def setup_config(filename):
    """Parse config file, setup config object and return config object

    :param filename: Config file name.
    :type filename: str

    :return: A config object that can be used to read configs.
    :rtype: Config object

    """
    config_file_dir = os.path.dirname(os.path.realpath(__file__))
    config_file_path = os.path.join(config_file_dir, filename)

    config = ConfigParser.SafeConfigParser()
    config.read(config_file_path)
    return config
