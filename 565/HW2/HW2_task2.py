from collections import Counter 

import numpy as np 

  

# Function to calculate the Index of Coincidence 

def index_of_coincidence(text): 

    #Write the code to calculate the IC  
    i = len(text)
    #conditioning for i<2
    if i < 2:
        return 0
    #if not then carry on
    f_count = Counter(text)
    #looping to find the sum 
    total_sum = 0
    for freq in f_count.values():
        total_sum += freq*(freq-1)
    ic = total_sum / (i * (i-1))   
    return ic 

  

# Function to calculate the average IC for different key lengths 

def average_ic(ciphertext, max_key_length): 
    avg_ics = [] 
    for key_length in range(1, max_key_length+1): 
        ics = [] 
        for i in range(key_length): 
            nth_letters = ciphertext[i::key_length]#write the code to create a substring of the ciphertext starting from index i and selecting every key_length-th character since these letters shift the same number
            ic = index_of_coincidence(nth_letters) 
            ics.append(ic) 
        avg_ic = np.mean(ics) 
        avg_ics.append((key_length, avg_ic)) 
    return avg_ics 

def key_finder(list, keylength, i): 
    smallest_x2 = float('inf') 
    best_c = ' ' 
    N = 0 
    expected_freq = [ 

        0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 

        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 

        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 

        0.00978, 0.0236, 0.0015, 0.01974, 0.00074 

    ] 
    observed_freq = [0] * 26 
    freq = [0] * 26 
    for j in range(i, len(list), keylength):
        freq[ord(list[j]) - ord('a')] += 1 
    N = sum(freq) 
    for j in range(26): 
        observed_freq[j] = freq[j] / N 
    for j in range(26): 
        x2 = 0 
        for k in range(26): 
             x2 += ((observed_freq[(j + k) % 26] - expected_freq[k]) ** 2) / expected_freq[k] 
        if x2 < smallest_x2: 
            smallest_x2 = x2 
            best_c = chr(ord('a') + j) 
    return best_c 

# Function to decrypt the ciphertext using the Vigenère cipher
def vigenere_decrypt(ciphertext, key):
    plaintext = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext.append(chr(value + 97))  # 97 is the ASCII value for 'a'
    return ''.join(plaintext)

#Task 2: step 1
#ciphertext 
ciphertext = "usojlbxpkieoiqmwucdyiaxamvknplbeaxcfjmvsjmvsfzblxstgrbbmfxgwyvhjgkamvknpaxacjbachvqnvkmggrqztwfnmxgljglrwquuelgclaqlbaypgqcnkivikfagrtbaaswmrkmmjwvbrbfyqvgmltmgfypulbamjmbyuqgdgvoukqhlvmuwcwlsjivbvnmmxstxrutewxqbrzwusvgmfnmusvgiiltrseuqvteykjtidbacvmullxmggrqldqlbavgwkqhlgjvbvaxpnmeyjbacqttimqwc" 

# Calculate and display the average IC for key lengths up to 10 (you can adjust this value) 
max_key_length = 10 
avg_ics = average_ic(ciphertext, max_key_length) 
# Print the average ICs for each key length 
for key_length, ic in avg_ics: 
    print(f"Key Length: {key_length}, Average IC: {ic:.4f}") 
# Identify the key length with the IC closest to the expected IC for the language (0.065 for English) 
expected_ic = 0.065 
closest_key_length = min(avg_ics, key=lambda x: abs(x[1] - expected_ic))[0] 
print(f"\nClosest key length to expected IC is: {closest_key_length}")




#Task 2: step 2
key = ''
for i in range(closest_key_length):
    key += key_finder(ciphertext, closest_key_length, i)
print(key)

plaintext = vigenere_decrypt(ciphertext, key)
print(f"\nplaintext: {plaintext}")