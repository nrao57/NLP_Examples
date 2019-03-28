def LevenshteinDistance(s, len_s, t, len_t):
    cost = 0

    # base case: empty strings
    if (len_s == 0): return len_t;
    if (len_t == 0): return len_s;

    # test if last characters of the strings match
    if (s[len_s-1] == t[len_t-1]):
        cost = 0;
    else:
        cost = 1;

    # return minimum of delete char from s, delete char from t, and delete char from both */
    return min(LevenshteinDistance(s, len_s - 1, t, len_t) + 1,
                 LevenshteinDistance(s, len_s, t, len_t - 1) + 1,
                 LevenshteinDistance(s, len_s - 1, t, len_t - 1) + cost);

s = "kitten"
t = "sitting"
dist = LevenshteinDistance(s, len(s), t, len(t))
print("The Levenshtein distance between {} and {} is {}".format(s, t, dist))

# Which word is most similar to woman and king?
import warnings; warnings.simplefilter('ignore')
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors

glove_input_file = 'glove.6B.50d.txt'
word2vec_output_file = glove_input_file + 'word2vec'
glove2word2vec(glove_input_file, word2vec_output_file)

# load the Stanford GloVe model
model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)
# calculate: (king - man) + woman = ?
result = model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
print(result)

# example comparing the verbs "run" and "sprint"
import nltk 
from nltk.corpus import wordnet 
  
w1 = wordnet.synset('run.v.01') 
w2 = wordnet.synset('sprint.v.01') 
print("The confidence in similarity is {}".format(w1.wup_similarity(w2))) 