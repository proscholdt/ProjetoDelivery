<h1> Projeto - Delivery Center </h1>

<h2> A ideia deste projeto é desenvolver um Relatório em Power BI sobre os indicadores solicitados. </h2>

**Ferramentas utilizadas:**  
Python   
Google Big Query
FIGMA  
Power Bi

<hr>

**Primeira Etapa**

Pré-tratamento de dados utilizando Python para que a base suporte a importação para o google big query.

Em Python utilizando a biblioteca pandas para carregar um arquivo CSV contendo dados de pedidos, onde várias colunas representam momentos de tempo em formato AM/PM. O objetivo é converter esses tempos para o formato de 24 horas. Uma função chamada convert_to_24h é definida para realizar essa conversão, verificando se o horário é AM ou PM e ajustando adequadamente. Essa função é então aplicada a cada coluna relevante no DataFrame. Após a conversão, o DataFrame atualizado é salvo em um novo arquivo CSV.


<div display = "inline">
          <img src="C:\Users\henrique\Desktop\xxxxxxx.png" /> 
          <hr>
</div>

<hr>

**Segunda Etapa**  

Criar a data-base no GOOGLE BIG QUERY, criar tabelas dimensão e tabela fato e adicionar dados.  

Nessa etapa vamos utilizar o GOOGLE BIG QUERY para criar a data-base contendo as tabelas do nosso conjunto.  


<div display = "inline">
          <img src="C:\Users\henrique\Desktop\yyyyyyyyy.png" /> 
</div>

<hr>

**Terceira Etapa**

Conectar o Power BI ao google big query
Fazer o tratamento de dados utilizando power query
Nessa etapa foram feitas tranformações em linguagem M, as tranformações estão disponiveis no arquivo .pbix anexo neste documento.
Foram realizadas as tarefas de:
Mesclagem de colunas, Remoção de duplicatas, desenvovimento de tabela calendario, tratamento de valores em braco,  entre outros presentes no arquivo.

<hr>

**Quarta Etapa**
Adequação do relacionamento estre as tabelas.

<div display = "inline">
          <img src="C:\Users\henrique\Desktop\zzzzzz.png" /> 
</div>

<hr>

**Quinta Etapa**

Desenvolvimento de Medidas Dax, as medidas estão presentes no arquivos .pbix, com nomeclatura de facil entendimento e devidamente comentadas. 

<hr>

**Sexta Etapa**

Eleboração de Storytelling e desenvolvimento de desing utilizando FIGMA.


<hr>

<hr>
