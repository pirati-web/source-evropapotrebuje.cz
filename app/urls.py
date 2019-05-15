# -*- encoding:utf-8 -*-

from django.conf.urls import include, url

from django.conf import settings as appSettings

from . import views

app_name = "app"
urlpatterns = [
    # Examples:
    url(r'^$', views.page_index, name="page_index"),

    url(r'^ar/$', views.page_index_ar, name="page_index_ar"),

    url(r'^program/$', views.page_program, name="page_program"),

    url(r'^program/spolecny-eu-pirati/(?P<part>[a-z-]+)/$', views.page_program_eu, name="page_program_eu"),
    url(r'^program/spolecny-eu-pirati/$', views.page_program_eu, name="page_program_eu"),

    url(r'^en/what-we-want/$', views.page_en_what_we_want, name="en_what_we_want"),
    url(r'^en/$', views.page_en_what_we_want, name="en_index"),
    url(r'^en/how-to-vote/$', views.page_en_how_to_vote, name="en_how_to_vote"),

    url(r'^sk/ako-volit/$', views.page_sk_jak_volit, name="page_sk_jak_volit"),

    url(r'^jak-volit/$', views.page_jak_volit, name="page_jak_volit"),
    url(r'^zapoj-se/$', views.page_zapoj_se, name="page_zapoj_se"),
    url(r'^proc-jit-volit/$', views.page_proc_jit_volit, name="page_proc_jit_volit"),
    url(r'^kandidati/$', views.page_kandidati, name="page_kandidati"),
    url(r'^eurovolby-2019/$', views.page_nalodeni, name="page_nalodeni"),

    url(r'^kandidati/marcel-kolaja/$', views.page_kandidati_detail, name="page_kandidati_1", kwargs={'person' : 'marcel-kolaja'}),
    url(r'^kandidati/marketa-gregorova/$', views.page_kandidati_detail, name="page_kandidati_2", kwargs={'person' : 'marketa-gregorova'}),
    url(r'^kandidati/mikulas-peksa/$', views.page_kandidati_detail, name="page_kandidati_3", kwargs={'person' : 'mikulas-peksa'}),
    url(r'^kandidati/lukas-blazej/$', views.page_kandidati_detail, name="page_kandidati_4", kwargs={'person' : 'lukas-blazej'}),
    url(r'^kandidati/jana-kolarikova/$', views.page_kandidati_detail, name="page_kandidati_5", kwargs={'person' : 'jana-kolarikova'}),

    url(r'^kandidati/ondrej-kolek/$', views.page_kandidati_detail, name="page_kandidati_6", kwargs={'person' : 'ondrej-kolek'}),
    url(r'^kandidati/nina-spitalnikova/$', views.page_kandidati_detail, name="page_kandidati_7", kwargs={'person' : 'nina-spitalnikova'}),
    url(r'^kandidati/eva-ticha/$', views.page_kandidati_detail, name="page_kandidati_8", kwargs={'person' : 'eva-ticha'}),
    url(r'^kandidati/lukas-lev-cervinka/$', views.page_kandidati_detail, name="page_kandidati_9", kwargs={'person' : 'lukas-lev-cervinka'}),
    #url(r'^kandidati/marek-necada/$', views.page_kandidati_detail, name="page_kandidati_10", kwargs={'person' : 'marek-necada'}),
    url(r'^kandidati/michal-gill/$', views.page_kandidati_detail, name="page_kandidati_10", kwargs={'person' : 'michal-gill'}),
    url(r'^kandidati/jiri-hoskovec/$', views.page_kandidati_detail, name="page_kandidati_11", kwargs={'person' : 'jiri-hoskovec'}),
    url(r'^kandidati/david-frantisek-wagner/$', views.page_kandidati_detail, name="page_kandidati_12", kwargs={'person' : 'david-frantisek-wagner'}),
    url(r'^kandidati/michal-salomoun/$', views.page_kandidati_detail, name="page_kandidati_13", kwargs={'person' : 'michal-salomoun'}),
    url(r'^kandidati/magdalena-dankova/$', views.page_kandidati_detail, name="page_kandidati_14", kwargs={'person' : 'magdalena-dankova'}),
    url(r'^kandidati/matej-sandor/$', views.page_kandidati_detail, name="page_kandidati_15", kwargs={'person' : 'matej-sandor'}),
    url(r'^kandidati/linda-matuskova/$', views.page_kandidati_detail, name="page_kandidati_16", kwargs={'person' : 'linda-matuskova'}),
    url(r'^kandidati/petr-jirman/$', views.page_kandidati_detail, name="page_kandidati_17", kwargs={'person' : 'petr-jirman'}),
    url(r'^kandidati/dan-lestina/$', views.page_kandidati_detail, name="page_kandidati_18", kwargs={'person' : 'dan-lestina'}),
    url(r'^kandidati/frantisek-kopriva/$', views.page_kandidati_detail, name="page_kandidati_19", kwargs={'person' : 'frantisek-kopriva'}),
    url(r'^kandidati/hynek-melichar/$', views.page_kandidati_detail, name="page_kandidati_20", kwargs={'person' : 'hynek-melichar'}),
    url(r'^kandidati/jiri-jansa/$', views.page_kandidati_detail, name="page_kandidati_21", kwargs={'person' : 'jiri-jansa'}),
    url(r'^kandidati/jan-licka/$', views.page_kandidati_detail, name="page_kandidati_22", kwargs={'person' : 'jan-licka'}),
    url(r'^kandidati/michael-polak/$', views.page_kandidati_detail, name="page_kandidati_23", kwargs={'person' : 'michael-polak'}),
    url(r'^kandidati/ladislav-koubek/$', views.page_kandidati_detail, name="page_kandidati_24", kwargs={'person' : 'ladislav-koubek'}),
    url(r'^kandidati/pavel-tauer/$', views.page_kandidati_detail, name="page_kandidati_25", kwargs={'person' : 'pavel-tauer'}),
    url(r'^kandidati/simon-barczi/$', views.page_kandidati_detail, name="page_kandidati_26", kwargs={'person' : 'simon-barczi'}),
    url(r'^kandidati/milos-vlach/$', views.page_kandidati_detail, name="page_kandidati_27", kwargs={'person' : 'milos-vlach'}),
    url(r'^kandidati/jiri-lehejcek/$', views.page_kandidati_detail, name="page_kandidati_28", kwargs={'person' : 'jiri-lehejcek'}),


]

