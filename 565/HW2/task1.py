from collections import Counter

# Initialize a dictionary to hold frequency counts for each position (1st to 7th) in the blocks
position_frequencies = {i: Counter() for i in range(8)}

# Sample ciphertext blocks
ciphertext_blocks = [
    "usojlbxp", "kieoiqmw", "ucdyiaxa", "mvknplbe", "axcfjmvs", "jmvsfzbl",
    "xstgrbbm", "fxgwyvhj", "gkamvknp", "axacjbac", "hvqnvkmg", "grqztwfn",
    "mxgljglr", "wquuelgc", "laqlbayp", "gqcnkivi", "kfagrtba", "aswmrkmm",
    "jwvbrbfy", "qvgmltmg", "fypulbam", "jmbyuqgd", "gvoukqhl", "vmuwcwls",
    "jivbvnmm", "xstxrute", "wxqbrzwu", "svgmfnmu", "svgiiltr", "seuqvtey",
    "kjtidaac", "vmullxmg", "grqldqlb", "avgwkqhl", "gjvbvaxp", "nmeyjbac",
    "qttimqwc"
]

# Iterate over each block and each position within the block
for block in ciphertext_blocks:
    for position in range(8):
        # Ensure the block is long enough
        if position < len(block):
            position_frequencies[position][block[position]] += 1

# Display the frequency of each letter for each position
for position in range(8):
    print(f"Position {position + 1}:")
    for letter, frequency in position_frequencies[position].items():
        print(f" {letter}: {frequency}")
