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

<font size="+12"><center>
Simulação de robôs para aplicações diversas.
</center></font>

**Conteúdo**

- [Autores](#autores)
- [Visão Geral do Projeto](#visão-geral-do-projeto)
  - [Empresa](#empresa)
  - [O Problema](#problema)
  - [Objetivos](#objetivos)
    - [Objetivos gerais](#objetivos-gerais)
    - [Objetivos específicos](#objetivos-específicos)
    - [Escopo Macro](#escopo-macro)
  - [Partes interessadas](#partes-interessadas)
- [Análise do Problema](#análise-do-problema)
  - [Proposta de Valor: Value Proposition Canvas](#proposta-de-valor-value-proposition-canvas)
  - [Matriz de Risco](#matriz-de-risco)
  - [Matriz Oceano Azul](#matriz-oceano-azul)
  - [Análise Financeira](#análise-financeira)
- [Entendimento do Metadesign](#entendimento-do-metadesign)
  - [Fatores mercadológicos](#fatores-mercadologicos)
  - [Sistema produto/design](#sistema-produto/design)
  - [Sustentabilidade ambiental](#sustentabilidade-ambiental)
- [Arquitetura da Solução](#arquitetura-da-solução)
  - [Requisitos](#requisitos)    
  - [Arquitetura da Solução - Versão 1](#arquitetura-da-solução---versão-1)
- [Inteface web (frontend)](#interface-web-(frontend))
  - [Entradas e saídas](#entradas-e-saidas)
  - [Mockup](#mockup)
- [Referências](#referências)

# Autores

* Bianca Cassemiro
* Gabriel Pascoli
* Henrique Santos
* Jackson Aguiar
* Luana Parra
* Pablo Ruan
* Rafael Katalan

# Visão geral do projeto

## Empresa
Presente em 10 países, a Gerdau é pioneira no setor do aço na implantação de iniciativas de inovação digital. Esse é o resultado do trabalho conjunto de todos os mais de 30 mil colaboradores.
A Gerdau é a maior empresa Brasileira produtora de aço e uma das principais fornecedoras de aços longos nas Américas e de aços especiais no mundo. No Brasil, também produz aços planos e minério de ferro. Além disso, é a maior recicladora da América Latina e, no mundo, transforma, anualmente, milhões de toneladas de sucata em aço, reforçando seu compromisso com o desenvolvimento sustentável das regiões onde atua. As ações das empresas Gerdau estão listadas nas bolsas de valores de São Paulo (B3), Nova Iorque (NYSE) e Madri (Latibex).
## Problema
## Objetivos
### Objetivos gerais
### Objetivos específicos
### Escopo macro
Inicialmente, é esperado uma sensibilização da relevância do tema durante o curso. E as motivações para avançarmos no desenvolvimento de tecnologias disruptivas para redução da exposição a riscos. É desejável que os alunos tenham uma aula sobre algumas definições com relação a Segurança. (Ex: conceitos de Risco x Perigo,
conceitos de gerenciamento de riscos, prevenção de acidentes ie: barreiras físicas, sistêmicas).
É esperado deste projeto que os alunos desenvolvam, em simulação, um robô capaz de se locomover em um ambiente de espaço confinado e coletar informações do mesmo, sem a utilização de geolocalização. Este robô pode se locomover via superfície ou por vias aéreas em ambientes que necessitem dessa abordagem. A simulação pode ser feita através de simuladores computacionais em conjunto com o ROS (Robot Operating System). A simulação física do robô é um adicional desejável. 
Este robô poderá ser utilizado por operadores e mantenedores em atividades de espaço confinado, utilizado como ferramenta para diagnóstico preliminar da atividade.
A solução passará por uma avaliação de validação dos times de inovação, segurança e gestão de riscos. A solução também será apresentada aos líderes de negócio.
## Partes interessadas
- Inteli
- Gerdau

# Análise do problema

## Proposta de valor (Value Proposition Canvas)
O Canvas da Proposta de Valor é uma ferramenta que pode ajudar a criar e posicionar produtos ou serviço em torno do que o cliente realmente valoriza e precisa. É uma ferramenta que lhe ajuda a encontrar o encaixe produto-mercado de forma estruturada. Dessa maneira, ele é composto por 2 blocos: a Proposta de Valor e o Segmento de Clientes.

![Proposta de Valor](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/proposta%20de%20valor.png)

A partir da imagem acima, é possível descrever mais detalhadamente cada segmento do Value Propositions Canvas:

**Tarefas do cliente (Customer Job)**: Primeiramente, é preciso descrever o que os funcionários da Gerdau estão tentando fazer, podendo ser tarefas que estão tentando realizar ou completar, problemas que estão tentando resolver ou necessidades que estão tentando satisfazer. (Contratação de uma empresa terceirizada para fazer a inspeção do ambiente; Envio de um trabalhador para adentrar o espaço confinado, mesmo não tendo garantia de segurança do ambiente)

**Dores (Pains)**: Em seguida, descrevemos as emoções negativas, custos e situações indesejadas, riscos e outras experiências ruins que a Gerdau pode vivenciar antes, durante ou após as tarefas listadas anteriormente. (Riscos na operação de inspeção de ambientes inóspitos; Falta de eficiência na inspeção de tais ambientes; Falta de acurácia e precisão na coleta dos dados dos gases)

**Ganhos (Gains)**: Após as dores, descrevemos os benefícios que a Gerdau espera, deseja ou seria surpreendida positivamente se existisse, incluindo utilidade funcional, ganhos sociais, emoções positivas e redução de custos. (Aumento da eficiência na coleta de dados e inspeção da estrutura; Redução do tempo necessário para realizar as atividades, resultando em economia de tempo e recursos; Aumento da segurança do ambiente de trabalho, reduzindo o risco de acidentes, além de contribuir para uma melhor imagem da Gerdau)

**Produtos e serviços (Products and services)**: Com o perfil do consumidor já desenhado, listamos todos os produtos e serviços em que a proposta de valor esta baseada. (Robô capaz de se mover em ambientes de espaço confinado e inspecioná-lo; Sensores para coletar condições atmosféricas; Robô programado para ter uma rotina pré-definida; Software para processamento e análise de dados coletados pelo robô; Serviços de manutenção e suporte para o robô e o software)

**Aliviadores de dores (Pain Relievers)**: Em seguida, descrevemos como os produtos e serviços aliviam as dores da Gerdau, como eles eliminam ou reduzem emoções negativas, custos e situações indesejadas, riscos que eles vivenciam ou vivenciaram antes, durante ou depois de um job-to-be-done. (Redução de riscos e perigos, evitando acidentes e melhorando a segurança dos trabalhadores; Maior precisão e eficiência na coleta de dados, o que  reduz o tempo gasto e erros humanos, além de melhorar a qualidade das análises; Robô autônomo ou com sua movimentação controlada por um controle remoto)

**Criadores de ganho (Gain Creators)**: Por fim, descrevemos como nossos produtos e serviços criam ganhos para a Gerdau. (Reduzir o risco de acidentes dos trabalhadores; A partir da coleta de dados via sensores, ter a possibilidade de ajudar a identificar/mitigar riscos de segurança, como vazamento de gases tóxicos/combustíveis; Aumentar a eficiência do método de inspeção; Coleta de dados de forma mais precisa e consistente; Monitoramento em tempo real; Inovação tecnológica incremental; Solução econômica e sustentável para a manutenção e inspeção de estruturas)

## Matriz de Riscos
A matriz de riscos é uma ferramenta visual utilizada para identificar e avaliar os riscos associados a um projeto, processo ou atividade. Desse modo, ela é composta por duas dimensões: a primeira representa a probabilidade de ocorrência de um risco, geralmente classificada como baixa, média ou alta; a segunda dimensão representa o impacto que o risco pode ter, caso ocorra, também classificado como baixo, médio ou alto. Por fim, a matriz de riscos é muito útil para a gestão de riscos, pois permite priorizar os riscos de acordo com sua probabilidade e impacto, facilitando a tomada de decisão sobre quais riscos devem ser tratados primeiro.

![Matriz de Riscos](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/matriz_de_riscos.png)

### Abordagens:
- Falta de conhecimento prévio sobre o projeto: Como plano de ação para esse risco, nós, estudantes do Inteli desenvolvendo o projeto, nos comprometemos a realizar todos os estudos necessários para cumprir com excelência todas as regras de negócio propostas pelo parceiro para o projeto.

- Manutenabilidade do Hardware: Como estamos lidando com uma implementação física, ela estará exposta às intempéries que podem diminuir a vida útil de seus componentes. Como plano de ação para esse risco, vamos considerar opções de proteção do hardware.

- Falhas de comunicação na equipe que está desenvolvendo o projeto: Para mitigar esse risco, aplicaremos derivações da metodologia ágil para manter a comunicação entre os membros do grupo sempre alinhada e focada no consenso entre as partes. Além disso, definiremos claramente os papéis e responsabilidades de cada membro da equipe, a fim de evitar ambiguidades e conflitos.

- Falhas de comunicação na transmissão de dados: Estudaremos formas de manter a comunicação via wifi o mais estável possível, considerando a melhor eficiência do sistema implementado. Também estabeleceremos procedimentos para monitorar continuamente a qualidade da transmissão de dados e para solucionar rapidamente quaisquer problemas que possam surgir.

- Falta de resistência do hardware a ambientes hostis: Para garantir a resistência do sistema a possíveis condições hostis, como temperaturas diferentes do ambiente, selecionaremos componentes de alta qualidade e resistência, além de considerar soluções de proteção adicionais, como caixas de proteção e materiais de vedação.

- Aumento exagerado do escopo do projeto: Para garantir a entrega da melhor solução possível, pensando nos riscos anteriormente citados, definiremos claramente o escopo do projeto e as funcionalidades a serem desenvolvidas. Também implementaremos processos de gerenciamento de mudanças para avaliar qualquer nova solicitação de funcionalidade e garantir que ela seja consistente com os objetivos do projeto e viável em termos de prazo e recursos.

- Vazamento eletrostático ou outro tipo de reação que pode colocar o gás dentro do duto em combustão: Como plano de ação para mitigar esse risco, isolaremos os circuitos para evitar vazamentos eletrostáticos.

## Matriz Oceano Azul
A matriz oceano azul foi desenvolvida com o objetivo de descobrir novas oportunidades de mercado e criar um produto único de alta qualidade, diferente dos concorrentes. Ademais, é possível ter um maior entendimento do que a Gerdau precisa e trazer melhorias/adaptações para o protótipo final atendendo às expectativas e necessidades da empresa. 

Nossa matriz oceano azul foi feita com base na análise entre nosso produto e os atuais concorrentes no mercado de robôs confinados.
Levamos em conta 6 atributos, são eles: preço, qualidade, tecnologia, conforto, comodidade e praticidade.

![Matriz Oceano Azul](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/matriz%20oceano%20azul.png)

Justificativa das pontuações referentes ao oceano azul:

- Preço: Através da parceria entre Inteli e Gerdau e da análise financeira realizada pelo grupo, concluímos que nosso produto tem um preço mais acessível em comparação aos produtos já consolidados no mercado, o que resultou em uma nota 8 na matriz.

- Qualidade: Considerando que o produto será desenvolvido por estudantes em um contexto educacional, a nota dada à qualidade é um pouco menor em relação aos concorrentes que possuem uma equipe de engenheiros já formados e uma empresa já estabelecida.

- Tecnologia: Para o desenvolvimento do projeto, utilizaremos softwares importantes e requisitados no mercado, mas o hardware será fornecido pela faculdade, o que pode não ser ideal para a solução proposta. Isso ocorre devido ao contexto educacional do projeto.

- Conforto: A parceria entre Inteli e Gerdau oferece ao cliente a possibilidade de sugerir e acompanhar de perto o desenvolvimento do produto, o que garante mais liberdade e conforto durante o processo.
 
- Comodidade: A presença da Gerdau durante o desenvolvimento do produto garante que o serviço seja customizado de acordo com as necessidades do cliente, trazendo comodidade na hora de desenvolver a solução.

- Praticidade: Embora não seja tão prático quanto simplesmente comprar um robô sob demanda, o produto será customizado para o cliente, o que resultará em facilidade de manutenção e utilização.

Após análise cuidadosa do gráfico, identificamos fatores que devem ser eliminados, reduzidos, aumentados e criados em nosso projeto. Além disso, observamos que o nosso produto se encontra no mesmo quadrante que produtos já consolidados no mercado, o que nos leva a propor um projeto com similaridades. 

**Eliminar**
- Robôs grandes e desajeitados que não podem manobrar em espaços estreitos
- Robôs que não são seguros para uso em ambientes perigosos e confinados
- Robôs que não têm sensores para ajudar na navegação e na análise de dados atmosféricos

**Reduzir**
- Custo de fabricação de robôs, mantendo a qualidade e a segurança
- Complexidade de operação do robô, tornando-o fácil de usar
- Tempo necessário para a manutenção do robô

**Elevar**
- Agilidade e capacidade de manobra do robô em terrenos difíceis, bem como uma melhor análise e coleta de dados atmoféricos
- Confiabilidade e durabilidade do robô
- Capacidade de navegação autônoma em ambientes confinados

**Criar**
- Novas funcionalidades para o robô, como a capacidade de detectar e responder a emergências em tempo real
- Novas formas de comunicação do robô com o operador
- Criar uma nova feature integrável com o sistema da Gerdau


# Entendimento do Metadesign

## Fatores mercadológicos

**Qual é o seu produto e como ele se orienta ao mercado? Como ele é precificado?**
Nosso produto consiste no robô "TurtleBot 3 Burger", programado para operar em ambientes confinados e coletar dados a partir de sensores de alta precisão. Esses dados são analisados por um operador, por meio de uma interface, para fornecer informações valiosas sobre o ambiente e suas condições atmosféricas, ajudando a prevenir acidentes e melhorar a produtividade. Para determinar o preço do nosso produto, consideramos vários fatores, incluindo o custo dos componentes e sensores utilizados, mão de obra necessária para desenvolvimento e implementação, despesas anuais de manutenção e o custo geral do projeto. Esses fatores são avaliados por meio de uma análise financeira, que nos permite chegar a um preço justo e competitivo para o mercado. 

**Qual é o cenário do mercado no qual o projeto se insere?**
A adoção de AGVs na manutenção industrial tem se tornado cada vez mais comum em escala global, principalmente em empresas de manufatura, logística e transporte que buscam aumentar sua eficiência e competitividade. No entanto, em São Paulo, Brasil, essa tecnologia ainda está em estágio inicial de adoção, com apenas algumas empresas de grande porte implementando AGVs em seus processos de transporte e manutenção. Apesar disso, a crescente demanda por eficiência e redução de custos pode levar a uma maior adoção de AGVs na manutenção industrial em São Paulo e em outras regiões do Brasil. Ademais, a falta de mão de obra qualificada na indústria pode impulsionar ainda mais a adoção de tecnologias de automação e robótica, incluindo AGVs.

Por fim, o projeto que estamos desenvolvendo se insere em um nicho específico, mas de grande importância para empresas que priorizam a segurança em seus processos industriais. Nosso objetivo é utilizar robôs para a manutenção e segurança de espaços confinados, fornecendo informações precisas e em tempo real sobre as condições ambientais e evitando a exposição de operadores humanos a riscos.

**Qual a visão do projeto proposto?**

Assim, o projeto tem como objetivo criar um AGV (Automated Guided Vehicle) capaz de entrar em espaços confinados e, por meio de sensores, analisar a presença de gases no ambiente, enviando essas leituras para o operador. Acreditamos que nossa solução pode modernizar e automatizar processos de segurança na Gerdau, melhorando a segurança dos funcionários durante a realização desses procedimentos.

Embora o uso de AGVs na segurança industrial ainda seja incipiente em São Paulo, no Brasil como um todo há um grande investimento nessa tecnologia. Não há restrições específicas para o uso de AGVs no país, mas existem normas de segurança que devem ser seguidas para garantir a integridade física dos trabalhadores e evitar acidentes.

Ao desenvolvermos nosso projeto, consideramos as restrições locais e o cenário brasileiro de AGVs, focando em atender às necessidades específicas de nosso cliente e agregar segurança ao processo de análise do ambiente.

## Sistema produto/design

**Qual a missão do projeto proposto?**
O projeto tem como objetivo principal que um robô faça a inspeção das condições atmosféricas de um ambiente confinado, que por conceito, designa um espaço fechado que pode apresentar condições inapropriadas para a presença humana. Essa inspeção é necessária para garantir que uma pessoa adentre o ambiente sem sofrer danos à sua saúde, ou haver algum tipo de acidente decorrente das condições atmosféricas. Portanto, a principal missão do projeto é garantir a segurança dos funcionários da Gerdau, de modo a evitar acidentes e aumentar a produtividade.


**Como se pensa em manter uma unidade formal entre o design do produto, as formas de divulgação e venda?**
De uma maneira geral, o produto buscará compartilhar confiança em atuar na manutenção do setor, por meio de inovações tecnológicas na análise e mapeamento de zonas confinadas improprias a pessoas. A associação da marca ao propósito da solução buscará melhor reflexão do setor de segurança no trabalho ao contextos ao qual o robô irá se inserir, sendo relevante a demonstração da evolução do setor ao longos dos tempos ao momento de termos processos que não é mais necessário vidas humanas em serviços arriscados, sendo isso uma proposta de marketing e venda apresentada a partir de uma percepção evolutiva do problema e solução.

## Sustentabilidade ambiental
Nosso produto é desenvolvido com foco na ecoeficiência, utilizando fontes renováveis de energia, como baterias recarregáveis, em vez de baterias alcalinas, sem a utilização de combustíveis fósseis. Além disso, o robô é projetado para ter uma vida útil prolongada, permitindo seu uso em futuros projetos da empresa e reduzindo a necessidade de substituição constante.

Equipado com sensores de última geração, o robô realiza análises precisas do ambiente, reduzindo acidentes e prevenindo falhas que possam afetar o meio ambiente. Isso garante a preservação da saúde dos trabalhadores envolvidos nas inspeções e contribui para um ambiente de trabalho mais seguro.

Além disso, nosso objetivo é envolver os trabalhadores no processo, garantindo sua participação sem comprometer sua segurança ou saúde. Com isso, buscamos não apenas oferecer um produto eficiente, mas também promover uma cultura de responsabilidade ambiental e social dentro da empresa.

## Análise Financeira
A Gerdau tem sedes industriais em 9 países nas Américas, mas consideraremos a implementação apenas para as unidades no Brasil. Segundo o site oficial da empresa, a Gerdau possui 25 usinas siderúrgicas, 10 unidades de transformação e corte e dobra, 2 unidades de mineração e 2 unidades de aços em território nacional. Considerando que para obter o resultado desejado seja necessário a implementação de 1 robô por unidade, seriam necessários 39 robôs, o que exigiria um investimento inicial de R$1.076.700,00. Para a manutenção da solução, estima-se um gasto anual de R$338.100,00, incluindo manutenção, custos operacionais e uma margem de aproximadamente 15% para possíveis problemas. A receita esperada com o projeto, como descrito anteriormente, é de R$3.942.900,00/ano, ou seja, é esperado já no primeiro ano um lucro de R$2.528.100,00. #(custo anual - receita anual)

### Custos:
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

### Receitas:
  - Redução de custos com acidentes operacionais;
  - Melhoria da eficiência operacional.

Para estimar os valores específicos para cada aspecto, é necessário ter acesso aos dados financeiros da Gerdau, incluindo o histórico de custos relacionados a acidentes operacionais e a eficiência operacional antes e depois da implementação do robô. Como não temos acesso a esses dados, faremos uma estimativa desses valores.

Assumiremos que a Gerdau tem um custo anual médio de 0,001% do faturamento total com acidentes operacionais, o que em 2020 seria de R$ 43,81 milhões (<a href="https://valor.globo.com/empresas/noticia/2021/02/24/lucro-da-gerdau-sobe-939percent-no-quarto-trimestre.ghtml">valor</a>). Esse custo incluiria processos trabalhistas, perda de produção, custos de manutenção de espaço e equipamentos, entre outros.

Com a implementação do robô, esperamos prevenir 90% dos acidentes, o que nos permitiria projetar uma economia anual de R$ 3.942.900,00.

### Análise do Investimento:

![Investimento Inicial](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/Investimento_Incial.png)

![Economia](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/Receita.png)

![Despesas](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/Despesas_Anuais.png)

![Analise do Investimento](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/Analise_Financeira.png)

# Arquitetura do Sistema

## Diagrama de blocos - Versão 1
<img src = "https://user-images.githubusercontent.com/99203402/235358909-034028ef-b4c0-4321-baf8-dd8a06624598.jpg" width="600">

Embora a imagem acima represente o primeiro esboço da arquitetura da solução, criamos uma nova versão para uma melhor visualização, apresentada na imagem abaixo.

![Arquitetura da Solução - v1]( https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/arquitetura%20da%20solu%C3%A7%C3%A3o%20v1.png) 

### Descrição:
Temos três componentes principais na arquitetura do sistema:

- O componente **embarcado** é responsável pela implementação do ROS2 (Robot Operating System) no sistema operacional Ubuntu, executado no microprocessador Raspberry Pi, que coordena os movimentos do robô por meio de comandos enviados para o microcontrolador Cortex M4 STM32F407. Além disso, alguns periféricos, como câmera, sensor de gás, sensor de temperatura e LIDAR (Light Detection and Ranging), serão acoplados ao sistema para melhorar sua eficiência e precisão. Todos os periféricos se comunicarão diretamente com o microprocessador, e a interface de comunicação escolhida para o robô é a pub/sub.

- O componente **backend** implementa a arquitetura ROS2 (Robot Operating System) para receber e enviar informações por meio dos tópicos pub/sub (publisher/subscriber), comunicando-se diretamente com o robô. Além disso, ele inclui um framework, um banco de dados e um ORM (Object-Relational Mapping). Além da interface pub/sub (publisher/subscriber), o backend também utiliza a comunicação HTTP (HyperText Transfer Protocol).

- O componente **frontend** utiliza do framework react para a paginação e CSS para a estilização. Ele se comunica com o resto do sistema por meio da interface HTTP disponibilizada pelo backend.

## HENRIQUE MARLON

## Análise de requisitos
### Requisitos Funcionais
- Inspeção dos ambientes durante e após da manutenção
- Detecção de condições atmosféricas (presença de gases tóxicos) dos espaços confinados
- Sensores para detectar os gases, e talvez detectar colisões
- Robô ser capaz de retornar ao ponto inicial em casos de erros/defeitos/objetos no meio do caminho
- Movimentação por joystick (casos de emergência)
- Interface web apresentando um dashboard com dados coletados e imagens em tempo real, além de poder gerar relatórios em PDF

### Requisitos não funcionais
- Funcionamento confiável e eficiente no processo de monitoramento e inspeção
- Confiança nos dados gerados
- Monitoramento e inspeção em tempo real
- Interface web de fácil compreensão por aqueles usuários que a utilizem 

## Análise de viabilidade técnica
O projeto é uma solução para os desafios enfrentados pelos técnicos que lidam com espaços confinados em seu dia a dia, tendo como objetivo principal simplificar as tarefas de segurança e inspeção, por meio de um sistema automatizado. Dessa maneira, optamos por adotar o TurtleBot Burger, um robô com capacidade de processamento adequada para os sistemas que iremos empregar, mesmo que ele enfrente algumas limitações em relação à sua mobilidade, especialmente em terrenos irregulares, sua vantagem reside em seu tamanho compacto, permitindo seu acesso a espaços confinados, além de ser uma ótima ferramenta educacional.

Ademais, o robô será equipado com sensores integrados projetados para detectar níveis de gases tóxicos no ambiente. Contudo, é importante mencionar que eles têm uma limitação e só podem detectar até cinco tipos de gases tóxicos. Assim mesmo sendo de uma natureza mais básica, os sensores selecionados são semelhantes aos utilizados na indústria.

Por fim, no que diz respeito ao armazenamento de dados, o robô contará com um sistema de comunicação baseado em tópicos, sendo assim essa configuração permite que as informações sejam transmitidas e armazenadas de forma eficiente. 

# Interface web (frontend)

Nossa interface minimalista foi cuidadosamente projetada para fornecer aos usuários a capacidade de editar facilmente as informações presentes em um relatório. Com um design limpo e simplificado, focamos na simplicidade e na clareza das funcionalidades, permitindo que o usuário tenha total controle sobre o conteúdo do relatório. 

Além da edição de informações, nossa interface também oferece a capacidade de controlar o início e o fim da movimentação de um robô. Com apenas alguns cliques, o usuário pode definir o momento exato em que o robô inicia ou conclui sua movimentação, garantindo assim um controle preciso do fluxo de trabalho.

Para a construção do frontend, utilizaremos o React como tecnologia principal, proporcionando eficiência e escalabilidade. Além disso, garantiremos a integração com os sistemas da Gerdau, aplicando sua identidade visual no design da interface. Isso resultará em uma experiência consistente e familiar para os usuários, facilitando a adoção do sistema e garantindo uma interface visualmente alinhada com a empresa.

## Entradas e saídas 
a) Definição das entradas e saídas necessárias para a interação com o usuário de modo a atender suas necessidades.

O robô contará com uma configuração de comunicação simplificada, proporcionando ao usuário uma interação intuitiva e eficiente. Com essa configuração, o usuário terá acesso a diversas entradas e saídas funcionais dentro da aplicação, permitindo uma experiência completa e satisfatória.

| Entrada                  | Saída                                             |
|-------------------------|-------------------------------------------------|
| Botão na interface      | Permite ativar a movimentação do robô. O mesmo botão também permite pausar a movimentação. |
| Input de título         |Permite ao usuário inserir o título da sala para fins de reconhecimento.  |
| Botão de gerar relatório |Ao ser acionado, gera um modal com base nas informações coletadas durante o ensaio. O modal irá conter dados relevantes e análises do ensaio realizado. |
| Página histórico        | Permite ao usuário acessar relatórios anteriores gerados pelo sistema. O usuário também pode baixar os relatórios em formato PDF para armazenamento ou compartilhamento posterior |

## Mockup
Para proporcionar uma experiência de usuário otimizada, decidimos desenvolver uma aplicação web com uma interface cuidadosamente projetada, que atende às necessidades específicas de entradas e saídas. A estrutura da aplicação foi elaborada de forma a garantir uma interação fluida e intuitiva, maximizando a usabilidade e a eficiência para os usuários.

<img width="565" alt="Captura de tela 2023-05-09 155102 (1)" src="https://github.com/2023M6T2-Inteli/Splinters/assets/99203402/1fd27f43-12cc-4b77-93ce-5603a29dff43">

# Simulação de rota 

A otimização de rotas é um elemento essencial no desenvolvimento de um sistema eficiente para um robô móvel. Neste contexto, a simulação apresentará os principais aspectos a serem abordados ao implementar um sistema de otimização de rota. 

Inicialmente, foi realizada uma análise detalhada e enumeração das possíveis rotas de navegação do robô, levando em consideração as exigências específicas da aplicação em questão e o caminho mais rápido. Em seguida, discutimos a importância de uma representação precisa do ambiente e das rotas escolhidas, utilizando grafos como uma ferramenta eficiente para visualizar e modelar as conexões entre os pontos relevantes. 

A seguir, temos o algoritmo em grafo para otimizar as rotas, com base em uma heurística que faça sentido no contexto do projeto.

## Algoritmo em grafo

O script Python (best_path.py) utiliza a biblioteca rclpy para controlar um robô tartaruga criando um grafo de nós e arestas com pesos baseados na distância entre os nós, encontrando o melhor caminho através de todos os nós usando o algoritmo do problema do caixeiro viajante da biblioteca networkx, e movendo o robô tartaruga ao longo do caminho publicando mensagens Twist no tópico cmd_vel e se inscrevendo em mensagens Odometry do tópico /odom. O script define funções para criar um grafo, encontrar o melhor caminho e controlar o robô tartaruga, bem como uma classe TurtleController que usa rclpy para criar um nó para publicar e se inscrever em mensagens. A função main solicita ao usuário que insira as coordenadas dos nós e arestas, cria um grafo, encontra o melhor caminho através de todos os nós e controla o robô tartaruga para se mover ao longo do caminho.

Tecnicamente, o script começa importando as bibliotecas necessárias e definindo uma função Graph para criar um grafo de nós e arestas com pesos baseados na distância entre os nós. A função define uma classe Position_Node para representar os nós com um nome e coordenadas x e y, e uma função Weighed_Edge para criar uma aresta entre dois nós com um peso baseado na distância entre eles. A função então solicita ao usuário que insira as coordenadas dos nós e adiciona-os ao grafo. Em seguida, solicita ao usuário que insira as arestas entre os nós e adiciona-as ao grafo com pesos baseados na distância entre os nós.

O script também define uma função best_path_all_nodes para encontrar o melhor caminho através de todos os nós no grafo usando o algoritmo do problema do caixeiro viajante da biblioteca networkx. A função recebe como entrada um grafo e um nó de origem e retorna uma lista de nós representando o melhor caminho através de todos os nós no grafo.

Em seguida, o script define uma classe TurtleController para controlar um robô tartaruga usando rclpy para criar um nó que publica mensagens Twist no tópico cmd_vel e se inscreve em mensagens Odometry do tópico /odom. A classe define uma função move_turtle que move o robô tartaruga ao longo do caminho publicando mensagens Twist no tópico cmd_vel com base na posição atual do robô e na próxima posição no caminho. A função calcula a diferença nas coordenadas x e y entre a posição atual e a próxima posição no caminho e usa isso para calcular um ângulo para virar em direção à próxima posição. A função então publica mensagens Twist com velocidades lineares e angulares para mover o robô em direção à próxima posição no caminho.

O código também define uma função de retorno de chamada pose_callback para a classe TurtleController que atualiza a posição atual do robô tartaruga com base em mensagens Odometry do tópico /odom.

Finalmente, o código define uma função main que cria um grafo de nós e arestas usando a entrada do usuário, encontra o melhor caminho através de todos os nós usando o algoritmo do problema do caixeiro viajante da biblioteca networkx, e controla um robô tartaruga para se mover ao longo do caminho usando rclpy. A função main inicializa rclpy, cria uma instância da classe TurtleController com o caminho calculado, gira até ser interrompida por um evento de usuário ou sistema, depois a destroi e desliga rclpy.

# Sistema de visão computacional
## Implementação do sistema de visão computacional

A implementação do sistema de visão computacional foi desenvolvida com o modelo de detecção de objetos pré-treinado, como o YOLOv8 (You Only Look Once versão 8) e é capaz de identificar rachaduras em paredes de concreto com o uso de um dataset do Roboflow. 

Explicação do notebook e script em Python:

1. **Preparação do Ambiente:** Instalação da biblioteca 'ultralytics'.

2. **Preparação do dataset:** Acessamos o dataset de rachaduras em paredes de concreto fornecido pela Roboflow.

3. **Treinamento do modelo:** Em um notebook, a partir do dataset do roboflow, treinamos o modelo com o código a seguir:

`!yolo train data=/content/crack-2/data.yaml model=sample_data/yolov8n.pt epochs=10 lr0=0.01`

4. Configuração do script:
Importar as bibliotecas necessárias:

``
from ultralytics import YOLO
import cv2 as cv
``

Carregue o modelo YOLO pré-treinado:

``
model = YOLO('./semana5/best.pt')
``

5. Detecção de Rachaduras:
Inicialize a captura de vídeo da webcam:

```python
capture = cv.VideoCapture(0)
``

Criação de um loop para capturar quadros (frames) da captura de vídeo e realizar a detecção de objetos:

```python
while True:
    _, frame = capture.read()
    result = model.predict(frame, conf=0.6)
    cv.imshow('frame', result[0].plot())
    if cv.waitKey(1) == ord('q'):
        break
```

No código acima, cada quadro capturado é passado para o modelo YOLO, que realiza a detecção de objetos com base nas rachaduras presentes no quadro. O resultado da detecção é exibido em uma janela com o nome 'frame'. O loop é interrompido quando a tecla 'q' é pressionada.

5. Execução do script: Execute o script Python no terminal ou prompt de comando. Assim, o script iniciará a captura de vídeo da webcam e exibirá os quadros com as detecções de rachaduras em tempo real.


## Validação da eficácia e performance do sistema de visão computacional

# Sistemas de segurança

## Implementação do sistema anticolisão.
## Fabricação e implementação dos dispositivos de segurança.
## Implementação do sistema de proteção contra comandos indesejados.
## Validação da eficácia dos sistemas de segurança.
