# A hub for my Nintendo Switch related projects

I'm going to put all my resources and discoveries related to Nintendo Switch here, which will probably be updated frequently in the coming days after the launch.

## NintenDAC dev board for Nintendo Switch modification

NintenDAC is a STM32 development board with up to 10 high-speed 12-bit DAC channels. I intend to use it for automating Joycon inputs, and maybe it would be suitable for TAS as well. 

The board has 2 versions. The bigger NintenDAC has more GPIOs and a dedicated high-speed DAC chip, so it's suitable for modifying the pro controller or the console itself:

![Alt text](http://i.imgur.com/ir8jZFO.jpg)

* 48MHz STM32F072R8T6 microcontroller, 64KB flash, 16KB RAM.
* MAX5723/MAX5724/MAX5725 8-channel high-speed SPI DAC + 2-channel built-in DAC.
* 1KB I2C EEPROM, user button, user LED.
* 36 GPIOs(or 40 using internal oscillators), BOOT0, RESET, VBAT, and SWD.
* USB for power and communication, standby wakeup on USB connection.
* Board size 4.1 x 4.1 cm, or 1.65 x 1.65 inch.

While the smaller NintenDAC mini is intended to be used on a Joycon:

![Alt text](http://i.imgur.com/f3qcFR7.jpg)

* 48MHz STM32F072C8T6 microcontroller, 64KB flash, 16KB RAM.
* Built-in 2-channel 12-bit DAC.
* 1KB I2C EEPROM, user button, user LED.
* 28 GPIOs(or 32 using internal oscillators), BOOT0, RESET, VBAT, and SWD.
* USB for power and communication, standby wakeup on USB connection.
* Board size 2.5 x 4.1 cm, or 1 x 1.6 inch.

Both present themselves to PC as a USB serial port, so no special drivers are needed. Simply connect the button and joystick test points to the headers to allow the joycon be controlled from a PC. Details and tutorials to come after I got my Switch.

## Communication protocol and Python library

For NintenDAC: under construction...

For NintenDAC mini: [click here](./NintenDAC_mini)

## Twitch Plays Nintendo Switch

I dug up and reused a portion of my old code for TwitchPlaysPokemonX, [see here](./TwitchPlaysNintendoSwitch).

