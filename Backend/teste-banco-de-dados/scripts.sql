
CREATE TABLE operadoras (
    registro_ans INT PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(10),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email_representante VARCHAR(255),
    nome_representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    regiao INT,
    data_registro DATE
);


CREATE TABLE demonstrativos_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    reg_ans INT,
    cd_conta VARCHAR(50),
    descricao VARCHAR(255),
    vl_saldo DECIMAL(18,2),
    vl_saldo_final DECIMAL(18,2),
    FOREIGN KEY (reg_ans) REFERENCES operadoras(registro_ans)
);


LOAD DATA LOCAL INFILE 'C:\\Users\\jeffe\\documents\\teste-estagio\\Backend\\Relatorio_cadop.csv' 
INTO TABLE operadoras
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:\\Users\\jeffe\\documents\\teste-estagio\\Backend\\1T2024.csv' 
INTO TABLE demonstrativos_contabeis
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS;

-- Consulta para as 10 operadoras com maiores despesas nos últimos 3 meses
SELECT reg_ans, SUM(vl_saldo) AS total_despesas
FROM demonstrativos_contabeis
WHERE descricao LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
AND data >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
GROUP BY reg_ans
ORDER BY total_despesas DESC
LIMIT 10;

-- Consulta para as 10 operadoras com maiores despesas no último ano
SELECT reg_ans, SUM(vl_saldo) AS total_despesas
FROM demonstrativos_contabeis
WHERE descricao LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
AND data >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY reg_ans
ORDER BY total_despesas DESC
LIMIT 10;
