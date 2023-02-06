# esp32_training

## 0.00.002 - 06/02/2023
### UPDATED
- firmware\lvgl-upython.bin
  - needs to be flashed to esp using:
    - `esptool.py -p COMX write_flash -fm dio -fs 4MB -ff 40m 0x0 .\lvgl-upython.bin`
      - `COMX` needs to reflect the proper COM port
      - `python -m pip install -U esptool`
	  
### ADDED
- software\mpyblockly
	  
### MOVED
- `ide\thonny-4` to `software\thonny-4`
- `examples\main.py` to `examples\main_orig.py`
  - contains original code of ckboa kku smart farm

## 0.00.001 - 04/02/2023
### ADDED

- CHANGELOG.md
- documents\esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf
- documents\การใช้งานหน้าจอทัชสกรีน.docx
- examples\main.py
- firmware\lvgl-upython.bin
  - MicroPython 1.19.1 + lvgl v8..
- ide\thonny-4.0.2.exe
- libraries\xpt2046.py
- wiring_diagram\ESP-WROOM-32 [ESP-32S] Module.fzpz
- wiring_diagram\pinout.xlsx
