from django.shortcuts import render

from django.http import HttpResponse




def about(request):
    return render(request,"home/about.html")
def Contact(request):
    return render(request,"home/contact.html")        
def home(request):
    people=[{'Name':'Aditya','Age': 12},
            {'Name':'Rmn','Age': 24},
            {'Name':'Saket','Age': 34},
            ]
    text = """A good school is a place where education extends far beyond textbooks and exams, shaping well-rounded individuals. 
    It's a nurturing environment where dedicated teachers inspire curiosity, critical thinking, and a love for learning. 
    In a good school, students feel safe, supported, and encouraged to explore their potential. It fosters a sense of 
    community, diversity, and inclusivity, respecting individual differences. A good school not only imparts academic 
    knowledge but also instills essential life skills, values, and character development. It provides extracurricular opportunities,
    encouraging talents beyond the classroom. Such schools prepare students for the challenges of the world, fostering creativity, 
    resilience and a lifelong thirst for knowledge. In essence, a good school is the foundation for a brighter future."""
    return render(request, "home/index.html", context={'people': people, 'tt': text})   
# dictonary  

