from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print( tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])
    
    
        
n = int(input())
parser = MyHTMLParser()
for _ in range(n):
    code = input()
    parser.feed(code)