import { handleLineWebhook } from "./lib/line-handlers.mjs";

export const handler = async (event) =>
  handleLineWebhook(event, {
    secret: (process.env.LINE_IMF_CHANNEL_SECRET || "").trim(),
    token: (process.env.LINE_IMF_CHANNEL_TOKEN || "").trim(),
    brand: "izu_music_fund",
  });
