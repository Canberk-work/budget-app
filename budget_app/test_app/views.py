from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.

#Relative path variable to use within the file
paths = [
            "index.html",
            "test_app",
]

path_lenghts = [];
for i in range(len(paths)):
    path_lenghts.append(len(paths[i]))


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_DIR = os.path.join(BASE_DIR, "index.html")
index_length = path_lenghts[0]+ path_lenghts[0] - 1 #subtract 1 to account for the slash in front
INDEX_DIR = INDEX_DIR[-index_length:]

print(INDEX_DIR[-index_length:])

def index(request):
    my_dict = {'insert_me':'using injections like a baaaus'}
    return render(request, INDEX_DIR, context=my_dict)
