def pattern(ciphertext):
    chunks = {}
    min_len = 2
    # make the max length a long common word (long word = fascinating = len 11)
    max_len = 11
    # we will use the Kasiski examination to find the length of the key
    # the Kasiski examination works by finding repeating sequences of letters in the ciphertext
    # find the repetitions using the kawiski method (2-11 length chunks)
    # find the distance between the repeating chunks and find the common multiples to figure out the length of the key
    # return the length of the key and the repeated chunks
    # after this we use the repeated chunks to decode into plaintext then figure out the letters of the key by comparing the plaintext to the ciphertext
    # the repeated chunks will most likely be common words like "the", "and", "that", etc.
    for i in range(len(ciphertext)):
        chunk = ""
        for j in range(min_len, max_len + 1):
            if i + j <= len(ciphertext):
                chunk = ciphertext[i:i + j]
                if chunk not in chunks:
                    chunks[chunk] = 1
                else:
                    chunks[chunk] += 1

    return chunks

# this function will decrypt the chunks of the patterned letter sequences that show the length of the key
# we will use the vigenere decryption method to decrypt the chunks
# the vigenere decryption method works by shifting the letters of the ciphertext back by the letters of the key
# based off the findings of the ciphertext chunks to plaintext, if they make sense then we will have the correct key length and key letters
def decryption(ciphertext, key):

def find_key():