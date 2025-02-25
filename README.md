# Image Steganography - Hide and Retrieve Secret Messages in Images

## 📌 Project Overview

This project implements a simple image-based steganography system that hides a secret message inside an image and retrieves it later using OpenCV.

## 🔥Features

✅ Encrypt a message by embedding it in an image

✅ Decrypt the message from the encrypted image

✅ Password protection for decryption

✅ Works with .jpg and .png images

## 📥Installation

Make sure you have Python installed. Then, install the required package:

`pip install opencv-python`

## 🚀Usage

### 🔒 Encryption - Hiding the Message

1.Place your image (image.jpg) in the same directory as the script.

2.Run encrypt.py and enter the secret message:

`python encrypt.py`

3.The script will generate encryptedImage.jpg with the hidden message.

4.The encrypted image will open automatically.

### 🔓 Decryption - Retrieving the Message

1.Run decrypt.py and provide the correct passcode:

`python decrypt.py`

2.If the passcode is correct, the hidden message will be revealed.

## File Structure

`📂 steganography-project

     │── encrypt.py      # Script to hide a message in an image

     │── decrypt.py      # Script to retrieve the hidden message

     │── image.jpg       # Original image (before encryption)

     │── encryptedImage.jpg # Encrypted image (after embedding message)

     │── README.md       # Project documentation`

## Example Output

### Encryption

`Enter secret message: Hello
Encryption complete! Image saved as encryptedImage.jpg`

### Decryption

`Enter the length of the secret message: 5
Enter passcode for decryption: mypassword
Decrypted message: Hello`

If the wrong passcode is entered:

`YOU ARE NOT AUTHORIZED`

## Troubleshooting

Image not found error? Ensure the image file exists and use the correct path.

Unicode error in file path? Use double backslashes `C:\\path\\to\\image.jpg` or a raw string `r"C:\path\to\image.jpg"`.

Image doesn’t open? Manually open `encryptedImage.jpg` from the directory.


