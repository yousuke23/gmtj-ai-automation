import { handleLineWebhook } from "./lib/line-handlers.mjs";

export const handler = async (event) =>
  handleLineWebhook(event, {
    secret: (process.env.LINE_TARNAR_CHANNEL_SECRET || "").trim(),
    token: (process.env.LINE_TARNAR_CHANNEL_TOKEN || "").trim(),
    brand: "tarnar",
  });
