CREATE DATABASE ans_dados;
USE ans_dados;
SET GLOBAL local_infile = 1;
  
CREATE TABLE demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reg_ans VARCHAR(6) NOT NULL,
    cd_conta_contabil VARCHAR(12) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    vl_saldo_inicial DECIMAL(15, 2) NOT NULL,
    vl_saldo_final DECIMAL(15, 2) NOT NULL, 
    data_registro DATE NOT NULL
);


CREATE TABLE operadoras_ativas (
	id INT AUTO_INCREMENT PRIMARY KEY,
	reg_ans VARCHAR(6),
    cnpj VARCHAR(14),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255) NULL,
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(100),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(8),
    ddd VARCHAR(2) NULL,
    telefone VARCHAR(40) NULL,
    fax VARCHAR(255) NULL,
    endereco_eletronico VARCHAR(100),
    representante VARCHAR(100),
    cargo_representante VARCHAR(100),
    regiao_de_comercializacao INTEGER NULL,
    data_registro_ans DATE
);
SHOW VARIABLES LIKE 'local_infile';