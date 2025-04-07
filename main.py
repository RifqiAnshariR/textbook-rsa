from rsa import generate_keys, encrypt, decrypt

def encrypt_file(input_file, output_file, public_key):
    _, n = public_key
    chunk_size = (n.bit_length() + 7) // 8 - 1  # 255 bytes. -1 for M < n
    with open(input_file, "rb") as f:
        plaintext = f.read()
    
    ciphertext = b''
    for i in range(0, len(plaintext), chunk_size):
        chunk = plaintext[i:i+chunk_size]
        # if len(chunk) < chunk_size:
        #     chunk += b'\x00' * (chunk_size - len(chunk))    # padding
        chunk_int = int.from_bytes(chunk, byteorder='big')
        ciphertext_int = encrypt(chunk_int, public_key)
        ciphertext += ciphertext_int.to_bytes((n.bit_length() + 7) // 8, byteorder='big')

    with open(output_file, "wb") as f:
        f.write(ciphertext)

def decrypt_file(input_file, output_file, private_key):
    _, n = private_key
    chunk_size = (n.bit_length() + 7) // 8
    with open(input_file, "rb") as f:
        ciphertext = f.read()
    
    plaintext = b''
    for i in range(0, len(ciphertext), chunk_size):
        chunk = ciphertext[i:i+chunk_size]
        chunk_int = int.from_bytes(chunk, byteorder='big')
        plaintext_int = decrypt(chunk_int, private_key)
        plaintext += plaintext_int.to_bytes((n.bit_length() + 7) // 8 - 1, byteorder='big')

    plaintext = plaintext.rstrip(b'\x00')   # remove padding
    
    with open(output_file, "wb") as f:
        f.write(plaintext)

if __name__ == "__main__":
    public_key, private_key = generate_keys()

    print("Public Key:", public_key)
    print("Private Key:", private_key)

    encrypt_file("./Test/audio.mp3", "./Test_Result/cipher.dat", public_key)
    decrypt_file("./Test_Result/cipher.dat", "./Test_Result/decrypted.mp3", private_key)
