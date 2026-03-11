import psutil
import json

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent()
    return {"cpu_usage": cpu_percent}

def get_ram_usage():
    ram_info = psutil.virtual_memory()
    ram_percent = ram_info.percent
    return {"ram_usage": ram_percent}

def get_disk_usage(disk):
    disk_info = psutil.disk_usage(disk)
    disk_percent = disk_info.percent
    return {"disk_usage": disk, "disk_percent": disk_percent}

def get_system_info():
    cpu_info = get_cpu_usage()
    ram_info = get_ram_usage()
    disk_info = get_disk_usage("/")

    return {
        "cpu_info": cpu_info,
        "ram_info": ram_info,
        "disk_info": disk_info
    }
