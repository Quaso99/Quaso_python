from sense_hat import SenseHat
import time

sense = SenseHat()


def display_temperature():
    while True:
      
        temperature = sense.get_temperature_from_pressure()
      
        temperature = round(temperature, 1)
         
        message = f"Temp: {temperature}C"
        
        sense.show_message(message, scroll_speed=0.1, text_colour=[255, 0, 0])
                
        time.sleep(2)

try:
    display_temperature()
except KeyboardInterrupt:

    sense.clear()
    print("Programm beendet")
