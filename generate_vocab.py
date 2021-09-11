import os
from tqdm import tqdm
import re
import numpy as np
import pandas as pd

def extract_vocab(n_low=2, n_high=50):
	path = './data/txts/'
	dirs = sorted([i for i in os.listdir(path) if '.' not in i])
	for directory in dirs:
		vocab = {}
		for txt_path in tqdm(sorted([path+directory+'/'+i for i in os.listdir(path+directory)]), desc=path+directory):
			with open(txt_path, 'r', encoding='utf-8') as f:
				txt = ' '.join([i.strip().replace('\n', ' ') for i in f.readlines()])
				txt = ''.join([i if i.isalpha() else ' ' for i in txt])
				txt = re.sub("\s\s+" , " ", txt.lower())
			for word in txt.split():
				if word not in list(vocab.keys()):
					vocab.update({word:1})
				else:
					vocab[word] += 1
		all_words = list(vocab.keys())
		for word in all_words:
			if vocab[word]>n_high or vocab[word]<n_low:
				vocab.pop(word)
		vocab = pd.DataFrame({'word':[i for i in vocab.keys()], 'n':[i for i in vocab.values()]})
		vocab.to_csv('./vocab/Vocab_'+str(directory)+'.csv', index=False)

if __name__ == '__main__':
	extract_vocab()