# 🌱 FarmTech Solutions — Fase 3: Banco de Dados Oracle

## 📋 Descrição do Projeto

Este repositório faz parte do PBL (Project-Based Learning) do curso de Inteligência Artificial, simulando o crescimento da startup fictícia **FarmTech Solutions**, uma consultoria de soluções para o agronegócio.

Nesta fase, os dados coletados pelos sensores agrícolas da Fase 2 foram carregados em um banco de dados relacional **Oracle**, utilizando o **Oracle SQL Developer** para criação da tabela, importação dos dados e execução de consultas SQL.

---

## 👥 Integrantes do Grupo

| Nome | RM |
|---|---|
| Antuny Marques | RM573852 |
| Tiago Gonçalves | RM570935 |
| Carlos Ribeiro | RM571449 |
| Lucas Ribeiro | RM572508 |
| Anderson Sapucaia | RM571668 |

---

## 🗂️ Estrutura do Repositório

```text
meugit/cursotiao/pbl/fase3/
├── Cap_01/
│   ├── consultas/
│   │   ├── codigo_usado.py
│   │   └── consultas.sql
│   ├── dados/
│   │   └── base_dados.csv
│   └── prints/
│       └── (19 capturas de tela)
└── Cap_10/
    ├── AntunyMarques_RM573852_fase3_cap1.ipynb
    ├── produtos_agricolas.csv
    └── README.md
```

---

## 🛠️ Tecnologias Utilizadas

- **Oracle Database XE** — banco de dados relacional
- **Oracle SQL Developer** — interface gráfica para gerenciamento do banco
- **SQL** — linguagem de consulta utilizada

---

## 🗄️ Conexão e Estrutura da Tabela

A conexão com o banco de dados Oracle foi estabelecida com sucesso através do Oracle SQL Developer, permitindo o gerenciamento e a criação do nosso schema.

📸 **Conexão ao Banco de Dados**
![Conexão Banco de Dados](meugit/cursotiao/pbl/fase3/Cap_01/prints/conexao_banco_dados_sql_oracle_developer.png)

---

## 📥 Importação e Origem dos Dados (Fase 2)

Os dados utilizados nesta Fase 3 foram originalmente simulados e coletados pelos sensores desenvolvidos na Fase 2. Toda a lógica de simulação física e os códigos-fonte em Python e C/C++ (para microcontroladores IoT/Arduino) estão documentados e hospedados no repositório oficial anterior:

🔗 **[Repositório FarmTech - Cana (Fase 2)](https://github.com/lstrefezza/1TIAOA-2026-fase2-cap1)**

O arquivo resultante dessa coleta, contendo 40 registros detalhados das variáveis de solo (umidade, pH, NPK, precipitação e status de irrigação), foi exportado como `base_dados.csv` e serviu como base de dados para a importação e modelagem no banco de dados Oracle nesta Fase 3. Como ponte de referência, o arquivo [codigo_usado.py](meugit/cursotiao/pbl/fase3/Cap_01/consultas/codigo_usado.py) aponta diretamente para essa origem.

📸 **Importação de Dados Concluída com Sucesso**
![Importação dados com sucesso](meugit/cursotiao/pbl/fase3/Cap_01/prints/importacao_dados_com_sucesso.png)

📸 **Amostragem dos Dados Importados**
![Amostragem dados importados](meugit/cursotiao/pbl/fase3/Cap_01/prints/amostragem_dados_sensores_importados.png)

---

A tabela `sensores` foi criada inicialmente. Durante o processo, identificamos a necessidade de refinar o tipo de dado do pH.

### ⚙️ Ajustes na Tabela (Tratamento da coluna pH)

Para garantir maior precisão nos registros de acidez do solo, foi realizado um processo de migração da coluna de pH de inteiro para decimal (`NUMBER(4,2)`):

1. **Criação da nova coluna decimal:**
![Criação nova coluna pH decimal](meugit/cursotiao/pbl/fase3/Cap_01/prints/criacao_nova_coluna_ph_decimal.png)

2. **Conversão e cópia dos valores da coluna antiga para a nova:**
![Conversão valores nova coluna pH decimal](meugit/cursotiao/pbl/fase3/Cap_01/prints/conversao_valores_nova_coluna_ph_decimal.png)

3. **Conferência dos valores atualizados:**
![Conferência valores pH decimal](meugit/cursotiao/pbl/fase3/Cap_01/prints/confericao_valores_ph_decimal.png)

4. **Exclusão da coluna antiga (inteiro):**
![Exclusão coluna pH inteiro](meugit/cursotiao/pbl/fase3/Cap_01/prints/exclusao_coluna_ph_inteiro.png)

5. **Renomeação da nova coluna para o nome original (`ph`):**
![Renomeação pH decimal](meugit/cursotiao/pbl/fase3/Cap_01/prints/renomeacao_ph_decimal.png)

6. **Efetivação das alterações (Commit):**
![Commit pH decimal](meugit/cursotiao/pbl/fase3/Cap_01/prints/commit_ph_decimal.png)


## 🔍 Consultas SQL Realizadas (Insights)

Abaixo estão listadas as consultas realizadas no banco de dados para a obtenção de insights sobre as condições do solo e as regras de irrigação.

### 1. Consulta Básica Geral
Retorna todos os registros da tabela `sensores`, permitindo verificar a integridade geral dos dados.
![Consulta Básica Geral](meugit/cursotiao/pbl/fase3/Cap_01/prints/consulta_basica_geral.png)

### 2. Média das Variáveis
Analisa as médias gerais de umidade, pH e precipitação.
![Consulta Média Variáveis](meugit/cursotiao/pbl/fase3/Cap_01/prints/consulta_media_variaveis.png)

### 3. Média de Irrigação por Umidade
Avalia a relação entre o nível de umidade do solo e o acionamento médio do sistema de irrigação.
![Média Irrigação por Umidade](meugit/cursotiao/pbl/fase3/Cap_01/prints/media_irrigacao_por_umidade.png)

### 4. Relação Irrigação vs Precipitação
Compara os dados de chuva (precipitação) com a ativação da irrigação, mostrando se a precipitação natural foi suficiente ou se precisou de irrigação artificial.
![Irrigação x Precipitação](meugit/cursotiao/pbl/fase3/Cap_01/prints/consulta_irrigacao_x_precipitacao.png)

### 5. Casos Críticos (Baixa Umidade)
Identifica situações críticas onde a umidade está muito baixa, exigindo atuação severa do sistema de irrigação.
![Consulta Baixa Umidade](meugit/cursotiao/pbl/fase3/Cap_01/prints/consulta_baixa_umidade_casos_criticos.png)

### 6. Registros que Necessitam de Irrigação
Contabiliza e filtra quantos registros específicos demandaram a ativação do sistema de irrigação (`irrigacao = 1`).
![Registros necessitam irrigação](meugit/cursotiao/pbl/fase3/Cap_01/prints/consulta_quantos_registros_necessitam_irrigacao.png)

### 7. Solos com Nível de Acidez Elevado (Solo Ácido)
Filtra os sensores onde o pH apresentou características de alta acidez, o que pode requerer correção (calagem).
![Consulta Solo Ácido](meugit/cursotiao/pbl/fase3/Cap_01/prints/consulta_solo_acido.png)

### 8. Solos com Todos os Nutrientes (N, P, K)
Busca por amostras ideais de solo, onde a presença de Nitrogênio (N), Fósforo (P) e Potássio (K) é satisfatória.
![Solo com todos nutrientes](meugit/cursotiao/pbl/fase3/Cap_01/prints/consulta_solo_com_todos_nutrientes.png)

### 9. Top 5 Maiores Precipitações
Lista os 5 registros com o maior volume de chuva (precipitação) identificado pelos sensores.
![Top 5 Maiores Precipitações](meugit/cursotiao/pbl/fase3/Cap_01/prints/top_5_maiores_precipitacoes.png)

### 10. Consulta de Dados Equilibrados
Identifica amostras onde o solo se encontra em condições ideais e equilibradas, com boa umidade, pH neutro e nutrientes presentes, dispensando a necessidade de irrigação.
![Consulta Dados Equilibrados](meugit/cursotiao/pbl/fase3/Cap_01/prints/consulta_dados_equilibrados.png)

---

## 📊 Principais Achados

- O sistema demonstra eficácia lógica: a irrigação está sendo ativada majoritariamente em momentos de **baixa umidade** e **baixa precipitação**.
- Foram identificadas amostras em condições **críticas** de baixa umidade, atestando a importância do monitoramento contínuo.
- A presença simultânea de macronutrientes (N, P, K) não foi registrada em todas as amostras, indicando possíveis áreas que demandariam adubação na vida real.
- As consultas mostram variações reais nos níveis de pH, onde casos de solo ácido foram claramente detectados, evidenciando a utilidade da mudança do tipo de dado de inteiro para decimal.

---

## 🎥 Vídeo Demonstrativo

📺 [Link do vídeo no YouTube](https://youtu.be/lCSyHjeVvOY)

> O vídeo demonstra o funcionamento do banco de dados, a execução das consultas no
> Oracle SQL Developer e a organização do repositório GitHub.

---

## 📚 Referências

- [Oracle SQL Developer Documentation](https://docs.oracle.com/en/database/oracle/sql-developer/)
- Global AI Jobs Barometer — PwC (2025)
- Material didático do curso de Inteligência Artificial — FIAP

---

*FarmTech Solutions — Fase 3 | Curso de Inteligência Artificial*
