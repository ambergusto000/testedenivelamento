import os
from django.core.management.base import BaseCommand
import pandas as pd
from operadoras.models import Operadora
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Importa operadoras de planos de saúde a partir de um arquivo CSV'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            help='Caminho completo para o arquivo CSV (opcional)',
        )
        parser.add_argument(
            '--update',
            action='store_true',
            help='Atualiza registros existentes em vez de pular',
        )

    def handle(self, *args, **options):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        csv_file = options.get('file') or os.path.join(base_dir, 'csv', 'dados')
        
        self.stdout.write(f"Procurando arquivo em: {csv_file}")
        
        if not os.path.exists(csv_file):
            if os.path.exists(csv_file + '.csv'):
                csv_file += '.csv'
            else:
                self.stdout.write(self.style.ERROR(f"Arquivo não encontrado: {csv_file} (com ou sem extensão .csv)"))
                return
        
        try:
            try:
                df = pd.read_csv(csv_file, encoding='utf-8', delimiter=';')
            except UnicodeDecodeError:
                df = pd.read_csv(csv_file, encoding='latin1', delimiter=';')
            

            self.stdout.write("Colunas encontradas no arquivo:")
            for col in df.columns:
                self.stdout.write(f"- {col}")
            
            column_mapping = {
                'Registro_ANS': 'registro_ans',
                'CNPJ': 'cnpj',
                'Razao_Social': 'razao_social',
                'Nome_Fantasia': 'nome_fantasia',
                'Modalidade': 'modalidade',
                'Logradouro': 'logradouro',
                'Numero': 'numero',
                'Complemento': 'complemento',
                'Bairro': 'bairro',
                'Cidade': 'cidade',
                'UF': 'uf',
                'CEP': 'cep',
                'DDD': 'ddd',
                'Telefone': 'telefone',
                'Fax': 'fax',
                'Endereco_eletronico': 'endereco_eletronico',
                'Representante': 'representante',
                'Cargo_Representante': 'cargo_representante',
                'Data_Registro_ANS': 'data_registro_ans'
            }
            

            for csv_col in column_mapping.keys():
                if csv_col not in df.columns:
                    raise ValueError(f"Coluna obrigatória não encontrada: {csv_col}")
            
            total_imported = 0
            total_updated = 0
            total_skipped = 0
            
            for index, row in df.iterrows():
                try:
                    defaults = {
                        'cnpj': row['CNPJ'],
                        'razao_social': row['Razao_Social'],
                        'nome_fantasia': row['Nome_Fantasia'],
                        'modalidade': row['Modalidade'],
                        'logradouro': row['Logradouro'],
                        'numero': row['Numero'],
                        'complemento': row['Complemento'] if pd.notna(row['Complemento']) else None,
                        'bairro': row['Bairro'],
                        'cidade': row['Cidade'],
                        'uf': row['UF'],
                        'cep': row['CEP'],
                        'ddd': row['DDD'],
                        'telefone': row['Telefone'],
                        'fax': row['Fax'] if pd.notna(row['Fax']) else None,
                        'endereco_eletronico': row['Endereco_eletronico'] if pd.notna(row['Endereco_eletronico']) else None,
                        'representante': row['Representante'],
                        'cargo_representante': row['Cargo_Representante'],
                        'data_registro_ans': pd.to_datetime(row['Data_Registro_ANS']).date()
                    }
                    
                    if options['update']:
                        operadora, created = Operadora.objects.update_or_create(
                            registro_ans=row['Registro_ANS'],
                            defaults=defaults
                        )
                        if created:
                            total_imported += 1
                        else:
                            total_updated += 1
                    else:
                        Operadora.objects.get_or_create(
                            registro_ans=row['Registro_ANS'],
                            defaults=defaults
                        )
                        total_imported += 1
                        
                except IntegrityError as e:
                    self.stdout.write(self.style.WARNING(f"Erro ao importar linha {index + 1}: {str(e)}"))
                    total_skipped += 1
                    continue
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Erro inesperado na linha {index + 1}: {str(e)}"))
                    total_skipped += 1
                    continue
                
                if (index + 1) % 100 == 0:
                    self.stdout.write(f"Processados {index + 1} registros...")
            
            self.stdout.write(self.style.SUCCESS(
                f"Importação concluída! "
                f"Total: {len(df)} | "
                f"Importados: {total_imported} | "
                f"Atualizados: {total_updated} | "
                f"Pulados: {total_skipped}"
            ))
            
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Arquivo não encontrado: {csv_file}"))
        except pd.errors.EmptyDataError:
            self.stdout.write(self.style.ERROR("O arquivo CSV está vazio"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro durante a importação: {str(e)}"))