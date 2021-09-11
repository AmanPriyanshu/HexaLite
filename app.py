import streamlit as st
import os
from search import main as search

def generate_urls(arr):
	urls, pages, base_urls = [], [], []
	for path in arr:
		url = path.replace('./data/txts', './data/pdfs')
		index = url.index('_page')
		page = str(int(url[index+5:-4])+1)
		pages.append(page)
		base_path = os.getcwd()
		base_path = 'file:///'+base_path.replace(' ', '%20').replace('\\', '/')
		url = url[:index]+'.pdf'+"#page="+page
		base_urls.append(url[1:])
		url = base_path+url[1:]
		urls.append(url)
	return urls, pages, base_urls

def app():
	extension = "https://github.com/AmanPriyanshu/HexaLite/blob/IT"
	st.title("IT - Book Searcher")
	topic = st.text_input("Enter Topic")
	txt = st.text_area('Enter text', height=275)
	if len(txt)!=0 and len(topic)!=0 and st.button("SEARCH"):
		paths = search(topic, txt)
		urls, pages, base_urls = generate_urls(paths)
		for i, (book, page) in enumerate(zip(base_urls, pages)):
			st.markdown("[Book: "+book[book.rindex('/')+1:book.index('.pdf')]+", Page: "+str(page)+"]("+extension+book+")")
		st.markdown("## If you're running Local Machine please copy the path below and remove the quotes, these are the generated links, which will open the pdf at the exact path.")
		st.write(urls)
if __name__ == '__main__':
	app()