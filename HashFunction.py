import random

def hashFunction(plaintext):
    hashV = 0
    random.seed(10)
    for letter in plaintext:
        hashV += ord(letter)  
        hashV += random.randint(1,10)
    return hashV % 512  



if __name__ == "__main__":
    plaintext = input("Enter a sentence to hash: ")
    hashValue = hashFunction(plaintext)
    print(f"Hashing plaintext: {hashValue}")
