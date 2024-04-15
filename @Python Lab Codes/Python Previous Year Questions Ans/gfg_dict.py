LL = ["Gfg", "is", "Good", "for"]
DD = {"Gfg": 5, "Best": 6}
K = "Gfg"

# Check if K is present in both LL and DD
if K in LL and K in DD:
    print("Value of", K, "is", DD[K])
else:
    print("Key", K, "is not present in both the list and the dictionary.")


