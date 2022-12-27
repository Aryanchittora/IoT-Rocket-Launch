from flask import Flask, render_template

from paho.mqtt import client as mqtt_client

app = Flask(__name__)
#Set the Hostname, Port & TopicName
topic = 'topicName/iot'
port = 1883
broker = 'broker.emqx.io'

client_id = 'test'
username = 'emqx'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client

#Define the first page of the web application
@app.route('/')
def index():
    return render_template('index.html')

#Define the button page of the web application
@app.route('/main')
def main():
    return render_template('main.html')

#Define the Release Orbital Arm button and connect with MQTT server
@app.route('/1', methods=['POST'])
def release():
    release_test()
    
    return render_template('1.html')


def release_test():
    client = connect_mqtt()
    client.loop_start()
    send_data(client, 1)

#Define the Main Engine Test button and connect with MQTT server
@app.route('/2', methods=['POST'])
def engine():
    engine_test()
    return render_template('2.html')

def engine_test():
    client = connect_mqtt()
    client.loop_start()
    send_data(client, 2)


#Define the Activate Hydrogen button and connect with MQTT server
@app.route('/3', methods=['POST'])
def hydrogen():
    hydrogen_test()
    return render_template('3.html')

def hydrogen_test():
    client = connect_mqtt()
    client.loop_start()
    send_data(client, 3)

#Define the Main Engine Ignite button and connect with MQTT server
@app.route('/4', methods=['POST'])
def ignite():
    ignite_test()
    return render_template('4.html')

def ignite_test():
    client = connect_mqtt()
    client.loop_start()
    send_data(client, 4)

#Define the Hydrogen Vent Arm button and connect with MQTT server
@app.route('/5', methods=['POST'])
def vent():
    vent_test()
    return render_template('5.html')

def vent_test():
    client = connect_mqtt()
    client.loop_start()
    send_data(client, 5)

#Define the Ignite both SRB's button and connect with MQTT server
@app.route('/6', methods=['POST'])
def srb():
    srb_test()
    return render_template('6.html')

def srb_test():
    client = connect_mqtt()
    client.loop_start()
    send_data(client, 6)

def send_data(client, msg):
    messge = str(msg)
    result = client.publish(topic, messge)
    status = result[0]

    if status == 0:
        print(f'Sending {msg} to {topic}')

if __name__ == "__main__":
    app.run(port=5001)





