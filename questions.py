import nltk
import sys

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    content = {}

    for index in os.listdir(directory):
        with open(os.path.join(directory, file), encoding='utf-8') as info:
            content[index] = info.read()
    return content


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    token = nltk.tokenize.word_token(document.lower())
    final = [index for index in token if not string.punctuation() and index not in nltk.corpus.stopwords.words("english")]
    return final

def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    dictionary = {}
    docLength = len(documents)

    unique_words = set(sum(documents.values(), []))

    for word in unique_words:
        count = 0
        for doc in documents.values():
            if word in doc:
                count += 1

        dictionary[word] = math.log(docLength/count)

    return dictionary


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    track = {}
    for filename, filecontent in files.items():
        info = 0
        for index in query:
            if index in filecontent:
                info += filecontent.count(index) * idfs[index]
        if info != 0:
            track[filename] = info

    sorted_by_score = [k for k, in sorted(scores.items(), key=lambda x: x[1], reverse=True)]
    return sorted_by_score[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    scores = {}
    for sentence, sentwords in sentences.items():
        score = 0
        for word in query:
            if word in sentwords:
                score += idfs[word]

        if score != 0:
            density = sum([sentwords.count(x) for x in query]) / len(sentwords)
            scores[sentence] = (score, density)

    sorted_by_score = [k for k, v in sorted(scores.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True)]

    return sorted_by_score[:n]


if __name__ == "__main__":
    main()
