file_name = 'text.txt'

# Create a function that takes an input file name 
def count_words(file): 
    # Create an empty dictionary 
    word_freq = {} 

    # Open the file in read mode 
    with open(file, 'r') as f: 
        # Read the contents of the file 
        for line in f: 
            # Strip the leading spaces and newline character 
            line = line.strip() 

            # Split the line into words 
            words = line.split(" ") 

            # Increase the count of each word 
            for word in words: 
                if not word in word_freq: 
                    word_freq[word] = 1
                else: 
                    word_freq[word] += 1

    # Print the frequency of each word 
    for key, value in word_freq.items(): 
        print(key, ":", value) 

# Call the function 
count_words(file_name)