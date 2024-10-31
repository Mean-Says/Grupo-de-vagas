import requests

url_base = 'http://localhost:3000'
get_chats_url = f"{url_base}/client/getChats/rafa020679"

response = requests.get(get_chats_url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Obtém o conteúdo JSON da resposta
    
    # Itera até 5 vezes ou a quantidade de chats disponíveis, o que for menor
    for i, chat in enumerate(data.get("chats", [])[:5]):
        chat_name = chat.get('name', 'N/A')
        chat_id = chat.get("id", {}).get("_serialized", 'N/A')
        chat_info = {
            "chat_name": chat_name,
            "chat_id": chat_id
        }
        print(chat_info)
else:
    print(f"Erro ao obter chats: {response.status_code}")
