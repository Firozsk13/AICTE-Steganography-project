import cv2
import os

def encrypt_image():
    try:
        
        img_path = "myimg.jpeg"
        img = cv2.imread(img_path)
        
        if img is None:
            print("Error: Could not read the image.")
            return

        msg = input("Enter secret message: ")
        password = input("Enter a passcode: ")

        d = {}
        for i in range(255):
            d[chr(i)] = i

        n = 0
        m = 0
        z = 0

        for i in range(len(msg)):
            img[n, m, z] = d[msg[i]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3

        cv2.imwrite("encryptedImage.png", img)  # Changed to PNG format due to some error
        
        with open("encryption_info.txt", "w") as f:
            f.write(f"{password}\n{len(msg)}")

        print("Encryption successful!")
        print("Encrypted image saved as 'encryptedImage.png'")
        
        os.system("start encryptedImage.png")  


    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    encrypt_image()