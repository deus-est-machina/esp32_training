# Flashing firmware

Download [esptool](https://github.com/espressif/esptool)

Replace `COM7` with the correct COM port that the `esp` is connected to.

`esptool.py -t -p COM7 write_flash -fm dio -fs 4MB -ff 40m 0x0 .\lvgl_upython.bin`
