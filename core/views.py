from django.shortcuts import render, redirect

from django.http import HttpResponse

from usuarios.models import UserProfile
from core.models import Vaga, Candidatura
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Imports para a view de registro do usuário
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

# Import para implementar o sistema de busca, assim como o ListView
from django.db.models import Q

import locale
locale.setlocale(locale.LC_ALL, 'nl_NL')

from django.http import JsonResponse
import json

# Create your views here.


# ---------------------------------------- VIEW - Página inicial ------------------------------------------------
def principal(request):

    empresa = UserProfile.objects.filter(perfil='empresa')

    dados = {'empresas':empresa}
    return render(request, 'index.html', dados)


# ---------------------------------------- VIEW - Página Perfil -------------------------------------------------
def perfil(request):
    usuario = request.user
    vaga = Vaga.objects.filter(empresa=usuario)
    candidato = Candidatura.objects.all()

    vaga_cand = Candidatura.objects.filter(candidato=usuario)

    dados = {'vagas':vaga, 'candidatos':candidato, 'vagas_cand':vaga_cand}
    return render(request, 'perfil.html', dados)


# ---------------------------------------- VIEW - Página de Relatório -------------------------------------------

def relatorio(request):

    vagas_jan = Vaga.objects.filter(data_publicacao__month=1).count()
    candidaturas_jan = Candidatura.objects.filter(data_candidatura__month=1).count()

    vagas_fev = Vaga.objects.filter(data_publicacao__month=2).count()
    candidaturas_fev = Candidatura.objects.filter(data_candidatura__month=2).count()

    vagas_mar = Vaga.objects.filter(data_publicacao__month=3).count()
    candidaturas_mar = Candidatura.objects.filter(data_candidatura__month=3).count()

    vagas_abr = Vaga.objects.filter(data_publicacao__month=4).count()
    candidaturas_abr = Candidatura.objects.filter(data_candidatura__month=4).count()

    vagas_mai = Vaga.objects.filter(data_publicacao__month=5).count()
    candidaturas_mai = Candidatura.objects.filter(data_candidatura__month=5).count()

    vagas_jun = Vaga.objects.filter(data_publicacao__month=6).count()
    candidaturas_jun = Candidatura.objects.filter(data_candidatura__month=6).count()

    vagas_jul = Vaga.objects.filter(data_publicacao__month=7).count()
    candidaturas_jul = Candidatura.objects.filter(data_candidatura__month=7).count()

    vagas_ago = Vaga.objects.filter(data_publicacao__month=8).count()
    candidaturas_ago = Candidatura.objects.filter(data_candidatura__month=8).count()

    vagas_set = Vaga.objects.filter(data_publicacao__month=9).count()
    candidaturas_set = Candidatura.objects.filter(data_candidatura__month=9).count()

    vagas_out = Vaga.objects.filter(data_publicacao__month=10).count()
    candidaturas_out = Candidatura.objects.filter(data_candidatura__month=10).count()

    vagas_nov = Vaga.objects.filter(data_publicacao__month=11).count()
    candidaturas_nov = Candidatura.objects.filter(data_candidatura__month=11).count()

    vagas_dez = Vaga.objects.filter(data_publicacao__month=12).count()
    candidaturas_dez = Candidatura.objects.filter(data_candidatura__month=12).count()



    dados = {
        'vagas_jan': json.dumps(vagas_jan),
        'vagas_fev': json.dumps(vagas_fev),
        'vagas_mar': json.dumps(vagas_mar),
        'vagas_abr': json.dumps(vagas_abr),
        'vagas_mai': json.dumps(vagas_mai),
        'vagas_jun': json.dumps(vagas_jun),
        'vagas_jul': json.dumps(vagas_jul),
        'vagas_ago': json.dumps(vagas_ago),
        'vagas_set': json.dumps(vagas_set),
        'vagas_out': json.dumps(vagas_out),
        'vagas_nov': json.dumps(vagas_nov),
        'vagas_dez': json.dumps(vagas_dez),
        'candidaturas_jan': json.dumps(candidaturas_jan),
        'candidaturas_fev': json.dumps(candidaturas_fev),
        'candidaturas_mar': json.dumps(candidaturas_mar),
        'candidaturas_abr': json.dumps(candidaturas_abr),
        'candidaturas_mai': json.dumps(candidaturas_mai),
        'candidaturas_jun': json.dumps(candidaturas_jun),
        'candidaturas_jul': json.dumps(candidaturas_jul),
        'candidaturas_ago': json.dumps(candidaturas_ago),
        'candidaturas_set': json.dumps(candidaturas_set),
        'candidaturas_out': json.dumps(candidaturas_out),
        'candidaturas_nov': json.dumps(candidaturas_nov),
        'candidaturas_dez': json.dumps(candidaturas_dez),
    }

    return render(request, 'relatorio.html', dados)

# ---------------------------------------- VIEW - Página de vagas -----------------------------------------------
def vagas(request):

    candidato = request.user
    vaga = Vaga.objects.all()


    dados = {'vagas':vaga}
    return render(request, 'vagas.html', dados)


# ------------------------------ VIEW definida com a função de criação / edição de Vaga ---------------------------

@require_POST
def nova_vaga(request):

    vaga_id = request.POST.get('vaga-field')

    empresa = request.user
    nome_vaga = request.POST['nome-vaga']
    faixa_salarial = request.POST['faixa-salarial']
    requisitos = request.POST['requisitos']
    descricao = request.POST['descricao']
    escolaridade_minima = request.POST['escolaridade-minima']
    data_publicacao = datetime.today()

    if vaga_id:
        vaga = Vaga.objects.get(id=vaga_id)

        empresa = request.user
        vaga.nome_vaga = nome_vaga
        vaga.salario = faixa_salarial
        vaga.requisitos = requisitos
        vaga.descricao = descricao
        vaga.escolaridade = escolaridade_minima
        vaga.save()
        messages.success(request, 'As informações da vaga foram alteradas.')
    else:
        novaVaga = Vaga.objects.create(
            nome_vaga=nome_vaga, 
            salario=faixa_salarial, 
            descricao=descricao, 
            requisitos=requisitos,
            escolaridade=escolaridade_minima,
            data_publicacao=data_publicacao,
            empresa=empresa
            )
        
        novaVaga.save()
        messages.success(request, 'Vaga cadastrada com sucesso.')

    return redirect('/perfil/')


# ---------------------------- VIEW definida com a função de Login -----------------------------------------------
def delete_vaga(request):

    vaga_id = request.POST.get('vaga-field')
    vaga = Vaga.objects.get(id=vaga_id)

    vaga.delete()

    messages.success(request, 'A vaga foi excluída.')
    return redirect('/perfil/')

# ---------------------------- VIEW definida com a função de Login -----------------------------------------------
def login_usuario(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('usuario')
        password = request.POST.get('senha')
        usuario = authenticate(username=username, password=password)
        if usuario is None:
            messages.error(request, "Usuário ou senha inválido(a)")
        else:
            login(request, usuario)
            return redirect('/')
    return redirect('/login/')


# ---------------------------- VIEW definida com a função de Candidatura -----------------------------------------

@require_POST
def candidatura(request):
    pontos = 0
    candidato = request.user

    vaga_id = request.POST['vaga-field']
    vaga = Vaga.objects.get(id=vaga_id)

    ver_candidatura = Candidatura.objects.filter(candidato=candidato, vaga=vaga)

    pretensao_salarial = request.POST['pretensao-salarial']
    ps = float(locale.atof(pretensao_salarial))
    ultima_escolaridade = request.POST['ultima-escolaridade']
    experiencia = request.POST['experiencia']
    data_candidatura = datetime.today()

    if vaga.salario == "Até R$ 1.000,00" and ps <= 1000.0:
        pontos += 1
    
    if vaga.salario == "De R$ 1.000,00 a 2.000,00" and ps <= 2000.0:
        pontos += 1

    if vaga.salario == "De R$ 2.000,00 a 3.000,00" and ps <= 3000.0:
        pontos += 1

    if vaga.salario == "Acima de R$ 3.000,00":
        pontos += 1

    if ultima_escolaridade == vaga.escolaridade:
        pontos += 1

    if not ver_candidatura:
        atualizaQuantCandidatos = Vaga.objects.get(id=vaga_id)
        atualizaQuantCandidatos.candidaturas = atualizaQuantCandidatos.candidaturas + 1
        atualizaQuantCandidatos.save()

        novaCandidatura = Candidatura.objects.create(candidato=candidato, vaga=vaga, pretensao_salarial=pretensao_salarial, ultima_escolaridade=ultima_escolaridade, experiencia=experiencia, pontos=pontos, data_candidatura=data_candidatura)
        novaCandidatura.save()
        messages.success(request, "Candidatura enviada com sucesso!")
    else:
        messages.error(request, "Você já havia se candidatado para essa vaga anteriormente.")

    return redirect('/vagas/')

# ---------------------------- VIEW para cadastro do candidato ---------------------------------------------------
def cadastro_candidato(request):
    return render(request, 'cadastro_candidato.html')

@require_POST
def cadastrar_candidato(request):
    try:
        usuario_aux1 = UserProfile.objects.get(username=request.POST['email'])

        if usuario_aux1:
            messages.error(request, "Já existe um usuário cadastrado com esse e-mail.")
            return redirect('/cadastro_candidato/')

    except UserProfile.DoesNotExist:
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        perfil = request.POST['perfil']
        email = request.POST['email']
        senha = request.POST['senha']
        senha_conf = request.POST['senha1']
        
        if request.FILES:
            doc = request.FILES
            foto = doc['file-foto']
        else:
            foto = None

        if senha != senha_conf:
            messages.error(request, "As senhas digitadas são diferentes.")
            return redirect('/cadastro_candidato/')

        novoUsuario = UserProfile.objects.create_user(first_name=nome, last_name=sobrenome, perfil=perfil, username=email, email=email, password=senha, foto=foto)
        novoUsuario.save()

        # Realiza o login automático após cadastro do usuário
        username = request.POST.get('email')
        password = request.POST.get('senha')
        usuario = authenticate(username=username, password=password)

        login(request, usuario)

    return redirect("/")


# ---------------------------- VIEW para cadastro da empresa ----------------------------------------------------
def cadastro_empresa(request):
    return render(request, 'cadastro_empresa.html')

@require_POST
def cadastrar_empresa(request):
    try:
        usuario_aux1 = UserProfile.objects.get(username=request.POST['email'])

        if usuario_aux1:
            messages.error(request, "Já existe uma empresa cadastrada com esse e-mail.")
            return redirect('/cadastro_empresa/')

    except UserProfile.DoesNotExist:
        empresa = request.POST['empresa']
        perfil = request.POST['perfil']
        email = request.POST['email']
        senha = request.POST['senha']
        senha_conf = request.POST['senha1']
        doc = request.FILES
        foto = doc['file-logo']

        if senha != senha_conf:
            messages.error(request, "As senhas digitadas são diferentes.")
            return redirect('/cadastro_empresa/')

        novoUsuario = UserProfile.objects.create_user(empresa=empresa, perfil=perfil, username=email, email=email, password=senha, foto=foto)
        novoUsuario.save()

        # Realiza o login automático após cadastro do usuário
        username = request.POST.get('email')
        password = request.POST.get('senha')
        usuario = authenticate(username=username, password=password)

        login(request, usuario)

    return redirect("/")


# ---------------------------- VIEW definida com a função de Logout ----------------------------------------------
def logout_user(request):
    logout(request)
    return redirect('/')