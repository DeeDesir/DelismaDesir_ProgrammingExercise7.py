#impott the re 
import re

#Function to split the paragraph into sentences
def split_into_sentences(paragraph):
    # Regular expression to split sentences based on '.', '?', or '!'
    sentences = re.split(r'(?<=\w[.?!])\s+', paragraph)
    return sentences

#Function to count and display the sentences
def display_sentences(paragraph):
    # Get the list of sentences
    sentences = split_into_sentences(paragraph)
    
# Count the number of sentences you have 
    num_sentences = len(sentences)
    
 #Display each of the sentences
    for i, sentence in enumerate(sentences, 1):
        print(f"Sentence {i}: {sentence.strip()}")
    
  #Display the total number of sentences
    print(f"\nTotal number of sentences: {num_sentences}")

# Main function to get user input and run the program
def main():
    # Input the paragraph
    paragraph = input("Enter a paragraph: ")
    
#Display sentences and count each
    display_sentences(paragraph)

#Run the program/ test it 
if __name__ == "__main__":
    main()
