# Sistema de Gestão para Marcenaria

Este projeto é um sistema web desenvolvido em Python utilizando Flask, criado com o objetivo de auxiliar no gerenciamento de clientes, orçamentos e projetos em uma marcenaria.

A aplicação permite registrar clientes, gerar orçamentos de móveis planejados e acompanhar o andamento dos projetos de produção. O sistema foi desenvolvido com foco em organização de processos e controle das etapas de produção, simulando o funcionamento de um pequeno ERP para marcenarias.

## Funcionalidades

* Cadastro de clientes
* Edição e exclusão de clientes
* Geração de orçamentos com cálculo automático
* Criação e gerenciamento de projetos
* Alteração de status dos projetos (Planejamento, Em produção, Finalizado)
* Dashboard com indicadores do sistema
* Listagem e edição rápida diretamente nas tabelas

## Tecnologias utilizadas

* Python
* Flask
* SQLAlchemy
* SQLite
* HTML5
* CSS3
* Jinja2

## Estrutura do projeto

O projeto foi organizado seguindo boas práticas de separação de responsabilidades:

* **models**: definição das entidades do banco de dados
* **routes**: rotas e controladores da aplicação
* **services**: lógica de negócio, como cálculo de orçamentos
* **templates**: interface do usuário com Jinja2
* **static**: arquivos estáticos como CSS

## Objetivo do projeto

Este sistema foi desenvolvido como parte de um portfólio para demonstrar conhecimentos em desenvolvimento web com Python, estruturação de aplicações com Flask e integração com banco de dados.

O projeto simula um ambiente real de gestão de uma marcenaria, permitindo praticar conceitos de arquitetura de software, CRUD completo e organização de aplicações web.
