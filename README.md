# Desafio - Furia Fãs CS GO Chat Bot
Projeto de um bot no telegram que interage conforme o usuário seleciona as opções de comando disponíveis. Foi desenvolvido essa solução proposta para o desafio Normal da Furia.

## Funcionalidades
- Informações sobre próximos jogos
- Equipe atual 
- Posição no ranking Mundial
- Mostre sua torcida para a equipe da FURIA

## Como rodar
1. Clone o repositório.
Na ferramenta "Git", clone o repositório utilizando o link abaixo:
git clone https://github.com/JoaoEduSB/Desafio_Furia_Fan_BOT.git

2. Instale as dependências: (Pode utilizar o terminal do Git, cmd, ou o próprio Visual Studio Code)
pip install -r requirements.txt

3. Clique com o botão direito no arquivo "Token.env", e escolha "Abrir com", então abra no seu bloco de notas e você terá que substituir o texto "seu_token_aqui" pelo token que você irá gerar no telegram.
BOT_TOKEN=seu_token_aqui

4.Como criar o seu Token de Bot no Telegram:
Abra o Telegram e procure pelo usuário @BotFather.
Inicie uma conversa e envie o comando /newbot
Siga as instruções para criar seu bot (você precisará escolher um nome e um username único).
Ao final, o BotFather irá enviar o TOKEN do seu novo bot — copie e cole no arquivo .env conforme o exemplo acima.

5. Execute o bot utilizando o comando abaixo:
python FuriaFanBot.py (Pode utilizar o terminal do Git, cmd, ou o próprio Visual Studio Code)
