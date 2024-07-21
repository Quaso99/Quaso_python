from sense_emu import SenseHat
from influxdb import InfluxDBClient
import time

# InfluxDB Verbindungsdetails
host = 'localhost'
port = 8086
user = 'xxxxx'
password = 'xxxx'
dbname = 'xxxxxxx'

# Sense HAT initialisieren
sense = SenseHat()
client = InfluxDBClient(host, port, user, password, dbname)

def write_to_influx():
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    data = [
        {
            "measurement": "sensehat",
            "tags": {
                "host": "raspberrypi"
            },
            "fields": {
                "temperature": temperature,
                "humidity": humidity,
                "pressure": pressure
            }
        }
    ]

    client.write_points(data)

try:
    while True:
        write_to_influx()
        time.sleep(60)
except KeyboardInterrupt:
    print("Programm beendet")
