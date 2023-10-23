from django.shortcuts import render, redirect
from django.http import HttpResponse  # Corrected import
import os
# abhhi model ko import krugo toh put the
# fetched data in db
from vege.models import *
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('recipe_name')
        des = data.get('recipe_description')
        img = request.FILES.get('recipe_Image')
        Recipe.objects.create(recipe_name=name,
                              recipe_description=des,
                              recipe_Image=img)
    queryset=Recipe.objects.all()
    return render(request, 'vege/recipes.html',  context={'recipes':queryset})

def Delete(request,id):
    queryset=Recipe.objects.get(id=id)
    print(queryset.recipe_Image)
    os.remove(queryset.recipe_Image.path)

    queryset.delete()
    return redirect('/recipes/')

def Update(request,id):
    queryset=Recipe.objects.get(id=id)
     
    if request.method=='POST':
        data=request.POST
        img = request.FILES.get('recipe_Image')
        queryset.recipe_name=data.get('recipe_name')
        queryset.recipe_description =data.get('recipe_description')
        queryset.save()  
        return redirect('/recipes/')
    return render(request,'vege/update.html',context={'Rec':queryset})
