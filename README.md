# 世界國旗探索

給國小學生的互動國旗網站：全世界 197 個國家，可以自由點、查、玩。

**線上觀看：** https://kevinchang0531.github.io/flags-around-the-world/

197 國＝聯合國 193 個會員國＋中華民國、梵蒂岡、巴勒斯坦、科索沃。

## 功能
- 🗺️ **世界地圖**：依洲上色，可以縮放、拖曳。點國家會打開介紹卡；小島國用圓點表示。
- 🚩 **國旗牆**：可以搜尋中英文國名，依洲、國旗顏色、國旗圖案（星星、月亮、十字、動物等）篩選，也能依面積或離中華民國的距離排序。「遮住國名」適合全班搶答。
- 📇 **介紹卡**：國旗的祕密、首都、語言、面積（和中華民國比）、離中華民國多遠、可轉動的地球、著名人物、老師問、冷知識。按 ← → 可以切換國家，Esc 關閉。
- 🎮 **遊戲**：看國旗猜國家、看國名找國旗、地圖找國家、國旗翻牌配對。可以選洲和難度。
- 🎲 **隨機抽一國**：適合上課點名或當作暖身題。

網址加 `#國碼` 可以直接開某一國，例如 `index.html#jp`；加 `#wall`、`#game` 可以直接開國旗牆或遊戲。

## ⚠️ 內容正確性
各國介紹由 AI 撰寫，再由另一個 AI 交叉查核，但仍可能有錯。AI 自己標出、建議上課前再確認的地方列在 [待確認清單.md](待確認清單.md)。

## 檔案與重建
- `index.html`：網站本體（`world.html` 只是轉址到這裡，保留舊連結用）
- `data/countries.js`（國家內容）、`data/world.js`（地圖）、`flags/`（197 面國旗 SVG）、`lib/`（d3、topojson）
- 原始資料：`data_raw/base.json`（國家基本資料）、`data_raw/content_*.json`（AI 撰寫的教學內容）、`data_raw/SPEC.md`（撰寫規格）
- 修改 `content_*.json` 後重建：
  ```bash
  python build_world.py   # 合併資料、產生 data/ 與待確認清單
  ```

## 素材來源
- 國旗：[flagcdn.com](https://flagcdn.com)（公有領域）
- 國家基本資料：[mledoze/countries](https://github.com/mledoze/countries)（ODbL）
- 互動地圖：[world-atlas](https://github.com/topojson/world-atlas)／Natural Earth（公有領域）
- 程式庫：d3、topojson-client（ISC 授權）
- 著名人物以表情符號代表，沒有使用真人照片
