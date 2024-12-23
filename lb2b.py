import re 
# Sample text 
text = """ 
John's email is [email protected]. He said, "Python is awesome!!"    It's a     great   language. 
Another email: [email protected].  
""" 
# 1. Remove special characters except for spaces and email-related characters. 
# Using regex to remove non-alphabetic characters and non-email symbols 
clean_text = re.sub(r"[^a-zA-Z0-9@\.\s]", "", text) 
print("Text after removing special characters:") 
print(clean_text) 

 
# 2. Convert the text to lowercase 
clean_text = clean_text.lower() 
print("\nText after converting to lowercase:") 
print(clean_text) 
# 3. Replace multiple spaces with a single space 
clean_text = re.sub(r"\s+", " ", clean_text) 
print("\nText after replacing multiple spaces:") 
print(clean_text) 
 
# 4. Extract all words starting with a vowel (a, e, i, o, u) 
vowel_words = re.findall(r"\b[aeiouAEIOU]\w+", clean_text) 
print("\nWords starting with a vowel:") 
print(vowel_words) 
 
# 5. Replace email addresses with '[email protected]' 
masked_text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[email protected]", clean_text) 
print("\nText after replacing emails:") 
print(masked_text)