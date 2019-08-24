from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def index(request):
    insertion_example = {'insert_me':'using injections like a baaaus'}
    return render(request, INDEX_DIR, context=insertion_example)

def help(request):
    insertion_example2 = {'help_example':'if you need help then Google it...'}
    return render(request, HELP_DIR, context=insertion_example2)

#Relative path variable generator to use within the file
#I've used the index name for everything as the html file name is index.html
paths = [
            "index.html",
            "budget_app",
            "help.html"
]

path_lenghts = [];
for i in range(len(paths)):
    path_lenghts.append(len(paths[i]))

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #gives the full path to base directory

#index.html
INDEX_DIR = os.path.join(BASE_DIR, paths[0]) #change the index value to match your paths list item
index_length = path_lenghts[0]+ path_lenghts[1] + 1 #adding 1 to account for the slash in middle
INDEX_DIR = INDEX_DIR[-index_length:] #gives the index_length amount of characters from the end. In this case "budget_app/index.html"
print(INDEX_DIR)
#help.html
HELP_DIR = os.path.join(BASE_DIR, paths[2]) #change the index value to match your paths list item
help_length = path_lenghts[2]+ path_lenghts[1] + 1 #adding 1 to account for the slash in middle
HELP_DIR = HELP_DIR[-help_length:] #gives the index_length amount of characters from the end. In this case "budget_app/index.html"
print(HELP_DIR)
