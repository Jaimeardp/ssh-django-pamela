from django.shortcuts import redirect, render


def welcome(request):
    #print('#$%$$$%! -> ',request.COOKIES.get('code', None))
    if request.user.is_authenticated:
        return redirect("respositorio_home")
    else:
        return render(request,"logmetadatos/welcome.html")
