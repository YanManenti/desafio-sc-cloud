# Desafio SC Cloud

### 1. Diferenciar as camadas 2 e 3 do modelo OSI, e indicar os protocolos utilizados para endereçamento nestas camadas.

**R:** A segunda camada do modelo OSI, conhecida como camada de Enlace, trabalha com transferência, detecção/correção de erros em frames de uma rede local. Isso é possível devido a suas duas subcamadas LLC e MAC.  

Exemplos de protocolos de endereçamento em enlace: MAC(Físico).

A terceira camada do modelo OSI, conhecida como camada de Rede, responde a pedidos da camada de transporte, trabalhando com a transferência incluindo roteamento de pacotes entre uma ou mais redes com a utilização de *routers*.

Exemplos de protocolos de endereçamento em rede: IP(Lógico).

A principal diferença entre as duas camadas é sua área de atuação. A camada de Enlace trabalha apenas em redes locais enquanto a camada de Rede usa *routing* para alcançar outras redes.   

### 2. Qual a diferença entre adotar uma solução proprietária como o sistema operacional Windows quando comparado a adoção de uma solução Open Source como o sistema operacional Ubuntu? Quais seriam os pontos negativos e positivos de cada abordagem?

**R:** A adoção de um *software* depende das necessidades de seu usuário. *Softwares* operacionais proprietários como o Windows da Microsoft e Open Source como o Ubuntu naturalmente não podem executar programas intercambiávelmente, ele deve ser reescrito ou emulado para tal.

Pontos positivos S.O. proprietário: maior compatibilidade com ecossistemas e outros aplicativos proprietários, maior familiariedade e alta garantia de suporte.

Pontos negativos S.O. proprietário: custo de licenciamento, maior alvo para ataques, pior desempenho e menor flexibilidade.

Pontos positivos S.O. Open Source: geralmente licenciamento grátis, bom suporte com disponibilidade variável, arquitetura segura, alto desempenho(especialmente em servidores), boa integração com outros projetos *open source* e alto nível de customização. 

Pontos negativos S.O. Open Source: pode exigir adaptações dependendo do *software* necessário e pode exigir adaptações dos usuários.

### 3. O que seria um projeto Open Source? Como empresas podem adotar tais tecnologias e o que isso acarreta?

**R:** *Softwares* Open Source são desenvolvidos de forma descentralizada e colaborativa, conta com a revisão, a produção pela comunidade e a possibilidade de gerar soluções bem específicas. Normalmente é mais flexível, veloz, barato e duradouro que as opções proprietárias. Além disso, todo o contexto de colaboração fica registrado com total transparência e ainda pode gerar novidades que vão além do próprio projeto.

A adoção de projetos Open Source por grande parte depende do seu licenciamento. Para adotar projetos Open Source a empresa necessita adotar *softwares* de origem Open Source como: Linux, Git, Apache HTTP Server, Node.js, Docker, Kubernetes, PostgreSQL, etc. Caso não seja compatível, a empresa ainda pode buscar adaptar uma solução Open Source ao seu *software*, neste caso ela deve fazer ou contratar terceiros para fazer alterações no projeto, tais alterações no Open Source serão salvas no respetivo repositório oficial(Upstreaming), trazendo melhorias para ambos empresa e projeto. 

Soluções empresariais Open Source são bem estabelecidas, testadas e suportadas. Uma empresa pode escolher projetos sob medida e fazer adaptações necessárias para que o seu produto funcione em conjunto. Tais práticas dão uma maior liberdade tecnológica e garante que a empresa evolua com o mercado.
