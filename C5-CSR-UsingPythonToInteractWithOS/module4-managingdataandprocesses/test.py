#!/usr/bin/env python3

import psutil
import shutil
import argparse

class Parser():
    def __init__(self, *args: list[str]) -> None:
        parser = argparse.ArgumentParser()
        if len(args) > 0:
            for x in args:
                parser.add_argument(x)
            self.__list_args = parser.parse_args()
    
    def get_list_args(self) -> list[str]:
        return self.__list_args

def check_storage(path:str) -> int:
    if path == None:
        return "You're not passing the path using --nyetorage argument"
    return shutil.disk_usage(path)

def check_cpu(percentage:float) -> int:
    if percentage == None:
        return "You're not passing the percentage using --nyepeu argument"
    return psutil.cpu_percent(float(percentage))

if __name__ == "__main__":
    parser = Parser("--nyetorage","--nyepeu")
    list_args = parser.get_list_args()

    print("Storage:", check_storage(list_args.nyetorage))
    print("CPU:", check_cpu(list_args.nyepeu))