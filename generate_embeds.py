import pandas as pd
import numpy as np
import os
import re
from tqdm import tqdm
import pickle

def save(path, obj):
	dbfile = open(path, 'ab')
	pickle.dump(obj, dbfile)                     
	dbfile.close()

def load(path):
	dbfile = open(path, 'rb')
	return pickle.load(dbfile)

def generate_dir_tree():
	path = './data/txts/'
	dirs = sorted([i for i in os.listdir(path) if '.' not in i])
	for directory in dirs:
		if not os.path.exists('./embeds/'+directory):
			os.mkdir('./embeds/'+directory)

def bag_of_words(txt, directory):
	df = pd.read_csv('./vocab/Vocab_'+str(directory)+'.csv')
	df = df.values
	words = df.T[0]
	words = [i for i in words]
	bog = [words.index(word) for word in txt.split() if word in words]
	return bog

def extract_bog():
	path = './data/txts/'
	dirs = sorted([i for i in os.listdir(path) if '.' not in i])
	for directory in dirs:
		bog = []
		bog_path = []
		for txt_path in tqdm(sorted([path+directory+'/'+i for i in os.listdir(path+directory)]), desc=path+directory):
			with open(txt_path, 'r', encoding='utf-8') as f:
				txt = ' '.join([i.strip().replace('\n', ' ') for i in f.readlines()])
				txt = ''.join([i if i.isalpha() else ' ' for i in txt])
				txt = re.sub("\s\s+" , " ", txt.lower())
				bog.append(bag_of_words(txt, directory))
				bog_path.append(txt_path)
		save('./embeds/'+directory+'.pt', {'BOG': bog, 'PATH': bog_path})

if __name__ == '__main__':
	extract_bog()