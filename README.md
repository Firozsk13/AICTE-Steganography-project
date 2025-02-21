# AICTE-Steganography-project

## Overview
This project implements **Image Steganography** using Python and OpenCV. It allows users to **hide a secret message** inside an image and retrieve it later using a password. This technique helps in secure communication without raising suspicion.

## Features
- **Text Embedding:** Hide a secret message inside an image by modifying pixel values.
- **Password Protection:** Messages can only be decrypted with the correct passcode.
- **Invisible to the Naked Eye:** The image looks unchanged after encoding.
- **Automated Encoding & Decoding:** Simple command-line interface for ease of use.

## Technologies Used
- **Python**
- **OpenCV (cv2)** - For image processing
- **OS Module** - For file handling

## Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/steganography-project.git
   cd steganography-project
   ```
2. **Install Dependencies**
   ```sh
   pip install opencv-python
   ```
3. **Run the Program**
   ```sh
   python encrypt.py
   python decrypt.py
   ```

## Usage
1. **Encoding a Message:**
   - Run the script and enter the secret message.
   - Provide a passcode for security.
   - The script generates an encrypted image (`encryptedImage.jpg`).

2. **Decoding a Message:**
   - Run the script again and enter the correct passcode.
   - If the passcode is correct, the hidden message will be displayed.

## Example
```
Enter secret message: Hello World!
Enter a passcode: 1234
[Encrypted image is saved]

Enter passcode for Decryption: 1234
Decryption message: Hello World!
```


🔗 **GitHub Repository:** (https://github.com/Firozsk13/AICTE-Steganography-project)

