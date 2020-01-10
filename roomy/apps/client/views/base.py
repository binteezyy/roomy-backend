from django.shortcuts import render

# GLOBAL CONTEXT
context = {
    'AUTHORS': 'PPTT',
}

def index(request):
    context.update(
        {
            'TITLE': "INDEX",
            'CONTENT': "SAMPLE CONTENT"
        }
    )
    return render(request,"components/index.html",context)

def explore(request):
    return render(request,"components/navigation/explore.html",context)

def about(request):
    return render(request,"components/navigation/about.html",context)

def faq(request):
    return render(request,"components/navigation/faq.html",context)
