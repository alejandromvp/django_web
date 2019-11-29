from django.shortcuts import render

def post_ranking1(request):
    return render(request, 'players/ranking.html', {})

def editar_ranking(request):
    return render(request, 'edit_player/edit.html', {})