''' Code taken and modified from:
    https://github.com/davidadamojr/TextRank'''

import nltk
import networkx as nx
import itertools
import editdistance

KEY_DELIMITER = " "


def filter_for_tags(tagged, tags=['NN', 'JJ', 'NNP']):  # tags = ['NOUN', 'ADJ']
    """Apply syntactic filters based on POS tags."""
    return [item for item in tagged if item[1] in tags]
    
def normalize(tagged):
    """Return a list of tuples with the first item's periods removed."""
    return [(item[0].replace('.', ''), item[1]) for item in tagged]

def unique_everseen(iterable, key=None):
    """List unique elements in order of appearance.

    Examples:
        unique_everseen('AAAABBBCCDAABBB') --> A B C D
        unique_everseen('ABBCcAD', str.lower) --> A B C D
    """
    seen = set()
    seen_add = seen.add
    if key is None:
        def key(x): return x
    for element in iterable:
        k = key(element)
        if k not in seen:
            seen_add(k)
            yield element

def build_graph(nodes):
    """Return a networkx graph instance.

    :param nodes: List of hashables that represent the nodes of a graph.
    """
    gr = nx.Graph()  # initialize an undirected graph
    gr.add_nodes_from(nodes)
    nodePairs = list(itertools.combinations(nodes, 2))

    # add edges to the graph (weighted by Levenshtein distance)
    for pair in nodePairs:
        firstString = pair[0]
        secondString = pair[1]
        levDistance = editdistance.eval(firstString, secondString)
        gr.add_edge(firstString, secondString, weight=levDistance)

    return gr


def extract_key_phrases(text):
    """Return a set of key phrases.

    :param text: A string.
    """
    # tokenize the text using nltk
    word_tokens = nltk.word_tokenize(text)

    # assign POS tags to the words in the text
    tagged = nltk.pos_tag(word_tokens)
    textlist = [x[0] for x in tagged]

    tagged = filter_for_tags(tagged)
    tagged = normalize(tagged)

    unique_word_set = unique_everseen([x[0] for x in tagged])
    word_set_list = list(unique_word_set)

    # this will be used to determine adjacent words in order to construct
    # keyphrases with two words

    graph = build_graph(word_set_list)

    # pageRank - initial value of 1.0, error tolerance of 0,0001,
    calculated_page_rank = nx.pagerank(graph, weight='weight')

    # most important words in ascending order of importance
    keyphrases = sorted(calculated_page_rank, key=calculated_page_rank.get,
                        reverse=True)

    # the number of keyphrases returned will be relative to the size of the
    # text (a third of the number of vertices)
    one_third = len(word_set_list) // 3
    keyphrases = keyphrases[0:one_third + 1]

    # take keyphrases with multiple words into consideration as done in the
    # paper - if two words are adjacent in the text and are selected as
    # keywords, join them together
    modified_key_phrases = set([])

    i = 0
    while i < len(textlist):
        w = textlist[i]
        if w in keyphrases:
            phrase_ws = [w]
            i += 1
            while i < len(textlist) and textlist[i] in keyphrases:
                phrase_ws.append(textlist[i])
                i += 1

            phrase = ' '.join(phrase_ws)
            if phrase not in modified_key_phrases:
                modified_key_phrases.add(phrase)
        else:
            i += 1

    return modified_key_phrases


def return_key_phrases(text, key_dilimiiter=KEY_DELIMITER):
    """Return a sring of key phrases. Each phrase is separated by a space by default.
        
        :param text: A string.
        :param key_dilimiiter: A string."""

    keys = extract_key_phrases(text)
    
    key_append = ""
    for phrase in keys:
        key_append += phrase + key_dilimiiter

    return str(key_append)
