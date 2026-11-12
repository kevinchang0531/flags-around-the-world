"""合併 data_raw/base.json 與 content_*.json，產生 data/countries.js 與 data/world.js。"""
import glob, json, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "data_raw")
COLORS = {"紅", "白", "藍", "綠", "黃", "黑", "橘", "其他"}
SYMS = {"星星", "太陽", "月亮", "十字", "動物", "植物", "武器", "文字", "徽章", "三角形", "圓形", "橫條紋", "直條紋"}
REGION = {"Asia": "亞洲", "Europe": "歐洲", "Africa": "非洲", "Oceania": "大洋洲"}

base = json.load(open(os.path.join(RAW, "base.json"), encoding="utf-8"))
content = {}
for f in sorted(glob.glob(os.path.join(RAW, "content_*.json"))):
    for c in json.load(open(f, encoding="utf-8")):
        content[c["id"]] = c

problems, out = [], []
for b in base:
    c = content.get(b["id"])
    if not c:
        problems.append(f"{b['id']} 缺內容")
        continue
    cont = REGION.get(b["region"]) or ("南美洲" if b["subregion"] == "South America" else "北美洲")
    for k in ["zh", "zhFull", "capital", "languages", "intro", "features", "flagMeaning", "flagColors", "flagSymbols", "people", "ask", "funFact"]:
        if k not in c:
            problems.append(f"{b['id']} 缺欄位 {k}")
    bad = set(c.get("flagColors", [])) - COLORS | set(c.get("flagSymbols", [])) - SYMS
    if bad:
        problems.append(f"{b['id']} 非法值 {bad}")
    out.append({
        "id": b["id"], "en": b["en"], "cont": cont, "latlng": b["latlng"], "area": b["area"],
        "landlocked": b["landlocked"],
        **{k: c.get(k) for k in ["zh", "zhFull", "capital", "languages", "intro", "features", "flagNick",
                                 "flagMeaning", "flagColors", "flagSymbols", "people", "ask", "funFact"]},
    })

os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
with open(os.path.join(ROOT, "data", "countries.js"), "w", encoding="utf-8") as f:
    f.write("window.COUNTRIES=" + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n")

# 地圖：把 ISO 數字代碼換成小寫兩碼，科索沃用名稱比對
topo = json.load(open(os.path.join(RAW, "countries-50m.json"), encoding="utf-8"))
num2id = {b["ccn3"]: b["id"] for b in base if b["ccn3"]}
for g in topo["objects"]["countries"]["geometries"]:
    name = g.get("properties", {}).get("name")
    g["id"] = "xk" if name == "Kosovo" else num2id.get(g.get("id"))
    g.pop("properties", None)
with open(os.path.join(ROOT, "data", "world.js"), "w", encoding="utf-8") as f:
    f.write("window.WORLD=" + json.dumps(topo, separators=(",", ":")) + ";\n")

# 給老師的待確認清單
lines = ["# 待確認清單", "", "AI 撰寫各國內容時自己標出、建議上課前再確認的地方。依洲排列。", ""]
for o in sorted(out, key=lambda x: (x["cont"], x["zh"])):
    chk = content[o["id"]].get("check") or []
    if chk:
        lines.append(f"- **{o['zh']}**（{o['id']}，{o['cont']}）：" + "；".join(chk))
with open(os.path.join(ROOT, "待確認清單.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print(f"國家 {len(out)} / {len(base)}")
for p in problems:
    print("  !", p)
sys.exit(1 if problems else 0)
