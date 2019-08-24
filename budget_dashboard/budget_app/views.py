from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def index(request):
    my_dict = {'insert_me':'using injections like a baaaus'}
    return render(request, INDEX_DIR, context=my_dict)


#Relative path variable generator to use within the file
#I've used the index name for everything as the html file name is index.html
paths = [
            "index.html",
            "budget_app",
]

path_lenghts = [];
for i in range(len(paths)):
    path_lenghts.append(len(paths[i]))

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #gives the full path to base directory
INDEX_DIR = os.path.join(BASE_DIR, paths[0]) #change the index value to match your paths list item
index_length = path_lenghts[0]+ path_lenghts[1] + 1 #adding 1 to account for the slash in middle
INDEX_DIR = INDEX_DIR[-index_length:] #gives the index_length amount of characters from the end. In this case "test_app/index.html"
