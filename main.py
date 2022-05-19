# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import paho.mqtt.client as mqtt  # import the client1

import datetime

import json

import mqtt_pub

import xls_read

#broker_address = "116.203.133.211"

#client = mqtt.Client("P1")  # create new instance
#client.connect(broker_address)  # connect to broker
#topic_pub = 'Up'


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    #now = datetime.datetime.now()
    #pack_mqtt = {'curr_time': now.strftime("%Y-%m-%d %H:%M:%S"), 'Temperature': 232,}
    #json_pack = json.dumps(pack_mqtt)


    #mqtt_pub.mqtt_pub(client,topic_pub, json_pack)

    xls_read.read_track()

    print ('GOPA')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
