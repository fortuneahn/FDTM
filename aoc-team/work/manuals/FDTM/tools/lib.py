import re,html
PAT=re.compile(r'<w:p(?:\s[^>]*)?/>|<w:p(?:\s[^>]*)?>.*?</w:p>',re.S)
def load(path):
    s=open(path,encoding='utf8').read()
    ps=[];gaps=[];pos=0
    for m in PAT.finditer(s):
        gaps.append(s[pos:m.start()]);ps.append(m.group(0));pos=m.end()
    tail=s[pos:]
    return gaps,ps,tail
def ptext(p):
    return html.unescape(''.join(re.findall(r'<w:t(?:\s[^>]*)?>(.*?)</w:t>',p,re.S)))
def in_table(gaps):
    # track tc depth through gaps+paras sequence
    return None
