import requests
import time

url_base = 'http://localhost:3000'

def read_jobs_from_file(filename):
    jobs = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            job_data = eval(line.strip())  # Converte a string do dicionário de volta para dicionário
            jobs.append(job_data)
    return jobs

def send_message(job):
    send_message = requests.post(
    url_base + '/client/sendMessage/rafa020679',
    json={
                "chatId" : "", # Aqui que voce precisa inserir o identificador. 
                "contentType" : "string",
                # Aqui abaixo voce pode colocar coisas direferentes caso queria mudar a mensagem.
                "content" : f'''Vaga Nova saindo do forno : 
                {job["title"]}
                {job["link"]}
                ''' 
            }
    )      
    if send_message.status_code == 200:
        print({f'Vaga enviada : {job["title"]}'})
    else:
        print(f"Erro ao enviar a mensagem : {job["title"]}")


jobs = read_jobs_from_file('jobs_results.txt')

for job in jobs:
    send_message(job)
    time.sleep(180) #Aqui voce define em segundos o intevalo de cada mensagem    



