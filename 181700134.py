#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import re

mapzzq=['内蒙古','新疆','广西','宁夏','西藏']
mapzzz=['凉山彝族','甘孜藏族','阿坝藏族羌族','果洛藏族','海南藏族','黄南藏族','海北藏族',
        '玉树藏族','海西蒙古族藏族','迪庆藏族','甘南藏族','延边朝鲜族','黔南布依族苗族',
        '黔东南苗族侗族','黔西南布依族苗族','恩施土家族苗族','湘西土家族苗族','西双版纳傣族',
        '文山壮族苗族','德宏傣族景颇族','楚雄彝族','红河哈尼族彝族','怒江傈僳族','大理白族',
        '临夏回族','伊犁哈萨克','博尔塔拉蒙古','巴音郭楞蒙古','克孜勒苏柯尔克孜','昌吉回族']
mapdiqu=['铜仁','毕节','海东','大兴安岭','和田','喀什','哈密','阿勒泰','阿克苏',
         '吐鲁番','塔城','山南','林芝','日喀则','阿里','那曲','昌都']
mapshi=['常州','连云港','泰州','南京','扬州','镇江','宿迁','盐城','徐州','南通','淮安','无锡',
        '苏州','湖州','杭州','舟山','嘉兴','衢州','金华','宁波','台州','绍兴','广元','绵阳',
        '资阳','巴中','德阳','眉山','成都','乐山','内江','自贡','攀枝花','达州','宜宾','泸州',
        '遂宁','雅安','南充','广安','赣州','上饶','宜春','抚州','新余','吉安','南昌','鹰潭',
        '景德镇','九江','萍乡','宁德','三明','福州','南平','龙岩','莆田','泉州','漳州','西宁',
        '辽源','白城','四平','长春','通化','吉林','白山','松原','六盘水','贵阳','遵义','安顺',
        '西安','延安','汉中','宝鸡','榆林','渭南','咸阳','安康','铜川','商洛','晋城','晋中',
        '阳泉','忻州','朔州','大同','运城','太原','吕梁','临汾','长治','廊坊','衡水','邢台',
        '石家庄','沧州','保定','邯郸','张家口','承德','唐山','秦皇岛','荆门','十堰','荆州',
        '随州','黄冈','咸宁','宜昌','襄樊','孝感','黄石','营口','沈阳','辽阳','大连','朝阳',
        '抚顺','本溪','鞍山','葫芦岛','盘锦','丹东','锦州','阜新','铁岭','怀化','长沙','常德',
        '岳阳','株洲','张家界','湘潭','益阳','娄底','衡阳','郴州','永州','邵阳','枣庄','德州',
        '济南','济宁','菏泽','滨州','烟台','潍坊','聊城','日照','泰安','东营','临沂','青岛',
        '威海','淄博','玉溪','曲靖','保山','昭通','普洱','昆明','丽江','临沧','新乡','驻马店',
        '南阳','漯河','安阳','平顶山','商丘','开封','郑州','濮阳','三门峡','周口','焦作','信阳',
        '许昌','洛阳','广州','湛江','汕尾','汕头','梅州','云浮','阳江','清远','茂名','揭阳',
        '惠州','潮州','河源','韶关','肇庆','江门','六安','淮南','铜陵','宣城','阜阳','宿州',
        '滁州','黄山','蚌埠','淮北','安庆','亳州','马鞍山','巢湖','芜湖','池州','合肥','白银',
        '陇南','金昌','兰州','武威','定西','酒泉','庆阳','天水','张掖','平凉','齐齐哈尔','鸡西',
        '黑河','佳木斯','哈尔滨','牡丹江','双鸭山','七台河','大庆','绥化','伊春','鹤岗','兴安盟',
        '呼伦贝尔','乌兰察布','巴彦淖尔','鄂尔多斯','通辽','赤峰','呼和浩特','包头','乌鲁木齐',
        '贵港','河池','贺州','柳州','北海','玉林','桂林','百色','钦州','梧州','来宾','崇左',
        '南宁','防城港','石嘴山','中卫','吴忠','固原','银川','拉萨',]
#1!张三,福建福州闽13599622362侯县上街镇福州大学10#111.
#2!李四,福建省福州13756899511市鼓楼区鼓西街道湖滨路110号湖滨大厦一层.
#2!寿佳,湖南省益阳市赫山13221817716区龙岭工业园春嘉路6号
################省##################
def Sheng(string):
    sheng=re.search(("(.*?省)|(.*?自治区)|上海市|北京市|天津市|重庆市|黑龙江"),string)
    if(sheng!=None):
        #print(sheng.group(0))
        return sheng.group(0)
    else:
        for a in mapzzq:
            if(string[0:2] in a):
                return a
            elif(string[0:3] in a):
                return a
        return string[0:2]

################市##################
def Shi(string):
    global zzz
    global dq
    global si
    shi=re.search("(.*?自治州)|(.*?[市])|(.*?地区)|(.*?[盟])",string)
    if(shi!=None):
        return shi.group(0)
    else:
        for a in mapshi:
            if(string[0:2] in a):
                si=1
                return a
            elif(string[0:3] in a):
                si=1
                return a
        for a in mapdiqu:
            if(string[0:2] in a):
                dq=1
                return a
            elif(string[0:3] in a):
                dq=1
                return a
            elif(string[0:4] in a):
                dq=1
                return a
        for a in mapzzz:
            if(string[0:4] in a):
                zzz=1
                return a
            elif(string[0:5] in a):
                zzz=1
                return a
            elif(string[0:6] in a):
                zzz=1
                return a
            elif(string[0:7] in a):
                zzz=1
                return a
            elif(string[0:8] in a):
                zzz=1
                return a
        return ""

###############区##################
def Qu(string):
    qu = re.search("(.*?旗)|(.*?区)|(.*?县)|(.*?市)",string)
    if(qu!=None):
        return qu.group(0)
    else:
        return ""

################街##################
def Jie(string):
    jie=re.search("(.*?街道)|(.*?镇)|(.*?乡)|(.*?园)",string)
    if(jie!=None):
        return jie.group(0)
    else:
        return ""

################路#################
def Lu(string):
    lu = re.search("(.*?路)|(.*?街)|(.*?巷)|(.*?道)",string)
    if(lu!=None):
        return lu.group(0)
    else:
        return ""

###############门牌号#################
def Meng(string):
    meng=re.search("(.*?号)|(.*?楼)",string)
    if(meng!=None):
        return meng.group(0)
    else:
        return ""

#############主############
string=input()
zzz=0
dq=0
si=0
level = string[0]
name=re.split(r'[!,]',string)
#print(name)
num=re.split(r'(1\d{10})',name[2])
#print(num)
add=num[0]+num[2]

################省##################
sheng=Sheng(add)
if (sheng=="北京" or sheng=="上海" or sheng=="重庆" or sheng=="天津"):
    add = add.replace(sheng,sheng+"市",1)
elif(sheng=="北京市" or sheng=="上海市" or sheng=="重庆市"or sheng=="天津市"):
    sheng=sheng[0:2]
elif(sheng[-1]!="省" and sheng[-1]!="区"):
    if(sheng!='内蒙古' and sheng!='新疆' and sheng!='广西' and sheng!='宁夏' and sheng!='西藏'):
        add = add.replace(sheng, '', 1)
        sheng=sheng + "省"
    else:
        if(sheng=='内蒙古'or sheng=='西藏'):
            add=add.replace(sheng,'',1)
            sheng=sheng+"自治区"
        elif(sheng=='新疆'):
            add=add.replace(sheng,'',1)
            sheng=sheng+"维吾尔自治区"
        elif(sheng=='广西'):
            add=add.replace(sheng,'',1)
            sheng=sheng+"壮族自治区"
        elif(sheng=='宁夏'):
            add=add.replace(sheng,'',1)
            sheng=sheng+"回族自治区"
else:
    add=add.replace(sheng,"",1)
#print(sheng)

###############市#################
shi=Shi(add)
#print(add)
if(shi==""):
    add = add.replace(shi, "", 1)
elif(shi[-1]!='洲' and shi[-1]!='市' and shi[-1]!='区' and shi[-1]!='盟'):
    add=add.replace(shi,"",1)
    if (si==1):
        shi=shi+"市"
    elif(dq==1):
        shi=shi+"地区"
    elif(zzz==1):
        shi=shi+"自治州"
else:
    add=add.replace(shi,"",1)
#print(shi)

###############区#################
#print(add)
qu = Qu(add)
#print(qu)
if(qu!=""):
    add=add.replace(qu,"",1)

###############街################
jie = Jie(add)
if(jie!=""):
    add=add.replace(jie,"", 1)
add=add.replace('.','')
add1=add
###############路################
lu=Lu(add)
if(lu!=""):
    add=add.replace(lu,"",1)

##############门牌号###############
meng = Meng(add)
if(meng!=""):
    add=add.replace(meng, "", 1)


d={}
d["姓名"]=name[1]
d["手机"]=num[1]
ad=[]
if(level=='1'):
    ad.append(sheng)
    ad.append(shi)
    ad.append(qu)
    ad.append(jie)
    ad.append(add1)
else:
    ad.append(sheng)
    ad.append(shi)
    ad.append(qu)
    ad.append(jie)
    ad.append(lu)
    ad.append(meng)
    ad.append(add)
d["地址"]=ad
#print(d)
json=json.dumps(d,ensure_ascii=False,indent=4)
print (json)
