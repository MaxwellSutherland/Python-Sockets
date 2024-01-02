from configparser import ConfigParser
config = ConfigParser()

def Config_INIT():
    try: config.read("config.ini")
    except:
        print("No file [config.ini]")
        exit()

def GetVariable(section, var):return config[section][var]
