from html import parser
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data: str) -> None:
        
        if data!='\n':
            print('Data :', data)

    def handle_comment(self, data: str):
         if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
         else:
            print(">>> Single-line Comment")
            print(data)

n = int(input())
code = ''
for _ in range(n):
    code += input()
    code += '\n'
   
parser = MyHTMLParser()
parser.feed(code)
parser.close()