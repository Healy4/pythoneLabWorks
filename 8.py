import re


def main(source):
    p = r"(\s*define\s@'([A-Za-z0-9-_]*).\s*..\s*#([0-9-]*))"
    matches = re.findall(p, source)
    response = {}
    for match in matches:
        response[match[1]] = match[2]
    return response
    
str = "define @'esenle_514' <= #1922 define @'zavele_925'<= #-8360 define @'lama_7' <= #-9385 define @'inre_98' <=#392"

print(main(str))