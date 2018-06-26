from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request, "home.html")

def count(request):
	fulltext = request.GET['fulltext']
	
	wordlist = fulltext.split()

	worddictionary = {}

	for word in wordlist:
		new_word = word.lower()
		if new_word in worddictionary:
			#increase here
			worddictionary[new_word] += 1
		else:
			#add to the dictionary
			worddictionary[new_word] = 1

	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, "count.html", {'fulltext': fulltext, "count": len(wordlist), "sortedwords": sortedwords})

def about(request):
	return render(request, "about.html")