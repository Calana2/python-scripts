import sys

if len(sys.argv) != 3 or sys.argv[1] == '-h':
    print("Usage: python3 combinator.py [min_length] [max_length]")
    exit(1)

def generate_combinations(alphabet, length, current_combination=""):
    # Genera len(alphabet)^length combinaciones
    if length == 0:
        print(current_combination)
        return
    for char in alphabet:
        generate_combinations(alphabet,length-1,current_combination+char)


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
characters = "`-=[];,',./\\~!@#$%^&*()_+{}:<>?|"
dictionary = alphabet + numbers + characters

min_length = int(sys.argv[1])
max_length = int(sys.argv[2])

for i in range(min_length,max_length+1):
    generate_combinations(dictionary,i)

