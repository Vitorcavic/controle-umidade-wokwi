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
<img width="1202" height="2078" alt="diagrama" src="https://github.com/user-attachments/assets/47ffeb59-6c5f-4f6e-b07d-a6598ba158a2" />

## Configurações
### Parâmetros ajustáveis
<img width="912" height="596" alt="params" src="https://github.com/user-attachments/assets/b30900c7-572b-432e-95c1-9847c0024647" />

## Telegram Bot
Crie um Bot: 
- Busque por @BotFather no Telegram
- Use o comando /newbot
- Guarde o token fornecido

Obtenha seu Chat ID:
- Envie uma mensagem para @userinfobot
- Anote seu ID numérico
Configure as Variáveis no código:
<img width="726" height="406" alt="telegram_cfg" src="https://github.com/user-attachments/assets/8ba97e2f-7433-4ced-8748-4c3a564a8823" />

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
<img width="2464" height="4092" alt="codigo_principal" src="https://github.com/user-attachments/assets/6475b119-e18c-4031-817c-c622aaac41d2" />

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
![IMG_6498](https://github.com/user-attachments/assets/1667307c-a8e3-443c-a3cf-ed5da2bf9cb8)

### Mensagem de Alerta de Umidade Alta
![IMG_6499](https://github.com/user-attachments/assets/7648a7f1-14b9-443f-8400-a609625c4091)

### Mensagem de Normalização
![IMG_6500](https://github.com/user-attachments/assets/c070fe24-51c4-40cf-b6c2-c450641c393a)

## Autores
- Gabriel de Carvalho Barros
- Rennys Rodrigues Cardoso
- Vítor Roggeri Cavicchiolli

