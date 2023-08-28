from difflib import SequenceMatcher

a = "미소식당"
b = "미소식당"

print(SequenceMatcher(None, a, b).ratio() * 100)