import extractor as ex

KEY_DELIMITER = ", "

def return_key_phrases(text, key_dilimiiter=KEY_DELIMITER):
    """Return a sring of key phrases. Each phrase is separated by a space by default.
        
        :param text: A string.
        :param key_dilimiiter: A string."""

    keys = ex.extract_key_phrases(text)
    
    key_append = ""
    for phrase in keys:
        key_append += phrase + key_dilimiiter

    return str(key_append)

if __name__ == '__main__':
    
    text = """ In this paper, we introduce TextRank - a graph-based ranking model for text processing,
        and show how this model can be successfully used in natural language applications. 
        In particular, we propose two innovative unsupervised methods for keyword and sentence
        extraction, and show that the results obtained compare favorably with previously published results 
        on established benchmark"""

    print(return_key_phrases(text))

    # text example taken from https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf
    # result of top 1 search result: https://tailieunhanh.com/vn/tlID812113_bao-cao-khoa-hoc-graphbased-ranking-algorithms-for-sentence-extraction-applied-to-text-summarization.html 
