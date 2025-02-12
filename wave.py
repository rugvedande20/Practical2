import time
import os
import noise
import numpy as np
import colorsys

def generate_wave(width=80, height=20, scale=0.1, speed=0.1):
    t = 0  # Time variable for animation
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # Clear screen
        for y in range(height):
            line = ""
            for x in range(width):
                value = noise.pnoise2(x * scale, y * scale + t, octaves=4)  # Perlin noise
                char = " .:-=+*#%@"[int((value + 1) / 2 * 9)]  # Map noise to characters
                colored_char = f"\033[38;5;{int((value + 1) / 2 * 255)}m{char}\033[0m"  # Add color
                line += colored_char
            print(line)
        t += speed
        time.sleep(0.1)  # Adjust speed of animation

if __name__ == "__main__":
    generate_wave()
