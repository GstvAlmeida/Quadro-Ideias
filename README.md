# Quadro de Ideias - Terço da Juventude 

Este projeto foi criado para simplificar e organizar a coleta de ideias, formas e elementos para a estruturação do Terço da Juventude. O objetivo é transformar sugestões soltas em um mural digital centralizado, visual e de fácil acesso para todos os envolvidos.

Desenvolvido como uma aplicação prática de fundamentos de engenharia de software e padrões de arquitetura web (MVT), o sistema utiliza o framework **Django** para garantir que cada contribuição seja devidamente registrada, armazenada e exibida em uma interface moderna. Este é um projeto focado em resolver problemas reais da comunidade enquanto consolida conhecimentos avançados de backend.

## Principais Funcionalidades

* **Persistência de Dados (Backend):** Toda ideia enviada é processada e armazenada de forma segura em um banco de dados relacional (SQLite), garantindo a integridade e o histórico das contribuições.
* **Upload de Referências Visuais:** O sistema permite o envio de imagens (PNG, JPG, WEBP) para ilustrar as ideias. As imagens são processadas pelo servidor e salvas fisicamente, mantendo o banco de dados leve e eficiente.
* **Interface Dinâmica e Interativa:** Frontend construído com foco em usabilidade (UI/UX), apresentando animações fluidas em CSS e interações via JavaScript, como o *preview* de imagens e suporte a *drag and drop*.
* **Mural em Tempo Real:** Assim que uma nova ideia é submetida, o sistema renderiza a sugestão em formato de *cards* responsivos e organizados logo abaixo do formulário.
* **Painel Administrativo:** Integração nativa com o `/admin` do Django para fácil gestão, moderação e controle do conteúdo cadastrado.

## Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework:** Django
* **Banco de Dados:** SQLite
* **Processamento de Imagem:** Pillow
* **Frontend:** HTML5, CSS3 e JavaScript

## Como Usar

O fluxo de trabalho foi projetado para ser rápido e eficiente:

1.  **Inicie o Sistema:** Com o ambiente virtual ativo, execute `python manage.py runserver` e acesse `http://127.0.0.1:8000/`.
2.  **Descreva a Ideia:** No campo de texto, digite a sua sugestão ou conceito para a estrutura.
3.  **Anexe uma Referência:** Arraste uma imagem para a zona de upload ou clique para selecionar. O sistema exibirá uma pré-visualização instantânea.
4.  **Envie para o Mural:** Clique no botão **"Enviar ideia"**. O backend validará os dados e salvará o registro.
5.  **Visualize o Resultado:** A página será atualizada e sua contribuição aparecerá no topo da lista de ideias, pronta para ser analisada pela equipe.