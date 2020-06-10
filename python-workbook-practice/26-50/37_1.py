# Question: Create a function that takes a text file as input and returns the number of words contained in the text file. 
# Please take into consideration that some words can be separated by a comma with no space. 
# For example "Hi,it's me." would need to be counted as three words. 
# For your convenience, you can use the text file in the attachment. (word1.txt)

def test_split():
    with open('word1.txt', 'r+') as open_file:
        D = open_file.read()
        print(D) # O/P: A tree is a woody perennial plant, typically with branches
        print(len(D))
        D.replace(" ", ",")
        print(D)
        print(len(D))

test_split()


