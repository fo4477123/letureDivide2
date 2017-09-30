import csv
import SQLAcess
import jieba
import jieba.analyse

stockname = [];newsDate=[];newsSource=[];newsauthor=[];
newsUrl=[];newsTitle=[];newsDescript=[];newscontent=[]

#請使用者輸入 股號
print("請輸入有興趣之股號")
stockNo = "2356"

#請使用者輸入欲查詢之日期
print("請輸入有興趣之日期")

#請使用者輸入欲查詢之日期
print("請輸入有興趣之日期2")

sql = "select * from wordpress.googlenews where stockname like '%"+stockNo+"%' and newsDate between '2017-07-01' and '2017-08-15' order by newsDate  "

result = SQLAcess.GetData(sql)
for row in result:
    stockname.append(row['stockname'])
    #newsDate.append(row['newsDate'])
    newsSource.append(row['newsSource'])
    newsauthor.append(row['newsauthor'])
    newsUrl.append(row['newsUrl'])
    newsTitle.append(row['newsTitle'])
    newsDescript.append(row['newsDescript'])
    newscontent.append(row['newscontent'])


#做詞句分析
if len(stockname) < 1 :
    print("there no data to analyze")
else :
    keywordList = []
    with open('keywords.csv', newline='', encoding = 'utf-8') as f:		
	reader = csv.reader(f)			
	for row in reader:
		if row == []:
			continue					
		keyword = str(row[0])
				
		try:
			jieba.suggest_freq(keyword, True)
			keywordList.append(keyword)
		except:
			print(keyword)
    #設定停止辭庫
    #jieba.analyse.set_stop_words(file_name)
    stpwrdpath = "Dictionary\stop_words.txt"
    stpwrd_dic = open(stpwrdpath, 'rb')
    stpwrd_content = stpwrd_dic.read()
    #将停用词表转换为list  
    stpwrdlst = stpwrd_content.splitlines()
    stpwrd_dic.close()

    for index in range(len(stockname)):        
        testFeatureTFIFD = jieba.analyse.extract_tags(newscontent[index], topK=50, withWeight=True, allowPOS=())
        
        testFeatureTextRank = jieba.analyse.textrank(newscontent[index], topK=50, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
        print("Default Mode: " + "/ ".join(testFeatureTFIFD))


