<table>
<tr>
<td>
<a href= "https://www2.gerdau.com.br/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Gerdau_logo_%282011%29.svg/1200px-Gerdau_logo_%282011%29.svg.png" alt="Gerdau" border="0" width="20%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

# Simulação de robôs para situações diversas - Gerdau

## Splinters

## Integrantes: Bianca Cassemiro, Gabriel Pascoli, Henrique Santos, Jackson Aguiar, Luana Parra, Pablo Ruan, Rafael Katalan

## Descrição

O projeto proposto é desenvolver um robô capaz de se movimentar em ambientes de espaço confinado, coletar dados utilizando sensores (principalmente de oxigênio e outros gases) e utilizar filmagens para auxiliar na inspeção prévia da estrutura. O objetivo principal é melhorar a segurança nas operações da Gerdau, mitigando a exposição ao risco dos colaboradores. A utilização de tecnologia robótica proporcionará uma avaliação prévia do ambiente, reduzindo a necessidade de acesso humano a esses espaços e, consequentemente, diminuindo os riscos associados. A implementação dessa solução trará benefícios significativos em termos de segurança, preservando a vida dos colaboradores e melhorando os indicadores de segurança da empresa. Além disso, o projeto visa desenvolver futuros líderes que se preocupem com a saúde e segurança dos colaboradores, independentemente da área de atuação.

## 🛠 Estrutura de pastas
```bash
.
├── LICENSE
├── README.md
├── .vscode
│   ├── c_cpp_properties.json
│   └── settings.json
├── docs
│   ├── assets
│   ├── _config.yml
│   ├── index.md
│   └── manual-splinters.docx.pdf
└── src
│   ├── .vscode
│   ├── backend-ros
|       |── ai
|       └── controllers
│   ├── backend
|       |── config
|       |── models
|       |── routers
|       └── services
│   ├── embedded
|       |── microcontroller
|       └── robot
│   ├── frontend
|       |── .next
|       |── components
|       |── pages
|       |── public
|       └── styles
    └── README.md

```
## 🛠 Instalação

Para instalar e configurar o sistema, siga as instruções detalhadas na pasta /docs.

### Tecnologias Utilizadas

- **Turtlebot3 Burguer:** Robô utilizado como AGV para realizar a inspeção dos espaços confinados, equipado com sensores de gás e câmera para captura de imagens.
- **ROS2:** Middleware de comunicação utilizado para integrar o AGV e os sensores ao sistema.
- **FastAPI:** Framework web utilizado para desenvolver a API que alimenta o dashboard e fornece os dados coletados pelo AGV.
- **YoloV8:** Um modelo de rede neural utilizado para detecção e análise de objetos, nesse caso, rachaduras nas paredes do ambiente.
- **React.js:** Biblioteca JavaScript para interfaces de usuário modernas e interativas.
- **Next.js:** Framework de desenvolvimento web utilizado para criar o frontend do dashboard, proporcionando uma experiência de usuário moderna e responsiva.
- **Supabase:** Banco de dados e serviço de armazenamento online de imagens utilizado para armazenar imagens capturadas pelo AGV durante a inspeção.
- **NAV2:** Pacote de navegação para o ROS2, responsável pelo planejamento de rotas e movimentação do AGV no espaço confinado.

## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"> This project is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>

## 🎓 Referências

Aqui estão as referências usadas no projeto.

1. <https://github.com/iuricode/readme-template>
2. <https://github.com/gabrieldejesus/readme-model>
3. <https://creativecommons.org/share-your-work/>

