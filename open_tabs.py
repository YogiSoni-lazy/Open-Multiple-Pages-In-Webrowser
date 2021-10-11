import re
import webbrowser


l1 = ['2283291', '2196350', '2028420', '2336199', '2442967', '2364020']

for i in f1:
  caseid = re.sub('\s','',i)
  l1.append(caseid)
  
for i in l1:
  webbrowser.get(using='google-chrome').open('https://example.com/_ui/search/ui/UnifiedSearchResults?searchType=2&sen=500&str=' + i)
