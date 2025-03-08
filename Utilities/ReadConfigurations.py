from configparser import ConfigParser


def read_configurations(category, key):
    config = ConfigParser()
    config.read("C:\Python selenium\BritsUIandAPI\Configurations\confi.ini")
    return config.get(category, key)