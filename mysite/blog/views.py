from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def post_ranking(request):
    return render(request, 'blog/ranking.html', {})
