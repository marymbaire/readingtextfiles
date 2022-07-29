# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content():
    with open('story.txt') as f:
        contents = f.read()
        print(contents)


read_file_content()


def count_words():
    # [assignment] Add your code here

    with open('story.txt') as f:
        contents = f.read()
        print("PLEASE ENTER WORD WHOSE OCCURRENCE IN THE TEXT YOU WANT TO CHECK:")
        word = input()
        print("'", word, "'", ":" , contents.count(word))
    # return {"as": 10, "would": 20}


count_words()

