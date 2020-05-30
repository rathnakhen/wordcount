import operator

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    if fulltext == "":
        return render(request, 'error.html')

    wordlist = fulltext.split()
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # Increase
            worddictionary[word] += 1
        else:
            # add to dictionary
            worddictionary[word] = 1
        sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'wordlist': fulltext, 'count': len(wordlist), 'dictionary': sortedwords})


def about(request):
    return render(request, 'about.html')


def error(request):
    return render(request, 'error.html')