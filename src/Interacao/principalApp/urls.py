from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.IndexView.as_view(), name='teste'),
    path('login/', views.loginView.as_view(), name='login'),
    path('transporte/', views.transporteView.as_view(), name='transporte'),
    path('operacao/', views.operacaoView.as_view(), name='operacao'),
    path('comercial/', views.comercialView.as_view(), name='comercial'),
    path('planilha/', views.planilhaView.as_view(), name='planilha'),
    path('desempenho/', views.desempenhoView.as_view(), name='desempenho'),
    # -------------  Planilhas  ---------------------
    path('planilhaComparativoMes/',
         views.planilhaComparativoMesView.as_view(), name='planilhaComparativoMes'),
    path('planilhaBaseInformacao/',
         views.planilhaBaseInformacaoView.as_view(), name='planilhaBaseInformacao'),
    path('planilhaGeralControle/',
         views.planilhaGeralControleView.as_view(), name='planilhaGeralControle'),
    path('planilhaMulta/', views.planilhaMultaView.as_view(), name='planilhaMulta'),
    path('planilhaRankingMotorista/',
         views.planilhaRankingMotoristaView.as_view(), name='planilhaRankingMotorista'),
    path('planilhaOcorrencias/',
         views.planilhaOcorrenciasView.as_view(), name='planilhaOcorrencias'),
    path('planilhaDeparaNfe/',
         views.planilhaDeparaNfeView.as_view(), name='planilhaDeparaNfe'),


]
