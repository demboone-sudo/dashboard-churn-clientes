# 📊 Dashboard Interativo: Análise de Retenção de Clientes (Churn Bancário)

## 🎯 O Problema de Negócio
A retenção de clientes é um dos maiores desafios do setor financeiro. Este projeto analisa uma base de dados com mais de 10.000 clientes de um banco para entender o comportamento daqueles que cancelaram seus cartões de crédito (Churn) em comparação aos que permaneceram ativos. 

O objetivo foi sair dos dados brutos e entregar um **painel interativo (Dashboard)** com insights acionáveis para as equipes de Marketing e Relacionamento.

## 💡 Principais Insights e Soluções Propostas
Através da análise exploratória, identifiquei 6 padrões críticos de cancelamento:

1. **A Regra dos Contatos:** Clientes que entram em contato com o banco 3 vezes ou mais têm uma taxa de cancelamento alarmante. 
   * *Ação:* Criar um gatilho no sistema para direcionar o cliente para uma equipe de retenção premium a partir do 3º contato.
2. **Engajamento de Produtos:** Clientes com apenas 1 ou 2 produtos contratados cancelam com muito mais facilidade do que aqueles com múltiplos produtos.
   * *Ação:* Oferecer benefícios para a contratação de um segundo produto (ex: isenção de anuidade) logo nos primeiros meses.
3. **Termômetro de Inatividade:** A probabilidade de churn dispara quando o cliente passa de 2 a 3 meses sem usar o cartão.
   * *Ação:* Disparar campanhas automatizadas de desconto (ex: iFood, Uber) no 2º mês de inatividade para reativar o uso.
4. **Volume de Transações:** Frequência importa mais que valor. Clientes que fazem menos de 40 transações no ano têm alto risco de evasão.
5. **Perfil Financeiro e Limite:** Existe uma correlação direta entre faixas salariais/limites de crédito específicos e a frustração do cliente, indicando que a concorrência pode estar oferecendo limites melhores para esse grupo.

## 🛠️ Tecnologias Utilizadas
Este projeto foi desenvolvido inteiramente em Python, com foco em manipulação de dados e criação de interfaces web rápidas:
* **[Python]** - Lógica principal.
* **[Pandas]** - Tratamento, limpeza (remoção de dados nulos e IDs) e manipulação da base de dados.
* **[Plotly Express]** - Geração de gráficos dinâmicos e interativos.
* **[Streamlit]** - Criação do Dashboard web responsivo.

## 🚀 Como Executar o Projeto
Se quiser rodar este dashboard na sua máquina, siga os passos abaixo:

1. Clone este repositório.
2. Certifique-se de ter o Python instalado.
3. Instale as dependências executando:
   ```bash
   pip install -r requirements.txt
   streamlit run analise.py
