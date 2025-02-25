import cv2

def decrypt_message(image_path, message_length, password, correct_password):
    if password != correct_password:
        print("YOU ARE NOT AUTHORIZED")
        return
    
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    c = {i: chr(i) for i in range(255)}
    
    n, m, z = 0, 0, 0
    decrypted_message = ""

    for _ in range(message_length):
        decrypted_message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    image_path = "encryptedImage.jpg"
    message_length = int(input("Enter the length of the secret message: "))
    password = input("Enter passcode for decryption: ")
    
    correct_password = "Edunet"  # Set the correct password
    decrypt_message(image_path, message_length, password, correct_password)
