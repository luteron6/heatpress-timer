---
title: "Heat Press Timer"
author: "@luteron6"
description: "An automatic timer for a heat press. No more phone stopwatches!"
created_at: "2025-05-20"
---

# Heat Press Timer
Made by: @luteron6
Total hours so far: 5

I have a heat press that I use to transfer DTF transfers. It's basically two pieces of metal that clamp down together. The top half heats up really hot to activate the transfer's adhesive backing. The only problem is that the DTF transfer needs a specific time in the heat press, and we haven't had a good solution to tracking that time. This project is an attempt to solve that problem.

## Day 1 - 5/19/2025 - 9:22 PM (2 hours)
Before I get started, I want to outline my goals:
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

## Day 2 - 5/20/2025 - 11:28 AM (3 hours)
Today I made a [PR](https://github.com/hackclub/highway/pull/58) to add my project to the submissions.yml file in the hackclub/highway repo.
I also tried to figure out how to connect the SPI display to the RP2040. This is my first time using the SPI protocol, and there's a lot more wires than the I2C protocol. Here's what I came up with:
![image](https://github.com/user-attachments/assets/2ae45ea8-3d49-4e6d-8690-1fb5ca3949ab).
I also started to layout the schematic in KiCad. I haven't used KiCad in a while, so I had to figure everything out with the footprints and stuff. Here's what I have so far:
![image](https://github.com/user-attachments/assets/ccf1a4c1-99e8-469f-b21d-9d446d653918)
