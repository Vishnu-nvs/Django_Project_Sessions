from django.shortcuts import render ,redirect

# Create your views here.
def session(request):
    cout=request.session.get('count',0)
    cout+=1
    request.session['count']=cout
    value=request.session['count']
    request.session.set_expiry(2)
    Ex_age=request.session.get_expiry_age()
    Ex_date=request.session.get_expiry_date()
    return render(request,'session.html',context={"value":value,"ex_age":Ex_age,"date":Ex_date})


def delete_session(request):
    del request.session['count']
    return redirect("/")
