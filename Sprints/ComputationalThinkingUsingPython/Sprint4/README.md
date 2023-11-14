# PYTHONCHALLENGE

<h1 align="center">
🚘<br>Guinchei Python
</h1>
 
<p align="center">
<img src="GuincheiLogo.svg" alt="Logo Guinchei" width=300>
</p>

> Repositório utilizado para a entrega do Challenge 4 de Python

## 📖 Sobre o Challenge

| _Challenge 4_ |                                       |
| ------------- | ------------------------------------- |
| _Curso_       | Análise e Desenvolvimento de Sistemas |
| _Disciplina_  | Computational Thinking Using Python   |
| _Professor_   | Albérico de Castro Barros Filho       |
| _Turma_       | 1TDSS                                 |

## ❗| Observação importante:

Caso o projeto imprima um erro de Instant Client, é necessário instalar o Instant Client do Oracle e extrair o arquivo .zip na pasta do projeto, disponível no link abaixo:
https://download.oracle.com/otn_software/nt/instantclient/2112000/instantclient-basic-windows.x64-21.12.0.0.0dbru.zip

## 📝| Descrição do projeto:

O projeto consiste em um programa em Python que permite a listagem, inserção, alteração e exclusão de modelos de veículos em um banco de dados ORACLE.
O programa permite a inserção de dados como marca, modelo e tipo, e a partir disso, é possível realizar as operações citadas anteriormente.
Os dados são armazenados em um banco de dados ORACLE fornecido pela FIAP.
O objetivo é visualizar o funcionamento de um CRUD (Create, Read, Update, Delete) em Python e a manipulação de um banco de dados ORACLE.

> Obs: Está alterando no banco de dados Oracle que está sendo utilizado na aplicação Web

## 📖| Instruções para execução do projeto:

1. Instalar as dependências necessárias para a execução do projeto (no arquivo requirements.txt)
2. Executar o arquivo main.py (caso não ache um banco de dados, executar o arquivo api.py)
3. A partir daí, o programa deve rodar normalmente, e será possível realizar as operações de listagem, inserção, alteração e exclusão de modelos de veículos.
4. A aplicação está self signed,

## 🚏| Endpoints:

| Método | Rota  | Descrição                |
| ------ | ----- | ------------------------ |
| GET    | /     | retorna todos os modelos |
| GET    | /<id> | retorna um modelo        |
| POST   | /     | cria um novo modelo      |
| PUT    | /<id> | atualiza um modelo       |
| DELETE | /<id> | remove um modelo         |

## 🫂| Créditos:

https://www.luiztools.com.br/post/base-de-dados-com-todas-as-marcas-e-modelos-de-veiculos/ - Csv com marcas e modelos de veículos

## ✍️ Integrantes

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Asteriuz">
        <img src="https://avatars.githubusercontent.com/u/89879115?v=4" width="115px;" alt="Foto do Augusto no GitHub"/><br>
        <sub>
          <strong>Augusto Barcelos Barros</strong>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/gribl88">
        <img src="https://avatars.githubusercontent.com/u/126920453?v=4" width="115px;" alt="Foto do Gabriel Gribl no GitHub"/><br>
        <sub>
          <strong>Gabriel Gribl de Carvalho</strong>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/GabrielSouzaQ">
        <img src="https://avatars.githubusercontent.com/u/126726456?v=4" width="115px;" alt="Foto do Gabriel Souza no GitHub"/><br>
        <sub>
          <strong>Gabriel Souza de Queiroz</strong>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/GabsBecca">
        <img src="https://avatars.githubusercontent.com/u/126920756?v=4" width="115px;" alt="Foto da Gabriela no GitHub"/><br>
        <sub>
          <strong>Gabriela Zanotto Alves Rodrigues</strong>
        </sub>
      </a>
  </tr>
</table>
