import paho.mqtt.client as mqtt  # import the client1



def mqtt_pub (mqtt_client,t_p,p_val):

    # print("Publishing message to topic", "Up")
    mqtt_client.publish(t_p, p_val)