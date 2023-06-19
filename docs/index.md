3. Descrição da arquitetura do sistema. (peso 0.5)

4. Sistema de locomoção e otimização de rota. (peso 1)

5. Interface de usuário. (peso 1)

6. Sistema de visão computacional. (peso 1)

7. Sistemas de segurança. (peso 1)

8. Backend. (peso 1)

9. Integração de sistemas. (peso 1)

10. Validação da eficácia do sistema. (peso 2.5)
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

- Bianca Cassemiro
- Gabriel Pascoli
- Henrique Santos
- Jackson Aguiar
- Luana Parra
- Pablo Ruan
- Rafael Katalan

# Visão geral do projeto

A seguir, apresentaremos uma visão geral do projeto, destacando seus objetivos, escopo e principais características. 

## Empresa

Presente em 10 países, a Gerdau é pioneira no setor do aço na implantação de iniciativas de inovação digital. Esse resultado é fruto do trabalho conjunto de todos os seus mais de 30 mil colaboradores.

A Gerdau é a maior empresa brasileira produtora de aço e uma das principais fornecedoras de aços longos nas Américas, além de ser uma das principais fornecedoras de aços especiais em nível global. No Brasil, também produz aços planos e minério de ferro. Além disso, é a maior recicladora da América Latina e, anualmente, transforma milhões de toneladas de sucata em aço, reforçando o seu compromisso com o desenvolvimento sustentável nas regiões onde atua. As ações da Gerdau estão listadas nas bolsas de valores de São Paulo (B3), Nova Iorque (NYSE) e Madri (Latibex).

## Problema

Um dos riscos críticos identificados nas operações da Gerdau é o Espaço Confinado. Esses são ambientes que não foram projetados para a permanência humana contínua e apresentam condições desafiadoras, como acesso limitado, ventilação insuficiente e possíveis alterações nos níveis de oxigênio. Considerando a importância da segurança como valor fundamental em todas as nossas decisões diárias e nosso compromisso com o objetivo de alcançar o "acidente zero", é crucial enfrentar esse problema.

Embora tenhamos rigorosos padrões de operação e manutenção definidos por diretrizes corporativas, bem como normas regulamentadoras, como a NR 33 no Brasil, a verificação dos espaços confinados ainda é realizada periodicamente, com rotinas de inspeção geralmente planejadas e conduzidas externamente a esses ambientes. Isso significa que os acessos a esses espaços são limitados às atividades previamente programadas, o que pode não ser suficiente para garantir a segurança total dos colaboradores.

Atualmente, a pré-avaliação desses espaços confinados por meio de equipamentos tecnológicos, como robôs e drones, já é uma prática adotada. No entanto, essas soluções ainda apresentam custos elevados, o que as torna utilizadas apenas de forma pontual na indústria como um todo. Contudo, é importante ressaltar que diversas universidades e centros de pesquisa estão dedicando esforços para estudar e aprimorar essas tecnologias, dada a relevância do tema e a necessidade de avançar na mitigação dos riscos e melhorar os indicadores de segurança para nossos colaboradores.

Assim, é essencial abordar o problema dos espaços confinados de forma abrangente, buscando soluções inovadoras e eficazes para aprimorar a segurança em nossas operações. A conscientização sobre os riscos envolvidos, a implementação de medidas preventivas mais abrangentes e o investimento em tecnologias de pré-avaliação acessíveis são elementos fundamentais para garantir um ambiente de trabalho seguro e promover a cultura de segurança em toda a organização.

## Objetivo geral

Por meio de uma solução de simulação, espera-se que um robô seja capaz de se locomover em ambientes de espaço confinado, coletar dados por meio de sensores, com foco especial em monitorar níveis de oxigênio e outros gases, além de utilizar filmagens para auxiliar na inspeção prévia da estrutura.

## Benefícios esperados

Segurança em primeiro lugar. Para nós, não há resultado mais importante do que preservar a vida das pessoas. É por isso que a Gerdau está empenhada em investir em soluções tecnológicas que visam reduzir a exposição dos nossos colaboradores em atividades de risco.

Pensando no futuro que almejamos construir, a Gerdau tem o compromisso de desenvolver nossos valores nos futuros líderes, de modo que eles possam manter uma constante preocupação com a saúde e segurança dos colaboradores, independentemente de sua área de atuação.

## Escopo macro

Inicialmente, espera-se que haja uma conscientização sobre a importância do tema ao longo do curso, bem como as motivações para avançarmos no desenvolvimento de tecnologias disruptivas visando a redução da exposição a riscos. É desejável que os alunos recebam uma aula introdutória sobre definições relacionadas à segurança, como os conceitos de Risco x Perigo, gerenciamento de riscos e prevenção de acidentes, incluindo barreiras físicas e sistêmicas.

Neste projeto, espera-se que os alunos desenvolvam, por meio de simulação, um robô capaz de se locomover em ambientes de espaço confinado e coletar informações sem a necessidade de geolocalização. Esse robô poderá se movimentar tanto na superfície quanto por vias aéreas, adaptando-se às exigências de cada ambiente. A simulação poderá ser realizada por meio de simuladores computacionais em conjunto com o ROS (Robot Operating System). É desejável também a implementação física do robô para fins de demonstração.

O objetivo do projeto é fornecer uma ferramenta aos operadores e mantenedores para auxiliar em atividades de espaço confinado, permitindo um diagnóstico preliminar da situação. A solução desenvolvida será submetida a uma avaliação de validação pelos times de inovação, segurança e gestão de riscos. Além disso, a solução será apresentada aos líderes de negócio, visando a possibilidade de implementação em escala maior.

## Partes interessadas

- Inteli
- Gerdau

# Análise do problema

No tópico de análise do problema, serão abordados diferentes aspectos relacionados à identificação e compreensão dos desafios existentes. Serão discutidos os riscos críticos presentes nas operações da Gerdau, com destaque para o Espaço Confinado, um dos principais focos de atenção. Serão explorados os procedimentos atuais de verificação e inspeção desses espaços, bem como as limitações e lacunas existentes.

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

### Abordagens

1. Falta de conhecimento prévio sobre o projeto: Como plano de ação para esse risco, nós, estudantes do Inteli desenvolvendo o projeto, nos comprometemos a realizar todos os estudos necessários para cumprir com excelência todas as regras de negócio propostas pelo parceiro para o projeto.
2. Manutenabilidade do Hardware: Como estamos lidando com uma implementação física, ela estará exposta às intempéries que podem diminuir a vida útil de seus componentes. Como plano de ação para esse risco, vamos considerar opções de proteção do hardware.
3. Falhas de comunicação na equipe que está desenvolvendo o projeto: Para mitigar esse risco, aplicaremos derivações da metodologia ágil para manter a comunicação entre os membros do grupo sempre alinhada e focada no consenso entre as partes. Além disso, definiremos claramente os papéis e responsabilidades de cada membro da equipe, a fim de evitar ambiguidades e conflitos.
4. Falhas de comunicação na transmissão de dados: Estudaremos formas de manter a comunicação via wifi o mais estável possível, considerando a melhor eficiência do sistema implementado. Também estabeleceremos procedimentos para monitorar continuamente a qualidade da transmissão de dados e para solucionar rapidamente quaisquer problemas que possam surgir.
5. Falta de resistência do hardware a ambientes hostis: Para garantir a resistência do sistema a possíveis condições hostis, como temperaturas diferentes do ambiente, selecionaremos componentes de alta qualidade e resistência, além de considerar soluções de proteção adicionais, como caixas de proteção e materiais de vedação.
6. Aumento exagerado do escopo do projeto: Para garantir a entrega da melhor solução possível, pensando nos riscos anteriormente citados, definiremos claramente o escopo do projeto e as funcionalidades a serem desenvolvidas. Também implementaremos processos de gerenciamento de mudanças para avaliar qualquer nova solicitação de funcionalidade e garantir que ela seja consistente com os objetivos do projeto e viável em termos de prazo e recursos.
7. Vazamento eletrostático ou outro tipo de reação que pode colocar o gás dentro do duto em combustão: Como plano de ação para mitigar esse risco, isolaremos os circuitos para evitar vazamentos eletrostáticos.
   
## Matriz Oceano Azul

A matriz oceano azul foi desenvolvida com o objetivo de descobrir novas oportunidades de mercado e criar um produto único de alta qualidade, diferente dos concorrentes. Ademais, é possível ter um maior entendimento do que a Gerdau precisa e trazer melhorias/adaptações para o protótipo final atendendo às expectativas e necessidades da empresa.

Nossa matriz oceano azul foi feita com base na análise entre nosso produto e os atuais concorrentes no mercado de robôs confinados. Levamos em conta 6 atributos, são eles: preço, qualidade, tecnologia, conforto, comodidade e praticidade.

1. Preço: Neste atributo, buscamos oferecer um preço competitivo em relação aos concorrentes, levando em consideração o valor percebido pelos clientes. A ideia é fornecer uma solução acessível e que proporcione um excelente custo-benefício.
2. Qualidade: A qualidade é um elemento crucial para o sucesso do produto. Buscamos entregar um robô em espaço confinado que seja robusto, durável e confiável, capaz de lidar com as demandas e desafios desse ambiente de forma eficiente e segura.
3. Tecnologia: A inovação tecnológica é um diferencial importante. Nosso objetivo é oferecer uma solução que utilize as tecnologias mais avançadas disponíveis, como sensores de alta precisão, algoritmos inteligentes de processamento de dados e sistemas de comunicação de última geração.
4. Conforto: A experiência do usuário é um fator determinante. Nosso robô em espaço confinado será projetado levando em consideração o conforto e a ergonomia, permitindo uma interação fácil e intuitiva para os operadores, mesmo em ambientes desafiadores.
5. Comodidade: Além de fornecer uma solução eficiente, buscamos facilitar o uso e a integração do robô em espaço confinado com os processos existentes. Isso inclui aspectos como a facilidade de transporte, configuração rápida e interface amigável, visando minimizar o tempo de implantação e aumentar a conveniência para os usuários.
6. Praticidade: A praticidade está relacionada à facilidade de uso, manutenção e suporte técnico. Nosso produto será projetado para simplificar as operações, minimizando a necessidade de treinamento extenso e oferecendo recursos de manutenção simplificados, com suporte técnico ágil e eficiente.

![Matriz Oceano Azul](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/matriz%20oceano%20azul.png)

Justificativa das pontuações referentes ao oceano azul:

1. Preço: A parceria entre Inteli e Gerdau permitiu uma análise financeira detalhada, resultando em um produto com um preço mais acessível em comparação aos produtos já consolidados no mercado. Essa estratégia busca conquistar clientes que buscam uma solução de qualidade a um custo mais atrativo, refletindo na pontuação de 8 na matriz.
2. Qualidade: Considerando o contexto educacional do projeto, no qual o produto será desenvolvido por estudantes, é importante reconhecer que a equipe possui recursos e experiência limitados em relação a concorrentes que contam com engenheiros formados e empresas estabelecidas. Portanto, embora se busque entregar um produto de alta qualidade, a pontuação pode ser um pouco menor em comparação aos competidores.
3. Tecnologia: No desenvolvimento do projeto, serão utilizados softwares de ponta, alinhados com as demandas do mercado. No entanto, é importante mencionar que o hardware será fornecido pela faculdade, o que pode impactar a excelência da solução proposta. Essa limitação é decorrente do contexto educacional do projeto e é necessário considerá-la na avaliação da pontuação atribuída.
4. Conforto: A parceria entre Inteli e Gerdau oferece ao cliente a oportunidade de participar ativamente no processo de desenvolvimento do produto, sugerindo modificações e acompanhando de perto o progresso. Essa interação direta proporciona maior conforto ao cliente, garantindo que suas necessidades sejam atendidas de forma personalizada.
5. Comodidade: A presença da Gerdau durante todo o desenvolvimento do produto permite uma abordagem personalizada e customizada para atender às necessidades específicas do cliente. Essa proximidade e colaboração com a empresa garantem um processo mais conveniente e alinhado com as expectativas do cliente.
6. Praticidade: Embora possa exigir mais tempo e esforço em comparação com a simples compra de um robô pronto para uso, o produto será customizado de acordo com as necessidades do cliente. Essa abordagem resulta em uma solução mais prática em termos de manutenção e utilização, atendendo às demandas específicas do ambiente confinado.

Após uma análise cuidadosa do gráfico, identificamos os fatores que devem ser eliminados, reduzidos, aumentados e criados em nosso projeto. Além disso, notamos que nosso produto se encontra no mesmo quadrante que produtos já consolidados no mercado, o que nos leva a propor um projeto com similaridades. Essa abordagem nos permitirá construir sobre as melhores práticas existentes, ao mesmo tempo em que buscamos diferenciar-nos com melhorias e adaptações específicas para atender às expectativas e necessidades da empresa Gerdau.

**Eliminar**

- Robôs grandes e desajeitados que não podem manobrar em espaços estreitos: A proposta é eliminar a limitação de tamanho e tornar o robô mais compacto e ágil, capaz de operar em ambientes confinados e de difícil acesso.
- Robôs que não são seguros para uso em ambientes perigosos e confinados: Buscamos eliminar qualquer risco de segurança, desenvolvendo um robô projetado especificamente para operar em ambientes confinados, com recursos de segurança aprimorados e certificações adequadas.
- Robôs que não têm sensores para ajudar na navegação e na análise de dados atmosféricos: O objetivo é eliminar a limitação de coleta de informações ambientais, incorporando sensores avançados que permitam uma análise precisa dos dados atmosféricos, identificando riscos e fornecendo alertas em tempo real.

**Reduzir**

- Custo de fabricação de robôs, mantendo a qualidade e a segurança: Buscamos otimizar os processos de fabricação, explorar parcerias estratégicas e utilizar tecnologias eficientes para reduzir os custos de produção, sem comprometer a qualidade e a segurança do produto final.
- Complexidade de operação do robô, tornando-o fácil de usar: Simplificaremos a interface e a operação do robô, desenvolvendo uma solução intuitiva e fácil de usar, mesmo para usuários não especializados. Isso reduzirá a curva de aprendizado e facilitará a adoção da tecnologia.
- Tempo necessário para a manutenção do robô: Projetaremos o robô com uma arquitetura modular e componentes de fácil substituição, reduzindo o tempo necessário para a manutenção e minimizando as interrupções nas operações.

**Elevar**

- Agilidade e capacidade de manobra do robô em terrenos difíceis, bem como uma melhor análise e coleta de dados atmosféricos: Nossa solução se concentrará em aprimorar a mobilidade do robô em terrenos desafiadores, tornando-o capaz de navegar com facilidade e coletar dados atmosféricos de forma precisa e abrangente.
- Confiabilidade e durabilidade do robô: Buscaremos aprimorar a confiabilidade e a durabilidade do robô, utilizando materiais de alta qualidade, testes rigorosos e implementando medidas de segurança adicionais para garantir um desempenho consistente e uma vida útil prolongada.
- Capacidade de navegação autônoma em ambientes confinados: Nosso objetivo é desenvolver algoritmos avançados de navegação autônoma, permitindo que o robô mapeie e navegue de forma independente em ambientes confinados, otimizando a eficiência e minimizando a necessidade de intervenção humana.

**Criar**

- Novas funcionalidades para o robô, como a capacidade de detectar e responder a emergências em tempo real: Implementaremos recursos avançados de detecção de emergências, como a identificação de gases tóxicos, incêndios ou situações de perigo iminente, permitindo uma resposta rápida e eficaz.
- Novas formas de comunicação do robô com o operador: Exploraremos tecnologias de comunicação inovadoras, como transmissão de vídeo em tempo real e interfaces de realidade aumentada, para aprimorar a interação e a colaboração entre o robô e o operador, mesmo à distância.
- Criar uma nova feature integrável com o sistema da Gerdau: Desenvolveremos uma funcionalidade exclusiva e personalizada que poderá ser integrada perfeitamente ao sistema existente da Gerdau, proporcionando uma solução completa e adaptada às necessidades específicas da empresa.

# Entendimento do Metadesign

## Fatores mercadológicos

**Qual é o seu produto e como ele se orienta ao mercado? Como ele é precificado?**

Nosso projeto proposto consiste em desenvolver um robô para inspeção de ambientes confinados, visando garantir a segurança dos funcionários e evitar acidentes decorrentes das condições atmosféricas. O robô será equipado com sensores de alta precisão para analisar a presença de gases e outras condições ambientais, fornecendo informações em tempo real aos operadores. Nosso produto se orienta ao mercado industrial, principalmente em setores como manufatura, logística e transporte, onde a adoção de tecnologias de automação, como AGVs, está se tornando cada vez mais comum.

A precificação do nosso produto levará em consideração diversos fatores, como o custo dos componentes e sensores utilizados, mão de obra necessária para o desenvolvimento e implementação, despesas anuais de manutenção e o custo geral do projeto. Realizaremos uma análise financeira abrangente para determinar um preço justo e competitivo para o mercado, considerando também a demanda e o valor agregado que nossa solução oferece em termos de segurança e eficiência.

**Qual é o cenário do mercado no qual o projeto se insere?**

A adoção de robôs AGVs na indústria está em ascensão globalmente, com empresas buscando aumentar sua eficiência operacional e reduzir custos por meio da automação. No entanto, no contexto específico de São Paulo, Brasil, a utilização de AGVs na manutenção industrial ainda está em estágio inicial, sendo adotada apenas por algumas grandes empresas. Apesar disso, a demanda por eficiência e a escassez de mão de obra qualificada na indústria podem impulsionar a adoção de tecnologias de automação e robótica, incluindo AGVs, em São Paulo e outras regiões do Brasil.

Nosso projeto se insere em um nicho específico, com foco na segurança em ambientes confinados. Visamos atender empresas que priorizam a segurança de seus processos industriais, oferecendo uma solução inovadora e tecnologicamente avançada. Ao considerar o cenário brasileiro de AGVs e as necessidades específicas de nossos clientes, buscamos contribuir para a modernização e automação dos processos de segurança na indústria.

**Qual a visão do projeto proposto?**

O projeto proposto tem como visão principal criar uma simulação de um robô de inspeção para ambientes confinados que possa ser utilizado pela Gerdau, visando melhorar a segurança dos funcionários durante os procedimentos realizados nesses espaços. Através da automação e coleta de dados precisos, pretendemos modernizar e aprimorar os processos de segurança industrial, contribuindo para um ambiente de trabalho mais seguro e eficiente.

## Sistema produto/design

**Qual a missão do projeto proposto?**

A principal missão do nosso projeto é garantir a segurança dos funcionários da Gerdau, fornecendo um robô de inspeção de ambientes confinados. Esse robô, equipado com sensores de alta precisão, será capaz de analisar as condições atmosféricas e fornecer informações em tempo real aos operadores, evitando a exposição humana a riscos e prevenindo acidentes decorrentes dessas condições. Além disso, buscamos aumentar a produtividade por meio da automação de tarefas de inspeção, permitindo que os funcionários se concentrem em atividades de maior valor agregado.

**Como se pensa em manter uma unidade formal entre o design do produto, as formas de divulgação e venda?**

A unidade formal entre o design do produto, as formas de divulgação e venda é essencial para transmitir uma mensagem consistente e fortalecer a identidade da solução. A estética do produto deve refletir sua função e propósito, transmitindo confiança e inovação. O design deve ser intuitivo, com interfaces claras e amigáveis para os operadores.

Na divulgação e venda da solução, é importante destacar os benefícios de segurança, eficiência e sustentabilidade ambiental que nosso produto oferece. Utilizaremos estratégias de marketing que enfatizem a evolução do setor de segurança industrial, destacando a importância de investir em tecnologias avançadas para prevenir acidentes e proteger os trabalhadores. Além disso, podemos utilizar materiais promocionais, como folhetos, vídeos e apresentações, para transmitir a proposta de valor do produto de forma clara e persuasiva.

A unidade formal entre o design do produto e as formas de divulgação e venda contribuirá para uma identidade consistente da solução, fortalecendo sua aceitação no mercado e facilitando a compreensão de seus benefícios pelos clientes em potencial.

## Sustentabilidade ambiental

Nosso projeto tem um forte compromisso com a sustentabilidade ambiental. O design do produto é orientado para a ecoeficiência, buscando minimizar o impacto ambiental. Optamos por utilizar fontes renováveis de energia, como baterias recarregáveis, em vez de baterias alcalinas e combustíveis fósseis. Dessa forma, reduzimos as emissões de gases de efeito estufa e promovemos a transição para uma matriz energética mais limpa.

Além disso, nosso robô é projetado para ter uma vida útil prolongada, com possibilidade de reutilização em futuros projetos da empresa, reduzindo a geração de resíduos eletrônicos e a necessidade de substituição frequente. A escolha de sensores de alta precisão contribui para a análise precisa do ambiente, prevenindo acidentes que poderiam resultar em danos ao meio ambiente.

Para promover uma cultura de responsabilidade ambiental e social, buscamos envolver os trabalhadores no processo, garantindo sua participação e segurança. Além disso, podemos promover treinamentos e conscientização sobre questões ambientais e incentivar práticas sustentáveis dentro da empresa, como a redução do consumo de energia e a gestão adequada de resíduos.

Ao considerar a sustentabilidade ambiental em nosso projeto, não apenas oferecemos uma solução eficiente, mas também contribuímos para a preservação do meio ambiente e promovemos uma atitude responsável em relação aos recursos naturais.

## Influências socioculturais
Nosso projeto é influenciado pelas demandas e necessidades socioculturais relacionadas à segurança dos trabalhadores e à eficiência operacional na indústria. Há uma crescente preocupação com a segurança no ambiente de trabalho e um maior interesse em adotar tecnologias avançadas para prevenir acidentes e proteger os funcionários. Além disso, a automação e a robótica estão se tornando cada vez mais comuns na indústria, refletindo uma mudança cultural em direção à modernização e eficiência.

Nossa solução busca atender essas influências socioculturais, oferecendo um robô de inspeção que contribua para um ambiente de trabalho seguro e produtivo. Através da automação e coleta de dados precisos, nosso projeto reflete a preocupação com a segurança e a busca por melhores condições de trabalho. Além disso, promovemos uma cultura de inovação e avanço tecnológico, incentivando a adoção de soluções mais eficientes e sustentáveis na indústria.

## Tipológico-formais e ergonômicos
O design do nosso produto é orientado por considerações tipológico-formais e ergonômicas. Buscamos criar um robô de inspeção que seja funcional e eficiente em sua forma, levando em consideração as necessidades operacionais e as restrições de espaços confinados. O tamanho e a forma do robô são projetados para permitir fácil manobrabilidade e acesso a áreas de difícil alcance, garantindo uma inspeção abrangente e precisa.

Além disso, consideramos a ergonomia na interação do operador com o robô. As interfaces e controles são projetados de forma intuitiva e ergonomicamente correta, minimizando a fadiga e o esforço durante a operação. Também levamos em consideração a segurança do operador, garantindo que o robô seja equipado com mecanismos de parada de emergência e sistemas de detecção de colisão.

A combinação de considerações tipológico-formais e ergonômicas resulta em um design que atende tanto às necessidades operacionais quanto às exigências de segurança e eficiência.

## Tecnologia produtiva e materiais empregados
Nossa solução se baseia em tecnologia avançada para garantir a eficiência e a confiabilidade do produto. Utilizamos o Robot Operating System (ROS2) como base para o desenvolvimento do sistema embarcado, permitindo uma coordenação eficiente dos movimentos do robô e a integração dos sensores de alta precisão. Além disso, implementamos interfaces de comunicação pub/sub (publisher/subscriber) e HTTP para garantir a troca de informações em tempo real entre o robô, o backend e o frontend do sistema.

Em relação aos materiais empregados, utilizamos componentes duráveis e de alta qualidade para garantir a resistência e a longevidade do robô. O uso de materiais leves, mas robustos, contribui para a mobilidade e a facilidade de manobra do robô em ambientes confinados. Também priorizamos a utilização de materiais e componentes que sejam sustentáveis e ecologicamente corretos, reduzindo o impacto ambiental do produto.

A tecnologia produtiva empregada envolve processos de fabricação avançados, como usinagem de precisão, montagem automatizada e testes rigorosos para garantir a qualidade do produto final. Buscamos otimizar os processos produtivos para garantir uma produção eficiente e atender à demanda do mercado.

A escolha cuidadosa de tecnologia produtiva e materiais empregados é fundamental para a qualidade, desempenho e sustentabilidade do nosso produto.

# Análise Financeira

A Gerdau possui sedes industriais em 9 países nas Américas, mas neste projeto consideraremos apenas as unidades localizadas no Brasil. De acordo com as informações fornecidas no site oficial da empresa, existem 25 usinas siderúrgicas, 10 unidades de transformação e corte e dobra, 2 unidades de mineração e 2 unidades de aços em território nacional. Levando em conta a necessidade de implementação de 1 robô por unidade para alcançar o resultado desejado, seria preciso adquirir um total de 39 robôs. Isso exigiria um investimento inicial estimado em R$1.076.700,00. Para a manutenção da solução, estima-se um custo anual de R$338.100,00, que inclui despesas de manutenção, custos operacionais e uma margem de cerca de 15% para eventuais problemas. Com base na descrição anterior, a receita esperada com o projeto é de R$3.942.900,00 por ano. Portanto, já no primeiro ano, espera-se um lucro de R$2.528.100,00, considerando a diferença entre a receita anual e o custo anual.

### Custos

- Custo do hardware (TurtleBot, Raspberry Pi 3, câmera DobotMagical, sensores de gases)
  - TurtleBot + Raspberry Pi 3: R$17.000/robô
  - Sensores de gases: R$400/robô
  - Câmera: R$400/robô

- Custos de mão de obra (desenvolvimento de software, montagem, testes)
  - Duração: 2 meses
  - Equipe: 3 engenheiros
  - Custo: R$51.000 (fonte: Glassdoor)
  - Implementação do projeto (1 engenheiro): R$8.500/local (fonte: Glassdoor)

- Custos de manutenção e atualização do software
  - Alocação da aplicação WEB: R$60.000/ano
  - Manutenção de hardware: R$1.000/ano*robô
  - Custo operacional: R$5.000/ano*robô

### Receitas

- Redução de custos com acidentes operacionais;
- Melhoria da eficiência operacional.

Para estimar os valores específicos para cada aspecto, é necessário ter acesso aos dados financeiros da Gerdau, incluindo o histórico de custos relacionados a acidentes operacionais e a eficiência operacional antes e depois da implementação do robô. Como não temos acesso a esses dados, faremos uma estimativa desses valores.

Assumiremos que a Gerdau tem um custo anual médio de 0,001% do faturamento total com acidentes operacionais, o que em 2020 seria de R$ 43,81 milhões (<a href="https://valor.globo.com/empresas/noticia/2021/02/24/lucro-da-gerdau-sobe-939percent-no-quarto-trimestre.ghtml">valor</a>). Esse custo incluiria processos trabalhistas, perda de produção, custos de manutenção de espaço e equipamentos, entre outros.

Com a implementação do robô, esperamos prevenir 90% dos acidentes, o que nos permitiria projetar uma economia anual de R$ 3.942.900,00.

### Análise do Investimento

![Investimento Inicial](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/Investimento_Incial.png)

![Economia](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/Receita.png)

![Despesas](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/Despesas_Anuais.png)

![Analise do Investimento](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/Analise_Financeira.png)

# Arquitetura do Sistema

A arquitetura do sistema proposta para a simulação e demonstração de um robô em espaço confinado com capacidade de obtenção de informações do ambiente e avaliação preliminar de atividades de operação e/ou manutenção é baseada em um conceito de Prova de Conceito (POC) e Produto Mínimo Viável (MVP). O objetivo é desenvolver um sistema robótico autônomo que possa explorar e interagir com o ambiente confinado de forma segura e eficiente. A arquitetura envolve a integração de diferentes componentes, como sensores para detecção de riscos atmosféricos, sistemas de navegação autônoma, algoritmos de tomada de decisão e um sistema de alerta sonoro ou outro meio de comunicação para notificar a presença de riscos. Além disso, a solução inclui a implementação de uma versão física simplificada do robô para fins de demonstração. Através dessa abordagem, busca-se validar a viabilidade e eficácia do conceito antes de um desenvolvimento completo do produto.

## Diagrama de blocos

<img src = "https://user-images.githubusercontent.com/99203402/235358909-034028ef-b4c0-4321-baf8-dd8a06624598.jpg" width="600">

Embora a imagem acima represente o primeiro esboço da arquitetura da solução, criamos uma nova versão para uma melhor visualização, apresentada na imagem abaixo.

![Arquitetura da Solução - v1]( https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/arquitetura%20da%20solu%C3%A7%C3%A3o%20v1.png) 

### Descrição

Temos três componentes principais na arquitetura do sistema:

- O componente **embarcado** é responsável pela implementação do ROS2 (Robot Operating System) no sistema operacional Ubuntu, executado no microprocessador Raspberry Pi, que coordena os movimentos do robô por meio de comandos enviados para o microcontrolador Cortex M4 STM32F407. Além disso, alguns periféricos, como câmera, sensor de gás, sensor de temperatura e LIDAR (Light Detection and Ranging), serão acoplados ao sistema para melhorar sua eficiência e precisão. Todos os periféricos se comunicarão diretamente com o microprocessador, e a interface de comunicação escolhida para o robô é a pub/sub.

- O componente **backend** implementa a arquitetura ROS2 (Robot Operating System) para receber e enviar informações por meio dos tópicos pub/sub (publisher/subscriber), comunicando-se diretamente com o robô. Além disso, ele inclui um framework, um banco de dados e um ORM (Object-Relational Mapping). Além da interface pub/sub (publisher/subscriber), o backend também utiliza a comunicação HTTP (HyperText Transfer Protocol).

- O componente **frontend** utiliza do framework react para a paginação e CSS para a estilização. Ele se comunica com o resto do sistema por meio da interface HTTP disponibilizada pelo backend.

## Análise de requisitos

### Requisitos Funcionais

1. Inspeção dos ambientes durante e após da manutenção
2. Detecção de condições atmosféricas (presença de gases tóxicos) dos espaços confinados
3. Sensores para detectar os gases, e talvez detectar colisões
4. Robô ser capaz de retornar ao ponto inicial em casos de erros/defeitos/objetos no meio do caminho
5. Movimentação por joystick (casos de emergência)
6. Interface web apresentando um dashboard com dados coletados e imagens em tempo real, além de poder gerar relatórios em PDF

### Requisitos não funcionais

1. Funcionamento confiável e eficiente no processo de monitoramento e inspeção
2. Confiança nos dados gerados
3. Monitoramento e inspeção em tempo real
4. Interface web de fácil compreensão por aqueles usuários que a utilizem

## Análise de viabilidade técnica

O projeto é uma solução para os desafios enfrentados pelos técnicos que lidam com espaços confinados em seu dia a dia, tendo como objetivo principal simplificar as tarefas de segurança e inspeção, por meio de um sistema automatizado. Dessa maneira, optamos por adotar o TurtleBot Burger, um robô com capacidade de processamento adequada para os sistemas que iremos empregar, mesmo que ele enfrente algumas limitações em relação à sua mobilidade, especialmente em terrenos irregulares, sua vantagem reside em seu tamanho compacto, permitindo seu acesso a espaços confinados, além de ser uma ótima ferramenta educacional.

Ademais, o robô será equipado com sensores integrados projetados para detectar níveis de gases tóxicos no ambiente. Contudo, é importante mencionar que eles têm uma limitação e só podem detectar até cinco tipos de gases tóxicos. Assim mesmo sendo de uma natureza mais básica, os sensores selecionados são semelhantes aos utilizados na indústria.

Por fim, no que diz respeito ao armazenamento de dados, o robô contará com um sistema de comunicação baseado em tópicos, sendo assim essa configuração permite que as informações sejam transmitidas e armazenadas de forma eficiente.

# Interface web (frontend)

Em nossa interface atual, estamos implementando algumas atualizações para melhorar a experiência do usuário. Começamos com a adição de uma tela de login que utiliza o nextAuth, uma biblioteca que nos permite autenticar apenas usuários com domínio da Gerdau. Isso garante que apenas pessoas autorizadas tenham acesso ao sistema.

Após o login, os usuários serão redirecionados para um dashboard inicial, onde poderão editar o relatório. No dashboard, eles terão a opção de modificar informações como título do relatório e adicionar observações relevantes. Além disso, estamos trabalhando para implementar uma funcionalidade adicional que permitirá que os usuários baixem o relatório em formato PDF, facilitando sua visualização e compartilhamento.

No dashboard, também teremos um botão para iniciar a movimentação do robô. Essa opção será especialmente útil para usuários que desejam coletar dados atmosféricos e explorar ambientes confinados. No entanto, pensando na flexibilidade, também incluiremos a opção de pausar a movimentação do robô, caso seja necessário interromper temporariamente suas atividades.
Em nossa interface atual, estamos implementando algumas atualizações para melhorar a experiência do usuário. Começamos com a adição de uma tela de login que utiliza o nextAuth, uma biblioteca que nos permite autenticar apenas usuários com domínio da Gerdau. Isso garante que apenas pessoas autorizadas tenham acesso ao sistema.

Por fim, desenvolveremos uma página de histórico que permitirá aos usuários acessar todos os relatórios anteriores. Nessa página, eles terão a opção de filtrar o histórico por data ou ID, facilitando a localização de relatórios específicos. Essa funcionalidade auxiliará os usuários a revisitar relatórios antigos, realizar comparações ou acessar informações relevantes de forma rápida e eficiente.

Essas melhorias na interface visam tornar o uso do sistema mais intuitivo, eficiente e personalizado para atender às necessidades dos usuários da Gerdau.

### Tela de Login
<img width="600" alt="Captura de tela 2023-05-29 141300" src="https://github.com/2023M6T2-Inteli/Splinters/assets/99203402/c8d549b9-a29d-412e-a7cd-804484789095">

### Dashboard
<img width="600" alt="Captura de tela 2023-05-29 141436" src="https://github.com/2023M6T2-Inteli/Splinters/assets/99203402/7a099e25-4665-4419-a632-8b859429d4db">

### Página de histórico
<img width="600" alt="Captura de tela 2023-05-29 141457" src="https://github.com/2023M6T2-Inteli/Splinters/assets/99203402/f0c50d63-ca09-4d20-bac0-31f589e2a17c">


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

## Algoritmo em grafo e movimentação

O script Python ```./src/embedded/modules/best_path.py``` utiliza a biblioteca rclpy para controlar um robô tartaruga criando um grafo de nós e arestas com pesos baseados na distância entre os nós, encontrando o melhor caminho através de todos os nós usando o algoritmo do problema do caixeiro viajante da biblioteca networkx, e movendo o robô tartaruga ao longo do caminho publicando mensagens Twist no tópico cmd_vel e se inscrevendo em mensagens Odometry do tópico /odom. O script define funções para criar um grafo, encontrar o melhor caminho e controlar o robô tartaruga, bem como uma classe TurtleController que usa rclpy para criar um nó para publicar e se inscrever em mensagens. A função main solicita ao usuário que insira as coordenadas dos nós e arestas, cria um grafo, encontra o melhor caminho através de todos os nós e controla o robô tartaruga para se mover ao longo do caminho.

Tecnicamente, o script começa importando as bibliotecas necessárias e definindo uma função Graph para criar um grafo de nós e arestas com pesos baseados na distância entre os nós. A função define uma classe Position_Node para representar os nós com um nome e coordenadas x e y, e uma função Weighed_Edge para criar uma aresta entre dois nós com um peso baseado na distância entre eles. A função então solicita ao usuário que insira as coordenadas dos nós e adiciona-os ao grafo. Em seguida, solicita ao usuário que insira as arestas entre os nós e adiciona-as ao grafo com pesos baseados na distância entre os nós.

O script também define uma função best_path_all_nodes para encontrar o melhor caminho através de todos os nós no grafo usando o algoritmo do problema do caixeiro viajante da biblioteca networkx. A função recebe como entrada um grafo e um nó de origem e retorna uma lista de nós representando o melhor caminho através de todos os nós no grafo.

Em seguida, o script define uma classe TurtleController para controlar um robô tartaruga usando rclpy para criar um nó que publica mensagens Twist no tópico cmd_vel e se inscreve em mensagens Odometry do tópico /odom. A classe define uma função move_turtle que move o robô tartaruga ao longo do caminho publicando mensagens Twist no tópico cmd_vel com base na posição atual do robô e na próxima posição no caminho. A função calcula a diferença nas coordenadas x e y entre a posição atual e a próxima posição no caminho e usa isso para calcular um ângulo para virar em direção à próxima posição. A função então publica mensagens Twist com velocidades lineares e angulares para mover o robô em direção à próxima posição no caminho.

O código também define uma função de retorno de chamada pose_callback para a classe TurtleController que atualiza a posição atual do robô tartaruga com base em mensagens Odometry do tópico /odom.

Finalmente, o código define uma função main que cria um grafo de nós e arestas usando a entrada do usuário, encontra o melhor caminho através de todos os nós usando o algoritmo do problema do caixeiro viajante da biblioteca networkx, e controla um robô tartaruga para se mover ao longo do caminho usando rclpy. A função main inicializa rclpy, cria uma instância da classe TurtleController com o caminho calculado, gira até ser interrompida por um evento de usuário ou sistema, depois a destroi e desliga rclpy.

### Sistema anticolisão

O sistema de anti-colisão implementado neste script utiliza o LIDAR (Light Detection and Ranging) do Turtlebot para verificar continuamente a presença de obstáculos à frente do robô. O LIDAR gera uma lista de pontos, representando as distâncias em relação ao robô. Os pontos selecionados para verificação correspondem às distâncias à frente do robô.

Caso seja detectado um objeto a uma distância inferior a 30cm do robô, e diretamente em sua trajetória, ou seja, se o robô continuar avançando, ocorrerá uma colisão iminente. Nesse momento, o modo de movimentação automática é interrompido e o controle passa para o modo manual.

No modo manual, o robô monitora as entradas do terminal, especificamente os comandos 'a', 'd', 'w', 'x' e 's', que correspondem a aumentar a velocidade angular para a esquerda, aumentar a velocidade angular para a direita, aumentar a velocidade linear para a frente, aumentar a velocidade linear para trás e parar completamente o robô, respectivamente. Essa funcionalidade permite que o operador do robô possa movimentá-lo para entender melhor o obstáculo através da câmera e desviar dele.

Além disso, o código também verifica a entrada 'k' para retornar ao modo automático. Quando essa entrada é recebida, o robô retoma o percurso preestabelecido e continua em direção ao próximo ponto que estava seguindo antes da interrupção.

O objetivo principal desse sistema é garantir a segurança do robô, evitando colisões com obstáculos. Ele proporciona ao operador a capacidade de controlar manualmente o robô para analisar e evitar obstáculos de maneira mais precisa, antes de retornar ao modo automático e prosseguir com sua rota planejada.

<a href="https://www.youtube.com/watch?v=KR6Fwj-3By8">Video demontrando movimentação do robo com sistema de otimização de rotas e sistema anti colisão</a>

# Sistema de visão computacional

## Implementação do sistema de visão computacional

A implementação do sistema de visão computacional foi desenvolvida com o modelo de detecção de objetos pré-treinado, YOLOv8 (You Only Look Once versão 8) e é capaz de identificar rachaduras em paredes de concreto com o uso de um dataset do Roboflow.

Explicação do notebook e script em Python:

1. **Preparação do Ambiente:** Instalação da biblioteca 'ultralytics'.

2. **Preparação do dataset:** No notebook, acessamos o dataset de rachaduras em paredes de concreto fornecido pela Roboflow.

3. **Treinamento do modelo:** A partir do dataset do roboflow, treinamos o modelo com o código a seguir:

```bash
!yolo train data=/content/crack-2/data.yaml model=sample_data/yolov8n.pt epochs=10 lr0=0.01
```

4. **Configuração do script:** 

Importar as bibliotecas necessárias:

```bash
from ultralytics import YOLO
import cv2 as cv
```

Carregar o modelo YOLO pré-treinado:

```bash
model = YOLO('./semana5/best.pt')
```

5. **Detecção de Rachaduras:**

Inicialização da captura de vídeo da webcam:

```bash
capture = cv.VideoCapture(0)
```

Criação de um loop para capturar quadros (frames) da captura de vídeo e realizar a detecção de objetos:

```bash
while True:
    _, frame = capture.read()
    result = model.predict(frame, conf=0.6)
    cv.imshow('frame', result[0].plot())
    if cv.waitKey(1) == ord('q'):
        break
```

No código acima, cada quadro capturado é passado para o modelo YOLO, que realiza a detecção de objetos com base nas rachaduras presentes no quadro. O resultado da detecção é exibido em uma janela com o nome 'frame'. O loop é interrompido quando a tecla 'q' é pressionada.

6. **Execução do script:** Execute o script Python no terminal ou prompt de comando. Assim, o script iniciará a captura de vídeo da webcam e exibirá os quadros com as detecções de rachaduras em tempo real.

## Validação da eficácia e performance do sistema de visão computacional

### Curva de confiança F1

A F1 Confidence Curve é uma métrica usada para avaliar a confiabilidade de um modelo de aprendizado de máquina em tarefas de classificação binária, representando a relação entre o valor de confiança atribuído pelo modelo a uma previsão e a pontuação F1 resultante dessa previsão.

![Curva F1](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/F1_curve.png)

A curva é útil para visualizar como o desempenho do modelo varia com diferentes níveis de confiança e identificar áreas onde ele pode estar superconfiante ou subconfiante, podendo ser valiosa na avaliação da calibração do modelo e na identificação de possíveis problemas de confiabilidade. Dessa maneira, na imagem temos uma parábola invertida, o que revela alguns pontos de uma relação não linear entre o valor de confiança atribuído pelo modelo e a pontuação F1 resultante.

### Curva Precision-Recall

A PR (Precision-Recall) Curve é uma métrica comumente usada para avaliar o desempenho de modelos de aprendizado de máquina em tarefas de classificação, especialmente quando há um desequilíbrio significativo entre as classes, representando a relação entre a precisão (precision) e o recall (revocação) do modelo em diferentes pontos de corte ao longo do espectro de confiança.

Sendo assim, a precisão mede a proporção de instâncias corretamente classificadas como positivas em relação ao total de instâncias classificadas como positivas, enquanto o recall mede a proporção de instâncias positivas corretamente identificadas em relação ao total de instâncias verdadeiramente positivas. Desse modo, ao plotar os valores de recall no eixo x e os valores de precisão no eixo y, a PR Curve oferece uma representação visual do trade-off entre essas duas métricas.

![Curva PR](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/PR_curve.png)

A curva acima, indica um trade-off entre precisão e recall. Nessa configuração, o modelo pode obter altas taxas de recall, ou seja, conseguir identificar corretamente a maioria das instâncias positivas, porém, em detrimento da precisão, resultando em um aumento das falsas positivas.

### Curva Precision-Confidence

A P Curve mostra como a precisão do modelo evolui à medida que o limite de classificação é ajustado, representando a proporção de verdadeiros positivos (TP) em relação ao número total de instâncias positivas (TP + falsos negativos, FN) à medida que o valor de corte é variado.

Dessa maneira, ao plotar os valores de recall no eixo x e os valores de precisão no eixo y, a curva permite visualizar como a precisão é afetada pelo equilíbrio entre os verdadeiros positivos e os falsos positivos.

![Curva P](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/P_curve.png)

A imagem acima, representa uma curva que mostra um aumento gradual na precisão à medida que o valor de corte é ajustado, ou seja, ao aumentar o limite de classificação, o modelo é capaz de identificar corretamente mais instâncias positivas em relação ao total de instâncias classificadas como positivas, resultando em uma maior taxa de precisão.

### Curva Recall-Confidence

A R Curve, ou Curva R, é uma métrica usada para avaliar a revocação (recall) de um modelo de aprendizado de máquina em tarefas de classificação binária, caracterizando a proporção de verdadeiros positivos (TP) em relação ao número total de instâncias positivas (TP + falsos negativos, FN) à medida que o valor de corte é variado.

Dessa maneira, ao plotar os valores de precisão no eixo x e os valores de recall no eixo y, a Curva R permite visualizar como a revocação é afetada pelo equilíbrio entre os verdadeiros positivos e os falsos negativos.

![Curva R](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/R_curve.png)

A imagem representa uma relação não linear entre o valor de corte e a revocação, tal configuração sugere que, ao ajustar o limite de classificação, o modelo pode alcançar uma revocação mais alta para determinados valores de corte.

### Matriz de confusão

A Matriz de Confusão é uma representação tabular usada para avaliar o desempenho de um modelo de aprendizado de máquina em tarefas de classificação, resumindo os resultados das previsões em relação aos valores verdadeiros das instâncias.

A matriz organiza as previsões em quatro categorias: verdadeiros positivos (TP), falsos positivos (FP), verdadeiros negativos (TN) e falsos negativos (FN). Assim, os verdadeiros positivos correspondem às instâncias corretamente classificadas como positivas, os falsos positivos representam as instâncias erroneamente classificadas como positivas, os verdadeiros negativos são as instâncias corretamente classificadas como negativas e os falsos negativos indicam as instâncias erroneamente classificadas como negativas.

![Matriz de Confusão](https://github.com/2023M6T2-Inteli/Splinters/blob/dev/docs/assets/confusion_matrix_normalized.png)

Quando os valores superiores são 0.79 e 1, indica que o modelo obteve uma alta taxa de acerto para a classe positiva, ou seja, isso significa que 79% das instâncias positivas foram corretamente classificadas como positivas, enquanto todas as instâncias negativas foram corretamente classificadas como negativas. 

Já os valores inferiores, indicam que 21% das instâncias negativas foram erroneamente classificadas como positivas (falsos positivos), enquanto as demais instâncias negativas foram corretamente classificadas como negativas.

## Integração do sistema de visão computacional com a arquitetura ROS2:

Para a implementação dessa integração foi necessário contruir um publisher que envia imagens coletadas da câmera acoplada ao robô ( Turtlebot ) e as publica em um tópico denominado "/camera". Do outro lado, temos um subscriber que recebe os dados enviados, os trata para o tipo de dado que o modelo reconhece como input e mostra na tela o resultado da análise feita após o método de predição ```result = model.predict(current_frame, conf=0.6)```.

### Descrição técnica:

#### **Subscriber:**

  1 - Importação dos pacotes e métodos necessários para o tratamento e renderização do output do modelo:
  
    ```
    import cv2
    import base64
    import asyncio
    import websockets
    from rclpy.node import Node
    from ultralytics import YOLO
    from cv_bridge import CvBridge
    from sensor_msgs.msg import Image
    ```
  2 - Definição da classe "Streaming" que traz a lógica de receber os dados, tratá-los, fazer o input deles para a análise por parte do modelo e renderização do resultado:

    ```
    class Streaming(Node):

    def __init__(self):
      super().__init__('image_subscriber')
      self.subscription = self.create_subscription(
        Image, 
        '/camera', 
        self.listener_callback, 
        10)
      self.subscription 
      self.bridge = CvBridge()
      self.websocket_url = "ws://localhost:8000/ws"
      self.websocket = websockets.connect(self.websocket_url)

    async def send_frame_via_websocket(self, frame_base64):
      async with self.websocket as websocket:
        await websocket.send(frame_base64)

    def listener_callback(self, data):
      self.get_logger().info('Receiving video frame')
      current_frame = self.bridge.imgmsg_to_cv2(data)
      model = YOLO("./yolo/best.pt")
      result = model.predict(current_frame, conf=0.6)
      annotated = result[0].plot()
      _, frames = cv2.imencode(".jpg", annotated)
      frame_base64 = base64.b64encode(frames).decode("utf-8")
      print ("início        " + frame_base64 + "        fim")
      asyncio.get_event_loop().run_until_complete(self.send_frame_via_websocket(frame_base64))
    ```
    
   3 - Para iniciar esse subscriber, atribuímos ao arquivo "main.py" localizado no path: ```./src/backend/ros``` o seguinte código:
   
    ```
    import rclpy
    from modules import Streaming


    def main(args=None):
        rclpy.init(args=args)
        image_subscriber = Streaming()
        rclpy.spin(image_subscriber)
        image_subscriber.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
      main()
    ```

#### **Publisher:**

   1 - Importação dos pacotes e métodos necessários para coletar as imagens da camera acoplada ao robô e publicá-las no tópico "/camera":

    ```
    import cv2 
    import rclpy
    from rclpy.node import Node
    from cv_bridge import CvBridge
    from sensor_msgs.msg import Image
    ```

  2 - Definição da classe "Camera" que traz a lógica de captar os dados da câmera acoplada ao robô, tratá-los e publicá-los no tópico "/camera" para que o "subscriber" possa recebê-los para fazer a lógica anteriormente descrita.
  
    ```
    class Camera(Node):
      def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Image, '/camera', 10)
        timer_period = 0.001
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.cap = cv2.VideoCapture(0)
        self.bridge = CvBridge()

      def timer_callback(self):
        ret, frame = self.cap.read()
        if ret == True:
          self.publisher_.publish(self.bridge.cv2_to_imgmsg(frame))
        self.get_logger().info('Publishing video frame')
    ```
  
  3 - Para iniciar esse publisher, atribuímos ao arquivo "main.py" localizado no path: ```./src/embedded``` o seguinte código:
  
    ```
    import rclpy
    from modules import Camera


    def main(args=None):
        rclpy.init()
        camera = Camera()
        rclpy.spin(camera)
        camera.destroy_node()
        rclpy.shutdown()


    if __name__ == "__main__":
        main()
    ```  
    
**Demonstração em vídeo:** https://www.youtube.com/watch?v=YvxhzSp2Roo

## Backend

### Supabase e FastAPI

Implementamos nossa infraestrutura de backend utilizando o framework FastAPI, uma solução que permite a criação eficiente e ágil de APIs. Todo o código está organizado em um arquivo principal chamado main.py, responsável por iniciar o servidor.

Ao iniciar o servidor, disponibilizamos uma variedade de rotas (também conhecidas como endpoints) que viabilizam diferentes operações. Essas rotas foram desenvolvidas para lidar com o registro de imagens, interação com o banco de dados e acesso aos registros de imagens e frames analisados por meio da visão computacional previamente implementada.

Uma das APIs centrais tem a responsabilidade de enviar as imagens analisadas pelo YoloV8 para o Supabase, um serviço online utilizado para armazenar e gerenciar os arquivos. Essa API possibilita o envio seguro das imagens ao Supabase, garantindo seu armazenamento e permitindo a recuperação posterior, caso necessário.

A seguir, apresentamos uma descrição abrangente de cada uma das APIs desenvolvidas, juntamente com as informações necessárias para sua utilização e os caminhos de acesso correspondentes. O objetivo dessa descrição é fornecer uma compreensão clara das funcionalidades e capacidades do nosso backend, permitindo que os desenvolvedores interajam de forma adequada e eficaz com as APIs, inclusive aproveitando a API para enviar imagens ao Supabase.

#### APIs e rotas

### Websocket

O websocket é implementado no nosso sistema para a integração do ros2 com o frontend para a transmissão dos frames, mediante utput do modelo YOLO, no frontend. O código abaixo descreve essa impmentação, a qual está presente no arquivo ```src/backend/app.py```:

```
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in connected_clients:
                await client.send_text(data)
    except Exception as e:
        print(f"WebSocket connection closed with exception: {e}")
    finally:
        connected_clients.remove(websocket)
```

- Nesse sentido, esse canal wenbsocket é utilizada pelo subscriber do tópico "/camera" presente no arquivo streaming e implementado na classe "Streaming":

```
class Streaming(Node):

  def __init__(self):
    super().__init__('image_subscriber')
    self.subscription = self.create_subscription(
      Image, 
      '/camera', 
      self.listener_callback, 
      10)
    self.subscription 
    self.bridge = CvBridge()
    self.websocket_url = "ws://localhost:8000/ws"
    self.websocket = websockets.connect(self.websocket_url)

  async def send_frame_via_websocket(self, frame_base64):
    async with self.websocket as websocket:
      await websocket.send(frame_base64)

  def listener_callback(self, data):
    self.get_logger().info('Receiving video frame')
    current_frame = self.bridge.imgmsg_to_cv2(data)
    model = YOLO("./yolo/best.pt")
    result = model.predict(current_frame, conf=0.6)
    annotated = result[0].plot()
    _, frames = cv2.imencode(".jpg", annotated)
    frame_base64 = base64.b64encode(frames).decode("utf-8")
    print ("início        " + frame_base64 + "        fim")
    asyncio.get_event_loop().run_until_complete(self.send_frame_via_websocket(frame_base64))
```

- Segue uma foto que demonstra essa integração:

![img_4917_720](https://github.com/2023M6T2-Inteli/Splinters/assets/89201795/a98ebefd-bad5-4b18-8c63-55f2d8117a7c)

- Continuando no âmbito de comunicação via websocket, temos também dados de bateria protos para serem levados para o frontend via websocket. Aqui, nós estamos tendo ainda alguns problemas para deixar estável a comunicação tanto da bateria, quanto dos frames da câmera ( tentaremos nessa sprint explorar o socketio para testar se conseguimos melhorar essa trasmissão ). Abaixo o cógiddo da so subscriber da bateria, coletando dados de da voltagem publicados no tópico ```/battery_state```. O código também contempla o cálculo para retonar para o frontend a porcentagem da bateria do robô em tempo real:

```
import rclpy
import asyncio
import websockets
from rclpy.node import Node
from sensor_msgs.msg import BatteryState


class Battery(Node):
    def __init__(self):
        super().__init__('battery_subscriber')
        self.subscription = self.create_subscription(
            BatteryState,
            '/battery_state', 
            self.listener_callback, 
            10)
        
    async def send_battery_via_websocket(self, relative_battery_percent):
        async with websockets.connect("ws://localhost:8000/battery") as websocket:
            await websocket.send(relative_battery_percent)

    def listener_callback(self, battery):
        relative_battery_percent = (battery.voltage - 11)/1.6

        asyncio.get_event_loop().run_until_complete(self.send_battery_via_websocket(str(relative_battery_percent)))
        print(relative_battery_percent)

def main():
    rclpy.init()
    battery = Battery()
    rclpy.spin(battery)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

## Descrição dos sensores

Com o intuito de possibilitar a coleta de dados que permitam a análise da segurança do ambiente confinado e da possibilidade de ocorrência de acidentes, foram selecionados sensores que permitem a obtenção de informações relevantes para a análise do ambiente. Os sensores selecionados foram:

### Sensor de qualidade do ar (MQ-135)

Esse sensor apresenta a capacidade de detectar gases que podem ser prejudiciais para a saúde humana, como o dióxido de carbono, monóxido de carbono, amônia, benzeno, álcool, fumaça, entre outros. Os gases coletados por esse sensor, quando encontrados em altas concentações, podem causar problemas respiratórios, tontura, náusea, entre outros sintomas, prejudicando a saúde e o bem estar dos trabalhadores.

Esse sensor apresenta uma saída digital, que fornece um resultado binário indicando quando há ou não a presença desses gases em concentrações elevadas, e uma saída analógica, que fornece um valor de tensão proporcional à concentração de gases detectada. A saída digital é utilizada para a detecção de gases, enquanto a saída analógica é utilizada para a obtenção de dados quantitativos sobre a concentração de gases. 

A partir de uma análise dos dados enviados pela saída analógica, que apontavam valores próximos a 80(condições normais de gases) e mais de 900 (quantidades muito altas de gases), foi possível construir uma escala, de valores aproximadamente entre 10 e 100. Quanto maior o valor obtido, maior a concentração de gases detectada. Essa transformação foi realizada para facilitar a visualização dos dados pelo usuário final, de forma mais clara e intuitiva.

### Sensor de temperatura e umidade (DHT11)

Esse sensor apresenta a capacidade de detectar a temperatura e a umidade do ambiente. A temperatura e a umidade são fatores que podem influenciar na saúde e no bem estar dos trabalhadores, além da conservação do ambiente confinado. Além disso, a temperatura e a umidade também podem influenciar na ocorrência de acidentes, como o aumento da probabilidade de incêndios e explosões.

Ao utilizar a biblioteca DHT.h, foi possível obter os valores de temperatura e umidade em graus Celsius e porcentagem, respectivamente. Esses valores são obtidos a partir de uma saída digital, que fornece um resultado binário indicando quando há ou não a presença desses gases em concentrações elevadas, e uma saída analógica, que fornece um valor de tensão proporcional à concentração de gases detectada. A saída digital é utilizada para a detecção de gases, enquanto a saída analógica é utilizada para a obtenção de dados quantitativos sobre a concentração de gases. A partir da saída analógica, foi possível construir uma escala, de valores aproximadamente entre 10 e 100. Quanto maior o valor obtido, maior a concentração de gases detectada. Essa transformação foi realizada para facilitar a visualização dos dados pelo usuário final, de forma mais clara e intuitiva.

## Utilização do microcontrolador

Devido à falta de portas analógicas do microprocessador Raspberry Pi 4 e também do microcontrolador OPEN-CR (integrados ao robô), foi necessário utilizar um microcontrolador externo para a coleta dos dados dos sensores. Com esse intuito, foi utilizado um microcontrolador Arduino Uno, que apresenta portas analógicas para a coleta dos dados dos sensores. A comunicação entre o microcontrolador e o Raspberry Pi 4 foi realizada por meio de uma comunicação serial, utilizando um cabo USB.
