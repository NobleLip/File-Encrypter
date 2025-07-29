```
  ███████▓██▓   ▓█████    ▓█████ ███▄    █ ▄████▄  ██▀███▓██   ██▓██▓███ ▄▄▄█████▓█████ ██▀███  
▓██   ▓██▓██▒   ▓█   ▀    ▓█   ▀ ██ ▀█   █▒██▀ ▀█ ▓██ ▒ ██▒██  ██▓██░  ██▓  ██▒ ▓▓█   ▀▓██ ▒ ██▒
▒████ ▒██▒██░   ▒███      ▒███  ▓██  ▀█ ██▒▓█    ▄▓██ ░▄█ ▒▒██ ██▓██░ ██▓▒ ▓██░ ▒▒███  ▓██ ░▄█ ▒
░▓█▒  ░██▒██░   ▒▓█  ▄    ▒▓█  ▄▓██▒  ▐▌██▒▓▓▄ ▄██▒██▀▀█▄  ░ ▐██▓▒██▄█▓▒ ░ ▓██▓ ░▒▓█  ▄▒██▀▀█▄  
░▒█░  ░██░██████░▒████▒   ░▒████▒██░   ▓██▒ ▓███▀ ░██▓ ▒██▒░ ██▒▓▒██▒ ░  ░ ▒██▒ ░░▒████░██▓ ▒██▒
 ▒ ░  ░▓ ░ ▒░▓  ░░ ▒░ ░   ░░ ▒░ ░ ▒░   ▒ ▒░ ░▒ ▒  ░ ▒▓ ░▒▓░ ██▒▒▒▒▓▒░ ░  ░ ▒ ░░  ░░ ▒░ ░ ▒▓ ░▒▓░
 ░     ▒ ░ ░ ▒  ░░ ░  ░    ░ ░  ░ ░░   ░ ▒░ ░  ▒    ░▒ ░ ▒▓██ ░▒░░▒ ░        ░    ░ ░  ░ ░▒ ░ ▒░
 ░ ░   ▒ ░ ░ ░     ░         ░     ░   ░ ░░         ░░   ░▒ ▒ ░░ ░░        ░        ░    ░░   ░ 
       ░     ░  ░  ░  ░      ░  ░        ░░ ░        ░    ░ ░                       ░  ░  ░     
                                          ░               ░ ░                                   
```

# 🔐 File Encrypter/Decrypter

A simple Python script to **encrypt and decrypt files** using the Fernet symmetric encryption from the `cryptography` library. Perfect for keeping your files safe and learning about encryption!


## 🚀 Features

- **Encrypt any file** with a Fernet key
- **Decrypt files** (with the same key)
- **Multiple encryption rounds** for extra security (or fun!)
- **Easy-to-use interactive CLI**
- **Example files included** for practice


## ⚠️ Warning

> **Never lose your Fernet key!**  
> You must use the exact same key to decrypt files you have encrypted.  
> The script lets you generate and copy a Fernet key before encrypting.


## 🗝️ Getting Started

### 1. Clone or Download

```sh
git clone https://github.com/yourusername/File-Encrypter.git
cd File-Encrypter
```

### 2. Install Requirements

```sh
pip install cryptography
```

### 3. Run the Script

```sh
python Encri.py
```

## 📝 Usage

1. **Generate a Fernet Key** (if you don't have one)
2. **Choose to Encrypt or Decrypt**
3. **Enter the file name and number of rounds**
4. **Done!**

### Example Session

- **Generate a Fernet Key:**  
  ![Fernet](Img/fernet.PNG)

- **Before Encryption:**  
  ![Before](Img/Before.PNG)

- **After Encryption:**  
  ![After](Img/After.PNG)


## 🤖 Author

Made by NobleLip



