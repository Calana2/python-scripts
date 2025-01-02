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
