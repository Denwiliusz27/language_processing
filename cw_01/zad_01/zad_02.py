import re

if __name__ == '__main__':
    # otwarcie pliku xml
    f = open("370035.xml", "rt", encoding="utf8")

    # zamiana <ex>x</ex> na x
    pattern_ex = r'<ex>(.*?)<\/ex>'
    regex_ex = re.compile(pattern_ex, re.DOTALL)
    new_text = re.sub(pattern_ex, r'\1', f.read())

    # zamiana <expan>x</expan> na x
    pattern_expan = r'<expan>(.*?)<\/expan>'
    regex_expan = re.compile(pattern_expan, re.DOTALL)
    result = re.sub(pattern_expan, r'\1', new_text)

    print(result)

    output_f = open("zad_2_out.xml", "wt", encoding="utf8")
    output_f.write(result)
