# GMTJ OS3 — PDF をこのフォルダへコピー（任意）

`site/gmtj-os/` のメインは **ブラウザ上デスクトップ（PDF 非表示）** です。別途ブラウザだけで PDF を置きたい場合に限り、**この `pdfs/` 配下**へ同名でコピーしてください（Git には PDF を含めません）。

ターミナル例（1〜10を一括）:

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation
mkdir -p site/gmtj-os/pdfs
for i in $(seq 1 10); do
  cp "/Users/tarnar/Desktop/GMTJ OS/GMTJ OS3_${i}.pdf" "site/gmtj-os/pdfs/"
done
```

あとはリポルートで `python3 -m http.server 8888` を起動し、ブラウザで  
**http://127.0.0.1:8888/site/gmtj-os/** を開きます。
