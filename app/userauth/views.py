from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User,Articles
from .forms import loginform

# Create your views here.
def zhuce(request):
    return render(request,'userauth/zhuce1.html')

def login(request):
    if request.method == 'GET':
        form = loginform(                                                                                                        )
        return render(request, 'userauth/login.html', {'form': form})
    else:
        form = loginform(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            request.session['phone'] = phone
            return redirect(reverse('userauth:index1'))
            # form = loginform()
            # return render(request, 'userauth/login.html', {'form': form})
        else:
            print(dir(form))
            print(form.errors)
            return render(request, 'userauth/login.html', {'form': form})


@csrf_exempt
def adduser(request):
    if request.is_ajax():
        phone = request.POST.get('phone', None)
        password = request.POST.get('ps', None)
        User.objects.create(phone=phone,password=password)
        return HttpResponse('ok')
    else:
        return HttpResponse('no')

def index1(request):
    phone = request.session.get('phone', None)
    if phone:
        obj = User.objects.filter(phone=phone).first()
        return render(request,'userauth/index1.html',{'obj':obj})

def details(request,con_id):
    Articles.objects.create(title='回家的路1',aname='张三',con='岁月苍苍，往事如烟。暮然回首间，已过了一年又一年。春去秋来，花开花落，走走停停间，又飘零了一季又一季。冷清街道口，是谁的一曲肝肠断，又将记忆的碎片，遗落于流年婉转间，电话听筒边，是谁的一番语重长，又将游子的心牵引到回家的方向?那一天，我背起了行囊，那一刻，我向你回望。那一天，你在我眼中是那么的美。那一瞬，你成了我心灵的寄存地。那一秒，我狠心转头而去，那一秒，你依然沉默不语。那一天，我带着你的期许，踏_上理想之路，一路无语。今天的我，站在异地，想象着故乡的你。忽然间又想起了故乡的你曾说的话语:只要四季不逝，你陪我一路前行。是啊，即使我在异地，你仍和我同在。昨天已经过去，明天还没到来,  我要把握今天，带着你的期许，在旭日东升之际勤奋投身工作，在风华正茂之时，躬身践行，奋斗不止。我要争取在四年之后，让你为我骄傲,  让我为你争光。我要在四年之后，身披黄金甲，踏雪归故士!无边的思绪又被耳边飘起了一曲天籁之音拉回:你说起那条回家的路，路上有开满鲜花的树，秋天里风吹花儿轻舞。今天，带着你的期许，在旭日东升之际勤奋投身工作，在风华正茂之时，躬身践行，分斗不止。我要争取在四年之后，让你为我骄傲，让我为你争光。我要在四年之后，身披黄金甲，踏雪归故土!')
    Articles.objects.create(title='回家的路2',aname='张三',con='岁月苍苍，往事如烟。暮然回首间，已过了一年又一年。春去秋来，花开花落，走走停停间，又飘零了一季又一季。冷清街道口，是谁的一曲肝肠断，又将记忆的碎片，遗落于流年婉转间，电话听筒边，是谁的一番语重长，又将游子的心牵引到回家的方向?那一天，我背起了行囊，那一刻，我向你回望。那一天，你在我眼中是那么的美。那一瞬，你成了我心灵的寄存地。那一秒，我狠心转头而去，那一秒，你依然沉默不语。那一天，我带着你的期许，踏_上理想之路，一路无语。今天的我，站在异地，想象着故乡的你。忽然间又想起了故乡的你曾说的话语:只要四季不逝，你陪我一路前行。是啊，即使我在异地，你仍和我同在。昨天已经过去，明天还没到来,  我要把握今天，带着你的期许，在旭日东升之际勤奋投身工作，在风华正茂之时，躬身践行，奋斗不止。我要争取在四年之后，让你为我骄傲,  让我为你争光。我要在四年之后，身披黄金甲，踏雪归故士!无边的思绪又被耳边飘起了一曲天籁之音拉回:你说起那条回家的路，路上有开满鲜花的树，秋天里风吹花儿轻舞。今天，带着你的期许，在旭日东升之际勤奋投身工作，在风华正茂之时，躬身践行，分斗不止。我要争取在四年之后，让你为我骄傲，让我为你争光。我要在四年之后，身披黄金甲，踏雪归故土!')
    Articles.objects.create(title='3回家的路2',aname='张三',con='岁月苍苍，往事如烟。暮然回首间，已过了一年又一年。春去秋来，花开花落，走走停停间，又飘零了一季又一季。冷清街道口，是谁的一曲肝肠断，又将记忆的碎片，遗落于流年婉转间，电话听筒边，是谁的一番语重长，又将游子的心牵引到回家的方向?那一天，我背起了行囊，那一刻，我向你回望。那一天，你在我眼中是那么的美。那一瞬，你成了我心灵的寄存地。那一秒，我狠心转头而去，那一秒，你依然沉默不语。那一天，我带着你的期许，踏_上理想之路，一路无语。今天的我，站在异地，想象着故乡的你。忽然间又想起了故乡的你曾说的话语:只要四季不逝，你陪我一路前行。是啊，即使我在异地，你仍和我同在。昨天已经过去，明天还没到来,  我要把握今天，带着你的期许，在旭日东升之际勤奋投身工作，在风华正茂之时，躬身践行，奋斗不止。我要争取在四年之后，让你为我骄傲,  让我为你争光。我要在四年之后，身披黄金甲，踏雪归故士!无边的思绪又被耳边飘起了一曲天籁之音拉回:你说起那条回家的路，路上有开满鲜花的树，秋天里风吹花儿轻舞。今天，带着你的期许，在旭日东升之际勤奋投身工作，在风华正茂之时，躬身践行，分斗不止。我要争取在四年之后，让你为我骄傲，让我为你争光。我要在四年之后，身披黄金甲，踏雪归故土!')
    Articles.objects.create(title='111回家2', aname='张三',con='岁月苍苍，往事如烟。暮然回首间，已过了一年又一年。春去秋来，花开花落，走走停停间，又飘零了一季又一季。冷清街道口，是谁的一曲肝肠断，又将记忆的碎片，遗落于流年婉转间，电话听筒边，是谁的一番语重长，又将游子的心牵引到回家的方向?那一天，我背起了行囊，那一刻，我向你回望。那一天，你在我眼中是那么的美。那一瞬，你成了我心灵的寄存地。那一秒，我狠心转头而去，那一秒，你依然沉默不语。那一天，我带着你的期许，踏_上理想之路，一路无语。今天的我，站在异地，想象着故乡的你。忽然间又想起了故乡的你曾说的话语:只要四季不逝，你陪我一路前行。是啊，即使我在异地，你仍和我同在。昨天已经过去，明天还没到来,  我要把握今天，带着你的期许，在旭日东升之际勤奋投身工作，在风华正茂之时，躬身践行，奋斗不止。我要争取在四年之后，让你为我骄傲,  让我为你争光。我要在四年之后，身披黄金甲，踏雪归故士!无边的思绪又被耳边飘起了一曲天籁之音拉回:你说起那条回家的路，路上有开满鲜花的树，秋天里风吹花儿轻舞。今天，带着你的期许，在旭日东升之际勤奋投身工作，在风华正茂之时，躬身践行，分斗不止。我要争取在四年之后，让你为我骄傲，让我为你争光。我要在四年之后，身披黄金甲，踏雪归故土!')
    con = Articles.objects.all().filter(id = con_id).first()
    phone = request.session.get('phone',None)
    aid = con_id
    # coms = comment.objects.all().filter(aid = con_id,del_id=0).order_by('-time')
    return render(request,'userauth/xiang.html',{'con':con,'aid':aid,'phone':phone})