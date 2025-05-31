# heatpress-timer
The repo for my heat press timer. I created this to solve a problem with my heat press. A heat press basically has a hot metal plate that moves up and down, used to transfer vinyl, DTF transfers, and other 'transfers' to a t-shirt or other garment. The problem is that the timer must be manually stopped and started, making the process inefficient. This project seeks to automate the timer starting and stopping process by detecting when the metal plate is lowered. <br>
It all revolves around this limit switch:<br>
![image](https://github.com/user-attachments/assets/cac63d9a-48a2-4de3-bed0-ec543ec16629)<br><br>
When this limit switch closes, it triggers the timer:<br>
![image](https://github.com/user-attachments/assets/cf751a43-2cc2-424e-9d4f-442f466fb078)<br>
The piezo is used to alert the user when the timer runs out of time. The plus and minus buttons allow the user to change the ammount of time the timer counts down from.
There's three main parts:
### The CAD
The case! Two parts, the top and the bottom. The /CAD folder has both parts as a STL, and everything as a STEP file.

### The PCB
It connects all the electronics! It's meant to be bolted to the back of the screen. Both the KiCAD source files and the gerber files are in there.

### The Code
I designed the code to run on [CircuitPython](https://circuitpython.org/board/seeed_xiao_esp32c6/). Still a work in progress, but essentially it changes the time with the buttons (+ and -), it resets the timer when the limit switch is triggered, and beeps when the timer is at 0. The last known time is stored in the file time.txt so that it persists across reboots.
