import re

text = "PO_VA aboba abb aroma_aob Fele"
text3 = "there_is_example"


text2 = "a special.text b lkdfjgkld,b"


x = re.search("a[b].*", text)
print(x)

z = re.search("a[b]{2,3}", text)
print(z)


#3
c = re.findall("[a-z]+_[a-z]+$", text)
print(c)

#4
v = re.findall("[A-Z][a-z]+", text)
print(v)

#5
b = re.search(r"[a].*[b]$", text2)
print(b)

#6
n = re.sub(r"[ ,.]", ":", text2)
print(n)


#7
def snake_to_camel_case(snake_str):
    components = snake_str.split('_')

    if components:
        camel_case_str = components[0] + ''.join(x.title() for x in components[1:])
    else:
        camel_case_str = ''
    return camel_case_str

string = "i_am_so_in_love"
camel_case = snake_to_camel_case(string)
print(camel_case)



#8
def split_at_uppercase(s):
    return re.findall('[A-Z][^A-Z]*', s)
print(split_at_uppercase("BeBaDoBeBB"))

#9
def insert_spaces(s):
    return re.sub(r'(?<=[a-zA-Z])(?=[A-Z])', ' ', s)
print(insert_spaces("IAmYoung"))

#10
def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
print(camel_to_snake("iAmSoInLove"))
