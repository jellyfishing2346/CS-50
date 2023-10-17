import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    pageList = {}
    linkPage = len(corpus[page])

    if linkPage:
        for linkInformation in corpus:
            pageList[linkInformation] = (1 - damping_factor) / len(corpus)
        for linkInformation in corpus[page]:
            pageList[linkInformation] = (1 - damping_factor) / linkPage
    else:
        for linkInformation in corpus:
            pageList[linkInformation] = len(corpus)
    return pageList


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pageList = {}
    for page in corpus:
        pageList[page] = 0
    page = random.choice(list(corpus.keys()))

    for index in range(1, n):
        current = transition_model(corpus, page, damping_factor)
        for page in pageList:
            pageList[page] = ((index-1) * pageList[page] + current[page]) / index
        page = random.choices(list(pageList.keys()), list(pageList.values()))[0]
    return pageList
    

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    rankInformation = {}
    throttle = 0.0005
    index = len(corpus)

    for pageKey in corpus:
        rankInformation[pageKey] = 1 / index

    while True:
        counting = 0
        for pageKey in corpus:
            newPage = (1 - damping_factor) / index
            amount = 0
            for pageInfo in corpus:
                if pageKey in corpus[pageInfo]:
                    linkNum = len(corpus[pageInfo])
                    counting = counting + rankInformation[pageInfo]/linkNum
                    amount = damping_factor * amount
                    newPage += amount
                    if abs(rankInformation[pageKey] - newPage) < throttle:
                        counting += 1
                    rankInformation[pageKey] = newPage
                if counting == index:
                    break
                return rankInformation

if __name__ == "__main__":
    main()
