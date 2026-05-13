#!/usr/bin/env node
/**
 * Append an item to site/automation/queue.json for scheduled SNS bridge.
 * Usage:
 *   node scripts/social-queue-add.mjs tarnar "2026-05-20T06:00:00Z" "タイトル" "https://example.com/post" "要約" "https://example.com/og.jpg"
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, "..");
const queuePath = path.join(root, "site", "automation", "queue.json");

const [brand, scheduledAt, title, url, summary = "", imageUrl = ""] = process.argv.slice(2);
if (!brand || !scheduledAt || !title || !url) {
  console.error(
    "Usage: node scripts/social-queue-add.mjs <tarnar|izu_music_fund> <ISO scheduledAt> <title> <url> [summary] [imageUrl]"
  );
  process.exit(1);
}

const raw = fs.readFileSync(queuePath, "utf8");
const data = JSON.parse(raw);
if (!Array.isArray(data.items)) data.items = [];

data.items.push({
  id: `q_${Date.now()}`,
  brand: brand === "izu_music_fund" ? "izu_music_fund" : "tarnar",
  scheduledAt,
  status: "pending",
  article: { title, url, summary, imageUrl },
});

fs.writeFileSync(queuePath, JSON.stringify(data, null, 2) + "\n", "utf8");
console.log("Updated", queuePath);
