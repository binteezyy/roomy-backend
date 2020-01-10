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
