from shutil import disk_usage
import psutil

def check_disk_usage(path = "/") -> float:
    du = disk_usage(path)
    return du.free/du.total*100

def check_cpu_percentage() -> float:
    return psutil.cpu_percent(0.1)