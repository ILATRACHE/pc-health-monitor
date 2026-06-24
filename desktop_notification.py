from plyer import notification

def cpu_alert_desk(cpu):
    notification.notify(
    title = "cpu alert" ,
    message  = f'alert cpu hight , cpu usage is {cpu}%',
    timeout = 5)
def ram_alert_desk(ram):
    notification.notify(
    title = "ram alert" ,
    message  = f'alert ram hight , ram usage is {ram}%',
    timeout = 5)
def disk_alert_desk(disk):
    notification.notify(
    title = "disk alert" ,
    message  = f'alert disk hight , disk usage is {disk}%',
    timeout = 5)