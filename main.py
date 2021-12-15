import textrank as tr

text = "A programming language comprises a set of instructions. It is used to produce various kinds of output. It is a language which involves a computer performing some kind of instructions or algorithm to produce some form of output."
# ans = tr.extract_sentences(text)
ans = tr.extract_key_phrases(text)

print(ans)