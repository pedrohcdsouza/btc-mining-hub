[Português](README.md) | [English](README.en.md)

# BTC Mining Hub

BTC Mining Hub é um projeto que simula um ambiente de mineração de Bitcoin, onde agentes se conectam a um servidor mestre para realizar transações de mineração. O projeto inclui um bot do Telegram para monitorar e interagir com o servidor.

## Visão Geral

O projeto é composto por dois componentes principais:
- **Agent**: Representa um minerador que se conecta ao servidor mestre para realizar transações de mineração.
- **Master**: O servidor que gerencia as transações de mineração e se comunica com os agentes.

## Estrutura do Projeto

- `Agent/main.py`: Script principal do agente que configura a conexão com o servidor e inicia a mineração.
- `Agent/mylib.py`: Biblioteca com funções auxiliares para o agente, incluindo a lógica de mineração.
- `Master/main.py`: Script principal do servidor que configura a conexão e gerencia os agentes.
- `Master/mylib.py`: Biblioteca com funções auxiliares para o servidor, incluindo a lógica de transações e integração com o bot do Telegram.

## Como Usar

### Configuração do Servidor (Master)

1. Navegue até o diretório `Master`.
2. Execute o script principal do servidor:
    ```sh
    python main.py
    ```
3. O servidor estará escutando na porta `31471` e pronto para aceitar conexões de agentes.

### Configuração do Agente (Agent)

1. Navegue até o diretório `Agent`.
2. Execute o script principal do agente:
    ```sh
    python main.py
    ```
3. Insira um nome de usuário quando solicitado.
4. O agente se conectará ao servidor e aguardará transações de mineração.

### Comandos do Servidor

- `/newtrans`: Cria uma nova transação de mineração.
- `/validtrans`: Lista as transações validadas.
- `/pendtrans`: Lista as transações pendentes.
- `/clients`: Lista os agentes conectados.
- `/close`: Fecha o servidor e desconecta todos os agentes.

### Bot do Telegram

O servidor inclui um bot do Telegram para monitorar e interagir com o servidor. Os comandos disponíveis são:
- `/start`: Lista os comandos disponíveis.
- `/validtrans`: Lista as transações validadas.
- `/pendtrans`: Lista as transações pendentes.
- `/clients`: Lista os agentes conectados.

## Requisitos

- Python 3.x
- Bibliotecas: `socket`, `sys`, `threading`, `struct`, `hashlib`, `datetime`, `requests`

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
