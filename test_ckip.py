# -*- coding: utf-8 -*-
from ckiptagger import WS, POS, NER

text = '傅達仁今將執行安樂死，卻突然爆出自己20年前遭緯來體育台封殺，他不懂自己哪裡得罪到電視台。'
ws = WS("./data")
pos = POS("./data")
ner = NER("./data")

ws_results = ws([text])
pos_results = pos(ws_results)
ner_results = ner(ws_results, pos_results)

print(ws_results)
print(pos_results)
for name in ner_results[0]:
    print(name)
    

chinese_function_words = set([
    "的", "地", "得", "而", "了", "於", "與", "也", "就", "及",
    "並", "但", "或", "因", "若", "如", "之", "所", "又", "雖",
    "卻", "即", "即使", "雖然", "然而", "的話", "則", "除非", "除了",
    "為了", "如何", "為何", "既", "既然", "那", "那麼", "還是", "是否",
    "對於", "對", "把", "從", "由", "至", "無", "只", "只有", "只要",
    "只是", "要是", "若是", "除非", "才", "總之", "否則", "儘管",
    "還", "當", "像", "便", "這", "那", "這些", "那些", "不但", "不僅",
    "甚至", "即便", "而且", "連", "都", "要麼", "再", "另", "另外", "如此",
    "即使", "如果", "便是", "儘管如此", "不過", "儘管", "即或", "即若", "縱使", "假如", "假若", "假使",
    "除非", "除了", "除此之外", "卻", "然而", "但是", "即便如此", "固然", "可是", "儘如", "如",
    "如同", "如下", "若", "若是", "若非", "不如", "猶如", "就像", "一般", "例如", "哪怕", "要不是", "要不然",
    "要是", "要么", "似乎", "大約", "就是說", "幾乎", "特別是", "相對", "關於", "只是", "然後", "之後", "其次",
    "首先", "是不是", "是因為", "那麼", "是否", "就是", "即是", "或者", "或是", "基本上", "基於", "有的是", "總的來說",
    "總的來看", "按照", "根據", "依據", "基於", "關於", "對於", "至於", "就是", "也就是", "即是", "也就是說", "那就是說",
    "也是", "也就是說", "畢竟", "最後", "總之", "總而言之", "一來", "二來", "不單", "不只", "不僅僅", "不僅如此", "不只是"
])

['FW', 'Na', 'Na', 'VG', 'Nb', 'Na', 'VG', 'FW', 'Na', 'COLONCATEGORY', 'Na', 'Na', 'Neu', 'Na', 'COLONCATEGORY', 'Nd', 'FW', 'Nd', 'WHITESPACE', 'P', 'Nc', 'VD', 'Na', 'COLONCATEGORY', 'Nc', 'Nc', 'Nc', 'Nc', 'Nc', 'WHITESPACE', 'Na', 'Na', 'COLONCATEGORY', 'FW', 'Neu', 'WHITESPACE', 'Na', 'Na', 'P', 'VE', 'VC', 'Neu', 'Na', 'PERIODCATEGORY', 'WHITESPACE', 'P', 'VE', 'PARENTHESISCATEGORY', 'Na', 'VHC', 'PARENTHESISCATEGORY', 'Ng', 'COMMACATEGORY', 'Nep', 'Na', 'VC', 'COMMACATEGORY', 'Cbb', 'VG', 'Na', 'PERIODCATEGORY', 'WHITESPACE', 'Nep', 'Na', 'Na', 'Caa', 'D', 'VC', 'Na', 'D', 'VC', 'VK', 'COLONCATEGORY', 'WHITESPACE', 'Na', 'Na', 'COLONCATEGORY', 'WHITESPACE', 'Na', 'FW', 'P', 'Nd', 'Nd', 'Nd', 'Nd', 'Nd', 'Ng', 'COMMACATEGORY', 'P', 'Neu', 'Nc', 'VCL', 'Nc', 'Nc', 'Nc', 'Nc', 'Nc', 'DE', 'Nb', 'Nc', 'Ncd', 'COMMACATEGORY', 'P', 'Na', 'Nb', 'D', 'VK', 'Ng', 'COMMACATEGORY', 'D', 'VC', 'Neu', 'Nf', 'FW', 'FW', 'Na', 'VG', 'Neu', 'Nf', 'Na', 'PAUSECATEGORY', 'Neu', 'Nf', 'Na', 'VG', 'Neu', 'Nf', 'DE', 'FW', 'Na', 'PAUSECATEGORY', 'Neu', 'Nf', 'Na', 'VG', 'Da', 'Neu', 'Nf', 'DE', 'FW', 'Nc', 'Na', 'COMMACATEGORY', 'A', 'VB', 'PAUSECATEGORY', 'VK', 'VD', 'PERIODCATEGORY', 'P', 'VC', 'Neqa', 'Na', 'Ng', 'COMMACATEGORY', 'Na', 'P', 'Nep', 'VCL', 'Na', 'Caa', 'Na', 'Na', 'Ng', 'COMMACATEGORY', 'D', 'VC', 'Nes', 'Nc', 'COMMACATEGORY', 'D', 'VA', 'PERIODCATEGORY', 'Na', 'Nb', 'VE', 'Ncd', 'Na', 'Ng', 'COMMACATEGORY', 'VC', 'Nc', 'Ncd', 'COMMACATEGORY', 'P', 'Na', 'VA', 'P', 'Na', 'PAUSECATEGORY', 'Cbb', 'VA', 'PERIODCATEGORY', 'Ncd', 'Na', 'P', 'VE', 'VH', 'PERIODCATEGORY', 'FW', 'FW', 'Nc', 'Nc', 'Na', 'Nc', 'Na', 'Nv', 'WHITESPACE', 'Nd', 'VH', 'Nes', 'Na', 'Neu', 'Na', 'P', 'VC', 'FW', 'COMMACATEGORY', 'FW', 'PARENTHESISCATEGORY', 'Na', 'Na', 'COLONCATEGORY', 'Nb', 'PARENTHESISCATEGORY', 'WHITESPACE', 'WHITESPACE', 'A', 'Na', 'DE', 'A', 'VH', 'WHITESPACE', 'PARENTHESISCATEGORY', 'FW', 'PARENTHESISCATEGORY', 'Na', 'COMMACATEGORY', 'Nes', 'Nc', 'VE', 'VG', 'Ncd', 'COLONCATEGORY', 'WHITESPACE', 'Na', 'Na', 'FW', 'FW', 'FW', 'VJ', 'Nd', 'COMMACATEGORY', 'Cbb', 'D', 'P', 'VE', 'VK', 'Nc', 'DE', 'Nd', 'Ng', 'VC', 'Nf', 'Na', 'Ng', 'COMMACATEGORY', 'P', 'Nc', 'VD', 'Na', 'Neu', 'Nf', 'COMMACATEGORY', 'Cbb', 'D', 'P', 'Na', 'Ncd', 'P', 'Na', 'VE', 'DE', 'Na', 'Na', 'PARENTHESISCATEGORY', 'FW', 'FW', 'PARENTHESISCATEGORY', 'PAUSECATEGORY', 'Na', 'Na', 'WHITESPACE', 'PARENTHESISCATEGORY', 'FW', 'PARENTHESISCATEGORY', 'PAUSECATEGORY', 'Na', 'Na', 'PARENTHESISCATEGORY', 'FW', 'FW', 'PARENTHESISCATEGORY', 'PAUSECATEGORY', 'Nc', 'Caa', 'Neqa', 'VJ', 'Na', 'Na', 'DE', 'Na', 'Caa', 'Na', 'PARENTHESISCATEGORY', 'FW', 'PARENTHESISCATEGORY', 'VD', 'VC', 'Na', 'DE', 'Na', 'Na', 'PERIODCATEGORY', 'WHITESPACE', 'WHITESPACE', 'Na', 'WHITESPACE', 'VH', 'FW', 'Neu', 'PAUSECATEGORY', 'FW', 'FW', 'P', 'Nd', 'Nd', 'Nd', 'Nd', 'Nd', 'Nd', 'Nd', 'Neqb', 'Ng', 'P', 'Nes', 'Nf', 'Na', 'Nd', 'Nd', 'Nd', 'Ng', 'VA', 'COMMACATEGORY', 'P', 'Nc', 'Nc', 'PARENTHESISCATEGORY', 'Na', 'FW', 'PARENTHESISCATEGORY', 'Nc', 'Ncd', 'COMMACATEGORY', 'P', 'Na', 'VC', 'Na', 'Neu', 'Caa', 'Na', 'Ng', 'COMMACATEGORY', 'D', 'P', 'A', 'VH', 'DE', 'Na', 'COMMACATEGORY', 'P', 'Nd', 'Nd', 'Nd', 'Nd', 'Nd', 'Nd', 'Ng', 'Nes', 'Nf', 'Neqb', 'COMMACATEGORY', 'P', 'Nes', 'Nc', 'VC', 'Nep', 'Neqa', 'Na', 'Na', 'Nb', 'Na', 'VA', 'D', 'P', 'Nd', 'Nd', 'Nd', 'Nd', 'Nd', 'Nd', 'COMMACATEGORY', 'P', 'Nc', 'FW', 'FW', 'Nc', 'Nc', 'Nc', 'Nc', 'Ncd', 'P', 'Na', 'VC', 'COMMACATEGORY', 'Cbb', 'P', 'Nes', 'Nf', 'Nd', 'Nd', 'Nd', 'P', 'VE', 'COMMACATEGORY', 'Nep', 'VA', 'D', 'VC', 'Na', 'Na', 'VJ', 'Nes', 'Nf', 'Neu', 'Nf', 'COMMACATEGORY', 'D', 'VK', 'Na', 'PERIODCATEGORY', 'WHITESPACE', 'Neu', 'PAUSECATEGORY', 'Na', 'P', 'Nc', 'Na', 'Nc', 'PARENTHESISCATEGORY', 'FW', 'FW', 'FW', 'FW', 'PARENTHESISCATEGORY', 'Nc', 'Nc', 'Na', 'PAUSECATEGORY', 'Nc', 'Nc', 'Na', 'Nc', 'Nc', 'Na', 'VC', 'Ng', 'COMMACATEGORY', 'VF', 'PARENTHESISCATEGORY', 'FW', 'PARENTHESISCATEGORY', 'VH', 'VE', 'PARENTHESISCATEGORY', 'FW', 'FW', 'PARENTHESISCATEGORY', 'VB', 'PERIODCATEGORY', 'FW']