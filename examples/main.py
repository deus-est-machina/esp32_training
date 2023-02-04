import lvgl as lv
import machine, dht
from machine import Pin
from time import sleep
import lodepng as png
from imagetools import get_png_info, open_png
# Import ILI9341 driver and initialized it

from ili9XXX import ili9341
disp = ili9341(spihost=1,mosi=23,miso=19,clk=18,cs=5,dc=21,rst=22, rot=0x20,width=320, height=240)
#disp = ili9341(spihost=1,mosi=23,miso=19,clk=18,cs=5,dc=21,rst=22, width=320, height=240)


from xpt2046 import xpt2046
touch = xpt2046(cs=33,mhz=1,transpose=False, cal_x0=3780, cal_y1=252, cal_x1=393, cal_y0=3751)

p4 = Pin(4, Pin.OUT)
relay12 = Pin(12, Pin.OUT)
relay13 = Pin(13, Pin.OUT)
relay14 = Pin(14, Pin.OUT)
relay15 = Pin(15, Pin.OUT)

##### main script #####

# Create a Tab view object
tabview = lv.tabview(lv.scr_act(), lv.DIR.LEFT, 80)

tabview.set_style_bg_color(lv.palette_lighten(lv.PALETTE.BLUE_GREY, 2), 0)

tab_btns = tabview.get_tab_btns()
tab_btns.set_style_bg_color(lv.palette_darken(lv.PALETTE.GREY, 3), 0)
tab_btns.set_style_text_color(lv.palette_lighten(lv.PALETTE.GREY, 5), 0)
tab_btns.set_style_border_side(lv.BORDER_SIDE.RIGHT, lv.PART.ITEMS | lv.STATE.CHECKED)


# Add 3 tabs (the tabs are page (lv_page) and can be scrolled
tab1 = tabview.add_tab("KKU SMART FARM")
tab2 = tabview.add_tab("RELAY CONTROL")
tab3 = tabview.add_tab("TEMP & HUMID")

tab1.set_style_bg_color(lv.palette_lighten(lv.PALETTE.DEEP_ORANGE, 3), 0)
tab1.set_style_bg_opa(lv.OPA.COVER, 0)

tab2.set_style_bg_color(lv.palette_lighten(lv.PALETTE.AMBER, 3), 0)
tab2.set_style_bg_opa(lv.OPA.COVER, 0)

tab3.set_style_bg_color(lv.palette_lighten(lv.PALETTE.BLUE, 3), 0)
tab3.set_style_bg_opa(lv.OPA.COVER, 0)

# Add content to the tabs
# Create label in the tab ad tab1
label = lv.label(tab1)
label.set_text("KKU SMART FARM")


# Add image in the label of tab
decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png
with open('kku9.png' ,'rb') as f:
      png_data = f.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data})

scr = lv.scr_act()
img1 = lv.img(tab1)
img1.center()
#img1.align(scr, lv.ALIGN.IN_TOP_LEFT, 0, 0)
img1.set_src(png_img_dsc)



# Create label in the tab ad tab2
label = lv.label(tab2)
label.set_text("RELAY CONTROL")
label.align(lv.ALIGN.CENTER, 0, 0)


# Create label in the tab ad tab2
def event_handlerR1(e):
    r1code = e.get_code()
    r1obj = e.get_target()
    if r1code == lv.EVENT.VALUE_CHANGED:
        if r1obj.has_state(lv.STATE.CHECKED):
            relay12.value(1)
        else:
            relay12.value(0)
def event_handlerR2(e):
    r2code = e.get_code()
    r2obj = e.get_target()
    if r2code == lv.EVENT.VALUE_CHANGED:
        if r2obj.has_state(lv.STATE.CHECKED):
            relay13.value(1)
        else:
            relay13.value(0)
def event_handlerR3(e):
    r3code = e.get_code()
    r3obj = e.get_target()
    if r3code == lv.EVENT.VALUE_CHANGED:
        if r3obj.has_state(lv.STATE.CHECKED):
            relay14.value(1)
        else:
            relay14.value(0)
def event_handlerR4(e):
    r4code = e.get_code()
    r4obj = e.get_target()
    if r4code == lv.EVENT.VALUE_CHANGED:
        if r4obj.has_state(lv.STATE.CHECKED):
            relay15.value(1)
        else:
            relay15.value(0)

tab2.set_flex_flow(lv.FLEX_FLOW.COLUMN_WRAP)
tab2.set_flex_align(lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)


main_label = lv.label(tab2)
main_label.set_text("RELAY 1")
sw = lv.switch(tab2)
sw.add_event_cb(event_handlerR1 ,lv.EVENT.ALL, None)


main_label = lv.label(tab2)
main_label.set_text("RELAY 2")
sw = lv.switch(tab2)
sw.add_event_cb(event_handlerR2 ,lv.EVENT.ALL, None)
# 
label3 = lv.label(tab2)
label3.set_text("")
# 
# 
main_label = lv.label(tab2)
main_label.set_text("RELAY 3")
sw = lv.switch(tab2)
sw.add_event_cb(event_handlerR3 ,lv.EVENT.ALL, None)
# 
main_label = lv.label(tab2)
main_label.set_text("RELAY 4")
sw = lv.switch(tab2)
sw.add_event_cb(event_handlerR4 ,lv.EVENT.ALL, None)


label = lv.label(tab3)
label.set_text("TEMPERATURE & HUMIDNITY")


def set_value(indic,v):
    meter.set_indicator_end_value(indic, v)   

    
#
# A meter with multiple arcs
#

meter = lv.meter(tab3)
meter.align(lv.ALIGN.CENTER, 0, 20)
meter.set_size(190, 190)

# Remove the circle from the middle
meter.remove_style(None, lv.PART.INDICATOR)

# Add a scale first
scale = meter.add_scale()
meter.set_scale_ticks(scale, 11, 2, 10, lv.palette_main(lv.PALETTE.GREY))
meter.set_scale_major_ticks(scale, 1, 2, 25, lv.color_hex3(0xeee), 10)
meter.set_scale_range(scale, 0, 100, 270, 90)

# Add a three arc indicator
indic1 = meter.add_arc(scale, 10, lv.palette_main(lv.PALETTE.BLUE), 0)
indic2 = meter.add_arc(scale, 10, lv.palette_main(lv.PALETTE.LIME), -10)

# Create an animation to set the value
a1 = lv.anim_t()
a1.init()
a1.set_values(0, 1)
a1.set_time(2000)
#a1.set_repeat_delay(100)
#a1.set_playback_delay(100)
#a1.set_playback_time(500)
a1.set_var(indic1)
#a1.set_repeat_count(lv.ANIM_REPEAT.INFINITE)
a1.set_custom_exec_cb(lambda a,val: set_value(indic1,val))
#lv.anim_t.start(a1)

a2 = lv.anim_t()
a2.init()
a2.set_values(0, 1)
a2.set_time(1000)
#a2.set_repeat_delay(100)
#a2.set_playback_delay(100)
#a2.set_playback_time(1000)
a2.set_var(indic2)
#a2.set_repeat_count(lv.ANIM_REPEAT.INFINITE)
a2.set_custom_exec_cb(lambda a,val: set_value(indic2,val))
#lv.anim_t.start(a2)




while True:        
    sensor = dht.DHT22(Pin(25))
    sensor.measure()
    temp = sensor.temperature()
    humi = sensor.humidity()
    a1.set_values(int(temp), int(temp))
    a2.set_values(int(humi), int(humi))
    lv.anim_t.start(a1)
    lv.anim_t.start(a2)
    sleep(10)
