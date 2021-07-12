from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class transporteView(TemplateView):
    template_name = 'transporte.html'


class operacaoView(TemplateView):
    template_name = 'operacao.html'
    
class comercialView(TemplateView):
    template_name = 'comercial.html'


class loginView(TemplateView):
    template_name = 'login.html'


class planilhaView(TemplateView):
    template_name = 'planilha.html'


class desempenhoView(TemplateView):
    template_name = 'desempenho.html'

# ----- Planilhas ---------
class planilhaComparativoMesView(TemplateView):
    template_name = 'planilhaComparativoMes.html'


class planilhaBaseInformacaoView(TemplateView):
    template_name = 'planilhaBaseInformacao.html'


class planilhaGeralControleView(TemplateView):
    template_name = 'planilhaGeralControle.html'
    

class planilhaMultaView(TemplateView):
    template_name = 'planilhaMulta.html'


class planilhaRankingMotoristaView(TemplateView):
    template_name = 'planilhaRankingMotorista.html'


class planilhaOcorrenciasView(TemplateView):
    template_name = 'planilhaOcorrencias.html'


class planilhaDeparaNfeView(TemplateView):
    template_name = 'planilhaDeparaNfe.html'


