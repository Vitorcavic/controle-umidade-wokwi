from machine import Pin
from time import sleep
import dht
import network
import urequests
import json

DHT_PIN = 15
LED_PIN = 13
HUM_HIGH = 40.0   # Acima disso liga
HUM_LOW = 30.0    # Abaixo disso desliga

# --- CONFIGURAÇÕES TELEGRAM
TELEGRAM_BOT_TOKEN = ""
TELEGRAM_CHAT_ID = ""

sensor = dht.DHT22(Pin(DHT_PIN))
led = Pin(LED_PIN, Pin.OUT)
led.value(0)
is_on = False

def send_telegram(message):
    """Envia mensagem para o Telegram"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        
        print("Enviando para Telegram...")
        response = urequests.post(url, json=payload)
        response.close()
        print("✅ Mensagem enviada com sucesso!")
        
    except Exception as e:
        print("❌ Erro ao enviar para Telegram:", e)

def connect_wifi():
    """Conecta ao Wi-Fi"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print("📡 Conectando ao Wi-Fi...")
        wlan.connect("Wokwi-GUEST", "")  # Wi-Fi do Wokwi
        
        for i in range(20):
            if wlan.isconnected():
                break
            sleep(0.5)
    
    if wlan.isconnected():
        print("✅ Wi-Fi Conectado! IP:", wlan.ifconfig()[0])
        return True
    else:
        print("❌ Falha na conexão Wi-Fi")
        return False

print("🚀 HumiSense - Iniciando...")

isWifiConnected = False

if connect_wifi():
    send_telegram("🔔 HumiSense Iniciado!\nSistema de monitoramento ativo e funcionando! ✅")
    isWifiConnected = True
else:
    print("ERRO NO WIFI")

if isWifiConnected: 
    while True:
        try:
            sensor.measure()
            hum = sensor.humidity()
            temp = sensor.temperature()
            
            print(f"🌡️ Temp: {temp:.1f}°C | 💧 Hum: {hum:.1f}%")

            if (not is_on) and hum >= HUM_HIGH:
                is_on = True
                led.value(1)
                print(">> ⚡ LIGANDO Desumidificador")
                
                mensagem = f"🚨 ALERTA - Umidade Alta!\n\n💧 Umidade: {hum:.1f}%\n🌡️ Temperatura: {temp:.1f}°C\n⚡ Desumidificador LIGADO"
                send_telegram(mensagem)
                
            elif is_on and hum <= HUM_LOW:
                is_on = False
                led.value(0)
                print(">> 🔌 DESLIGANDO Desumidificador")
                
                mensagem = f"✅ Umidade Normalizada!\n\n💧 Umidade: {hum:.1f}%\n🌡️ Temperatura: {temp:.1f}°C\n⚡ Desumidificador DESLIGADO"
                send_telegram(mensagem)

        except OSError as e:
            print("❌ Erro na leitura do sensor:", e)

        sleep(10)
