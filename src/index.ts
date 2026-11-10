import { Bot, webhookCallback } from "grammy";

// Описываем переменные окружения (токен мы зададим через Wrangler)
export interface Env {
  BOT_TOKEN: string;
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    // Инициализируем бота с токеном из секретов Cloudflare
    const bot = new Bot(env.BOT_TOKEN);

    // Обработчик команды /start
    bot.command("start", (ctx) => {
      return ctx.reply(`Привет, ${ctx.from?.first_name}! Я бот на TypeScript. Напиши что-нибудь.`);
    });

    // Обработчик любого текстового сообщения (Эхо)
    bot.on("message:text", (ctx) => {
      return ctx.reply(`Ты написал: ${ctx.message.text}`);
    });

    // Передаем запрос в обработчик webhook от grammY
    return webhookCallback(bot, "cloudflare-mod")(request, env, ctx);
  },
};
