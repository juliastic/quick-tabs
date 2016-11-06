import webbrowser, time, sys, argparse, os

parser = argparse.ArgumentParser()    
parser.add_argument('file')

args = parser.parse_args()  
file = args.file
if os.stat(file).st_size == 0:
	sys.exit('Cannot parse empty text file')

with open(file) as url_file:
    urls = [line.strip() for line in url_file]
webbrowser.open(urls[0])
time.sleep(1)
for url in urls[1:]:
    webbrowser.open_new_tab(url)