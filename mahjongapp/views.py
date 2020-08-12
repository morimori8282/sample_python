from django.shortcuts import render
from .models import UserModel, EventModel, EventDetailModel, EventRoundModel
from django.urls import reverse
from urllib.parse import urlencode
from django.shortcuts import redirect
import re

# Create your views here.

# ユーザ一覧
def indexfunc(request):
    object_list = UserModel.objects.all()
    # print(object_list)
    return render(request, 'index.html', {'object_list': object_list})

# サインイン
def loginfunc(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        object_user = UserModel.objects.filter(name=username, password=password).values('id')

        if(object_user.count() == 1):
            # セッションを作成して履歴画面へ
            request.session['userId'] = object_user[0]["id"]
            return redirect('historyTop')

            # 認証エラー
            return render(request, 'login.html', {'Error': 'ユーザ名またはパスワードが違います'})
    
    return render(request, 'login.html')

# 履歴
def historyTopfunc(request):
    object_list = EventModel.objects.all()
    # print(object_list)
    # print('---------------')
    return render(request, 'historyTop.html', {'object_list': object_list})

# 履歴詳細
def historyDetailfunc(request):
    if request.method == 'POST' :
        eventId = request.POST['eventId']
        # eventId = request.POST.get('eventId')
    
    if request.method == 'GET' :
        eventId = request.GET['eventId']

    # イベントモデル
    object_event = EventModel.objects.get(pk=eventId)

    # イベントラウンド
    object_eventCntRow = EventDetailModel.objects.filter(event_id=eventId).values('roundId').order_by('roundId').distinct()
    
    # イベント参加ユーザ(ユーザ名が取得できない)
    object_eventUserRow = EventDetailModel.objects.filter(event_id=eventId).values('user_id', 'user').order_by('user_id').distinct()
    object_userRow = UserModel.objects.order_by('id')

    # イベント詳細モデル
    object_list = EventDetailModel.objects.filter(event_id=eventId).order_by('user_id', 'roundId')
    
    return render(request, 'historyDetail.html', {
                     'object_event' : object_event
                    ,'object_eventCntRow': object_eventCntRow
                    ,'object_eventUserRow': object_eventUserRow
                    ,'object_userRow' : object_userRow
                    ,'object_list': object_list
                    })

# 履歴更新
def historyDetailAddfunc(request):
    
    # ログインしていない場合、ログイン画面へ
    if 'userId' not in request.session and 'btnBack' not in request.POST:
        return render(request,'login.html')

    if request.method == 'POST':
        eventId = request.POST['eventId']
        
        if 'btnBack' in request.POST:
            return redirect('historyTop')

        elif 'btnAdd' in request.POST:
            # 最大値取得
            object_eventCntRow = EventDetailModel.objects.filter(event_id=eventId).values('roundId').order_by('roundId').reverse()[0]
            # Insert対象のラウンド
            nextRound = object_eventCntRow['roundId'] + 1
            # 今回の参加ユーザ
            # object_eventUserRow = EventDetailModel.objects.filter(event_id=eventId).values('user_id', 'user').order_by('user_id').distinct()
            # if object_eventUserRow != None:
            #     for user in object_eventUserRow:
            #         newData = EventDetailModel(roundId=nextRound, score=0, user=user.user_id, event=eventId)
            #         newData.save()
            # else:
            object_eventUserRow = UserModel.objects.all()
        
            # 外部キー設定用にインスタンス生成
            eventInstance = EventModel.objects.get(id=eventId)
            for user in object_eventUserRow:
                # 外部キー設定用にインスタンス生成
                userInstance = UserModel.objects.get(id=user.id)
                # イベント詳細テーブルにデータを挿入する。外部キーはインスタンスを渡す
                newData = EventDetailModel(roundId=nextRound, score=0, event=eventInstance, user=userInstance)
                # print(newData.save().query)
                newData.save()

            
        elif 'btnUpdate' in request.POST:
            print('-------update--------')
            for reqPost in request.POST:
                # print(score)
                if re.match(r'score-[+-]?\d+', reqPost) :
                    score = str(reqPost).split("-")
                    # 更新対象モデル
                    updObject = EventDetailModel.objects.get(id=int(score[1]))
                    updObject.score = int(request.POST[reqPost])
                    updObject.save()
                    # print(request.POST[reqPost])

                else:
                    print('noMatch')

            # scoreの更新


        elif 'btnDelete' in request.POST:
            print('-------delete--------')


        # リダイレクト先のパスを取得する
        redirect_url = reverse('historyDetail')

        # パラメータのdictをurlencodeする。複数のパラメータを含めることも可能
        parameters = urlencode({'eventId': eventId})

        # URLにパラメータを付与する
        url = '{}?{}'.format(redirect_url, parameters)
        return redirect(url)

    else:
        return redirect('historyTop')


# ユーザメンテナンス
def userCtlfunc(request):
    
    # ログインしていない場合、ログイン画面へ
    if 'userId' not in request.session and 'btnBack' not in request.POST:
        return render(request,'login.html')

    if request.method == 'GET':
        # データの取得
        object_user = UserModel.objects.get(id = request.GET["userId"])
        return render(request, 'userCtl.html', {'object_user': object_user})

    elif request.method == 'POST':
        # データ更新処理
        # TODO

        # リダイレクト先のパスを取得する
        redirect_url = reverse('index')
        # URLにパラメータを付与する
        url = '{}'.format(redirect_url)
        return redirect(url)

    else:
        return redirect('historyTop')