from flask import Flask
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1235630253750091896/M5k9A0TMgUJ8sjxBHqH_Os_Pt28uZU0robXH0IpM67sPr4HfTUWlgUghQZtq9cEQEyU7"

@app.route('/', methods=['GET'])
def index():
    ipv4 = requests.get('https://api.ipify.org?format=json').json().get('ip')
    ipv6 = requests.get('https://api64.ipify.org?format=json').json().get('ip')
    
    send_ip_to_discord(ipv4, ipv6)
    
    return "OK"

def send_ip_to_discord(ipv4, ipv6):
    data = {
        "content": f"Adresse IPv4 : {ipv4}\nAdresse IPv6 : {ipv6}"
    }
    
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code != 200:
        print("Échec de l'envoi des adresses IP au webhook Discord")

if __name__ == '__main__':
    app.run(debug=True)