import board
import digitalio
import displayio
from fourwire import FourWire
from adafruit_st7789 import ST7789
import time

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
up = digitalio.DigitalInOut(board.IO1)
up.direction = digitalio.Direction.INPUT
up.pull = digitalio.Pull.UP

down = digitalio.DigitalInOut(board.IO2)
down.direction = digitalio.Direction.INPUT
down.pull = digitalio.Pull.UP

trigger = digitalio.DigitalInOut(board.IO3)
trigger.direction = digitalio.Direction.INPUT
trigger.pull = digitalio.Pull.UP

piezo = digitalio.DigitalInOut(board.IO22)
piezo.direction = digitalio.Direction.OUTPUT
#End IO setup

# Setup display
displayio.release_displays()
spi = board.SPI()
while not spi.try_lock():
    pass
spi.configure(baudrate=24000000)
spi.unlock()

display_bus = FourWire(spi, command=board.D6, chip_select=board.D7, reset=board.D5)
display = ST7789(display_bus, width=240, height=320, rotation=90)

splash = displayio.Group()
display.root_group = splash
#end display setup

color_bitmap = displayio.Bitmap(240, 320, 1)
palette = displayio.Palette(3)
palette[0] = 0x000000  # Black
palette[1] = 0xFFFFFF  # White
palette[2] = 0xFF0000  # Red

num_disp = displayio.TileGrid(color_bitmap, pixel_shader=palette, x=0, y=0)
splash.append(num_disp)

timer_label = label.Label(terminalio.FONT, text=str(sec), color=0xFFFFFF, x=100, y=160)
splash.append(timer_label)

counting_down = False

while True:
    #If the up button is pressed, increase the timer by 0.5 seconds. Save sec to file. Update the display.
    if not up.value:
        sec += 0.5
        timer_label.text = str(sec)
        save_sec(sec)
        time.sleep(0.2)

    #If the down button is pressed, decrease the timer by 0.5 seconds. Save sec to file. Update the display.
    if not down.value:
        sec -= 0.5
        save_sec(sec)
        if sec < 1: #can't be less than 1 second timer
            sec = 1
        timer_label.text = str(sec)
        time.sleep(0.2)

    #If the heat press is closed, start the timer and display the countdown.
    if not trigger.value and not closed:
        start = time.monotonic()
        end = start + sec
        while time.monotonic() < end and not trigger.value:
            remaining = max(0, end - time.monotonic())
            timer_label.text = "{:.1f}".format(remaining)
            time.sleep(0.05)
        timer_label.text = "0.00"
        while not trigger.value and timer_label.text == "0.00":
            piezo.value = True
            time.sleep(0.5)
            piezo.value = False

    #If the heat press is closed, prevent the timer from starting again until it is opened.
    while not trigger.value:
        time.sleep(0.001)
    closed = True

    while trigger.value:
        # If the heat press is opened, reset the timer and display.
        timer_label.text = str(sec)
        closed = False
        time.sleep(0.001)