#using regex
import re
a = "dfgkjd# dkl# fd.fd fdg"
res = re.sub(r'\W+', "", a)
#or
res = re.sub(r'[^a-zA-Z0-9]', '', a)
#or
pattern = re.compile('\W')
res = re.sub(pattern, '', a)

#using alnum  function
res = ''.join(filter(str.isalnum, a))
res = ''.join(c for c in a if c.isalnum())
