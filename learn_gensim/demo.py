import logging
import re

import gensim
from sklearn import datasets

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def load_stopwords():
    stopwords = []
    with open('stopwords.txt', 'r') as f:
        for line in f.readlines():
            stopwords.append(line.strip())
    return stopwords


def tokenize(text):
    text = text.lower()
    words = re.sub("\W", " ", text).split()
    words = [w for w in words if w not in stopwords]
    return words


def bow2tokens(bow, d):
    l = []
    for id in bow:
        t = (d.id2token[id[0]], id[1])
        l.append(t)
    return l


if __name__ == '__main__':
    news_dataset = datasets.fetch_20newsgroups(subset="all", remove=("headers", "footers", "quotes"))
    documents = news_dataset.data
    #
    # stopwords = load_stopwords()
    # print(documents[0])
    # processed_docs = [tokenize(doc) for doc in documents]
    # word_count_dict = gensim.corpora.Dictionary(processed_docs)
    # word_count_dict.filter_extremes(no_below=20, no_above=0.1)
    #
    # # word_count_dict = gensim.corpora.Dictionary.load('dict.txt')
    # bag_of_words_corpus = [word_count_dict.doc2bow(pdoc) for pdoc in processed_docs]
    #
    # word_count_dict.save("dict.pkl")
    # gensim.corpora.MmCorpus.serialize('corpus.mm', bag_of_words_corpus)


    # lda_model = gensim.models.LdaModel(bag_of_words_corpus, num_topics=50, id2word=word_count_dict, passes=5)
    # # lda_model.save('lda.txt')
    # # lda_model = gensim.models.LdaModel.load('lda.txt')
    # lda_model.get_document_topics(bag_of_words_corpus[0])

    word_count_dict = gensim.corpora.Dictionary.load('dict.pkl')
    bag_of_words_corpus = gensim.corpora.MmCorpus('corpus.mm')
    tfidf = gensim.models.TfidfModel(bag_of_words_corpus)
    corpus_tfidf = tfidf[bag_of_words_corpus]
    # for doc in corpus_tfidf:
    #     print(doc)

    lsi = gensim.models.LsiModel(corpus_tfidf, id2word=word_count_dict, num_topics=20)
    corpus_lsi = lsi[corpus_tfidf]

    ##query
    # lsi = gensim.models.LsiModel(bag_of_words_corpus, id2word=word_count_dict, num_topics=20)

    index = gensim.similarities.MatrixSimilarity(lsi[tfidf[bag_of_words_corpus]])
    index.save('deerwester.index')
    index = gensim.similarities.MatrixSimilarity.load('deerwester.index')

    sims = index[lsi[tfidf[bag_of_words_corpus[0]]]]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    print('sim of ', bow2tokens(bag_of_words_corpus[0], word_count_dict))
    count = 0
    for sim in sims:
        print('similarities: ', sim[1], sim[0], '###: ', bow2tokens(bag_of_words_corpus[sim[0]], word_count_dict))
        count += 1
        if count > 10:
            break
