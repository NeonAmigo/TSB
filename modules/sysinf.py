import platform
import sys
import time
import psutil

def get_system_info():
    os = platform.platform()
    python_version = sys.version.split('\n')[0]
    system_time = time.strftime('%H:%M:%S')
    uptime = get_uptime()
    bot_runtime = get_bot_runtime()
    disk_usage = get_disk_usage()

    info = {
        'OS': os,
        'Python Version': python_version,
        'System Time': system_time,
        'Uptime': uptime,
        'Bot Runtime': bot_runtime,
        'Disk Usage': disk_usage
    }

    return info

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime = time.strftime('%H:%M:%S', time.gmtime(uptime_seconds))
        return uptime

def get_bot_runtime():
    bot_runtime = "00:00:00"
    return bot_runtime

def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    used = disk_usage.used / (1024**3)
    total = disk_usage.total / (1024**3)
    return f'{used:.2f} GB / {total:.2f} GB'

system_info = get_system_info()

syss = ('⚙️ Информация о системе:\n'
      '🖥️ ОС:', system_info['OS'], '\n'
      '🐍 Версия Python:', system_info['Python Version'], '\n'
      '🕧️ Системное время:', system_info['System Time'], '\n'
      '⏳️ Прошло с запуска системы:', system_info['Uptime'], '\n'
      '⌛️ Время работы бота:', system_info['Bot Runtime'], '\n'
      '💽 Занято файлами:', system_info['Disk Usage'])