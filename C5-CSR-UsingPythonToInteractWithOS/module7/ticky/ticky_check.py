#!/usr/bin/env python3

import sys,re,csv


def write_csv(thedict:dict) -> None:
    ...

def read_log(data) -> None:
    err_count = {}
    with open(data,"r") as f:
        for l in f.readlines():
            found = re.search(r"ERROR ([\w ]*) .*", l)
            # if found:
            if found := re.search(r"ERROR ([\w ]*) .*", l):
                if found[1] not in err_count:
                    err_count[found[1]] = 1
                else:
                    err_count[found[1]] += 1
    
    sorted_err_cnt = dict(sorted(err_count.items(), key=lambda x:x[1], reverse=True))
    with open("error_csv.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["Error", "Count"])
        writer.writeheader()
        for l in sorted_err_cnt.items():
            writer.writerow({"Error": l[0], "Count": l[1]})

    usr_cnt={}
    # pattern_count=r".*: (\w*) .*\] \(([\w]*)\)"
    with open(data, "r") as f:
        for l in f.readlines():
            # found=re.search(r".*: (\w*) .*\] \(([\w]*)\)", l)
            if found := re.search(r".*: (\w*) .*\] \(([\w]*)\)", l):
                if found[2] not in usr_cnt:
                    if found[1].lower()=="error":
                        usr_cnt[found[2]] = {"INFO":0, "ERROR":1}
                    else:
                        usr_cnt[found[2]] = {"INFO":1, "ERROR":0}
                else:
                    if found[1].lower()=="error":
                        usr_cnt[found[2]]["ERROR"] += 1
                    else:
                        usr_cnt[found[2]]["INFO"] += 1

    sorted_usr_cnt=dict(sorted(usr_cnt.items()))
    # for l in sorted_usr_cnt.items():
    #     print(l[0], l[1])
    with open("user_statistics.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["Username", "INFO", "ERROR"])
        writer.writeheader()
        for l in sorted_usr_cnt.items():
            writer.writerow({"Username": l[0], "INFO": l[1]["INFO"], "ERROR": l[1]["ERROR"]})


if __name__ == "__main__":
    read_log(sys.argv[1])