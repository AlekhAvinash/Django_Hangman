from django.shortcuts import render
from django.http import JsonResponse
from .mech import ostr


def app(request):
    if request.method == "POST" and request.POST["opt"] == "update":
        key = ostr.inp(request.POST["val"].strip())
        rep = {
            "stk": key.clr,
            "val": key.val,
            "out": ostr.cstr,
            "hnt": ostr.hint,
            "ctr": ostr.ictr,
            "win": ostr.winn,
            "ptr": str(ostr.ptrs),
        }
        return JsonResponse(rep, safe=False)
    elif request.method == "POST" and request.POST["opt"] == "start":
        ostr.start()
        rep = {
            "out": ostr.cstr,
            "ptr": ostr.ptrs,
            "hnt": ostr.hint,
        }
        return JsonResponse(rep, safe=False)
    else:
        ostr.start()
        getr = lambda inp: list(map(ostr.kfnd, inp))
        context = {
            "keys": [
                {"key": getr("qwertyuiop")},
                {"key": getr("asdfghjkl")},
                {"key": getr("zxcvbnm")},
            ],
            "ostr": ostr,
        }
        return render(request, "gamebase.html", context)


def about(request):
    return render(request, "about.html")
