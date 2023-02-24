from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('''
                        <button><a href="/about">About</a></button>
                        <button><a href="/youtube">Youtube</a><button>
                        ''')
def about(request):
    return HttpResponse('''<h1>You tube main page</h1>
                            <button><a href="/">back</a></button>''')
def youtube(request):
    return HttpResponse('''<h1>code with harry</h1>
                            <button><a href="/">back</a></button>''')


def removepunc(request):
    capture=request.GET.get('text','default')
    print(capture)
    return HttpResponse('response has been submitted')

def templates(request):
    # params={'name':'mohit','place':'Delhi','roll':'123'}
    return render(request,'index2.html')

def analyze(request):
    text=request.POST.get('text','Empty')
    checkbox=request.POST.get('check','off')
    uppercase=request.POST.get('case','off')
    new_line=request.POST.get('new_line','off')
    word_count=request.POST.get('word_count','off')\

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    status="ERROR!, please choose at least one option"

    analyze_text="";count=0;space=0

    if checkbox=="on":
        status=""
        for char in text:
            if char not in punctuations:
                analyze_text=analyze_text+char
    if uppercase=='on':
        status=""
        if len(analyze_text)!=0:
            analyze_text=analyze_text.upper()
        else:
            analyze_text=text.upper()
    if new_line=='on':
        status=""
        if len(analyze_text)!=0:
            new_text=""
            for char in analyze_text:
                if char!='\n' and char!='\r':
                    new_text=new_text+char
            analyze_text=new_text
        else:
            for char in text:
                if char!='\n' and char!='\r':
                    analyze_text=analyze_text+char
    if word_count=='on':
        if len(analyze_text)==0:
            space=text.count(" ")

            word=text.split(" ")
            for x in word:
                if word!=" ":
                    count=count+1
        else:
            space=analyze_text.count(" ")
            word=analyze_text.split(" ")
            for x in word:
                if word!=" ":
                    count=count+1
    if len(analyze_text)==0:
        analyze_text=text
    
    
    params={'purpose':'Remove Punctuation','Analyzed_Text':analyze_text,'word_count':count,'space_count':space,'Status':status}
    return render(request,'analyze.html',params)
