# 1 Firstly, use the input function to promt the user to enter a string.

phrase = str(input("Enter phrase or sentence: "))

# define a function to return reversed string

def reversed_string(string):
    return string[::-1]

# use the split keyword to split the phrase into separate words into a list, 
# so it can be iterated over, set longest word as an empty string

words = phrase.split()
def longest_word(words):
    longest_word = ""
    
    for word in (words):
        if len(word) > len(longest_word):
            longest_word = word
            
    return longest_word

longest_word = longest_word(words)

def shortest_word(words):
    shortest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
            
    return shortest_word

shortest_word = shortest_word(words)

response1 = f"Reversed string: {reversed_string(phrase)}"
response2 = f"Longest word: \"{longest_word}\""
response3 = f"Shortest word: \"{shortest_word}\""

responses = [response1, response2, response3]

for index, response in enumerate(responses, 1):
    print(f"\n{index}. {response}")

character = input("\nEnter any letter to count it's number of occurence: ")

def occurence_of_letter(character):
    occurence = 0
    for char in phrase:
        if char == character:
            occurence += 1
    return occurence

occurence_of_letter(character)

response4 = f"""
4. The letter \"{character}\" occurs {occurence_of_letter(character)} times in the phrase

Thank you for your time
Enjoy the rest of the day
    
    Bye!
"""
print(response4)

# ============================================================================






