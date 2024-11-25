import network
import time
import ubinascii
import machine
from umqtt.simple import MQTTClient

# Wi-Fi credentials
SSID = "dit is geen modum"
PASSWORD = "L0L-het-is-het-wel"

# Azure IoT Hub credentials
IOT_HUB_HOSTNAME = "SteamBox.azure-devices.net;DeviceId=2003;SharedAccessKey=Kc+QVkohzVZzf+zBAa52dqZnISNHgswnK5sKEaICauk="
DEVICE_ID = "2003"
DEVICE_KEY = "Kc+QVkohzVZzf+zBAa52dqZnISNHgswnK5sKEaICauk="

# MQTT configuration
BROKER = IOT_HUB_HOSTNAME
TOPIC = "devices/{}/messages/devicebound/#".format(DEVICE_ID)

# GPIO setup
POWER_PIN = machine.Pin(15, machine.Pin.OUT)

# Connect to Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        time.sleep(1)
    print("Connected:", wlan.ifconfig())

# Generate SAS Token
def generate_sas_token():
    import hmac
    import hashlib
    import base64
    from time import time
    
    expiry = int(time() + 3600)  # Token valid for 1 hour
    uri = "{}/devices/{}".format(IOT_HUB_HOSTNAME, DEVICE_ID)
    string_to_sign = "{}\n{}".format(uri, expiry)
    key = base64.b64decode(DEVICE_KEY)
    signature = hmac.new(key, string_to_sign.encode('utf-8'), hashlib.sha256).digest()
    signature = base64.b64encode(signature).decode('utf-8')
    return "SharedAccessSignature sr={}&sig={}&se={}".format(uri, signature, expiry)

# Handle incoming MQTT messages
def handle_message(topic, msg):
    print("Message received:", msg)
    if msg == b'TURN_ON':
        POWER_PIN.value(1)  # Turn ON
        print("Power ON")
    elif msg == b'TURN_OFF':
        POWER_PIN.value(0)  # Turn OFF
        print("Power OFF")

# Main logic
def main():
    connect_to_wifi()
    sas_token = generate_sas_token()
    client = MQTTClient(DEVICE_ID, BROKER, user="{}@sas.root.{}".format(DEVICE_ID, IOT_HUB_HOSTNAME), password=sas_token)
    client.set_callback(handle_message)
    client.connect()
    client.subscribe(TOPIC)
    print("Connected to Azure IoT Hub and subscribed to topic:", TOPIC)

    while True:
        client.check_msg()  # Non-blocking, listens for incoming messages
        time.sleep(1)

# Run the program
main()
