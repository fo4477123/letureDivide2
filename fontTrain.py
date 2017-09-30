import jieba
import jieba.analyse
import logging

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # jieba custom setting.
    jieba.set_dictionary('jieba_dict/dict.txt')

    # load stopwords set
    stopwordset = set()
    with open('jieba_dict/stopwords.txt','r',encoding='utf-8') as sw:
        for line in sw:
            stopwordset.add(line.strip('\n'))

    #output = open('wiki_seg2.txt','w', encoding = 'utf8')
    tdidf= open('tdidftxt.txt','w', encoding = 'utf8')
    texts_num = 0
    jieba.enable_parallel(12)
   # with open('wiki_texts.txt','r', encoding = 'utf8') as content :
    #    for line in content:
    #        
    #        words = jieba.cut(line, cut_all=False)
    #        for word in words:
    #            if word not in stopwordset:
    #                output.write(word +' ')
    #        texts_num += 1
    #        if texts_num % 10000 == 0:
    #            logging.info("已完成前 %d 行的斷詞" % texts_num)
    #output.close()
    content = open('wiki_texts.txt','r', encoding = 'utf8')
    try:
        print("Ready caculate")
        idf = jieba.analyse.textrank(content.read(), topK=270132, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
        print("End caculate")
        tdidf.write(idf)
        logging.info("已完成前行的斷詞")
    except:        
        print("12348")
if __name__ == '__main__':
	main()