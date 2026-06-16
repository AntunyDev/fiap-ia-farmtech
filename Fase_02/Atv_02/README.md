<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="https://raw.githubusercontent.com/agodoi/templateFiapVfinal/main/assets/logo-fiap.png" alt="FIAP Logo" width="200">
  </a>
</p>

# 🚜 FarmTech Cana - Inteligência na Gestão de Colheitas

## 👨‍🎓 Integrantes: 
- **Antuny Marques**
- **Tiago Gonçalves**
- **Carlos Ribeiro** 
- **Lucas** 
- **Anderson**

## 👩‍🏫 Professores:
### Tutor(a) 
- **Nicolly**
### Coordenador(a)
- **André Godoi**

---

## 📜 Descrição - Contexto e Problema

O Brasil é o líder mundial na produção de cana-de-açúcar, alcançando recordes que ultrapassam **620 milhões de toneladas** por safra. No entanto, o setor enfrenta um desafio crítico: **as perdas na colheita**.

Estudos indicam que, enquanto na colheita manual as perdas raramente passam de **5%**, na colheita mecânica esse índice sobe drasticamente para **15%**. Esse gap de produtividade representa um prejuízo astronômico: apenas no estado de São Paulo, estima-se uma perda anual de **R$ 20 milhões**.

Para combater esse cenário, o produtor precisa de estratégias de monitoramento precisas, planejamento eficiente e análise de dados em tempo real para otimizar o uso de colhedoras e reduzir o desperdício.

## 💡 A Solução: FarmTech Cana

O **FarmTech Cana** surge como uma ferramenta de **Agrotech** focada em transformar dados de campo em decisões estratégicas. O sistema permite ao gestor rural:

1.  **Monitorar Precisamente**: Registrar cada colheita, comparando a produtividade esperada com a real.
2.  **Identificar Gargalos**: Calcular automaticamente o percentual de perda e o prejuízo financeiro causado por ineficiências.
3.  **Alertar Desvios**: O sistema emite avisos imediatos quando as perdas ultrapassam as referências técnicas (5% para manual e 15% para mecânico).
4.  **Análise Comparativa**: Gerar relatórios que permitem avaliar se a mecanização está operando dentro dos padrões de eficiência ou se necessita de ajustes.

---

## 🛠️ Funcionalidades Técnicas

Desenvolvido para gerenciar a cadeia produtiva, o sistema integra:
- **Gestão de Talhões**: Cadastro completo com UUID, variedades de cana e área produtiva.
- **Registro de Colheitas**: Entrada de dados com validação rigorosa para evitar erros.
- **Relatórios Avançados**: Tabelas organizadas no terminal para visualização de ineficiências.
- **Base de Dados Robusta**: Persistência dupla via **JSON** (local) e **Oracle Database** (corporativo).
- **Logs de Auditoria**: Registro de todas as operações em arquivo de texto.

---

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Arquivos de configuração específicos do GitHub.
- <b>assets</b>: Imagens e elementos visuais.
- <b>config</b>: Arquivos de configuração (`.env` e `requirements.txt`).
- <b>documents</b>: Documentação e arquivos de dados (`dados.json`). Na subpasta "other", estão os logs.
- <b>scripts</b>: Scripts auxiliares.
- <b>src</b>: Todo o código fonte (`main.py` e módulos).
- <b>README.md</b>: Guia geral do projeto.

---

## 🎨 Interface e Usabilidade (Tema Verde e Amarelo)

O sistema oferece uma experiência de **Agrotech moderna**:
- **Interface Visual**: Uso da biblioteca Rich com paleta Verde e Amarelo.
- **Limpeza de Fluxo**: Terminal otimizado com limpeza automática de tela.
- **Tabelas Organizadas**: Visualização clara de dados complexos.

---

## ⚙️ Instalação e Execução

### Pré-requisitos
- **Python 3.10+**
- **Oracle Instant Client** configurado.

### Passo a Passo

1. **Instale as dependências:**
   ```bash
   py -m pip install -r config/requirements.txt
   ```

2. **Execute o sistema:**
   A partir da raiz do projeto:
   ```bash
   py src/main.py
   ```

---

## ✅ Atendimento aos Requisitos da Atividade (Cap. 3 ao 6)

Este projeto foi desenhado sob medida para atender a todos os critérios da avaliação de **Gestão do Agronegócio em Python**:

- [x] **Área do Agronegócio Clara:** Foco no monitoramento e redução de perdas na colheita mecanizada de cana-de-açúcar (dor real de mercado estipulada no README).
- [x] **Subalgoritmos:** Uso extensivo de funções e procedimentos com passagem de parâmetros. 
  - *Exemplo:* `calcular_perda(producao_esperada, perda_percentual)` em `colheitas.py` retornando os cálculos operacionais e `listar_talhoes(talhoes)` atuando como procedimento de fluxo.
- [x] **Estruturas de Dados Abordadas:**
  - **Dicionários e Tabelas de Memória:** O estado completo transita na memória antes de ser salvo (ex: `estado = {"talhoes": {}, "colheitas": [], "historico": []}`).
  - **Listas:** Armazenamento em array das colheitas globais.
  - **Tuplas:** Garantindo a integridade e prevenindo alterações no código estático com constantes como `VARIEDADES_CANA` e `METODOS_COLHEITA`.
- [x] **Manipulação de Arquivos (Texto e JSON):** O estado possui persistência de arquivos.
  - *JSON:* Consolidado transacional armazenado na raiz em `dados.json`.
  - *Texto:* Tracking de log da aplicação em modo *append* no arquivo texto `log.txt`.
- [x] **Conexão com Banco de Dados Oracle:** O módulo `banco.py` gerencia a ingestão chamando a biblioteca `oracledb`, isolando as variáveis `.env` e utilizando conceito de `MERGE` em SQL para evitar replicação de dados.
- [x] **Consistir as Entradas do Usuário:** Impossibilita o usuário quebrar o app ao digitar letras ou formatações indesejadas em perguntas, os métodos `_validar_float` limitam inclusive tamanhos `min / max` via exceções nativas.
- [x] **Apresentação Limpa (Usabilidade):** Com base técnica sólida pela importação da framework **Rich**, as impressões deixam a caótica visualização padrão de prompt e assumem um grid profissional, limpo (graças as limpezas de stdout de terminal) com o esquema visual baseado em cores padronizadas Agro.

---

## 🗃 Histórico de lançamentos
* **0.1.3 - 20/04/2026**
    * Atualização do README.md.
* **0.1.2 - 14/04/2026**
    * Implementação da lógica de gestão e interface Rich.
    * Estruturação simplificada com foco em usabilidade.
* **0.1.1 - 13/04/2026**
    * Melhorias na lógica e funcionalidades gerais.
    * Correção de erros e bugs e adição de validação de entradas de dados.
* **0.1.0 - 12/04/2026**
    * Desenvolvimento Inicial do projeto, estruturação e planejamento.
    * Desenvolvimentos das Principais funções.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
