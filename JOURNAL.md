---
title: "Heat Press Timer"
author: "@luteron6"
description: "An automatic timer for a heat press. No more phone stopwatches!"
created_at: "2025-05-19"
---

# Heat Press Timer
Made by: @luteron6

Total hours so far: 5.5

Estimated Cost: $21.21

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

I also created this repo for my journal any other files. Furthermore, I tried to draw up a rough schematic for the timer:

![IMG_1361](https://github.com/user-attachments/assets/3e9e7e71-966d-4c20-bfd8-45f18f30369a)

## Day 2 - 5/20/2025 - 11:28 AM (3 hours)
Today I made a [PR](https://github.com/hackclub/highway/pull/58) to add my project to the submissions.yml file in the hackclub/highway repo.

I also tried to figure out how to connect the SPI display to the RP2040. This is my first time using the SPI protocol, and there's a lot more wires than the I2C protocol. Here's what I came up with:<br>
![image](https://github.com/user-attachments/assets/2ae45ea8-3d49-4e6d-8690-1fb5ca3949ab)<br>
I also started to layout the schematic in KiCad. I haven't used KiCad in a while, so I had to figure everything out with the footprints and stuff. Here's what I have so far:<br>
![image](https://github.com/user-attachments/assets/ccf1a4c1-99e8-469f-b21d-9d446d653918)<br>

## Day 2 (Session 2) - 5/20/2025 - 3:09 PM (30 minutes)
OK! I just saw the 'Sourcing parts' page on the Highway docs. I literally found all the same parts on Aliexpress for a lot cheaper. Hopefully it's not a scam. I also needed some solder. Here are the new parts:
* [XIAO RP2040](https://www.aliexpress.us/item/3256807240972277.html): $7.49
* [2" SPI LCD Display](https://www.aliexpress.us/item/3256808536058388.html): $8.21
* [Momentary Push Buttons (black)](https://www.aliexpress.us/item/3256804444014370.html): $2.00
* [Limit Switches (with handle)](https://www.aliexpress.us/item/3256805965729300.html): $1.34
* [Buzzer](https://www.aliexpress.us/item/3256802480381355.html): $2.17
* [Solder](https://pyrodrone.com/products/tbs-solder-spool-100g): $10.99
* New Total: $32.20<br>

## Day 3 - 5/21/2025 - 3:02 PM (3.5 hours)
Today I drew up what I think I want the case to look like:<br>
![thumbnail_IMG_1362](https://github.com/user-attachments/assets/004920bf-8ca2-43e1-9d23-5c76fc7cca23)

I also edited my schematic:<br>
![image](https://github.com/user-attachments/assets/70ed2b3e-688f-4fcc-a066-e17ae1155573)


The vertical switch will be outside the case, connected by a wire. The buttons (to change the length of the timer) are on the top, and so is the piezo buzzer.
I also designed a PCB to be mounted to the back of the screen (still needs a lot of work):<br>
![image](https://github.com/user-attachments/assets/12387b42-46d8-4c92-80f0-1bd4aad6bb94)
![image](https://github.com/user-attachments/assets/fbbf3db4-44bf-45d0-8282-09dd9364c08a)
![image](https://github.com/user-attachments/assets/cdd44746-a6df-4215-b856-0e70713a5d28)
