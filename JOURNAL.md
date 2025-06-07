---
title: "Heat Press Timer"
author: "@luteron6"
description: "An automatic timer for a heat press. No more phone stopwatches!"
created_at: "2025-05-19"
---

# Heat Press Timer
Made by: @luteron6

Total hours so far: 24

Estimated Cost: $89.44 (including tax, shipping, and fees)

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

## Day 4 - 5/22/2025 - 5:26 PM (2 hours)
Today I refined my PCB. I think it's almost done:<br>
![image](https://github.com/user-attachments/assets/131b3771-1e11-4726-b0ad-1615dd544e08)<br>
I added holes, filleted the corners, and made the buzzer pads wider. I intend to solder the buzzer directly to the PCB, and I don't know how wide the terminals are. I also routed the PCB. I don't know what size the standoffs/screws are on the display, so I'll have to see when I get it. Next I'll have to work on the case, then the code.

## Day 5 - 5/23/2025 - 9:32 PM (4 hours)
I decided to add my name, date, and title to the PCB. The I exported it as a STEP file for doing CAD later. I also found the STEP file for the display, so I could put them together in Onshape. Then I worked in Onshape for the rest of my time, making the case. The longest part was probably figuring out what I wanted to make the tolerances, and also the heat press inserts and screws. I'm also really new to CAD and Onshape, most of the time I was looking up tutorials and how-to guides. Anyway, I decided I will try and use M2 hardware (hopefully it's M2), but I'll buy the screen first to see what size the standoffs are. Below is my screen and PCB:<br>
![image](https://github.com/user-attachments/assets/ec5b5d21-2e94-4f5d-9dbc-c39e19df613e)<br>
Here's the hardware in my case:<br>
![image](https://github.com/user-attachments/assets/e05f6ad6-a91b-4e2d-86a2-72f3ccc4f0b3)<br>

## Day 6 - 5/25/2025 - 8:20 PM (2 hours)
Phew! Yesterday was crazy and I couldn't find time to work on this. But I thought about it last night, and itoccurred to me that the RP2040 doesn't have wifi. So it won't have the interactive CircuitPython web interface. So I switched to the [XIAO ESP32 C6](https://www.seeedstudio.com/Seeed-Studio-XIAO-ESP32C6-p-5884.html). Here's the actual [Aliexpress link](https://www.aliexpress.us/item/3256807240718259.html) ($9.84). I also rerouted my PCB.<br>
I also forgot to add a hole for the USB-C port on the XIAO. I also filleted the edges of the case and the USB-C port. Here's what I came up with:<br>
![image](https://github.com/user-attachments/assets/02460e06-6ae9-4ded-b915-c488f37f3452)<br>
Now for the code. It took me a while to find drivers (CircuitPython libraries) for the display. The hardest part is not being able to run the code - once I get the parts it'll be so much easier.

## Day 7 - 5/30/2025 - 10:27 PM (4 hours)
OK! I think it's done. I finished my code, created my BOM.csv, exported the gerbers, the case STEP file and STLs, and added everything to this repo. I also updated the readme.

## Day 8 - 6/7/2025 - 11:23 AM (3 hours)
I updated my README with a BOM, added my PCB to the BOM (I forgot earlier), and edited my case to add some flair. Here's pictures of my new case:
<br><br><img src="https://github.com/user-attachments/assets/dff80192-1d91-4fd8-a98f-41bee4fac884" height=250>
<img src="https://github.com/user-attachments/assets/ed8abd47-b5bc-434f-ad20-50d305c1c8c0" height=250>
<img src="https://github.com/user-attachments/assets/d4eebb42-06b4-4b47-96ac-228bfb1b74f5" height=250>
<img src="https://github.com/user-attachments/assets/0b99a52b-97c0-40d4-b6e9-54ceb0884bcc" height=250><br>

