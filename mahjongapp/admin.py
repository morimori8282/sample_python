from django.contrib import admin
from .models import UserModel, EventModel, EventParticipantModel, EventDetailModel, EventRoundModel
# Register your models here.

# adminサイトで編集可能にする
admin.site.register(UserModel)
admin.site.register(EventModel)
admin.site.register(EventParticipantModel)
admin.site.register(EventDetailModel)
admin.site.register(EventRoundModel)
