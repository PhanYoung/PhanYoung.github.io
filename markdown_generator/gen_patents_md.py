#### config #####

bold_name = '杨帆'

#################



import pandas as pd

template = \
'''---
title: "{title}"
collection: patents
permalink: /patents/{file}
excerpt: '{excerpt}'
date: {date}
venue: '{SN}, CN'
paperurl: 'http://phanyoung.github.io/files/{SN_}.pdf'
citation: '{AUTHOR}. {title}: 中国, {SN} [P]. {date}.'
---

**专利号**：{SN}  
**申请日**：{date}  
**发明人**:  {AUTHOR}  
**摘要**： {abstract_zh}  
**Abstract**:  {abstract_en}  

* [在线阅读](http://www.soopat.com/Patent/{SN_p})  
* [专利下载](http://phanyoung.github.io/files/{SN_p}.pdf)
'''

content_keys = ['title', 'date', 'SN_', 'excerpt', 'SN', 'AUTHOR', 'abstract_zh', 'abstract_en', 'SN_p', 'file']


def gen_md(d):
    sn = d['SN']
    sn_p, sn_s = sn.split('.')
    d['SN_p'] = sn_p
    d['SN_'] = sn_p + '-' + sn_s
    d['file'] = d['date'] + '-' + d['SN_']
    authors = d['author'].strip()
    d['AUTHOR'] = authors.replace(' ', ',').replace(bold_name, '<b>'+bold_name+'</b>')
    content = {k: d[k] for k in content_keys}
    return template.format(**content), d['file']


def gen_md_files(df, path=''):
    for _, d in df.iterrows():
        try:
            md_str, filename = gen_md(d)
            with open(path+filename+'.md', 'w') as f:
                f.write(md_str)
        except:
            contnue


import sys
if __name__ == '__main__':
    if len(sys.argv) < 2:
       exit() 
    pd.read_csv(sys.argv[1], dtype=str)
    


