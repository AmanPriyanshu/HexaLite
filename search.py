import pickle
import numpy as np
from generate_embeds import bag_of_words, load
import re
import pandas as pd

def one_hot(bog, directory):
	vocab_shape = pd.read_csv('./vocab/Vocab_'+directory+'.csv')
	vocab_shape = vocab_shape.values
	enc = np.zeros(len(vocab_shape))
	enc[bog] += 1
	return enc

def main(directory, txt):
	txt = ''.join([i if i.isalpha() else ' ' for i in txt])
	txt = re.sub("\s\s+" , " ", txt.lower())
	bog = bag_of_words(txt, directory)
	enc = one_hot(bog, directory)
	details = load('./embeds/'+directory+'.pt')
	bog_enc = np.stack([one_hot(bog, directory) for bog in details['BOG']])
	t = np.stack([np.linalg.norm(bog) for bog in bog_enc])
	cosine = np.dot(enc, bog_enc.T)/(np.linalg.norm(enc)*t)
	indexes = np.argsort(cosine)[::-1]
	paths = np.array(details['PATH'])
	paths = paths[indexes]
	paths = paths[:5]
	return paths

if __name__ == '__main__':
	directory = input("Enter Topic: ")
	path = input("Enter Path: ")
	with open(path, 'r', encoding='utf-8') as f:
		txt = ' '.join([i.strip().replace('\n', ' ') for i in f.readlines()])
	paths = main(directory, txt)
	print(paths)