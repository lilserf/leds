from neopixel import Neopixel
import utime

num_pixels = 10
num_bands = 10

strip = Neopixel(num_pixels, 0, 0, "RGB")

pixels_per = num_pixels / num_bands
hue_per = 65535 / num_bands

strip.clear()
strip.show()

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 180, 0)
green = (0, 255, 0)
teal = (0, 128, 128)
blue = (0, 0, 255)
violet = (120, 0, 255)
colors_rgb = (red, orange, yellow, green, teal, blue, violet)

def basic_cycle():
    while True:
        for color in colors_rgb:
            strip.fill(color)
            utime.sleep(2)
            strip.show()

def hue_rotate():
    hue = 0
    
    while True:
        color = strip.colorHSV(hue, 255, 255)
        strip.fill(color)
        hue += 100
        utime.sleep(0.05)
        strip.show()

def divide_spectrum():
    num_steps = 10
    hue_step = 65535 / num_steps
    led_step = int(num_pixels / num_steps)
    
    colors = [strip.colorHSV(int(i * hue_step), 255, 200) for i in range(num_steps)]
    
    curr = 0
    for color1, color2 in zip(colors, colors[1:]):
        strip.set_pixel_line_gradient(curr, curr+led_step, color1, color2)
        curr += led_step

    strip.show()

def basic_chase():
    for i in range(num_pixels):
        color = colors_rgb[i % len(colors_rgb)]
        strip.set_pixel(i, color)
    
    strip.show()
    while True:
        strip.rotate_left(1)
        utime.sleep(0.5)
        strip.show()

#basic_cycle()
#hue_rotate()
#divide_spectrum()
        
basic_chase()
    
