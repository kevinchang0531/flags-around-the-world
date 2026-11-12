# 國旗環遊世界

給國小學生的互動 HTML 簡報：跟著 9 面國旗認識五大洲的國家，每國三頁，分別是國旗的祕密、國家介紹與位置、著名人物。

**線上觀看：** https://kevinchang0531.github.io/flags-around-the-world/

## 內容（34 頁）
- 引起動機：封面、猜國旗暖身、今天的任務
- 世界地圖總覽：點國旗可直接跳到該國
- 9 國：台灣、日本、印度（亞洲）、英國、法國（歐洲）、美國（北美洲）、巴西（南美洲）、埃及（非洲）、澳洲（大洋洲）
- 喚起行動：9 國比一比（可排序表格）、看國旗猜國家小測驗、回家任務「設計班旗」

## 操作
| 按鍵 | 功能 |
|---|---|
| ← → / 空白鍵 | 切頁（也可點畫面左右兩側，手機可左右滑） |
| F | 全螢幕 |
| N | 顯示／隱藏教師備註（答案與延伸提問） |
| M | 回到世界地圖 |

網址後面加 `#頁碼` 可直接開到那一頁，例如 `#5`。

## 檔案
- `index.html`：成品，單一檔案，圖片都內嵌，直接用瀏覽器開就能用
- `template.html` + `build.py`：原始碼；改完內容後執行 `python build.py` 重新產生 `index.html`
- `assets_dl/`：國旗 SVG 與世界地圖
- `slides/generated/`：封面與結尾插圖（AI 生成）

## 素材來源
- 國旗：[flagcdn.com](https://flagcdn.com)（公有領域）
- 世界地圖：Daniel R. Strebe, [Equirectangular projection SW.jpg](https://commons.wikimedia.org/wiki/File:Equirectangular_projection_SW.jpg), Wikimedia Commons, CC BY-SA 3.0
- 封面與結尾插圖：AI 生成（gpt-image-2）
- 著名人物以表情符號代表，沒有使用真人照片
