from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordcount = fulltext.split()
    worddic ={}
    for word in wordcount:
        if word in worddic:
            worddic[word]+=1;
        else:
            worddic[word]=1;

    sortedwords = sorted(worddic.items(),key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordcount),'sortedwords':sortedwords})

def about(request):
    return render(request,'about.html')