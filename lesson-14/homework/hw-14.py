################################# Task -1 ########################################
# import numpy as np
# def fahrenheit_to_celsius(f):
#     return (f - 32) * 5 / 9
# vectorized_conversion = np.vectorize(fahrenheit_to_celsius)
# fahrenheit_array = np.array([32, 68, 100, 212, 77])
# celsius_array = vectorized_conversion(fahrenheit_array)
# print("Fahrenheit:", fahrenheit_array)
# print("Celsius:", celsius_array)
################################# Task -2 ########################################
# import numpy as np
# def custom_power(base, exponent):
#     return base ** exponent
# vectorized_power = np.vectorize(custom_power)
# bases = np.array([2, 3, 4, 5])
# exponents = np.array([1, 2, 3, 4])
# result = vectorized_power(bases, exponents)
# print("Bases:    ", bases)
# print("Exponents:", exponents)
# print("Results:  ", result)
################################# Task -3 ########################################
# import numpy as np
# A = np.array([
#     [4, 5, 6],
#     [3, -1, 1],
#     [2, 1, -2]
# ])
# b = np.array([7, 4, 5])
# solution = np.linalg.solve(A, b)
# print("Solution [x, y, z]:", solution)
################################ Task -4 ########################################
import numpy as np
from PIL import Image
import os

# ==== QISM 1: Elektr tarmog'ining tenglamalarini yechish ====

def solve_currents():
    A = np.array([
        [10, -2,  3],
        [-2,  8, -1],
        [ 3, -1,  6]
    ])
    b = np.array([12, -5, 15])
    currents = np.linalg.solve(A, b)
    print(">> Tok kuchlari [I1, I2, I3]:", currents)
    return currents

# ==== QISM 2: Rasmni tahrirlash ====

def load_image(path):
    return np.array(Image.open(path))

def flip_image(img_array):
    flipped_h = np.flip(img_array, axis=1)  
    flipped_v = np.flip(flipped_h, axis=0) 
    return flipped_v

def add_noise(img_array, noise_level=30):
    noise = np.random.randint(-noise_level, noise_level + 1, img_array.shape, dtype='int16')
    noisy = img_array.astype('int16') + noise
    return np.clip(noisy, 0, 255).astype('uint8')

def brighten_channels(img_array, brighten_value=40):
    bright = img_array.astype('int16')
    bright[..., 0] += brighten_value 
    return np.clip(bright, 0, 255).astype('uint8')

def apply_mask(img_array, mask_size=100):
    h, w = img_array.shape[:2]
    start_y = (h - mask_size) // 2
    start_x = (w - mask_size) // 2
    img_array[start_y:start_y+mask_size, start_x:start_x+mask_size] = 0  
    return img_array

def save_image(img_array, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # papkani avtomatik yaratadi
    Image.fromarray(img_array).save(output_path)
    print(f">> Rasm saqlandi: {output_path}")


def process_image(image_path, output_path):
    img = load_image(image_path)  
    img = flip_image(img)  
    img = add_noise(img) 
    img = brighten_channels(img)  
    img = apply_mask(img)  
    save_image(img, output_path) 

# ==== ASOSIY FUNKSIYA ====

if __name__ == "__main__":

    solve_currents()
    
    image_path = r"C:\Python\homework\photo_2025-05-08_18-08-33.jpg"


    output_path = "images/birds_modified.png"  
    
    process_image(image_path, output_path)
