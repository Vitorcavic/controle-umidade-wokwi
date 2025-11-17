# Sistema de Controle de Umidade com Simulação Wokwi

[Projeto](https://wokwi.com/projects/447877276853019649)

Sistema de controle de umidade que monitora condições ambientais e envia notificações via Telegram quando a umidade atinge limites pré-definidos.

## Funcionalidades

-  **Monitoramento contínuo** de temperatura e umidade com sensor DHT22
-  **Controle automático** do desumidificador (LED)
-  **Notificações inteligentes** via Telegram Bot
-  **Simulação** em tempo real
-  **Configuração fácil** de limites e intervalos

## Hardware Necessário

|  Componente  | Quantidade |             Função            | Pino ESP32 |
|--------------|------------|-------------------------------|------------|
| ESP32        | 1          | Microcontrolador              | -          |
| DHT22        | 1          | Sensor de Umidade/Temperatura | D15        |
| LED Vermelho | 1          | Indicador do Desumidificador  | D13        |
| Resistor     | 1          | Proteção do LEDs              | -          |

## Esquema do circuito
<img width="1588" height="1888" alt="code" src="https://github.com/user-attachments/assets/7b978740-7fb0-439c-a74b-27a0573cc0c0" />

## Configurações
### Parâmetros ajustáveis
<img width="1172" height="824" alt="configs_ajustáveis" src="https://github.com/user-attachments/assets/9cc84850-1548-4868-b907-e31a37be7756" />

## Telegram Bot
Crie um Bot:

- Busque por @BotFather no Telegram
- Use o comando /newbot
- Guarde o token fornecido

Obtenha seu Chat ID:

- Envie uma mensagem para @userinfobot
- Anote seu ID numérico
Configure as Variáveis no código:
<img width="926" height="444" alt="configs_telegram" src="https://github.com/user-attachments/assets/30c9f2ce-00f8-4856-92d3-8824d8fdd476" />

## Instalação
### No Wokwi Simulator
- Crie um novo projeto ESP32 em wokwi.com
- Substitua o código pelo conteúdo de main.py
- Configure o diagram.json com o esquema fornecido
- Execute a simulação

### Em Hardware Real
- Conecte os componentes conforme o diagrama
- Faça upload do código para o ESP32
- Monitore via Serial Monitor (115200 baud)

## Código Pincipal
<img width="2418" height="3864" alt="codigo_principal" src="https://github.com/user-attachments/assets/b3895486-4d44-4111-80aa-3c89fdf1d72c" />

## Como funciona
### Fluxo
Inicialização:
- Conecta no Wi-Fi
- Envia mensagem de inicialização
- Inicia monitoramento

Monitoramento contínuo:
- Lê a temperatua e umidade a cada 10 segundos
- Exibe dados no Serial Monitor

Controle Automático:
- Umidade ≥ 40%: Liga LED + notificação Telegram
- Umidade <= 30%: Desliga LED + notificação Telegram

## Notificações no Telegram
### Mensagem de Inicialização e Monitoramento
<img width="555" height="77" alt="Captura de tela 2025-11-17 135422" src="https://github.com/user-attachments/assets/de00e2a1-430a-4577-8226-1ebc962fa024" />

### Mensagem de Alerta de Umidade Alta
<img width="338" height="162" alt="Captura de tela 2025-11-17 135440" src="https://github.com/user-attachments/assets/cba0d5cf-dfe0-4fca-8f39-fd0f80e6a9c5" />

### Mensagem de Normalização
<img width="390" height="159" alt="Captura de tela 2025-11-17 135457" src="https://github.com/user-attachments/assets/1c6abc6c-8958-4f10-8b9b-258177f406d3" />

## Autores
- Gabriel de Carvalho Barros
- Rennys Rodrigues Cardoso
- Vítor Roggeri Cavicchiolli

