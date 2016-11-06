import webbrowser, time, sys, argparse, os, re

parser = argparse.ArgumentParser()    
parser.add_argument('file')

args = parser.parse_args()  
file = args.file
if os.stat(file).st_size == 0:
	sys.exit('Cannot parse empty text file')

with open(file) as url_file:
    urls = [line.strip() for line in url_file]

urls = [url for url in urls]
for url in urls:
	try:
		url = re.search("(?P<url>https?://[^\s]+)", url).group("url")
		webbrowser.open_new_tab(url)
		time.sleep(1)
	except:
		pass