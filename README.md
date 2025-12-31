#  Criador de Ficha de personagem RPG  – Python Tkinter

## Sobre o projeto
Este projeto é um aplicativo desktop em Python, desenvolvido como projeto de estudo durante a faculdade. A proposta foi criar uma ferramenta simples para criação e gerenciamento de fichas de RPG, explorando interface gráfica, lógica de jogo e persistência básica de dados. Não se trata de um produto comercial, mas de um exercício prático de programação e organização de aplicações desktop.

---


## Ideia do projeto
O aplicativo permite que o usuário crie personagens de RPG, escolha raça e classe, veja a imagem do personagem mudar dinamicamente conforme essas escolhas, gere atributos aleatórios no estilo RPG (força, agilidade, etc.), salve a ficha criada e acesse uma tela para listar e ler personagens já criados. A ideia foi simular, de forma simples, o processo clássico de criação de personagem em RPGs de mesa.

---


## Funcionamento geral
A aplicação inicia em uma tela principal com um menu simples, oferecendo opções para criar personagem, listar personagens ou sair. Na tela de criação, o usuário seleciona raça e classe, a imagem do personagem é atualizada automaticamente conforme essas escolhas e os atributos são gerados de forma aleatória. Na tela de listagem, os personagens salvos são exibidos, permitindo a visualização das fichas criadas anteriormente. Toda a interface foi construída diretamente com Tkinter, utilizando imagens e posicionamento manual de elementos, prática comum em projetos acadêmicos.

---


## Tecnologias utilizadas
O projeto foi desenvolvido utilizando Python como linguagem principal, Tkinter para construção da interface gráfica, recursos de exibição de imagens (PhotoImage / Pillow) para troca visual dos personagens e PyMySQL como experimento acadêmico de persistência de dados. A estrutura do código foi organizada de forma modular, distribuída nos arquivos JanelaInicial.py (tela principal), JanelaCadastro.py (criação de personagens) e JanelaListaPerson.py (listagem e leitura das fichas).

---


## Como rodar o projeto
Para executar o projeto é necessário ter o Python 3.x instalado.
Após clonar o repositório com `git clone https://github.com/willqos15/RPG-PYTHON.git`, acesse a pasta do projeto e execute o arquivo principal com `python JanelaInicial.py`. O aplicativo será iniciado em uma janela gráfica com o menu inicial.

---


## Estrutura do projeto

├── JanelaInicial.py        # Tela principal  
├── JanelaCadastro.py       # Criação de personagens  
├── JanelaListaPerson.py   # Listagem e leitura das fichas  
├── imagens/               # Imagens usadas na interface  
└── README.md  

---


## Observações
Este é um projeto antigo, desenvolvido com foco educacional. O código reflete o nível técnico e os objetivos acadêmicos da época, não segue padrões modernos de arquitetura e não possui fins comerciais.

---


## Objetivo educacional
Este projeto foi importante para consolidar conceitos como programação em Python, desenvolvimento de interfaces gráficas com Tkinter, uso de eventos e callbacks, organização de aplicações com múltiplas janelas e implementação de lógica básica inspirada em sistemas de RPG.
