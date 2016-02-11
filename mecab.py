import MeCab

mt = MeCab.Tagger("-Ochasen")
print(mt.parse("本日は晴天なり。"))
