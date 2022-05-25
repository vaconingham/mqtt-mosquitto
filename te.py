from encodings import utf_8
import json, _aix_support


msg_log = {
    1234: "54",
    5423: "43",
    7465: "23"
}

def decode():
    payload = b'{\n    "1": 29.0,\n    "2": 29.0,\n    "3": 29.0\n}'
    new = json.loads(payload.decode('utf_8'))
    print(new)

decode()