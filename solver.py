def vowel_replace(word,index):
    vowels = ['a','e','i','o','u']
    words = []
    for vowel in vowels:
        words.append(word[:index]+vowel+word[index+1:])
    return words

def all_indexes(word,item):
    indices = [i for i, x in enumerate(word) if x == item]
    return indices
    
def word_permutations(word):
    words = []
    indexes = []
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        indexes += all_indexes(word,vowel)
    for index in indexes:
        words.append(vowel_replace(word,index))
    return words
    
        

letters = [chr(i) for i in range(65,90+1)]
vowels = ['a','e','i','o','u']
#words = set([])
#for letter in letters:
#    word_list = open(letter+" Words.txt").read().splitlines()
#    words = words.union(set(word_list))
words = set(open("wordsEn.txt").read().splitlines())
while words:
    word = words.pop()
    ideas = word_permutations(word)
    for single_idea in ideas: #list of all the permutations
        for idea in single_idea: #each word in the permutation
            if (not idea in words) and (not idea==word):
                break
        else:
            print single_idea
        
                
 