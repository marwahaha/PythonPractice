from difflib import SequenceMatcher

s = SequenceMatcher(None, "5b2e5368656c6c436c617373496e666f5d0d0a", "fffe5b003000780030003400300033005d000d")
t = s.get_matching_blocks()
j = str(t[0])
print(j)