import jieba
import jieba.analyse
txt = open(r"./leture/test.txt", mode='r')
print("12345")

#testmatrix = jieba.cut(txt.read(),cut_all=False)

#print("Default Mode: " + "/ ".join(testmatrix))


testFeature = jieba.analyse.extract_tags(txt.read())
print("Default Mode: " + "/ ".join(testFeature))