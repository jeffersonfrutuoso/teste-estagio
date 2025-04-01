
CREATE TABLE operadoras (
    Registro_ANS INT PRIMARY KEY,
    CNPJ VARCHAR(20),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(100),
    Logradouro VARCHAR(255),
    Numero VARCHAR(10),
    Complemento VARCHAR(255),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP VARCHAR(10),
    DDD VARCHAR(5),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    Regiao_de_Comercializacao INT,
    Data_Registro_ANS DATE
);


CREATE TABLE demonstrativos_contabeis (
    DATA_STR DATE,
    REG_ANS INT,
    CD_CONTA_CONTABIL VARCHAR(50),
    DESCRICAO VARCHAR(255),
    VL_SALDO_INICIAL DECIMAL(18,2),
    VL_SALDO_FINAL DECIMAL(18,2),
    FOREIGN KEY (REG_ANS) REFERENCES operadoras(Registro_ANS) ON DELETE CASCADE
);


LOAD DATA LOCAL INFILE 'C:\\Users\\jeffe\\documents\\teste-estagio\\Backend\\teste-banco-de-dados\\Relatorio_cadop.csv' 
INTO TABLE operadoras
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS;


LOAD DATA LOCAL INFILE 'C:\\Users\\jeffe\\documents\\teste-estagio\\Backend\\teste-banco-de-dados\\1T2024_cleaned.csv' 
INTO TABLE demonstrativos_contabeis
FIELDS TERMINATED BY ';'  
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS;



-- Consulta para as 10 operadoras com maiores despesas nos últimos 3 meses
SELECT REG_ANS, SUM(VL_SALDO_INICIAL) AS total_despesas
FROM demonstrativos_contabeis
WHERE descricao LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
AND DATA_STR >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
GROUP BY REG_ANS
ORDER BY total_despesas DESC
LIMIT 10;

-- Consulta para as 10 operadoras com maiores despesas no último ano
SELECT REG_ANS, SUM(VL_SALDO_INICIAL) AS total_despesas
FROM demonstrativos_contabeis
WHERE descricao LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
AND DATA_STR >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY REG_ANS
ORDER BY total_despesas DESC
LIMIT 10;





