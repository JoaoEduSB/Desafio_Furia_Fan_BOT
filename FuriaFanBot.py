from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
import os
import datetime
import random

# Carregar variáveis de ambiente
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Lista dos próximos jogos (sem jogos programados)
proximos_jogos = []

# Função para obter a saudação com base no horário
def saudacao():
    hora_atual = datetime.datetime.now().hour
    if 5 <= hora_atual < 12:
        return "Bom dia!"
    elif 12 <= hora_atual < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

# Teclado principal
def teclado_principal():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📅 Próximos Jogos", callback_data="proximos_jogos")],
        [InlineKeyboardButton("🎯 Line-up Atual", callback_data="lineup")],
        [InlineKeyboardButton("🏆 Ranking Atual", callback_data="ranking")],
        [InlineKeyboardButton("💬 Torça com a FURIA", callback_data="mostre_sua_torcida")]
    ])

# Teclado de confirmação
def teclado_confirmacao():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("👍 Sim", callback_data="continuar_sim"), InlineKeyboardButton("👎 Não", callback_data="continuar_nao")]
    ])

# Mensagem de boas-vindas
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    saudacao_texto = saudacao()
    await update.message.reply_text(
        f"{saudacao_texto} 👋 Seja bem-vindo ao Chat de Fãs da FURIA CS:GO! 🎮\nEscolha uma opção abaixo para interagir:",
        reply_markup=teclado_principal()
    )

# Tratamento dos botões principais
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "proximos_jogos":
        await query.message.reply_text("📢 Não há jogos programados no momento.")
        await query.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

    elif query.data == "lineup":
        await query.message.reply_text("🎯 Line-up Atual da FURIA:\n- arT\n- yuurih\n- KSCERATO\n- chelo\n- FalleN")
        await query.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

    elif query.data == "ranking":
        await query.message.reply_text("🏆 Ranking Atual:\nFURIA está em 5º lugar no ranking mundial de CS:GO! 🔥")
        await query.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

    elif query.data == "mostre_sua_torcida":
        torcida_variantes = [
            "Vamos FURIA! 🖤💛 #DIADEFURIA", "FURIA é vida! 🔥 Vamos, FURIA! 💪",
            "Vai, FURIA! Vamos com tudo! 💥", "FURIA! A equipe que nunca para de brilhar! 🌟",
            "FURIA, a força do Brasil! 🇧🇷🔥 Vamos FURIA!"
        ]
        torcida_texto = random.choice(torcida_variantes)
        await query.message.reply_text(f"📣 {torcida_texto}")
        await query.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

    elif query.data == "continuar_sim":
        await query.message.reply_text("Selecione a opção que deseja:", reply_markup=teclado_principal())

    elif query.data == "continuar_nao":
        await query.message.reply_text("Obrigado! Volte sempre para acompanhar a FURIA! 🖤💛")

# Funções específicas para cada comando digitado
async def comando_proximos_jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📢 Não há jogos programados no momento.")
    await update.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

async def comando_lineup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 Line-up Atual da FURIA:\n- arT\n- yuurih\n- KSCERATO\n- chelo\n- FalleN")
    await update.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

async def comando_ranking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏆 Ranking Atual:\nFURIA está em 5º lugar no ranking mundial de CS:GO! 🔥")
    await update.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

async def comando_mostre_sua_torcida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    torcida_variantes = [
        "Vamos FURIA! 🖤💛 #DIADEFURIA", "FURIA é vida! 🔥 Vamos, FURIA! 💪",
        "Vai, FURIA! Vamos com tudo! 💥", "FURIA! A equipe que nunca para de brilhar! 🌟",
        "FURIA, a força do Brasil! 🇧🇷🔥 Vamos FURIA!"
    ]
    torcida_texto = random.choice(torcida_variantes)
    await update.message.reply_text(f"📣 {torcida_texto}")
    await update.message.reply_text("Deseja continuar?", reply_markup=teclado_confirmacao())

# Função para tratar mensagens não reconhecidas
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔄 Reiniciar Chat", callback_data="reiniciar")],
        [InlineKeyboardButton("❌ Não", callback_data="nao_reiniciar")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("❓ Não entendemos o que você quis dizer. Deseja reiniciar o chat?", reply_markup=reply_markup)

# Configurar comandos
async def configurar_comandos(application):
    comandos = [
        BotCommand(command="start", description="Iniciar o bot"),
        BotCommand(command="proximosjogos", description="Ver próximos jogos da FURIA"),
        BotCommand(command="lineup", description="Ver line-up atual"),
        BotCommand(command="ranking", description="Ver ranking atual"),
        BotCommand(command="mostresuatorcida", description="Mostre sua torcida para a FURIA"),
    ]
    await application.bot.set_my_commands(comandos)

# Função principal
async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("proximosjogos", comando_proximos_jogos))
    application.add_handler(CommandHandler("lineup", comando_lineup))
    application.add_handler(CommandHandler("ranking", comando_ranking))
    application.add_handler(CommandHandler("mostresuatorcida", comando_mostre_sua_torcida))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    await configurar_comandos(application)
    print("✅ Bot rodando...")
    await application.run_polling()

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    import asyncio
    asyncio.run(main())
