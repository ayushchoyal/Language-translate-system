const API_BASE = "http://127.0.0.1:8000"; // change if you deploy elsewhere


const sourceLang = document.getElementById("sourceLang");
const targetLang = document.getElementById("targetLang");
const inputText = document.getElementById("inputText");
const outputText = document.getElementById("outputText");
const translateBtn = document.getElementById("translateBtn");
const swapBtn = document.getElementById("swapBtn");
const statusSpan = document.getElementById("status");


swapBtn.addEventListener("click", () => {
const a = sourceLang.value;
sourceLang.value = targetLang.value;
targetLang.value = a;
});


translateBtn.addEventListener("click", async () => {
const src = sourceLang.value.trim();
const tgt = targetLang.value.trim();
const raw = inputText.value.trim();
if (!raw) {
outputText.value = "";
return;
}


const lines = raw.split(/\n+/).map(s => s.trim()).filter(Boolean);
statusSpan.textContent = "Translating...";


try {
const res = await fetch(`${API_BASE}/translate`, {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify({ source_lang: src, target_lang: tgt, texts: lines })
});


if (!res.ok) {
const err = await res.json().catch(() => ({ detail: res.statusText }));
throw new Error(err.detail || `HTTP ${res.status}`);
}


const data = await res.json();
outputText.value = data.translations.join("\n");
statusSpan.textContent = "Done";
} catch (e) {
outputText.value = "";
statusSpan.textContent = `Error: ${e.message}`;
}
});