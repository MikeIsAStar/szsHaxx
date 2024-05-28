<p align="center">
    <img alt="szsHaxx banner" src="./data/save/banner/img/banner.png" />
</p>

# szsHaxx

Injects arbitrary code into Mario Kart Wii.

# Explanation

In Mario Kart Wii, competition data is stored within the game's save data. The course data for competitions is compressed using a proprietary compression format (`Yaz`) that was developed by Nintendo. The decompression function can be exploited via meticulously crafted compressed data, resulting in an overflow of the output buffer. In this instance, the buffer overflow leads to an arbitrary write, which grants the ability to write a single word to any memory address. By writing a branch instruction to the game's exception handler, code execution can be diverted in the event of a game crash. Following the arbitrary write, a Data Storage Interrupt (`DSI`) exception is triggered, resulting in code execution being redirected to the payload.

# Usage

1. Obtain an SD card that has a capacity of 2 gigabytes or less
2. Format the SD card to FAT16 or FAT32
3. Create the filepath `sd:/private/wii/title/RMC[E|P|J|K]` on the SD card. The final character should match the version of Mario Kart Wii that will be used
4. Transfer the `data.bin` file that corresponds to the version of Mario Kart Wii that will be used into the aforementioned folder
5. Place the `boot.elf` file to be executed on the root of the SD card (`sd:/`)
6. Enable WiiConnect24
7. Delete the save data for the version of Mario Kart Wii that will be used
8. Transfer the save data from the SD card to the Wii
9. Launch Mario Kart Wii
10. Start the competition

# Credits

## Code

- Many thanks to Team Twiizers for creating `Savezelda`
- Many thanks segher for creating `twintig`

## Images

- Many thanks to jay for creating the banner
- Many thanks to chillz for creating the icons

## Translations

Many thanks to the individuals listed below for their help with translations.

### Italian

- LNLenost

### Japanese

- custard
- varemi

### Korean

- juno

# Media

[![szsHaxx (NEW Wii Exploit) Tested on Real Hardware!](https://i.ytimg.com/vi/vJXF7F2b2S4/hqdefault.jpg)](https://www.youtube.com/watch?v=vJXF7F2b2S4)
[![szsHaxx Demonstration](https://i.ytimg.com/vi/YkNf34A5zk4/hqdefault.jpg)](https://www.youtube.com/watch?v=YkNf34A5zk4)
