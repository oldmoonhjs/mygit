import sys
import os

class inv(object):										#声明类
 def __init__(self,input_keyword,input_voice,input_photo):
  self.keyword = input_keyword
  self.voice = input_voice
  self.photo = input_photo


url = "F:\\a";											#文件夹根目录

objectlist = os.listdir(url);							#读取目录名

dic = {};

for n in objectlist:									#产生多少个对象进入字典
 name = n;
 keywordurl = url+"\\"+n+"\\"+"keyword.txt";
 keyfile = open(keywordurl,'r');
 keyword = keyfile.read();								#对象中的keyword即为目录下文档中的内容
 voice = url+"\\"+n+"\\"+"voice.wav";
 photo = url+"\\"+n+"\\"+"photo.jpg";
 n = inv(keyword,voice,photo);
 dic[name] = n;


#test
for k in dic:
	print dic[k].keyword +"  "+ dic[k].voice +"  "+ dic[k].photo;





