from django.shortcuts import render
def index(request):
    return render(request,'newsapp/index.html')
def moviesinfo(request):
    head_msg='Latest movie information'
    msg1='RRR will finish the shoot very quikly'
    msg2='sarkari vari pata director vamsi paidipalli'
    msg3='chiranjeevi remakes the movie of lucifer'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)
def sportsinfo(request):
        head_msg='Latest sports information'
        msg1='dhon will play in another ipl match'
        msg2='good bye to sachin'
        msg3='devdtt padikial in rcb was unreachable'
        my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
        return render(request,'newsapp/news.html',context=my_dict)
def politicsinfo(request):
    head_msg='Latest politics information'
    msg1='worst ysrcp government'
    msg2='roads  in this government very very worst'
    msg3='next c.m pawan kalyan'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)
