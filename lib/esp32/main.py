from esp_api import *
from default import api
import _thread

do_connect()
esp = ESP32("timtonix", my_local_ip())

scan_lock = _thread.allocate_lock()
scan_lock.acquire()

# Scan for available devices
receiver = _thread.start_new_thread(esp.udp_receiver, ())
scaner = _thread.start_new_thread(esp.udp_scan, (2236, scan_lock,))

while esp.target_ip == []:
    if scan_lock.locked() is True:
        pass
    else:
        print("NO HOST RIP")
        scan_lock.acquire()
        scaner = _thread.start_new_thread(esp.udp_scan, (2236, scan_lock,))
        print("restart")

print(esp.target_ip)
sended = False
while sended is False:
    if esp.button_green.value() == 0:
        morse_time = esp.get_button_time()
        morse_message = api.convert_button_time(morse_time)
        esp.udp_sender(morse_message, esp.target_ip[0][0], esp.target_ip[0][1])
        sended = True



