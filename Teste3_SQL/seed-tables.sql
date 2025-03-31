SET GLOBAL local_infile = 1;
SHOW VARIABLES LIKE 'local_infile';
SHOW WARNINGS;

-- 2023_T1
-- Foi necessário trocar as vírgulas por pontos, pois o decimal aceita apenas pontos.
LOAD DATA LOCAL INFILE "C:/Users/bolac/OneDrive/Área de Trabalho/Teste_Nivelamento_Augusto_Ramos/outros/csv/1T2023.csv"
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, reg_ans, cd_conta_contabil, descricao, 
 @vl_saldo_inicial, @vl_saldo_final)
SET 
 vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
 vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');



-- 2023_T2
LOAD DATA LOCAL INFILE "C:/Users/bolac/OneDrive/Área de Trabalho/Teste_Nivelamento_Augusto_Ramos/outros/csv/2T2023.csv"
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, reg_ans, cd_conta_contabil, descricao, 
 @vl_saldo_inicial, @vl_saldo_final)
SET 
 vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
 vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');


-- 2023_T3
LOAD DATA LOCAL INFILE "C:/Users/bolac/OneDrive/Área de Trabalho/Teste_Nivelamento_Augusto_Ramos/outros/csv/3T2023.csv"
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, reg_ans, cd_conta_contabil, descricao, 
 @vl_saldo_inicial, @vl_saldo_final)
SET 
 vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
 vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');


-- 2023_T4
-- O dado de data neste arquivo do quarto trimestre de 2023 não está de acordo com o padrão utilizado normalmente para o banco de dados. Está em formato de data DD/MM/AAAA
LOAD DATA LOCAL INFILE "C:/Users/bolac/OneDrive/Área de Trabalho/Teste_Nivelamento_Augusto_Ramos/outros/csv/4T2023.csv"
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data_registro, reg_ans, cd_conta_contabil, descricao, 
 @vl_saldo_inicial, @vl_saldo_final)
SET 
 data_registro = STR_TO_DATE(@data_registro, '%d/%m/%Y'),
 vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
 vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');



-- 2024_T1
LOAD DATA LOCAL INFILE "C:/Users/bolac/OneDrive/Área de Trabalho/Teste_Nivelamento_Augusto_Ramos/outros/csv/1T2024.csv"
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, reg_ans, cd_conta_contabil, descricao, 
 @vl_saldo_inicial, @vl_saldo_final)
SET 
 vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
 vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');


-- 2024_T2
LOAD DATA LOCAL INFILE "C:/Users/bolac/OneDrive/Área de Trabalho/Teste_Nivelamento_Augusto_Ramos/outros/csv/2T2024.csv"
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, reg_ans, cd_conta_contabil, descricao, 
 @vl_saldo_inicial, @vl_saldo_final)
SET 
 vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
 vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');


-- 2024_T3
LOAD DATA LOCAL INFILE "C:/Users/bolac/OneDrive/Área de Trabalho/Teste_Nivelamento_Augusto_Ramos/outros/csv/3T2024.csv"
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, reg_ans, cd_conta_contabil, descricao, 
 @vl_saldo_inicial, @vl_saldo_final)
SET 
 vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
 vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');


-- 2024_T4
LOAD DATA LOCAL INFILE "C:/Users/bolac/OneDrive/Área de Trabalho/temp/4T2024.csv"
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, reg_ans, cd_conta_contabil, descricao, 
 @vl_saldo_inicial, @vl_saldo_final)
SET 
 vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
 vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');


-- Operadoras ativas (só 1 arquivo)
LOAD DATA LOCAL INFILE "C:/Users/bolac/OneDrive/Área de Trabalho/temp/dados.csv"
INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(reg_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, @regiao_de_comercializacao, data_registro_ans)
SET 
  regiao_de_comercializacao = NULLIF(@regiao_de_comercializacao, '');
