import psutil
import time
from telegram_notification import send_message
from desktop_notification import cpu_alert_desk , ram_alert_desk , disk_alert_desk
from check_pc_connection import check_connection
from creat_rapport import info , error , warning
from read_repport import main_event
def monitoring(cpu_limit,ram_limit,disk_limit):
    send_cpu = False
    send_ram = False
    send_disk = False
    previous_conection_stat = None
    
    while True :
        conection_stat= check_connection()
        cpu= psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('C://').percent
        if cpu < cpu_limit :
            info(f'{cpu},cpu ok')
            send_cpu = False
        else :
            if not send_cpu :
                cpu_alert_desk(cpu)
                if conection_stat :
                    send_message(f'alert cpu hight , cpu usage is {cpu}%')
                    warning(f'alert cpu hight , cpu usage is {cpu}%')
                else : 
                    error(f"cpu : {cpu},Failed to send Telegram message")
                send_cpu = True
            else :
                warning(f'cpu hight , alert already send')
        if ram < ram_limit :
            info(f'{ram},ram ok')
            send_ram = False
        else :
            if not send_ram :
                ram_alert_desk(ram)
                if conection_stat :
                    send_message(f'alert ram hight , ram usage is{ram}%')
                    warning(f'alert ram hight , ram usage is{ram}%')
                else : 
                    error(f"ram : {ram},Failed to send Telegram message")
                send_ram = True
            else :
                warning(f'ram hight , alert already send')
        if disk < disk_limit :
            info(f'{disk}, disk ok')
            send_disk = False
        else :
            if not send_disk :
                disk_alert_desk(disk)
                if conection_stat :
                    send_message(f'alert disk hight , disk is {disk}')
                    warning(f'alert disk hight , disk is {disk}')
                else : 
                    error(f"disk : {disk} , Failed to send Telegram message")
                send_disk = True
        print(cpu)
        print(ram)
        print(disk)
        time.sleep(10)
        if previous_conection_stat == False and conection_stat ==True:
            send_message("internet_back")
            main_rapport = main_event()
            send_message(main_rapport)
        previous_conection_stat = conection_stat