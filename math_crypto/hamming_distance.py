def hamming_distance(bytes1, bytes2):
    if len(bytes1) != len(bytes2):
        print("Arrays must have the same length")
        return
    distance = 0
    for b1, b2 in zip(bytes1,bytes2):
        distance += bin(b1 ^ b2).count('1')
    return distance

