from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Operadora

@api_view(['GET'])
def buscar_operadoras(request):
    termo_uf = request.GET.get('uf', '')
    termo_nome_fantasia = request.GET.get('nome_fantasia', '')
    termo_razao_social = request.GET.get('razao_social', '')
    termo_cnpj = request.GET.get('cnpj', '')
    termo_registro_ans = request.GET.get('registro_ans', '')
    termo_cidade = request.GET.get('cidade', '')
    termo_representante = request.GET.get('representante', '')
    termo_modalidade = request.GET.get('modalidade', '')
    termo_telefone = request.GET.get('telefone', '')
    
    termo_geral = request.GET.get('q', '')

    filtros = Q()
    

    if termo_geral:
        filtros |= Q(nome_fantasia__icontains=termo_geral)
        filtros |= Q(razao_social__icontains=termo_geral)
        filtros |= Q(cnpj__icontains=termo_geral)
        filtros |= Q(registro_ans__icontains=termo_geral)
        filtros |= Q(cidade__icontains=termo_geral)
        filtros |= Q(uf__icontains=termo_geral)
        filtros |= Q(representante__icontains=termo_geral)
        filtros |= Q(modalidade__icontains=termo_geral)
        filtros |= Q(telefone__icontains=termo_geral)
    else:
      
        if termo_uf:
            filtros &= Q(uf__icontains=termo_uf)
        if termo_nome_fantasia:
            filtros &= Q(nome_fantasia__icontains=termo_nome_fantasia)
        if termo_razao_social:
            filtros &= Q(razao_social__icontains=termo_razao_social)
        if termo_cnpj:
            filtros &= Q(cnpj__icontains=termo_cnpj)
        if termo_registro_ans:
            filtros &= Q(registro_ans__icontains=termo_registro_ans)
        if termo_cidade:
            filtros &= Q(cidade__icontains=termo_cidade)
        if termo_representante:
            filtros &= Q(representante__icontains=termo_representante)
        if termo_modalidade:
            filtros &= Q(modalidade__icontains=termo_modalidade)
        if termo_telefone:
            filtros &= Q(telefone__icontains=termo_telefone)

   
    queryset = Operadora.objects.filter(filtros)[:50] if filtros else Operadora.objects.none()

    
    resultados = [
        {
            'id': operadora.id,
            'registro_ans': operadora.registro_ans,
            'cnpj': operadora.cnpj,
            'razao_social': operadora.razao_social,
            'nome_fantasia': operadora.nome_fantasia,
            'modalidade': operadora.modalidade,
            'logradouro': operadora.logradouro,
            'numero': operadora.numero,
            'complemento': operadora.complemento,
            'bairro': operadora.bairro,
            'cidade': operadora.cidade,
            'uf': operadora.uf,
            'cep': operadora.cep,
            'ddd': operadora.ddd,
            'telefone': operadora.telefone,
            'fax': operadora.fax,
            'email': operadora.endereco_eletronico,
            'representante': operadora.representante,
            'cargo_representante': operadora.cargo_representante,
            'data_registro': operadora.data_registro_ans.strftime('%d/%m/%Y')
        }
        for operadora in queryset
    ]

    return Response({'resultados': resultados})