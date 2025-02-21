import cv2

def decrypt_image():
    try:
        encrypted_img = cv2.imread("encryptedImage.png") 
        
        if encrypted_img is None:
            print("Error: Could not read the encrypted image.")
            return

        input_password = input("Enter passcode for Decryption: ")

        try:
            with open("encryption_info.txt", "r") as f:
                stored_password = f.readline().strip()
                msg_length = int(f.readline().strip())
        except FileNotFoundError:
            print("Error: Encryption info file not found.")
            return

        # Verify password
        if input_password != stored_password:
            print("YOU ARE NOT AUTHORIZED!")
            return

        c = {}
        for i in range(255):
            c[i] = chr(i)

        decrypted_msg = ""
        n = 0
        m = 0
        z = 0

        for i in range(msg_length):
            pixel_value = int(encrypted_img[n, m, z])
            decrypted_msg += c[pixel_value]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3

        print("Decrypted message:", decrypted_msg)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    decrypt_image()