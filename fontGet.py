# -*- coding: utf-8 -*-
import logging
import sys
import SQLAcess
import re

def main():
    newscontent = []
    sql = "select * from wordpress.googlenews "
    result = SQLAcess.GetData(sql)
    for row in result:
        newscontent.append(row['newscontent'])
    #if len(sys.argv) != 2:
     #   print("Usage: python3 " + sys.argv[0] + " wiki_data_path")
      #  exit()

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #wiki_corpus = WikiCorpus(sys.argv[1], dictionary={})
    
    texts_num = 0
    
    with open("wiki_texts.txt",'w',encoding='utf-8') as output:
        for text in newscontent:
            text = re.sub(r"[a-zA-Z<></>0-9&;=._?:()-]", "", text)
            output.write(' '.join(text) + '\n')
            texts_num += 1
            if texts_num % 10000 == 0:
                logging.info("已處理 %d 篇文章" % texts_num)
if __name__ == "__main__":
    main()