import json
data_file       = str()
new_file        = str()

def InitFiles(df, nf):
    global      data_file
    global      new_file
    data_file   = df
    new_file    = nf

def ChangeData(ip, var, value):
    with open(data_file, "r") as f: data = json.load(f)
    data[ip][var] = value
    with open(data_file, "w") as f: json.dump(data, f, indent=4)

def WriteJson(data):
    with open(data_file, "w") as f: json.dump(data, f, indent=4)

def CreatePlayer(ip):
    with open(new_file) as f: new = json.load(f)["new"]
    print(new)
    with open(data_file) as f:
        data        = json.load(f)
        data[ip]    = new
    WriteJson(data)

def BanPlayer(ip):
    with open(new_file) as f: new = json.load(f)["new"]
    print(new)
    with open(data_file) as f:
        data        = json.load(f)
        data["bans"].append(ip)
    WriteJson(data)

def AlreadyExists(ip):
    with open(data_file, "r") as f: data = json.load(f)
    return ip in data

def KeyExists(ip, key):
    with open(data_file, "r") as f: data = json.load(f)
    return key in data[ip]

def AmIBanned(ip):
    with open(data_file, "r") as f: data = json.load(f)
    return ip in data["bans"]

def ViewJSON():
    with open(data_file, "r") as f: data = json.load(f)
    return str(data)
