# Desafio - Furia Fãs CS GO Chat Bot
Projeto de um bot no telegram que interage conforme o usuário seleciona as opções de comando disponíveis. Foi desenvolvido essa solução proposta para o desafio Normal da Furia.

## Funcionalidades
- Informações sobre próximos jogos
- Equipe atual 
- Posição no ranking Mundial
- Mostre sua torcida para a equipe da FURIA

## Demonstração de uso
https://github.com/user-attachments/assets/27bfbbb7-9668-4dfe-92b3-338a8672ad3f

## Como rodar ou criar o seu chat a partir desse
1. Clone o repositório. <br/>
Na ferramenta "Git", clone o repositório utilizando o link abaixo: <br/>
git clone https://github.com/JoaoEduSB/Desafio_Furia_Fan_BOT.git

2. Instale as dependências: (Pode utilizar o terminal do Git, cmd, ou o próprio Visual Studio Code)<br/>
pip install -r requirements.txt

3. Clique com o botão direito no arquivo "Token.env"<br/>
Escolha "Abrir com" <br/>
Então abra no seu bloco de notas e você terá que substituir o texto "seu_token_aqui" pelo token que você irá gerar no telegram.

**BOT_TOKEN=seu_token_aqui**

Como criar o seu Token de Bot no Telegram: <br/>
Abra o Telegram e procure pelo usuário @BotFather. <br/>
Inicie uma conversa e envie o comando /newbot <br/>
Siga as instruções para criar seu bot (você precisará escolher um nome e um username único).<br/>
Ao final, o BotFather irá enviar o TOKEN do seu novo bot — copie e cole no arquivo .env conforme o exemplo acima.

4. Fique a vontade para se aventurar no código e após finalizar suas alterações, siga com o passo 5.

5. Execute o bot utilizando o comando abaixo:<br/>
python FuriaFanBot.py (Pode utilizar o terminal do Git, cmd, ou o próprio Visual Studio Code)
