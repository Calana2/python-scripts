def fixed_xor(var1, var2):
    if len(var1) != len(var2):
        print("Params must be the same length")
        return bytes(0)
    result = []
    for i in range(0, len(var1)):
        result.append(var1[i] ^ var2[i])
    return bytes(result)

def repeated_xor(msg, key):
    if len(key) > len(msg):
        print("Key must be less or equal than the message")
    result = []
    key_index = 0
    for i in range(0,len(msg)):
        result.append(msg[i] ^ key[key_index])
        key_index = (key_index+1) % len(key)
    return bytes(result)

def single_xor(msg, key):
    result = []
    for i in range(0,len(msg)):
        result.append(msg[i] ^ key)
    return bytes(result)
