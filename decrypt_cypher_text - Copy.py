def decrypt_cypher_text(encrypted_text, key):
#     # function implementation here...
    
    decrypted_text = ""  # Initialize an empty string to store the decrypted text
    
    # Loop through each character in the encrypted text
    for char in encrypted_text:
        # Step 1: Convert character to its ASCII code using ord()
        ascii_code = ord(char)
        
        # Step 2: Subtract the key from the ASCII code
        adjusted_code = ascii_code - key
        
        # Step 3: Find the remainder when divided by 256
        decrypted_code = adjusted_code % 256
        
        # Step 4: Convert the resulting ASCII code back to a character using chr()
        decrypted_char = chr(decrypted_code)
        
        # Append the decrypted character to the result
        decrypted_text += decrypted_char
    
    # Return the fully decrypted text
    return decrypted_text
# Test case: 
encrypted_text = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu"
key = 3

# Decrypt the text using the function
decrypted_text = decrypt_cypher_text(encrypted_text, key)

# Print the decrypted text
print(decrypted_text)
