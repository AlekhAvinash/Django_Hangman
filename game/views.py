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
            "ctr": ostr.ictr,
            "win": ostr.winn,
            "ptr": str(ostr.ptrs),
        }
        print(rep)
        return JsonResponse(rep, safe=False)
    elif request.method == "POST" and request.POST["opt"] == "start":
        ostr.start("Fire Palace")
        rep = {
            "out": ostr.cstr,
            "ptr": ostr.ptrs,
        }
        return JsonResponse(rep, safe=False)
    else:
        ostr.start("Fire Palace")
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
