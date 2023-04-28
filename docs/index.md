<table>
<tr>
<td>
<a href= "https://www2.gerdau.com.br/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Gerdau_logo_%282011%29.svg/1200px-Gerdau_logo_%282011%29.svg.png" alt="Gerdau" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

<font size="+12"><center>

</center></font>

# Análise Financeira

## Custos:

  - Custo do hardware (TurtleBot, Raspberry Pi 3, câmera DobotMagical, sensores de gases)
    - TutleBot + raspberry Pi 3 -> R$17000/robo
    - Sensores de gases -> R$400/robo
    - Camera -> R$400/robo
  - Custos de mão de obra (desenvolvimento de software, montagem, testes)
    - 2 Meses; equipe de 3 engenheiros -> R$51000 (fonte: Glassdoor)
    - Implementação do projeto (1 engenheiro) -> R$8.500/local (fonte: Glassdoor)
  - Custos de manutenção e atualização do software
    - Alocação da aplicação WEB - R$60.000/ano
    - Manutenção Hardware - R$1000/ano*robo
    - Custo Operacional - R$5000/ano*robo

## Receitas:

  - Redução de custos com acidentes operacionais;
  - Melhoria da eficiência operacional.

- Para estimar os valores específicos para cada aspecto, é necessário ter acesso aos dados financeiros da Gerdau, incluindo o histórico de custos relacionados a acidentes operacionais e a eficiência operacional antes e depois da implementação do robô. Como não temos acesso a estes dados faremos uma estimativa destes valores.
  
- Assumiremos que a Gerdau tem um custo anual médio de 0,001% do faturamento total com acidentes operacionais, o que em 2020 seria R$ 43,81M(<a href="https://valor.globo.com/empresas/noticia/2021/02/24/lucro-da-gerdau-sobe-939percent-no-quarto-trimestre.ghtml">*valor*</a>). Esse custo incluiria processos trabalhistas, perda de protução, custos de manutenção de espaço e equipamentos, etc.

- Com a implementação do robo, esperamos previnir 90% dos assidentes, sendo assim, podemos projetar uma economia anual de R$ 3.942.900,00.

## Análise do Investimento:

- A Gerdau tem sedes industriais em 9 países, nas Américas, mas consideraremos a implementação apenas para as unidades no Brasil. Segundo o site oficial da empresa, a Gerdau tem 25 usinas siderúrgicas, 10 unidades de transformação e corte e dobra, 2 unidades de mineração e 2 unidades de aços em territorio nacional. Cosiderando que para obter o resultado desejado fosse nessario a implementação de 1 robo por unidade, devem ser produzidos 39 robos, o que exigiria um investimento incial de R$1.076.700,00. Para o matimento da solução estimasse um gasto anual de R$338.100,00 incluindo manutenção, custos operacionais e uma margem de aproximadamente 15% para possiveis problemas. A receita esperada com o projeto, como descrito anteriormente, é de R$3.942.900,00/ano, ou seja, é esperado já no primeiro ano um lucro de R$2.528.100,00. #(custo anual - receita anual)

# Matriz de Riscos:

![Matriz de Riscos](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/matriz_de_riscos.png)

- Uma matriz de riscos é uma ferramenta visual utilizada para identificar e avaliar os riscos associados a um projeto, processo ou atividade. Ela é composta por duas dimensões: a primeira representa a probabilidade de ocorrência de um risco, geralmente classificada em baixa, média ou alta; a segunda dimensão representa o impacto que o risco pode ter caso ocorra, também classificado em baixo, médio ou alto. A matriz de riscos é uma ferramenta muito útil para a gestão de riscos, pois permite que os riscos sejam priorizados de acordo com sua probabilidade de ocorrência e impacto, facilitando a tomada de decisão sobre quais riscos devem ser tratados primeiro.

## Matriz de Riscos ( ***Abordagens*** ):

- Falta de conhecimento prévio sobre o projeto: Como plano de ação para esse risco nós, como estudantes do Inteli que estamos desenvolvendo o projeto, vamos nos comprometer fazer todos os autoestudos necessários para cumprir com excelência todas as regras de negócio propostas pelo parceiro para o projeto.

- Manutenabilidade do Hardware: como estamos lidando com uma implementação física ela está estará exposta as intempéries que podem diminuir a vida útil dos seus componentes.

- Falhas de comunicação na equipe que está desenvolvendo o projeto: Aplicaremos derivações da metodologia ágil para manter a comunicação entre os membros do grupo sempre alinhada, pensando sempre no consenso entre as partes.

- Falhas de comunicação na trasmissão de dados: Estudaremos formas de manter a comunicação via wifi o mais estável possível, pensando na melhor eficiência dos sistema implementado.

- Faltas de resistência do harware à ambientes hostis: O sistema deve resistir a possíveis condições hostis como, por exemplo, condições de temperaturas diferentes da ambiente.

- Aumento exagerado do escopo do projeto: Pensando em conciliar o estudo necessário para desenvolver o projeto e o próprio desenvolvimento do projeto, deve-se tomar cuidado com as features que nós, como grupo que estamos desenvolvendo o projeto, iremos construir de forma que sejá entregue a melhor solução, pensando inclusive nos pontos anteriormente citados.

- O vazamento eletrostático ou outro tipo de reação que pode colocar o gás dentro do duto em combustão: Iremos isolar os circuitos para mitigar esse problema.

# Analise Financeira

![Investimento Inicial](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/Investimento_Incial.png)

![Economia](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/Receita.png)

![Despesas](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/Despesas_Anuais.png)

![Analise do Investimento](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/Analise_Financeira.png)

<a href="https://docs.google.com/spreadsheets/d/1lK-txT79qHuZfYMwxpR1C5zox9V9MTNEQukWj-0ohFg/edit?usp=sharing">Planilha<a>
