import re

str = r'.?ay/*?1/djd!@#$%^&*()_+/*-+'
punc = r'[?/\'\\+_!(@*#&$^%)-]'
print(re.sub(punc,"",str))
	