from utilities.views.decorators import render

@render(template="www/slash.html")
def slash(request):
    return {"message":"Hello World"}
