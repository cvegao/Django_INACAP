from django.shortcuts import render, redirect


def set_conditions(request):
    if request.method == 'POST':
        request.session["max_moves"] = int(request.POST["max_moves"])
        request.session["min_gold"] = int(request.POST["min_gold"])
        return redirect("index_bonus")

    return render(request, "set_conditions.html")
