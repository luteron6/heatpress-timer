# Heat Press Timer
Made by: @luteron6
Total hours so far: 1

I have a heat press that I use to transfer DTF transfers. It's basically two pieces of metal that clamp down together. The top half heats up really hot to activate the transfer's adhesive backing. The only problem is that it needs a good timer so I can know when it's been pressed long enough. This project is an attempt to solve that problem.

## Day 1 - 5/19/2025 - 9:22 PM (2 hours)
Before I get started, I wanted to outline my goals:
* The timer will be automatically started by the close of the heat press.
* A display to counting down until the heat press should be lifted.
* A buzzer to alert me when it's done.
* Two buttons to change the length of the timer.

Today I drew up a schematic for my project. I've used a SeeedStudio XIAO RP2040 before, so I'm going to try to use that again. No idea if it will have enough pins.
I also researched some parts, mostly on Amazon. Here's what I've found:
* [RP 2040](https://www.amazon.com/Microcontroller-Dual-Core-MicroPython-CircuitPython-Interfaces/dp/B09NNVNW7M/): $9.99
* [2" LCD Screen](https://www.amazon.com/2inch-IPS-LCD-Display-Module/dp/B082GFTZQD/): $14.39
* [Vertical Limit Switch](https://www.amazon.com/HUAREW-Vertical-Mechanical-3018-PROVer-3018-MX3/dp/B0B38X86NY/): $11.99
* [Buzzer](https://www.amazon.com/Gikfun-Terminals-Passive-Electronic-Arduino/dp/B01GJLE5BS/): $7.28
* [Momentary Buttons](https://www.amazon.com/Gebildet-250VAC-Prewired-Momentary-Railway/dp/B083JWJPW5/): $7.99
* Total Estimated Costs: $51.64
I also created this repo for my journal any other files.
I also tried to draw up a rough schematic for the timer:
![IMG_1361](https://github.com/user-attachments/assets/3e9e7e71-966d-4c20-bfd8-45f18f30369a)
