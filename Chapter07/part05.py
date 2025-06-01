# Check if two words are anagrams (same letters in different order)

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

# Convert both to lowercase and remove spaces
word1 = word1.replace(" ", "").lower()
word2 = word2.replace(" ", "").lower()

# First check if lengths are equal
if len(word1) != len(word2):
    print("They are not anagrams. (Different lengths)")
else:
    # If lengths are equal, check sorted characters
    if sorted(word1) == sorted(word2):
        print("They are anagrams.")
    else:
        print("They are not anagrams.")
