import extractor as ex

if __name__ == '__main__':
    
    # text = """ In this paper, we introduce TextRank - a graph-based ranking model for text processing,
    #     and show how this model can be successfully used in natural language applications. 
    #     In particular, we propose two innovative unsupervised methods for keyword and sentence
    #     extraction, and show that the results obtained compare favorably with previously published results 
    #     on established benchmark"""
    text ='I love my family. My family gave me everything'
    keys = ex.return_key_phrases(text)

    print(keys)

    # text example taken from https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf
    # result of top 1 search result: https://tailieunhanh.com/vn/tlID812113_bao-cao-khoa-hoc-graphbased-ranking-algorithms-for-sentence-extraction-applied-to-text-summarization.html 
