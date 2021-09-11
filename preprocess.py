from extract_text import build_dir_tree, extract
from generate_vocab import extract_vocab
from generate_embeds import extract_bog

def main():
	build_dir_tree()
	extract()
	extract_vocab()
	extract_bog()

if __name__ == '__main__':
	main()