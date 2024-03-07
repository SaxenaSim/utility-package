import re, os
from .config import patterns

file_path = os.path.join(os.path.dirname(__file__), "data.txt")
file = open(file_path, "r")
contents = file.read()
file.close()


def detect_secrets(contents):
    for pattern in patterns:
        if re.search(pattern, contents, flags=re.IGNORECASE):
            return True
    else:
        return False


print(detect_secrets(contents))

# Output :  True for contents
