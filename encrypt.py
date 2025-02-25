import cv2
import os

def encrypt_message(image_path, output_path, message):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    d = {chr(i): i for i in range(255)}

    n, m, z = 0, 0, 0
    for char in message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite(output_path, img)
    print(f"Encryption complete! Image saved as {output_path}")
    os.system(f"start {output_path}")  # Open the image on Windows

if __name__ == "__main__":
    image_path = "C:/Users/sumab/OneDrive/Pictures/Saved Pictures/image.jpg" # Replace with the correct path
    output_path = "encryptedImage.jpg"
    msg = input("Enter secret message: ")
    encrypt_message(image_path, output_path, msg)
