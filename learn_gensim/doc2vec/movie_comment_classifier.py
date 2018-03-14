# -*- coding: utf-8 -*-

import os.path
import pickle
import re
from os import listdir

import gensim
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression


def get_dataset():
    dataset = []
    datalabels = []
    docLabels = []

    dirs = {'/Users/ring/Code/Machine Learning/Resource/aclImdb/train/neg/': 0,
            '/Users/ring/Code/Machine Learning/Resource/aclImdb/train/pos/': 1,
            '/Users/ring/Code/Machine Learning/Resource/aclImdb/test/neg/': 0,
            '/Users/ring/Code/Machine Learning/Resource/aclImdb/test/pos/': 1
            }

    for key, value in dirs.items():
        print('loading data from: ' + key)
        files = [f for f in listdir(key) if f.endswith('.txt')]
        for file in files:
            with open(key + file, 'r', encoding='utf-8') as infile:
                dataset.append(tokenize(infile.read()))
                datalabels.append(value)

            if 'train' in key:
                prefix = 'train'
            else:
                prefix = 'test'
            docLabels.append(prefix + '_' + str(value) + '_' + file)

    # #使用1表示正面, 0表示负面
    # y = np.concatenate((np.ones(len(pos_reviews)), np.zeros(len(neg_reviews))))
    trainset, testset, trainlabels, testlabels, train_doc_labels, test_doc_labels = train_test_split(dataset,
                                                                                                     datalabels,
                                                                                                     docLabels,
                                                                                                     test_size=0.2)
    return trainset, testset, trainlabels, testlabels, train_doc_labels, test_doc_labels


def load_stopwords(file):
    stopwords = []
    with open(file, 'r') as f:
        for line in f.readlines():
            stopwords.append(line.strip())
    return stopwords


def tokenize(text):
    text = text.lower()
    words = re.sub("\W", " ", text).split()
    words = [w for w in words if w not in stopwords]
    return words


class LabeledLineSentence(object):
    def __init__(self, doc_list, labels_list):
        self.labels_list = labels_list
        self.doc_list = doc_list

    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
            yield gensim.models.doc2vec.LabeledSentence(doc, [self.labels_list[idx]])


if __name__ == '__main__':

    stopwords = load_stopwords('../stopwords.txt')
    # dir = '/Users/ring/Code/Machine Learning/Resource/aclImdb/train/neg/'
    #
    # docLabels = [f for f in listdir(dir) if f.endswith('.txt')]
    # print(docLabels)

    if os.path.exists('doc2vec.model') and os.path.exists('datas.plk'):
        d2v_model = gensim.models.doc2vec.Doc2Vec.load('doc2vec.model')
        datas = pickle.load(open('datas.plk', 'rb'))
        trainset = datas['trainset']
        testset = datas['testset']
        trainlabels = datas['trainlabels']
        testlabels = datas['testlabels']
        train_doc_labels = datas['train_doc_labels']
        test_doc_labels = datas['test_doc_labels']
    else:
        # data = []
        # for doc in docLabels:
        #     line = open(dir + doc, encoding="utf-8").read()
        #     data.append(tokenize(line))
        # print('------------','data loaded')

        trainset, testset, trainlabels, testlabels, train_doc_labels, test_doc_labels = get_dataset()
        datas = {
            'trainset': trainset,
            'testset': testset,
            'trainlabels': trainlabels,
            'testlabels': testlabels,
            'train_doc_labels': train_doc_labels,
            'test_doc_labels': test_doc_labels
        }
        pickle.dump(datas, open('datas.plk', 'wb'))

        # iterator returned over all documents
        it = LabeledLineSentence(trainset, train_doc_labels)

        """doc2vec 模型参数
        min_count: 忽略频率低于这个值的词
        window: the window size of the skip-gram model
        size: dimensionality of the feature vectors in output
        sample: threshold for configuring which higher-frequency words are randomly downsampled
        workers: use this many worker threads to train the model
        alpha: is the initial learning rate (will linearly drop to `min_alpha` as training progresses).
        """
        model = gensim.models.Doc2Vec(size=100, min_count=0, alpha=0.025, min_alpha=0.025)
        model.build_vocab(it)

        # training of model
        for epoch in range(10):
            print('iteration ', str(epoch + 1))
            model.train(it, total_examples=model.corpus_count, epochs=model.iter)
            model.alpha -= 0.002
            model.min_alpha = model.alpha
            model.train(it, total_examples=model.corpus_count, epochs=model.iter)
        # saving the created model
        model.save('doc2vec.model')
        print('------------', 'model saved')
        d2v_model = model

    # start test
    # docvec = d2v_model.docvecs[1]
    # print(docvec)
    # sims = d2v_model.docvecs.most_similar('0_3.txt')
    # print(sims)


    train_docvec = [d2v_model.docvecs[l] for l in train_doc_labels]
    test_docvec = [d2v_model.infer_vector(l) for l in testset]

    classifier = LogisticRegression()
    classifier.fit(np.array(train_docvec), np.array(trainlabels))
    score = classifier.score(np.array(test_docvec), np.array(testlabels))

    print('------------', 'score: ' , score)
