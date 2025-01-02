FILENAME="raw_6.txt"

english_frequencies = {
        'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95,
        'S': 6.28, 'H': 6.09, 'R': 5.99, 'D': 4.32, 'L': 4.03, 'U': 2.88,
        'C': 2.71, 'M': 2.61, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'P': 1.82,
        'Y': 1.75, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'J': 0.10,
        'Q': 0.10, 'Z': 0.07, ' ': 13.00}

def english_score(data):
    if not data:
        return 0
    letter_counts = {}
    total_letters = 0
    for byte in data:
        char = chr(byte).upper()
        if 'A' <= char <= 'Z' or char == ' ':
            letter_counts[char] = letter_counts.get(char,0) + 1
            total_letters += 1
    score = 0
    if total_letters > 0:
        for char, freq in english_frequencies.items():
            observer_freq = letter_counts.get(char,0) 
            score += observer_freq * freq
            score -= abs(observer_freq/100 - freq) / 10 
    return score

def hamming_distance(bytes1, bytes2):
    if len(bytes1) != len(bytes2):
        print("Arrays must have the same length")
        return
    distance = 0
    for b1, b2 in zip(bytes1,bytes2):
        distance += bin(b1 ^ b2).count('1')
    return distance


def normalized_hamming_distance(file , blocksize):
    try:
        with open(file,"rb") as file:
            hd_normalized = 0
            n = 0
            while True:
                    data = file.read(blocksize*2)
                    if len(data) != blocksize*2:
                        break
                    a = data[:blocksize]
                    b = data[blocksize:]
                    hd_normalized += (hamming_distance(a,b) / blocksize)
                    n += 1
            file.close()
            return (hd_normalized / n)
    except FileNotFoundError:
        print("Error opening the file")

def get_trans_blocks(file , keysize):
    raw_blocks = []
    blocks = []
    try:
        with open(file,"rb") as file:
            while True:
                    raw_block = file.read(keysize)
                    if len(raw_block) != keysize:
                        break
                    raw_blocks.append(raw_block)
                        
            file.close()
    except FileNotFoundError:
        print("Error opening the file")
    for i in range(0,keysize):
        block = bytearray(len(raw_blocks))
        for n,b in enumerate(raw_blocks):
            block[n]=b[i]
        blocks.append(block)
    return blocks

def single_xor(msg, key):
    result = []
    for i in range(0,len(msg)):
        result.append(msg[i] ^ key)
    return bytes(result)

# --- MAIN --- 

KEYSIZE = 2
data_measure = {"hamming_distance":normalized_hamming_distance(FILENAME,KEYSIZE), "keysize":KEYSIZE}
for i in range(KEYSIZE+1,41):
    hd_now = normalized_hamming_distance(FILENAME,i) 
    if hd_now < data_measure["hamming_distance"]:
        data_measure["hamming_distance"] = hd_now
        data_measure["keysize"] = i
blocks = get_trans_blocks(FILENAME,data_measure["keysize"])
print(f"The key length is: [{data_measure["keysize"]}]")

key = ""
for b in blocks:
    char = 0
    xb = single_xor(b,0)
    ES = english_score(xb)
    for c in range(1,255):
        xored_block = single_xor(b,c)
        es = english_score(xored_block)
        if es > ES:
            ES = es
            char = c
    key += chr(char)

print(f"The key is: [{key}]")
