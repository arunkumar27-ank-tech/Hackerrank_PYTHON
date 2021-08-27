import re
card_valid = r"^[456]\d{3}(-\d{4}){3}$|^[456]\d{15}$"
no_repeat = r'(\d)(-?\1){3}'
for _ in range(int(input())):
    card = input()
    print(f'{"Valid" if re.match(card_valid,card)and not re.search(no_repeat,card) else "InValid"}')