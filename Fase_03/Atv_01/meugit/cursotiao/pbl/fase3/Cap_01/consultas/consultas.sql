-- =========================================================
-- PROJETO FASE 3 - CONSULTAS SQL
-- Banco Oracle - Dados Sensores Agrícolas
-- =========================================================


-- =========================================================
-- 1. CONSULTA GERAL DOS DADOS
-- Objetivo:
-- Exibir todos os registros importados da tabela.
-- =========================================================

SELECT * 
FROM DADOS_SENSORES;



-- =========================================================
-- 2. MÉDIA DAS PRINCIPAIS VARIÁVEIS
-- Objetivo:
-- Calcular médias de umidade, pH e precipitação.
-- =========================================================

SELECT 
    AVG(umidade) AS media_umidade,
    AVG(ph) AS media_ph,
    AVG(precipitacao) AS media_precipitacao
FROM DADOS_SENSORES;



-- =========================================================
-- 3. QUANTIDADE DE REGISTROS COM IRRIGAÇÃO
-- Objetivo:
-- Contar quantos registros possuem irrigação ativa (1)
-- e desativada (0).
-- =========================================================

SELECT 
    irrigacao,
    COUNT(*) AS total
FROM DADOS_SENSORES
GROUP BY irrigacao;



-- =========================================================
-- 4. RELAÇÃO ENTRE PRECIPITAÇÃO E IRRIGAÇÃO
-- Objetivo:
-- Visualizar os dados organizados pela maior precipitação.
-- =========================================================

SELECT 
    precipitacao,
    irrigacao
FROM DADOS_SENSORES
ORDER BY precipitacao DESC;



-- =========================================================
-- 5. CASOS DE BAIXA UMIDADE
-- Objetivo:
-- Identificar solos com umidade abaixo de 40.
-- =========================================================

SELECT *
FROM DADOS_SENSORES
WHERE umidade < 40;



-- =========================================================
-- 6. SOLOS ÁCIDOS (PH BAIXO)
-- Objetivo:
-- Identificar registros com pH abaixo de 6.
-- =========================================================

SELECT *
FROM DADOS_SENSORES
WHERE ph < 6;



-- =========================================================
-- 7. SOLOS COM TODOS OS NUTRIENTES (NPK)
-- Objetivo:
-- Exibir registros onde N, P e K possuem valor 1.
-- =========================================================

SELECT *
FROM DADOS_SENSORES
WHERE n = 1
  AND p = 1
  AND k = 1;



-- =========================================================
-- 8. MÉDIA DE UMIDADE POR STATUS DE IRRIGAÇÃO
-- Objetivo:
-- Comparar a média de umidade entre registros irrigados
-- e não irrigados.
-- =========================================================

SELECT 
    irrigacao,
    AVG(umidade) AS media_umidade
FROM DADOS_SENSORES
GROUP BY irrigacao;



-- =========================================================
-- 9. TOP 5 MAIORES PRECIPITAÇÕES
-- Objetivo:
-- Mostrar os 5 registros com maior precipitação.
-- =========================================================

SELECT *
FROM DADOS_SENSORES
ORDER BY precipitacao DESC
FETCH FIRST 5 ROWS ONLY;



-- =========================================================
-- 10. DADOS COM UMIDADE EQUILIBRADA
-- Objetivo:
-- Exibir registros com umidade entre 40 e 60.
-- =========================================================

SELECT *
FROM DADOS_SENSORES
WHERE umidade BETWEEN 40 AND 60;



-- =========================================================
-- 11. VERIFICAR ESTRUTURA DA TABELA
-- Objetivo:
-- Mostrar colunas e tipos de dados da tabela.
-- =========================================================

DESC DADOS_SENSORES;



-- =========================================================
-- 12. CRIAR NOVA COLUNA DECIMAL PARA PH
-- Objetivo:
-- Criar uma coluna decimal para corrigir os valores do pH.
-- =========================================================

ALTER TABLE DADOS_SENSORES
ADD ph_decimal NUMBER(4,2);



-- =========================================================
-- 13. CONVERTER PH INTEIRO PARA DECIMAL
-- Objetivo:
-- Corrigir os valores de pH dividindo por 10.
-- Exemplo:
-- 65 -> 6.50
-- =========================================================

UPDATE DADOS_SENSORES
SET ph_decimal = ph / 10.0;



-- =========================================================
-- 14. VALIDAR CORREÇÃO DO PH
-- Objetivo:
-- Comparar os valores antigos e novos do pH.
-- =========================================================

SELECT 
    ph,
    ph_decimal
FROM DADOS_SENSORES;



-- =========================================================
-- 15. REMOVER COLUNA PH ANTIGA (OPCIONAL)
-- Objetivo:
-- Excluir a coluna antiga após validação da correção.
-- =========================================================

ALTER TABLE DADOS_SENSORES
DROP COLUMN ph;



-- =========================================================
-- 16. RENOMEAR NOVA COLUNA PARA PH
-- Objetivo:
-- Renomear a coluna corrigida para manter o nome original.
-- =========================================================

ALTER TABLE DADOS_SENSORES
RENAME COLUMN ph_decimal TO ph;



-- =========================================================
-- 17. SALVAR ALTERAÇÕES NO BANCO
-- Objetivo:
-- Confirmar permanentemente as alterações realizadas.
-- =========================================================

COMMIT;