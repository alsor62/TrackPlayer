import time
import datetime
import paho.mqtt.client as mqtt
import json
import random

import mqtt_pub

def read_track ():
    #track = pd.read_excel ('track_boot.xlsx')
    #print (track)
    file1 = open("tb1.txt", "r")
    nc ='.'
    fuel_full = 27.3
    m100f = 5.7

    prog_dist = (fuel_full/m100f)*100
    print('prg = ',prog_dist)

    lines = 0

    for line in file1:
        lines += 1
    print (lines)
    file1.close

    broker_address = "116.203.133.211"

    client = mqtt.Client("P1")  # create new instance
    client.connect(broker_address)  # connect to broker
    topic_pub = 'CarOS/Telemetry'

    time.sleep(3)

    file1 = open("tb1.txt", "r")



    while True:
        for line in file1:
            cline = line.strip()
            p1 = cline.find(' ')
            p2 = cline.find(' ',p1+1)
            delay = cline [p1:p2]

            p3 = cline.find(' ',p2+1)
            pname = cline [p2:p3]

            p4 = cline.find(' ',p3+1)
            pval = cline[p3:p4]

            p5 = cline.find(' ',p4+1)
            gps_s = cline[p4:p5]

            p6 = cline.find(' ', p5 + 1)
            gps_d = cline[p5:p6]

            pd = delay.find(',')
            if pd > 0:
                temp = list(delay)
                temp[pd] = nc
                delay = "".join(temp)
                fdelay = float(delay)
            else:
                fdelay = 0

            print('fdelay ', fdelay)

            pn = pname.find('NOP')
            if pn < 0:
                now = datetime.datetime.now()
                #print('curr time ',  now.strftime("%Y-%m-%d %H:%M:%S"))
                #print(fdelay,' name ',pname, 'val ', pval,' gps_s ',gps_s, 'gps_d ', gps_d)
                if pname.find('UFUEL') > 0:
                    pf = pval.find(',')
                    if pf > 0:
                        temp1 = list(pval)
                        temp1[pf] = nc
                        pval = "".join(temp1)
                        ffu = float(pval)
                        fuel_full = fuel_full - ffu
                        #print('FUEL = ', fuel_full)
                        #time.sleep(3)

                elif pname.find('M100FUEL') > 0:
                    pv1 = pval.find(',')
                    if pv1 > 0:
                        temp1 = list(pval)
                        temp1[pv1] = nc
                        pval = "".join(temp1)
                        m100f = float(pval)

                        #print('NEW 100L = ', m100f)
                        #prog_dist = (fuel_full/m100f)*100

                        #ctr_time = now1.strftime("%Y-%m-%d %H:%M:%S")

                        #pack_mqtt = {'curr_time': ctr_time, 'M100FUEL': m100f, 'PROGDIST': prog_dist,}
                        #print ('prognoz = ',prog_dist)
                        #time.sleep(5)

                elif pname.find('VGPS') > 0:

                    now1 = datetime.datetime.now()

                    ctr_time = now1.strftime("%Y-%m-%d %H:%M:%S")
                    # ctr_time = '33333'

                    if pval == '0':
                        lidar = 9999.99
                    else:
                        lidar = random.uniform(0.3, 4.5)

                    pack_mqtt = {'curr_time': ctr_time,'VGPS': pval, 'LATIT': gps_s, 'LONGT': gps_d, 'M100FUEL': m100f,'PROGDIST': prog_dist,'LIDAR1': lidar}
                    json_pack = json.dumps(pack_mqtt)
                    mqtt_pub.mqtt_pub(client, topic_pub, json_pack)
                else:
                    now1 = datetime.datetime.now()

                    ctr_time = now1.strftime("%Y-%m-%d %H:%M:%S")
                    # ctr_time = '33333'

                    pack_mqtt = {'curr_time': ctr_time, pname: pval,}
                    json_pack = json.dumps(pack_mqtt)
                    mqtt_pub.mqtt_pub(client, topic_pub, json_pack)






            else:

                now1 = datetime.datetime.now()

                ctr_time = now1.strftime("%Y-%m-%d %H:%M:%S")
                #ctr_time = '33333'
                #lidar = random.uniform(0.3,4.5)

                pack_mqtt = {'curr_time': ctr_time, 'CLIMATIC1': 18.7,}
                json_pack = json.dumps(pack_mqtt)
                mqtt_pub.mqtt_pub(client, topic_pub, json_pack)

                print('.')

            if fdelay > 0:
                time.sleep(fdelay)




        file1.close
        print('ddd')
        break