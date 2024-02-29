#!/usr/bin/env python3

import subprocess
import sys

def get_file_name(x: str) -> str:
    return x.strip().split("/")[-1]

try: 
    with open(sys.argv[1]) as f:
        for x in f.readlines():
            old_x = get_file_name(x)
            new_x = get_file_name(x).replace("jane","jdoe")
            subprocess.run(["mv",f"./data/{old_x}", f"./data/{new_x}"])
except FileNotFoundError:
    sys.exit("!!!!??")

# #!/usr/bin/env python3

# import subprocess
# import sys

# def get_file_name(x: str) -> str:
#     return x.strip().split("/")[-1]

# try:
#     with open(sys.argv[1]) as f:
#         for x in f.readlines():
#             old_x = get_file_name(x)
#             new_x = get_file_name(x).replace("jane","jdoe")
#             print(old_x, new_x)
#             subprocess.run(["mv","../data/"+old_x, "../data/"+new_x])
# except FileNotFoundError:
#     sys.exit("!!!!??")
