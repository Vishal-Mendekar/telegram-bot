from app.rag.pipeline import rag_pipeline
from app.memory.session import add_message, get_history
from app.llm.client import generate_answer


async def handle_ask(update, context):
    user_id = update.effective_user.id
    query = " ".join(context.args)

    if not query:
        await update.message.reply_text("Please provide a query.")
        return

    history = get_history(user_id)

    answer = rag_pipeline(query, history)

    add_message(user_id, query, answer)

    await update.message.reply_text(answer)


async def handle_help(update, context):
    await update.message.reply_text(
        "/ask <query>\n/summarize\n/help"
    )


async def handle_summarize(update, context):
    user_id = update.effective_user.id
    history = get_history(user_id)

    if not history:
        await update.message.reply_text("No history to summarize.")
        return

    text = "\n".join([f"Q: {q}\nA: {a}" for q, a in history])

    summary = generate_answer(f"Summarize:\n{text}")

    await update.message.reply_text(summary)