# encoding: utf-8
"""
@version: 1.0
@author: Jarrett
@file: run_word_cloud
@time: 2020/3/20 18:17
"""
import jieba
import codecs
import re
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt

filename = "./mytxtfile.txt"
f = codecs.open(filename,encoding='UTF-8')
mytxt = f.read()
f.close()

mytxt = re.sub(r"\d","",mytxt)
mytxt = re.sub(r"、","",mytxt)

mytxt_list = jieba.cut(mytxt)

print(mytxt_list)
ljr_list = list(mytxt_list)
list_set = set(ljr_list) #新建另外一个
item_count = {}
for item in list_set:
    #print(f"{item}:{ljr_list.count(item)}")
    item_count[item] = [ljr_list.count(item)]

dic = sorted(item_count.items(), key = lambda item:item[1])
print(dic)

mytxt = " ".join(mytxt_list)
#print(mytxt)

font_path="msyh.ttc"
wc = WordCloud(
    font_path=font_path,
    background_color='white',  # 背景色
    #mask=image,  # 背景图
    #stopwords=STOPWORDS,  # 设置停用词
    max_words=100,  # 设置最大文字数
    max_font_size=100,  # 设置最大字体
    width=800,
    height=1000,
)

# 生成词云
#image_colors = ImageColorGenerator()
wc.generate(mytxt)
print(wc)

# 使用matplotlib,显示词云图
plt.imshow(wc)  # 显示词云图
plt.axis('off')  # 关闭坐标轴
plt.show()
# 保存图片
wc.to_file('news.png')
