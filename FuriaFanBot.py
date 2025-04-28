from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
import datetime
import random

TOKEN = ''

# Lista dos próximos jogos
proximos_jogos = [
    {"data": "28/04/2025", "oponente": "Team Liquid", "hora": "18:00"},
    {"data": "01/05/2025", "oponente": "Astralis", "hora": "20:00"},
    {"data": "03/05/2025", "oponente": "Navi", "hora": "15:00"},
    {"data": "04/05/2025", "oponente": "FaZe Clan", "hora": "19:00"},
]

# Função para obter a saudação com base no horário
def saudacao():
    hora_atual = datetime.datetime.now().hour
    if 5 <= hora_atual < 12:
        return "Bom dia!"
    elif 12 <= hora_atual < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

# Criação do teclado principal
def teclado_principal():
    keyboard = [
        [InlineKeyboardButton("📅 Próximos Jogos", callback_data="proximos_jogos")],
        [InlineKeyboardButton("🎯 Line-up Atual", callback_data="lineup")],
        [InlineKeyboardButton("🏆 Ranking Atual", callback_data="ranking")],
        [InlineKeyboardButton("💬 Torça com a FURIA", callback_data="mostre_sua_torcida")],
    ]
    return InlineKeyboardMarkup(keyboard)

# Teclado de confirmação ("Deseja continuar?")
def teclado_confirmacao():
    keyboard = [
        [
            InlineKeyboardButton("👍 Sim", callback_data="continuar_sim"),
            InlineKeyboardButton("👎 Não", callback_data="continuar_nao"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

# Mensagem de boas-vindas
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    saudacao_texto = saudacao()
    await update.message.reply_text(
        f"{saudacao_texto} 👋 Seja bem-vindo ao Chat de Fãs da FURIA CS:GO! 🎮\nEscolha uma opção abaixo para interagir:",
        reply_markup=teclado_principal()
    )

# Tratamento dos botões principais
# Tratamento dos botões principais
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "proximos_jogos":
        jogos = "\n".join([f"📅 {jogo['data']} - {jogo['oponente']} às {jogo['hora']}" for jogo in proximos_jogos])
        await query.message.reply_text(f"📢 Próximos Jogos da FURIA até 04/05/2025:\n\n{jogos}")
        await query.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

    elif query.data == "lineup":
        await query.message.reply_text(
            "🎯 Line-up Atual da FURIA:\n- arT\n- yuurih\n- KSCERATO\n- chelo\n- FalleN"
        )
        await query.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

    elif query.data == "ranking":
        await query.message.reply_text(
            "🏆 Ranking Atual:\nFURIA está em 5º lugar no ranking mundial de CS:GO! 🔥"
        )
        await query.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

    elif query.data == "mostre_sua_torcida":
        # Torcida aleatória
        torcida_variantes = [
            "Vamos FURIA! 🖤💛 #DIADEFURIA",
            "FURIA é vida! 🔥 Vamos, FURIA! 💪",
            "Vai, FURIA! Vamos com tudo! 💥",
            "FURIA! A equipe que nunca para de brilhar! 🌟",
            "FURIA, a força do Brasil! 🇧🇷🔥 Vamos FURIA!"
        ]
        torcida_texto = random.choice(torcida_variantes)  # Torcida aleatória
        await query.message.reply_text(f"📣 {torcida_texto}")
        await query.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

    elif query.data == "continuar_sim":
        await query.message.reply_text("Selecione a opção que deseja:", reply_markup=teclado_principal())

    elif query.data == "continuar_nao":
        # Envia a mensagem de agradecimento e o próximo jogo
        jogo_proximo = proximos_jogos[0]
        await query.message.reply_text(f"Nos vemos no próximo jogo:\n📅 {jogo_proximo['data']} - {jogo_proximo['oponente']} às {jogo_proximo['hora']}")
        await query.message.reply_text("Obrigado! Volte sempre para acompanhar a FURIA! 🖤💛")

    elif query.data == "reiniciar":
        await query.message.reply_text(
            "👋 Reiniciando o chat!\nEscolha uma opção abaixo para interagir:",
            reply_markup=teclado_principal()
        )
    elif query.data == "nao_reiniciar":
        # Quando o usuário clicar em "Não", exibe a mensagem de agradecimento e o próximo jogo, sem repetir os botões
        jogo_proximo = proximos_jogos[0]
        await query.message.reply_text(f"Nos vemos no próximo jogo:\n📅 {jogo_proximo['data']} - {jogo_proximo['oponente']} às {jogo_proximo['hora']}")
        await query.message.reply_text("Obrigado! Volte sempre para acompanhar a FURIA! 🖤💛")
        
    else:
        # Se clicar errado, mostrar "Não" para o reinício
        keyboard = [
            [InlineKeyboardButton("🔄 Reiniciar Chat", callback_data="reiniciar")],
            [InlineKeyboardButton("❌ Não", callback_data="nao_reiniciar")]  # Botão "Não" adicionado
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(
            "❓ Não entendemos o que você quis dizer. Deseja reiniciar o chat?",
            reply_markup=reply_markup
        )


# Função para tratar mensagens não reconhecidas
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Exibe os botões "Reiniciar Chat" e "Não"
    keyboard = [
        [InlineKeyboardButton("🔄 Reiniciar Chat", callback_data="reiniciar")],
        [InlineKeyboardButton("❌ Não", callback_data="nao_reiniciar")]  # Botão "Não" adicionado
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "❓ Não entendemos o que você quis dizer. Deseja reiniciar o chat?",
        reply_markup=reply_markup
    )

# Configurar os comandos que aparecem no "/"
async def configurar_comandos(application):
    comandos = [
        BotCommand(command="start", description="Iniciar o bot"),
        BotCommand(command="proximosjogos", description="Ver próximos jogos da FURIA"),
        BotCommand(command="lineup", description="Ver line-up atual"),
        BotCommand(command="ranking", description="Ver ranking atual"),
        BotCommand(command="mostresuatorcida", description="Mostre sua torcida para a FURIA"),
    ]
    await application.bot.set_my_commands(comandos)

# Comandos via "/"
async def comando_proximos_jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jogos = "\n".join([f"📅 {jogo['data']} - {jogo['oponente']} às {jogo['hora']}" for jogo in proximos_jogos])
    await update.message.reply_text(f"📢 Próximos Jogos da FURIA até 04/05/2025:\n\n{jogos}")
    await update.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

async def comando_lineup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎯 Line-up Atual da FURIA:\n- arT\n- yuurih\n- KSCERATO\n- chelo\n- FalleN")
    await update.message.reply_text("Deseja continuar?",
        reply_markup=teclado_confirmacao()
    )

async def comando_ranking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 Ranking Atual:\nFURIA está em 5º lugar no ranking mundial de CS:GO! 🔥"),
    await update.message.reply_text("Deseja continuar?",
        reply_markup=teclado_confirmacao()
    )

async def comando_mostre_sua_torcida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Torcida aleatória
    torcida_variantes = [
        "Vamos FURIA! 🖤💛 #DIADEFURIA",
        "FURIA é vida! 🔥 Vamos, FURIA! 💪",
        "Vai, FURIA! Vamos com tudo! 💥",
        "FURIA! A equipe que nunca para de brilhar! 🌟",
        "FURIA, a força do Brasil! 🇧🇷🔥 Vamos FURIA!"
    ]
    torcida_texto = random.choice(torcida_variantes)  # Torcida aleatória
    await update.message.reply_text(f"📣 {torcida_texto}")
    await update.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("proximosjogos", comando_proximos_jogos))
app.add_handler(CommandHandler("lineup", comando_lineup))
app.add_handler(CommandHandler("ranking", comando_ranking))
app.add_handler(CommandHandler("mostresuatorcida", comando_mostre_sua_torcida))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

# Programa principal
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("proximosjogos", comando_proximos_jogos))
    app.add_handler(CommandHandler("lineup", comando_lineup))
    app.add_handler(CommandHandler("ranking", comando_ranking))
    app.add_handler(CommandHandler("mostresuatorcida", comando_mostre_sua_torcida))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    await configurar_comandos(app)

    print("✅ Bot rodando...")
    await app.run_polling()

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    import asyncio
    asyncio.run(main())