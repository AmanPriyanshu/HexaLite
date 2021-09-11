import PyPDF2
import os
from tqdm import trange

def get_text(path_in, path_out):
	pdfFileObj = open(path_in, 'rb') 
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
	count = 0
	for page_idx in trange(pdfReader.numPages, desc=path_in):
		path = path_out+'_page'+str(page_idx)+'.txt'
		if not os.path.exists(path):
			try:
				pageObj = pdfReader.getPage(page_idx)
				txt = pageObj.extractText()
				if len(txt)>10:
					with open(path, 'w', encoding='utf-8') as f:
						f.write(txt)
			except:
				count+=1
				continue
	pdfFileObj.close()
	if count>0:
		print("Couldn't map "+str(count)+' page/(s)')

def build_dir_tree():
	path_in = './data/pdfs/'
	path_out = './data/txts/'
	dirs = sorted([i for i in os.listdir(path_in) if '.' not in i])
	if not os.path.exists(path_out):
		print("Generating texts...")
		os.mkdir(path_out)
	for directory in dirs:
		if not os.path.exists(path_out+directory):
			os.mkdir(path_out+directory)

def extract():
	path_in = './data/pdfs/'
	path_out = './data/txts/'
	dirs = sorted([i for i in os.listdir(path_in) if '.' not in i])
	for directory in dirs:
		for pdf in sorted([i for i in os.listdir(path_in+directory)]):
			get_text(path_in+directory+'/'+pdf, path_out+directory+'/'+pdf[:-4])

if __name__ == '__main__':
	build_dir_tree()
	extract()