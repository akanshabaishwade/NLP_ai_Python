import nltk
from nltk.stem import PorterStemmer

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.stemmer = PorterStemmer()

    def insert(self, sentence):
        words = nltk.word_tokenize(sentence.lower())
        stemmed_words = [self.stemmer.stem(word) for word in words]

        current = self.root
        for word in stemmed_words:
            if word not in current.children:
                current.children[word] = TrieNode()
            current = current.children[word]
        current.is_word = True

    def autocomplete(self, prefix):
        words = nltk.word_tokenize(prefix.lower())
        stemmed_words = [self.stemmer.stem(word) for word in words]

        current = self.root
        for word in stemmed_words:
            if word not in current.children:
                return []
            current = current.children[word]
        return self._get_autocomplete_words(current)

    def _get_autocomplete_words(self, node, current_word=""):
        words = []
        if node.is_word:
            words.append(current_word)
        for word, child in node.children.items():
            child_words = self._get_autocomplete_words(child, current_word + word)
            words.extend(child_words)
        return words


# Example usage
sentences = [
    "I love to code",
    "Code is my passion",
    "Coding makes me happy",
    "Happy coding!"
]

trie = Trie()
for sentence in sentences:
    trie.insert(sentence)

partial_sentence = input("Enter a partial sentence: ")
suggestions = trie.autocomplete(partial_sentence)
if suggestions:
    # print(suggestions, 'suggestion')
    autocomplete_suggestions = [partial_sentence + suggestion + " " for suggestion in suggestions]
    print("Autocomplete suggestions:")
    for suggestion in autocomplete_suggestions:
        print(suggestion)
else:
    print("No autocomplete suggestions.")
