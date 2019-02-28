import io
import random
from  PIL import  Image,ImageDraw,ImageFont
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,'index.html')


def basedemo(request):
    return render(request,'basedemo.html',
                  context={'name':'张三','age':18,'height':175,'score':[70,90,100],
                                        'username':'zyz','scoredir':['语文:99','数学:85','英语:72'],
                                        'names':['张三','李四','王五','赵六','孙七'],'title':'Hello Django'})


def includedemo(request):
    goods_list = ['iPhone','iPad','Mac','Watch']
    return render(request,'includedemo.html',context={'goods_list':goods_list})


def home(request):

    temp = 'H<sub2></sub>0'

    return render(request,'home.html',context={'temp':temp})


def cart(request):
    return render(request,'cart.html')


def mine(request):
    return render(request,'mine.html')


def login(request):
    random_str = str(random.randrange(1000,10000))

    return render(request,'login.html',context={'random_str':random_str})


def loginview(request):
    return HttpResponse('正在登录....')


def verifycode(request):
    # 定义图片颜色
    bgcolor = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))


    width = 120
    height = 40
    # 创建图片
    image = Image.new('RGB',(width,height),bgcolor)


    # 创建画笔
    draw = ImageDraw.Draw(image)


    # 释放画笔
    del draw

    # 随机数生成
    temp = '1234567890qwertyuiopasdfghjklzxcvbnm'
    random_str = ''
    for i in  range(0,4):
        random_str += [random.randrange(0,len(temp))]


    # 字体类型


    # 字体颜色




    # 字体位置


    # 文件操作
    buff = io.BytesIO()
    image.save(buff,'png')

    # 返回图片
    return  HttpResponse(buff.getvalue()),