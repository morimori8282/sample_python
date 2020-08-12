from django.db import models

# Create your models here.

# ユーザ
class UserModel(models.Model):
    class Meta:
        verbose_name_plural = ("ユーザモデル")

    name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 20)
    author = models.IntegerField(default = 0)
    image = models.ImageField(upload_to = '')
    goodRule = models.TextField(default = '')
    specialty = models.CharField(max_length = 100)
    remarks = models.TextField(default = '')

    # adminサイトで作られるオブジェクトに可読性を持たせる
    def __str__(self): 
        return self.name

# イベント
class EventModel(models.Model):
    class Meta:
        verbose_name_plural = ("イベントモデル")

    eventDate = models.DateField()
    title = models.CharField(max_length = 100)
    remarks = models.TextField(default = '')
    image = models.ImageField(upload_to = '')
    roundCnt = models.IntegerField(default = 0)

    # 外部キー
    winner = models.ForeignKey('UserModel'
                                , verbose_name=("event_winnerId")
                                , related_name="event_winnerId"
                                , on_delete=models.PROTECT
                                , default=1)
    
    # adminサイトで作られるオブジェクトに可読性を持たせる
    def __str__(self): 
        return self.title

# 参加者(イベント参加者合計)
class EventParticipantModel(models.Model):
    class Meta:
        verbose_name_plural = ("イベント合計モデル")
    
    score = models.IntegerField(default = 0)
    rank = models.IntegerField(default = 0)
    remarks = models.TextField(default = '')

    # 外部キー
    event = models.ForeignKey('EventModel'
                                , verbose_name=("eventParticipantModel_eventId")
                                , related_name="eventParticipantModel_eventId"
                                , on_delete=models.PROTECT
                                , default=1)

    user = models.ForeignKey('UserModel'
                                , verbose_name=("eventParticipantModel_userId")
                                , related_name="eventParticipantModel_userId"
                                , on_delete=models.PROTECT
                                , default=1)

    # adminサイトで作られるオブジェクトに可読性を持たせる
    def __str__(self): 
        return self.remarks


# 参加者(イベントラウンド合計)
class EventRoundModel(models.Model):
    class Meta:
        verbose_name_plural = ("イベントラウンド合計モデル")
    
    roundId = models.IntegerField(default = 0)
    score = models.IntegerField(default = 0)
    remarks = models.TextField(default = '', null = True, blank = True)

    # 外部キー
    event = models.ForeignKey('EventModel'
                                , verbose_name=("EventRoundModel_eventId")
                                , related_name="EventRoundModel_eventId"
                                , on_delete=models.PROTECT
                                , default=1)

    # userId = models.ForeignKey('UserModel'
    #                             , verbose_name=("EventRoundModel_userId")
    #                             , related_name="EventRoundModel_userId"
    #                             , on_delete=models.PROTECT
    #                             , default=1)

    # adminサイトで作られるオブジェクトに可読性を持たせる
    def __str__(self): 
        return str(self.eventId) + '-' + str(self.roundId)

# イベント詳細
class EventDetailModel(models.Model):
    class Meta:
        verbose_name_plural = ("イベント詳細モデル")

    roundId = models.IntegerField()
    score = models.IntegerField()

    # 外部キー
    event = models.ForeignKey('EventModel'
                                , verbose_name=("eventDetailModel_eventId")
                                , related_name="eventDetailModel_eventId"
                                , on_delete=models.PROTECT
                                , default=1)

    user = models.ForeignKey('UserModel'
                                , verbose_name=("eventDetailModel_userId")
                                , related_name="eventDetailModel_userId"
                                , on_delete=models.PROTECT
                                , default=1)

    # adminサイトで作られるオブジェクトに可読性を持たせる
    def __str__(self): 
        return str(self.event) + '-' + str(self.roundId) + '-' + str(self.user)