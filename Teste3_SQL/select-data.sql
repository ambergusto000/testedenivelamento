SELECT 
    o.razao_social,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras_ativas o ON d.reg_ans = o.reg_ans
WHERE d.data_registro >= '2024-10-01' AND d.data_registro <= '2024-12-31'
AND d.descricao LIKE 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE' 
GROUP BY o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;


SELECT 
    o.razao_social,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras_ativas o ON d.reg_ans = o.reg_ans
WHERE YEAR(d.data_registro) = 2024
AND d.descricao LIKE 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE' 
GROUP BY o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;
