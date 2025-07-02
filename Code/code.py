import board
import digitalio
import displayio
from fourwire import FourWire
from adafruit_st7789 import ST7789
import time
from adafruit_display_text import label
import pwmio
import terminalio
import wifi
from adafruit_bitmap_font import bitmap_font

# Load font
font = bitmap_font.load_font("/fonts/LeagueSpartan-Bold-16.bdf")

# Import last saved timer value from time.txt
def load_sec():
    try:
        with open("/settings.txt", "r") as f:
            return float(f.read())
    except Exception:
        return 8  # default value if file not found or invalid

def save_sec(value):
    with open("/settings.txt", "w") as f:
        f.write(str(value))

sec = load_sec()

#Setup the piezo, trigger, +, and - buttons
# Timer UP button
up = digitalio.DigitalInOut(board.A1)
up.direction = digitalio.Direction.INPUT
up.pull = digitalio.Pull.UP

# Timer DOWN button
down = digitalio.DigitalInOut(board.A2)
down.direction = digitalio.Direction.INPUT
down.pull = digitalio.Pull.UP

#Trigger
trigger = digitalio.DigitalInOut(board.D3)
trigger.direction = digitalio.Direction.INPUT
trigger.pull = digitalio.Pull.UP

#Buzzer (passive)
buzzer_pin = board.D4
buzzer = pwmio.PWMOut(buzzer_pin, duty_cycle=0, frequency=1000)  # 1kHz frequency

# Setup display
displayio.release_displays()
spi = board.SPI()
while not spi.try_lock():
    pass
spi.configure(baudrate=24000000)
spi.unlock()

display_bus = FourWire(spi, command=board.D6, chip_select=board.D7, reset=board.D5)
display = ST7789(display_bus, width=320, height=240, rotation=90,)

splash = displayio.Group()
display.root_group = splash


color_bitmap = displayio.Bitmap(320, 240, 1)
palette = displayio.Palette(3)
palette[0] = 0x000000  # Black
palette[1] = 0xFFFFFF  # White
palette[2] = 0xFF0000  # Red

num_disp = displayio.TileGrid(color_bitmap, pixel_shader=palette, x=0, y=0)
splash.append(num_disp)

timer_label = label.Label(font, text=str(sec), color=0xFFFFFF, x=135, y=120, scale=1)
splash.append(timer_label)
#end display setup

ip_address = wifi.radio.ipv4_address
#Display IP and password on screen
ip_label = label.Label(terminalio.FONT, text="IP: " + str(ip_address) + "  PW:password", color=0xFFFFFF, x=5, y=10)
splash.append(ip_label)

hc = label.Label(terminalio.FONT, text="made with love by a hack clubber", color=0xFFFFFF, x=130, y=232)
splash.append(hc)

#End IO setup
counting_down = False

while True:
    #If the up button is pressed, increase the timer by 0.5 seconds. Save sec to file. Update the display.
    if not up.value:
        sec += 0.5
        buzzer.duty_cycle = 2**15
        time.sleep(0.04)
        buzzer.duty_cycle = 0
        timer_label.text = "{:.2f}".format(sec)
        save_sec(sec)
        time.sleep(0.04)

    #If the down button is pressed, decrease the timer by 0.5 seconds. Save sec to file. Beep. Update the display.
    if not down.value:
        sec -= 0.5
        buzzer.duty_cycle = 2**15
        time.sleep(0.04)
        buzzer.duty_cycle = 0
        save_sec(sec)
        if sec < 1: #can't be less than 1 second timer
            sec = 1
        timer_label.text = "{:.2f}".format(sec)
        time.sleep(0.04)

    while trigger.value:
        # If the heat press is opened, reset the timer and display.
        timer_label.text = "{:.2f}".format(sec)
        closed = False
        time.sleep(0.05)
        break

        #If the heat press is closed, prevent the timer from starting again until it is opened.
    while not trigger.value:
        time.sleep(0.05)
        closed = True
        break
    
    #If the heat press is closed, start the timer and display the countdown.
    if not trigger.value and closed:
        start = time.monotonic()
        end = start + sec
        while time.monotonic() < end and not trigger.value:
            remaining = max(0, end - time.monotonic())
            timer_label.text = "{:04.2f}".format(remaining)
            time.sleep(0.05)
            if trigger.value:
                break
            if remaining <= 0.1:
                while True:
                    timer_label.text = "0.00"
                    palette[0] = 0xFF0000
                    buzzer.duty_cycle = 2**15
                    time.sleep(0.1)  # Buzzer on for half a second
                    palette[0] = 0x000000
                    # Turn off the buzzer
                    buzzer.duty_cycle = 0  # Turn off
                    time.sleep(0.1)  # Pause for half a second
                    if trigger.value:
                        break               
                break
