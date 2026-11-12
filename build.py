import os
import json

base_dir = r"C:\Users\PC\.gemini\antigravity\scratch\tro-choi-doan-so"
js_path = os.path.join(base_dir, "audio_data.js")

with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bé Vui Học Tập 🎈 - Bé Đoán Số & Đố Ký Tự</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700;800&family=Sigmar&display=swap" rel="stylesheet">
  <!-- Canvas Confetti CDN -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

  <style>
    :root {{
      --primary: #FF5E7E;
      --secondary: #4facfe;
      --accent: #FFA000;
      --success: #2e7d32;
      --danger: #d32f2f;
      --bg-gradient: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 50%, #fed6e3 100%);
    }}

    * {{
      box-sizing: border-box;
      user-select: none;
      -webkit-user-select: none;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Quicksand', sans-serif;
      min-height: 100vh;
      background: var(--bg-gradient);
      overflow-x: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
    }}

    /* Mây bay nền */
    .cloud {{
      position: fixed;
      background: rgba(255, 255, 255, 0.75);
      border-radius: 100px;
      pointer-events: none;
      z-index: 1;
      animation: floatCloud linear infinite;
    }}
    .cloud::before, .cloud::after {{
      content: '';
      position: absolute;
      background: inherit;
      border-radius: 50%;
    }}
    .cloud-1 {{ width: 140px; height: 45px; top: 12%; left: -160px; animation-duration: 35s; }}
    .cloud-1::before {{ width: 50px; height: 50px; top: -22px; left: 25px; }}
    .cloud-1::after {{ width: 70px; height: 70px; top: -35px; right: 25px; }}

    .cloud-2 {{ width: 180px; height: 55px; top: 35%; left: -200px; animation-duration: 45s; animation-delay: 15s; opacity: 0.6; }}
    .cloud-2::before {{ width: 60px; height: 60px; top: -30px; left: 30px; }}
    .cloud-2::after {{ width: 85px; height: 85px; top: -45px; right: 35px; }}

    .cloud-3 {{ width: 120px; height: 40px; top: 75%; left: -150px; animation-duration: 28s; animation-delay: 7s; opacity: 0.8; }}
    .cloud-3::before {{ width: 45px; height: 45px; top: -20px; left: 20px; }}
    .cloud-3::after {{ width: 55px; height: 55px; top: -25px; right: 20px; }}

    @keyframes floatCloud {{
      0% {{ transform: translateX(0); }}
      100% {{ transform: translateX(calc(100vw + 250px)); }}
    }}

    /* Khung ứng dụng chính */
    .app-container {{
      position: relative;
      z-index: 5;
      width: 100%;
      max-width: 960px;
      padding: 1rem 1.2rem 3rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
    }}

    /* Thanh Điều Hướng Menu Toàn Cục */
    .nav-bar {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(12px);
      padding: 0.7rem 1.4rem;
      border-radius: 35px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08), 0 0 0 2px rgba(255, 255, 255, 0.95);
      margin-bottom: 1.5rem;
      flex-wrap: wrap;
      gap: 10px;
    }}

    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: 'Sigmar', cursive;
      font-size: 1.35rem;
      color: #FF5E7E;
      cursor: pointer;
      text-decoration: none;
      transition: transform 0.2s;
    }}
    .nav-brand:hover {{
      transform: scale(1.04);
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .nav-btn {{
      background: #f1f5f9;
      color: #334155;
      border: 1.5px solid transparent;
      padding: 7px 16px;
      border-radius: 20px;
      font-family: inherit;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    .nav-btn:hover {{
      background: #e2e8f0;
      transform: translateY(-2px);
    }}
    .nav-btn.active {{
      background: linear-gradient(135deg, #6366f1, #8b5cf6);
      color: white;
      box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35);
    }}

    /* Các màn hình chính (Screens) */
    .screen {{
      width: 100%;
      display: none;
      flex-direction: column;
      align-items: center;
      text-align: center;
      animation: fadeIn 0.35s ease-out;
    }}
    .screen.active {{
      display: flex;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(14px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* =========================================================
     *  MÀN HÌNH TRANG CHỦ / MENU CHỌN TRÒ CHƠI
     * ========================================================= */
    .home-hero {{
      margin-top: 0.5rem;
      margin-bottom: 2rem;
    }}
    .home-title {{
      font-family: 'Sigmar', cursive;
      font-size: clamp(2.3rem, 5.5vw, 3.6rem);
      background: linear-gradient(135deg, #FF1361, #FFA000);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 4px 8px rgba(255, 19, 97, 0.25));
      margin-bottom: 0.6rem;
      letter-spacing: 1px;
    }}
    .home-desc {{
      font-size: 1.25rem;
      font-weight: 600;
      color: #334155;
      max-width: 620px;
      line-height: 1.6;
    }}

    .game-cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.8rem;
      width: 100%;
      max-width: 860px;
      margin-top: 0.5rem;
    }}

    .game-card {{
      background: rgba(255, 255, 255, 0.94);
      border-radius: 35px;
      padding: 2.2rem 1.8rem;
      box-shadow: 0 16px 35px rgba(0, 0, 0, 0.08), 0 0 0 3px rgba(255, 255, 255, 0.9);
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    .game-card:hover {{
      transform: translateY(-8px) scale(1.02);
      box-shadow: 0 24px 45px rgba(0, 0, 0, 0.14), 0 0 0 4px rgba(255, 255, 255, 1);
    }}

    .game-card-icon {{
      width: 90px;
      height: 90px;
      border-radius: 30px;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 3.2rem;
      margin-bottom: 1.2rem;
      box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease;
    }}
    .game-card:hover .game-card-icon {{
      transform: scale(1.12) rotate(6deg);
    }}

    .card-theme-1 .game-card-icon {{
      background: linear-gradient(135deg, #ff758c, #ff4070);
    }}
    .card-theme-2 .game-card-icon {{
      background: linear-gradient(135deg, #4facfe, #00f2fe);
    }}

    .game-card-badge {{
      position: absolute;
      top: 18px;
      right: 20px;
      font-size: 0.82rem;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: 14px;
      text-transform: uppercase;
    }}
    .badge-hot {{
      background: #ffe3e3;
      color: #e03131;
    }}
    .badge-new {{
      background: #d3f9d8;
      color: #2b8a3e;
      border: 1px solid #b2f2bb;
    }}

    .game-card-title {{
      font-family: 'Sigmar', cursive;
      font-size: 1.7rem;
      color: #1e293b;
      margin-bottom: 0.6rem;
    }}

    .game-card-info {{
      font-size: 1.05rem;
      color: #64748b;
      font-weight: 600;
      line-height: 1.5;
      margin-bottom: 1.6rem;
      flex-grow: 1;
    }}

    .btn-card-action {{
      width: 100%;
      border: none;
      padding: 0.95rem 1.8rem;
      border-radius: 25px;
      font-family: inherit;
      font-weight: 800;
      font-size: 1.15rem;
      color: white;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s;
    }}
    .card-theme-1 .btn-card-action {{
      background: linear-gradient(135deg, #FF5E7E, #FF8E53);
      box-shadow: 0 8px 18px rgba(255, 94, 126, 0.35);
    }}
    .card-theme-2 .btn-card-action {{
      background: linear-gradient(135deg, #38ef7d, #11998e);
      box-shadow: 0 8px 18px rgba(17, 153, 142, 0.35);
    }}
    .btn-card-action:hover {{
      filter: brightness(1.08);
      transform: scale(1.02);
    }}

    /* =========================================================
     *  TRÒ CHƠI 1: BÉ VUI ĐOÁN SỐ (1 - 10)
     * ========================================================= */
    .game1-header {{
      width: 100%;
      max-width: 800px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.9);
      padding: 0.7rem 1.4rem;
      border-radius: 25px;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06);
      margin-bottom: 1.2rem;
    }}
    .score-badge {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 1.1rem;
      font-weight: 700;
      color: #333;
    }}
    .round-tag {{
      background: linear-gradient(135deg, #FF6B6B, #FF8E53);
      color: white;
      padding: 5px 16px;
      border-radius: 20px;
      font-weight: 800;
      font-size: 1rem;
    }}

    .speaker-section {{
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(12px);
      padding: 1.4rem 2rem;
      border-radius: 35px;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08), 0 0 0 3px rgba(255, 255, 255, 0.85);
      width: 100%;
      max-width: 650px;
      margin-bottom: 1.6rem;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    .speaker-btn {{
      position: relative;
      background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
      border: none;
      width: 90px;
      height: 90px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      box-shadow: 0 10px 25px rgba(255, 107, 107, 0.45);
      transition: transform 0.2s;
    }}
    .speaker-btn:hover {{ transform: scale(1.06); }}
    .speaker-btn:active {{ transform: scale(0.95); }}
    .speaker-btn::before, .speaker-btn::after {{
      content: '';
      position: absolute;
      width: 100%; height: 100%;
      border-radius: 50%;
      background: rgba(255, 107, 107, 0.4);
      z-index: -1;
      opacity: 0;
    }}
    .speaker-btn.speaking::before {{ animation: ripple 1.2s ease-out infinite; }}
    .speaker-btn.speaking::after {{ animation: ripple 1.2s ease-out 0.4s infinite; }}

    @keyframes ripple {{
      0% {{ transform: scale(1); opacity: 0.85; }}
      100% {{ transform: scale(1.8); opacity: 0; }}
    }}

    .bubble-arena {{
      width: 100%;
      max-width: 840px;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      align-items: center;
      gap: 1.5rem;
      padding: 0.8rem 0 1.5rem;
      min-height: 230px;
    }}

    .number-bubble {{
      position: relative;
      width: 115px;
      height: 115px;
      border-radius: 50%;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
      font-family: 'Sigmar', cursive;
      font-size: 3.1rem;
      color: white;
      text-shadow: 0 3px 6px rgba(0, 0, 0, 0.3);
      box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15),
                  inset -8px -8px 16px rgba(0, 0, 0, 0.2),
                  inset 10px 10px 20px rgba(255, 255, 255, 0.6);
      transition: transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.25s;
      animation: bubbleFloat 4s ease-in-out infinite alternate;
    }}
    .number-bubble::after {{
      content: '';
      position: absolute;
      top: 12%; left: 20%;
      width: 30px; height: 16px;
      background: rgba(255, 255, 255, 0.7);
      border-radius: 50%;
      transform: rotate(-35deg);
      filter: blur(1px);
      pointer-events: none;
    }}
    .number-bubble:hover {{
      transform: scale(1.15) translateY(-8px);
    }}
    .bubble-theme-1 {{ background: radial-gradient(circle at 35% 35%, #ff758c, #ff4070); animation-delay: 0s; }}
    .bubble-theme-2 {{ background: radial-gradient(circle at 35% 35%, #4facfe, #00f2fe); animation-delay: 0.6s; }}
    .bubble-theme-3 {{ background: radial-gradient(circle at 35% 35%, #43e97b, #38f9d7); animation-delay: 1.2s; }}
    .bubble-theme-4 {{ background: radial-gradient(circle at 35% 35%, #fa709a, #fee140); animation-delay: 1.8s; }}
    .bubble-theme-5 {{ background: radial-gradient(circle at 35% 35%, #b176ff, #6234f4); animation-delay: 2.4s; }}

    @keyframes bubbleFloat {{
      0% {{ transform: translateY(0px) rotate(0deg); }}
      100% {{ transform: translateY(-16px) rotate(3deg); }}
    }}

    .bubble-shake {{
      animation: shake 0.6s ease-in-out !important;
      background: radial-gradient(circle at 35% 35%, #ff6b6b, #c92a2a) !important;
      opacity: 0.65;
    }}
    @keyframes shake {{
      0%, 100% {{ transform: translateX(0); }}
      20%, 60% {{ transform: translateX(-12px) rotate(-6deg); }}
      40%, 80% {{ transform: translateX(12px) rotate(6deg); }}
    }}

    .bubble-correct {{
      animation: popSuccess 0.8s forwards !important;
      background: radial-gradient(circle at 35% 35%, #51cf66, #2b8a3e) !important;
      z-index: 10;
    }}
    @keyframes popSuccess {{
      0% {{ transform: scale(1); }}
      50% {{ transform: scale(1.35) rotate(10deg); filter: brightness(1.2); }}
      100% {{ transform: scale(1.15) rotate(0deg); }}
    }}

    .feedback-banner {{
      min-height: 55px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      font-size: 1.35rem;
      font-weight: 800;
      border-radius: 25px;
      padding: 0.5rem 1.8rem;
      margin-top: 0.5rem;
      opacity: 0;
      transform: translateY(10px);
      transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    .feedback-banner.show {{
      opacity: 1;
      transform: translateY(0);
    }}
    .feedback-banner.correct {{
      background: #d3f9d8;
      color: #2b8a3e;
      border: 2px solid #69db7c;
      box-shadow: 0 8px 20px rgba(81, 207, 102, 0.25);
    }}
    .feedback-banner.wrong {{
      background: #ffe3e3;
      color: #c92a2a;
      border: 2px solid #ffa8a8;
      box-shadow: 0 8px 20px rgba(255, 107, 107, 0.2);
    }}

    /* =========================================================
     *  TRÒ CHƠI 2: ĐÂY LÀ SỐ GÌ? ĐÂY LÀ CHỮ GÌ? (TÍNH NĂNG MỚI)
     * ========================================================= */
    .game2-card-container {{
      width: 100%;
      max-width: 880px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(12px);
      border-radius: 35px;
      padding: 2rem;
      box-shadow: 0 18px 45px rgba(0, 0, 0, 0.08), 0 0 0 3px rgba(255, 255, 255, 0.9);
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    .game2-title {{
      font-family: 'Sigmar', cursive;
      font-size: 2.2rem;
      background: linear-gradient(135deg, #0284c7, #6366f1);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 0.4rem;
    }}

    .game2-subdesc {{
      color: #475569;
      font-weight: 600;
      font-size: 1.05rem;
      margin-bottom: 1.5rem;
      max-width: 650px;
      line-height: 1.5;
    }}

    /* Bảng thiết lập của Phụ huynh */
    .parent-config-box {{
      width: 100%;
      background: #f8fafc;
      border: 2px dashed #cbd5e1;
      border-radius: 25px;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      text-align: left;
    }}

    .parent-config-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1rem;
    }}
    .parent-badge {{
      background: #e0e7ff;
      color: #4338ca;
      font-weight: 800;
      font-size: 0.9rem;
      padding: 4px 12px;
      border-radius: 12px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .char-input-group {{
      margin-bottom: 1.2rem;
    }}
    .char-input-group label {{
      display: block;
      font-weight: 700;
      color: #1e293b;
      margin-bottom: 8px;
      font-size: 1.05rem;
    }}
    .char-input-field {{
      width: 100%;
      padding: 0.9rem 1.2rem;
      border-radius: 18px;
      border: 2px solid #cbd5e1;
      font-family: 'Quicksand', sans-serif;
      font-weight: 700;
      font-size: 1.25rem;
      color: #0f172a;
      background: white;
      outline: none;
      transition: border-color 0.2s;
    }}
    .char-input-field:focus {{
      border-color: #6366f1;
      box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.15);
    }}

    /* Nút chọn nhanh Presets */
    .preset-chips-container {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 1.4rem;
    }}
    .preset-chip {{
      background: white;
      border: 1.5px solid #e2e8f0;
      color: #475569;
      padding: 6px 14px;
      border-radius: 20px;
      font-family: inherit;
      font-weight: 700;
      font-size: 0.9rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .preset-chip:hover {{
      background: #f1f5f9;
      border-color: #6366f1;
      color: #4338ca;
      transform: translateY(-2px);
    }}

    .btn-start-quiz {{
      background: linear-gradient(135deg, #6366f1, #3b82f6);
      color: white;
      border: none;
      padding: 1rem 2.2rem;
      border-radius: 30px;
      font-family: inherit;
      font-weight: 800;
      font-size: 1.25rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      width: 100%;
      box-shadow: 0 10px 20px rgba(99, 102, 241, 0.35);
      transition: all 0.25s;
    }}
    .btn-start-quiz:hover {{
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 14px 25px rgba(99, 102, 241, 0.45);
    }}

    /* Vùng Đố Bé (Interactive Flashcards Grid) */
    .quiz-active-area {{
      display: none;
      width: 100%;
      flex-direction: column;
      align-items: center;
    }}
    .quiz-active-area.show {{
      display: flex;
    }}

    .quiz-stats-bar {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #f8fafc;
      padding: 0.8rem 1.4rem;
      border-radius: 20px;
      margin-bottom: 1.5rem;
      border: 1.5px solid #e2e8f0;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .quiz-stat-item {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #334155;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* Lưới các thẻ ký tự (Character Cards) */
    .char-cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 1.4rem;
      width: 100%;
      margin-bottom: 2rem;
    }}

    /* Từng thẻ ký tự 3D với hiệu ứng Hover phát âm */
    .char-card {{
      background: white;
      border-radius: 28px;
      padding: 1.2rem 1rem;
      box-shadow: 0 10px 24px rgba(0, 0, 0, 0.07), 0 0 0 2px #e2e8f0;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      cursor: pointer;
      transition: all 0.28s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}

    .char-card:hover {{
      transform: translateY(-8px) scale(1.04);
      box-shadow: 0 18px 36px rgba(0, 0, 0, 0.12), 0 0 0 3px #6366f1;
    }}

    /* Khi đang phát giọng đọc hỏi thẻ này */
    .char-card.hover-speaking {{
      animation: cardPulse 1.2s infinite alternate;
      border-color: #f59e0b;
      box-shadow: 0 0 0 4px #fbbf24, 0 15px 30px rgba(245, 158, 11, 0.25);
    }}
    @keyframes cardPulse {{
      from {{ transform: scale(1.02); }}
      to {{ transform: scale(1.08); }}
    }}

    /* Trạng thái đã được phụ huynh đánh giá */
    .char-card.evaluated-correct {{
      background: #f0fdf4;
      border-color: #22c55e !important;
      box-shadow: 0 10px 24px rgba(34, 197, 94, 0.18), 0 0 0 2px #86efac;
    }}
    .char-card.evaluated-wrong {{
      background: #fef2f2;
      border-color: #ef4444 !important;
      box-shadow: 0 10px 24px rgba(239, 68, 68, 0.18), 0 0 0 2px #fca5a5;
    }}

    /* Huy hiệu loại ký tự (Số / Chữ) */
    .char-type-pill {{
      font-size: 0.78rem;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 12px;
      margin-bottom: 0.4rem;
      text-transform: uppercase;
    }}
    .pill-number {{
      background: #e0f2fe;
      color: #0369a1;
    }}
    .pill-letter {{
      background: #fce7f3;
      color: #be185d;
    }}

    /* Ký tự lớn nổi bật */
    .char-glyph {{
      font-family: 'Sigmar', cursive;
      font-size: 4.6rem;
      line-height: 1.1;
      margin: 0.4rem 0 0.8rem;
      color: #1e293b;
      text-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
      transition: transform 0.2s;
    }}
    .char-card:hover .char-glyph {{
      transform: scale(1.1);
    }}
    .char-card.evaluated-correct .char-glyph {{
      color: #15803d;
    }}
    .char-card.evaluated-wrong .char-glyph {{
      color: #b91c1c;
    }}

    /* Biểu tượng loa khi hover */
    .hover-speaker-hint {{
      font-size: 0.82rem;
      font-weight: 700;
      color: #64748b;
      display: flex;
      align-items: center;
      gap: 4px;
      margin-bottom: 0.8rem;
      background: #f8fafc;
      padding: 3px 10px;
      border-radius: 12px;
    }}

    /* Khu vực Phụ Huynh Đánh Giá */
    .parent-eval-controls {{
      width: 100%;
      border-top: 1.5px solid #f1f5f9;
      padding-top: 0.8rem;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .eval-label {{
      font-size: 0.78rem;
      font-weight: 800;
      color: #94a3b8;
      text-align: center;
      margin-bottom: 2px;
      text-transform: uppercase;
    }}
    .eval-btn-group {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
    }}
    .btn-eval {{
      border: none;
      padding: 7px 10px;
      border-radius: 14px;
      font-family: inherit;
      font-weight: 800;
      font-size: 0.88rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      transition: all 0.2s;
    }}
    .btn-eval-correct {{
      background: #dcfce7;
      color: #166534;
      border: 1.5px solid #86efac;
    }}
    .btn-eval-correct:hover, .btn-eval-correct.selected {{
      background: #22c55e;
      color: white;
      border-color: #16a34a;
      box-shadow: 0 4px 10px rgba(34, 197, 94, 0.35);
    }}

    .btn-eval-wrong {{
      background: #fee2e2;
      color: #991b1b;
      border: 1.5px solid #fca5a5;
    }}
    .btn-eval-wrong:hover, .btn-eval-wrong.selected {{
      background: #ef4444;
      color: white;
      border-color: #dc2626;
      box-shadow: 0 4px 10px rgba(239, 68, 68, 0.35);
    }}

    /* Nút nghe đáp án mẫu */
    .btn-reveal-sample {{
      background: #f1f5f9;
      border: none;
      padding: 5px 8px;
      border-radius: 10px;
      font-family: inherit;
      font-size: 0.78rem;
      font-weight: 700;
      color: #475569;
      cursor: pointer;
      margin-top: 4px;
      transition: all 0.15s;
    }}
    .btn-reveal-sample:hover {{
      background: #e2e8f0;
      color: #0f172a;
    }}

    /* Nút hoàn thành bài đố */
    .btn-finish-quiz {{
      background: linear-gradient(135deg, #10b981, #059669);
      color: white;
      border: none;
      padding: 1rem 2.5rem;
      border-radius: 30px;
      font-family: inherit;
      font-weight: 800;
      font-size: 1.25rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 10px 22px rgba(16, 185, 129, 0.35);
      transition: all 0.25s;
    }}
    .btn-finish-quiz:hover {{
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 14px 28px rgba(16, 185, 129, 0.45);
    }}

    /* Màn hình tổng kết (Summary) */
    .summary-card {{
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(15px);
      padding: 2.5rem 2rem;
      border-radius: 40px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.12), 0 0 0 4px rgba(255, 255, 255, 0.85);
      max-width: 580px;
      width: 100%;
      margin-top: 1rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    @keyframes popIn {{
      0% {{ opacity: 0; transform: scale(0.7); }}
      100% {{ opacity: 1; transform: scale(1); }}
    }}

    .trophy-icon {{
      font-size: 4.8rem;
      animation: bounce 1s infinite alternate ease-in-out;
    }}
    @keyframes bounce {{
      from {{ transform: translateY(0); }}
      to {{ transform: translateY(-12px); }}
    }}

    .summary-stats-box {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      width: 100%;
      margin: 1.2rem 0;
    }}
    .stat-pill-box {{
      padding: 1rem;
      border-radius: 20px;
      text-align: center;
    }}
    .box-green {{
      background: #f0fdf4;
      border: 2px solid #bbf7d0;
      color: #166534;
    }}
    .box-red {{
      background: #fef2f2;
      border: 2px solid #fecaca;
      color: #991b1b;
    }}

    #fireworksCanvas {{
      position: fixed;
      top: 0; left: 0;
      width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 999;
    }}

    @media (max-width: 600px) {{
      .app-container {{ padding: 0.6rem; }}
      .nav-bar {{ padding: 0.6rem 1rem; }}
      .game2-card-container {{ padding: 1.2rem 0.9rem; }}
      .char-cards-grid {{ grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 1rem; }}
      .char-glyph {{ font-size: 3.6rem; }}
    }}
  </style>
</head>
<body>

  <div class="cloud cloud-1"></div>
  <div class="cloud cloud-2"></div>
  <div class="cloud cloud-3"></div>

  <canvas id="fireworksCanvas"></canvas>

  <div class="app-container">

    <!-- THANH ĐIỀU HƯỚNG MENU TOÀN CỤC -->
    <nav class="nav-bar">
      <div class="nav-brand" id="btnNavHome">
        <span>🎈</span>
        <span>BÉ VUI HỌC TẬP</span>
      </div>

      <div class="nav-links">
        <button class="nav-btn active" id="btnNavMenu">
          <span>🏠 Menu Trò Chơi</span>
        </button>
        <button class="nav-btn" id="btnNavGame1">
          <span>🎈 Trò 1: Đoán Số (1-10)</span>
        </button>
        <button class="nav-btn" id="btnNavGame2">
          <span>🔤 Trò 2: Đố Số & Chữ</span>
        </button>
      </div>
    </nav>

    <!-- =========================================================
         MÀN HÌNH 0: MENU CHỌN TRÒ CHƠI (HOME HUB)
         ========================================================= -->
    <section class="screen active" id="screenHome">
      <div class="home-hero">
        <h1 class="home-title">GÓC HỌC TẬP VUI NHỘN</h1>
        <p class="home-desc">
          Chào mừng các bé và ba mẹ! Hãy chọn trò chơi yêu thích bên dưới để cùng luyện nghe, luyện mắt và phát âm thật chuẩn nhé!
        </p>
      </div>

      <div class="game-cards-grid">
        <!-- Card Trò chơi 1 -->
        <div class="game-card card-theme-1" id="cardChooseGame1">
          <div class="game-card-badge badge-hot">Rất Vui ⭐</div>
          <div class="game-card-icon">🎈</div>
          <h2 class="game-card-title">Bé Vui Đoán Số</h2>
          <p class="game-card-info">
            Lắng nghe giọng đọc bí mật từ <strong>1 đến 10</strong>, nhanh tay chọn bong bóng đúng để bắn pháo hoa rực rỡ chúc mừng!
          </p>
          <button class="btn-card-action">
            <span>🎮 CHƠI ĐOÁN SỐ</span>
            <span>➔</span>
          </button>
        </div>

        <!-- Card Trò chơi 2 (Tính năng mới) -->
        <div class="game-card card-theme-2" id="cardChooseGame2">
          <div class="game-card-badge badge-new">Mới Ra Mắt ✨</div>
          <div class="game-card-icon">🔤</div>
          <h2 class="game-card-title">Đố Bé: Số Gì? Chữ Gì?</h2>
          <p class="game-card-info">
            Người lớn nhập số (0-9) hoặc chữ (A-Z). Khi <strong>di chuột vào</strong> ký tự sẽ có giọng đọc hỏi, phụ huynh nghe bé trả lời và đánh giá ✔️ / ❌!
          </p>
          <button class="btn-card-action">
            <span>👨‍👩‍👧 VÀO ĐỐ BÉ NGAY</span>
            <span>➔</span>
          </button>
        </div>
      </div>
    </section>

    <!-- =========================================================
         MÀN HÌNH 1: TRÒ CHƠI 1 - BÉ VUI ĐOÁN SỐ (1-10)
         ========================================================= -->
    <section class="screen" id="screenGame1">
      <div class="game1-header">
        <div class="score-badge">
          <span>⭐</span>
          <span>Điểm: <strong id="scoreVal1" style="color: #FF5E7E">0</strong></span>
        </div>
        <div class="round-tag" id="roundIndicator1">
          Vòng 1 / 10
        </div>
        <button class="nav-btn" id="btnBackToHomeFromG1" style="padding: 4px 12px; font-size: 0.88rem;">
          🏠 Đổi Trò Chơi
        </button>
      </div>

      <div class="speaker-section">
        <div style="font-size: 1.3rem; font-weight: 700; color: #2b3a4a; margin-bottom: 0.8rem;">
          🎧 Bé bấm vô loa để nghe số bí mật nè:
        </div>

        <button class="speaker-btn" id="btnSpeakNumber1" title="Bấm nghe lại số bí mật nghen">
          <svg style="width: 46px; height: 46px; fill: white;" viewBox="0 0 24 24">
            <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
          </svg>
        </button>

        <span style="margin-top: 10px; font-size: 1rem; font-weight: 700; color: #e65100; background: #fff3e0; padding: 5px 16px; border-radius: 14px;">
          Bấm loa để nghe lại nghen bé!
        </span>
      </div>

      <div class="bubble-arena" id="bubbleArena1"></div>

      <div class="feedback-banner" id="feedbackBanner1">
        <span id="feedbackIcon1">🎉</span>
        <span id="feedbackText1">Bé giỏi quá chừng luôn!</span>
      </div>
    </section>

    <!-- =========================================================
         MÀN HÌNH 2: TRÒ CHƠI 2 - ĐÂY LÀ SỐ GÌ? ĐÂY LÀ CHỮ GÌ?
         ========================================================= -->
    <section class="screen" id="screenGame2">
      <div class="game2-card-container">
        <h1 class="game2-title">ĐÂY LÀ SỐ GÌ? ĐÂY LÀ CHỮ GÌ?</h1>
        <p class="game2-subdesc">
          Trò chơi tương tác giữa phụ huynh và bé: Người lớn nhập danh sách số (0-9) hoặc chữ (A-Z). Khi <strong>di chuột vào</strong> ký tự, giọng đọc sẽ cất lên câu hỏi để bé trả lời!
        </p>

        <!-- BẢNG CÀI ĐẶT DÀNH CHO PHỤ HUYNH -->
        <div class="parent-config-box" id="parentConfigBox">
          <div class="parent-config-header">
            <div class="parent-badge">
              <span>👨‍👩‍👧 DÀNH CHO PHỤ HUYNH THIẾT LẬP</span>
            </div>
            <span style="font-size: 0.85rem; color: #64748b; font-weight: 600;">Hỗ trợ số 0-9 & chữ cái A-Z</span>
          </div>

          <div class="char-input-group">
            <label for="inputCustomChars">Nhập danh sách số hoặc chữ cần hỏi bé:</label>
            <input type="text" id="inputCustomChars" class="char-input-field" placeholder="Ví dụ: 0, 5, 8, A, B, C, M, N (hoặc bấm chọn nhanh bên dưới)" value="0, 1, 2, 5, 9, A, B, C, D, E">
          </div>

          <!-- Nút chọn nhanh (Presets) -->
          <div style="font-weight: 700; font-size: 0.9rem; color: #475569; margin-bottom: 6px;">Chọn nhanh bộ ký tự có sẵn:</div>
          <div class="preset-chips-container">
            <button class="preset-chip" data-preset="digits_all">🔢 Tất cả số (0 - 9)</button>
            <button class="preset-chip" data-preset="letters_az">🔤 Bảng chữ cái (A - Z)</button>
            <button class="preset-chip" data-preset="vowels">🌟 Nguyên âm (A, E, I, O, U)</button>
            <button class="preset-chip" data-preset="rand_5">🎲 Ngẫu nhiên 5 ký tự</button>
            <button class="preset-chip" data-preset="rand_10">🎲 Ngẫu nhiên 10 ký tự</button>
            <button class="preset-chip" data-preset="mix_common">🎈 Số & Chữ cơ bản</button>
          </div>

          <button class="btn-start-quiz" id="btnStartQuiz">
            <span>🚀 BẮT ĐẦU ĐỐ BÉ NGAY</span>
          </button>
        </div>

        <!-- VÙNG BÀI ĐỐ CHO BÉ (HIỆN KHI ĐÃ BẤM BẮT ĐẦU) -->
        <div class="quiz-active-area" id="quizActiveArea">
          <div class="quiz-stats-bar">
            <div class="quiz-stat-item">
              <span>📋 Tổng số câu hỏi:</span>
              <strong id="quizTotalCount" style="color: #6366f1;">0</strong>
            </div>
            <div class="quiz-stat-item">
              <span>✔️ Đã đúng:</span>
              <strong id="quizCorrectCount" style="color: #16a34a;">0</strong>
            </div>
            <div class="quiz-stat-item">
              <span>❌ Cần ôn lại:</span>
              <strong id="quizWrongCount" style="color: #dc2626;">0</strong>
            </div>
            <button class="nav-btn" id="btnResetConfig" style="font-size: 0.85rem; padding: 4px 12px;">
              ⚙️ Nhập danh sách khác
            </button>
          </div>

          <!-- Lưới hiển thị các thẻ ký tự -->
          <div class="char-cards-grid" id="charCardsGrid">
            <!-- Từng thẻ ký tự sẽ được tạo tự động -->
          </div>

          <button class="btn-finish-quiz" id="btnFinishQuiz">
            <span>🏁 HOÀN THÀNH & TỔNG KẾT ĐÁNH GIÁ</span>
          </button>
        </div>
      </div>
    </section>

    <!-- =========================================================
         MÀN HÌNH TỔNG KẾT CHUNG (SUMMARY SCREEN)
         ========================================================= -->
    <section class="screen" id="screenSummary">
      <div class="summary-card">
        <div class="trophy-icon">🏆</div>
        <h2 style="font-family: 'Sigmar', cursive; color: #1e293b; margin-top: 10px;" id="summaryTitle">XUẤT SẮC QUÁ BÉ ƠI!</h2>
        
        <div style="font-size: 2.8rem; font-family: 'Sigmar', cursive; color: #FF5E7E; margin: 0.5rem 0;" id="summaryScoreVal">
          10 / 10
        </div>
        
        <p style="font-size: 1.2rem; font-weight: 700; color: #475569; margin-bottom: 1.2rem;" id="summaryComment">
          Bé nhận biết chữ số siêu đỉnh luôn nghen!
        </p>

        <div class="summary-stats-box" id="summaryStatsDetails" style="display: none;">
          <div class="stat-pill-box box-green">
            <div style="font-size: 1.8rem; font-weight: 800;" id="sumCorrectBadge">0</div>
            <div style="font-weight: 700;">Ký tự đọc đúng ✔️</div>
          </div>
          <div class="stat-pill-box box-red">
            <div style="font-size: 1.8rem; font-weight: 800;" id="sumWrongBadge">0</div>
            <div style="font-weight: 700;">Ký tự cần ôn lại ❌</div>
          </div>
        </div>

        <div style="display: flex; gap: 12px; width: 100%; margin-top: 0.8rem;">
          <button class="btn-play-large" id="btnRestartCurrentGame" style="flex: 1; padding: 0.9rem 1.4rem; font-size: 1.15rem;">
            <span>🔄 Chơi Lại</span>
          </button>
          <button class="nav-btn" id="btnBackHomeFromSummary" style="flex: 1; justify-content: center; font-size: 1.1rem; border-radius: 30px;">
            <span>🏠 Về Menu</span>
          </button>
        </div>
      </div>
    </section>

  </div>

  <!-- SCRIPT ÂM THANH & LOGIC GAME -->
  <script>
{js_content}

    /* =========================================================
     *  TRÌNH PHÁT GIỌNG ĐỌC NHÚNG CHUẨN (EMBEDDED AUDIO PLAYER)
     * ========================================================= */
    let currentAudioObj = null;

    function playVoice(key, onEndCallback) {{
      if (currentAudioObj) {{
        currentAudioObj.pause();
        currentAudioObj.currentTime = 0;
      }}

      const audioSrc = (typeof EMBEDDED_AUDIO !== 'undefined' && EMBEDDED_AUDIO[key]) ? EMBEDDED_AUDIO[key] : `audio/${{key}}.mp3`;
      currentAudioObj = new Audio(audioSrc);

      currentAudioObj.onended = () => {{
        if (onEndCallback) onEndCallback();
      }};
      currentAudioObj.onerror = () => {{
        if (onEndCallback) onEndCallback();
      }};

      currentAudioObj.play().catch(err => {{
        console.log('Chờ tương tác để phát audio:', err);
      }});
    }}

    /* Web Audio Effects (Tone synthesis) */
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

    function playTone(freq, duration, type = 'sine', gainVal = 0.25) {{
      if (audioCtx.state === 'suspended') audioCtx.resume();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
      gain.gain.setValueAtTime(gainVal, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + duration);
    }}

    function playVictoryChime() {{
      const notes = [523.25, 659.25, 783.99, 1046.50];
      notes.forEach((freq, idx) => {{
        setTimeout(() => playTone(freq, 0.25, 'triangle', 0.25), idx * 85);
      }});
    }}

    function playWrongSound() {{
      if (audioCtx.state === 'suspended') audioCtx.resume();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(260, audioCtx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(120, audioCtx.currentTime + 0.3);
      gain.gain.setValueAtTime(0.18, audioCtx.currentTime);
      gain.gain.linearRampToValueAtTime(0.01, audioCtx.currentTime + 0.3);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + 0.3);
    }}

    function playBubblePop() {{
      playTone(600 + Math.random() * 200, 0.08, 'sine', 0.2);
    }}

    /* Canvas Fireworks */
    const canvas = document.getElementById('fireworksCanvas');
    const ctx = canvas.getContext('2d');
    let particles = [];

    function resizeCanvas() {{
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }}
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    class FireworkParticle {{
      constructor(x, y, color) {{
        this.x = x; this.y = y; this.color = color;
        const angle = Math.random() * Math.PI * 2;
        const speed = Math.random() * 7 + 2;
        this.vx = Math.cos(angle) * speed;
        this.vy = Math.sin(angle) * speed;
        this.alpha = 1; this.friction = 0.96; this.gravity = 0.15;
        this.size = Math.random() * 4 + 2;
      }}
      update() {{
        this.vx *= this.friction; this.vy *= this.friction;
        this.vy += this.gravity; this.x += this.vx; this.y += this.vy;
        this.alpha -= 0.018;
      }}
      draw() {{
        ctx.save();
        ctx.globalAlpha = Math.max(0, this.alpha);
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }}
    }}

    function createFirework(x, y) {{
      const colors = ['#FF1493', '#00FFFF', '#FFD700', '#FF4500', '#7B68EE', '#32CD32', '#FF69B4'];
      const chosenColor = colors[Math.floor(Math.random() * colors.length)];
      for (let i = 0; i < 45; i++) {{
        particles.push(new FireworkParticle(x, y, chosenColor));
      }}
    }}

    function animateFireworks() {{
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      for (let i = particles.length - 1; i >= 0; i--) {{
        const p = particles[i];
        p.update();
        p.draw();
        if (p.alpha <= 0) particles.splice(i, 1);
      }}
      requestAnimationFrame(animateFireworks);
    }}
    animateFireworks();

    function triggerCelebration(originX, originY) {{
      for (let i = 0; i < 3; i++) {{
        setTimeout(() => {{
          const rx = originX || (window.innerWidth * (0.25 + Math.random() * 0.5));
          const ry = originY || (window.innerHeight * (0.2 + Math.random() * 0.4));
          createFirework(rx, ry);
        }}, i * 150);
      }}

      if (typeof confetti === 'function') {{
        confetti({{
          particleCount: 75,
          spread: 80,
          origin: {{
            x: originX ? originX / window.innerWidth : 0.5,
            y: originY ? originY / window.innerHeight : 0.5
          }},
          colors: ['#ff0055', '#ff9900', '#00ddff', '#33ff33', '#9933ff']
        }});
      }}
    }}

    /* =========================================================
     *  ĐIỀU HƯỚNG MÀN HÌNH (ROUTER / NAVIGATION)
     * ========================================================= */
    const screenHome = document.getElementById('screenHome');
    const screenGame1 = document.getElementById('screenGame1');
    const screenGame2 = document.getElementById('screenGame2');
    const screenSummary = document.getElementById('screenSummary');

    const btnNavHome = document.getElementById('btnNavHome');
    const btnNavMenu = document.getElementById('btnNavMenu');
    const btnNavGame1 = document.getElementById('btnNavGame1');
    const btnNavGame2 = document.getElementById('btnNavGame2');

    let currentActiveGame = 'game1'; // 'game1' | 'game2'

    function navigateTo(targetScreen) {{
      [screenHome, screenGame1, screenGame2, screenSummary].forEach(s => s.classList.remove('active'));
      targetScreen.classList.add('active');

      // Update nav buttons
      [btnNavMenu, btnNavGame1, btnNavGame2].forEach(b => b.classList.remove('active'));
      if (targetScreen === screenHome) btnNavMenu.classList.add('active');
      else if (targetScreen === screenGame1) btnNavGame1.classList.add('active');
      else if (targetScreen === screenGame2) btnNavGame2.classList.add('active');

      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    btnNavHome.addEventListener('click', () => navigateTo(screenHome));
    btnNavMenu.addEventListener('click', () => navigateTo(screenHome));
    btnNavGame1.addEventListener('click', () => {{
      currentActiveGame = 'game1';
      navigateTo(screenGame1);
      startRound1();
    }});
    btnNavGame2.addEventListener('click', () => {{
      currentActiveGame = 'game2';
      navigateTo(screenGame2);
    }});

    document.getElementById('cardChooseGame1').addEventListener('click', () => {{
      currentActiveGame = 'game1';
      navigateTo(screenGame1);
      startRound1();
    }});
    document.getElementById('cardChooseGame2').addEventListener('click', () => {{
      currentActiveGame = 'game2';
      navigateTo(screenGame2);
    }});

    document.getElementById('btnBackToHomeFromG1').addEventListener('click', () => navigateTo(screenHome));
    document.getElementById('btnBackHomeFromSummary').addEventListener('click', () => navigateTo(screenHome));

    /* =========================================================
     *  TRÒ CHƠI 1: BÉ VUI ĐOÁN SỐ (1-10)
     * ========================================================= */
    const TOTAL_ROUNDS_1 = 10;
    let currentRound1 = 1;
    let score1 = 0;
    let currentTargetNumber1 = null;
    let isWaitingAnswer1 = false;

    const scoreVal1 = document.getElementById('scoreVal1');
    const roundIndicator1 = document.getElementById('roundIndicator1');
    const bubbleArena1 = document.getElementById('bubbleArena1');
    const btnSpeakNumber1 = document.getElementById('btnSpeakNumber1');
    const feedbackBanner1 = document.getElementById('feedbackBanner1');
    const feedbackText1 = document.getElementById('feedbackText1');
    const feedbackIcon1 = document.getElementById('feedbackIcon1');

    function startRound1() {{
      isWaitingAnswer1 = true;
      feedbackBanner1.className = 'feedback-banner';

      roundIndicator1.textContent = `Vòng ${{currentRound1}} / ${{TOTAL_ROUNDS_1}}`;
      currentTargetNumber1 = Math.floor(Math.random() * 10) + 1;

      // Sinh 5 bong bóng
      const numbers = [currentTargetNumber1];
      while (numbers.length < 5) {{
        const r = Math.floor(Math.random() * 10) + 1;
        if (!numbers.includes(r)) numbers.push(r);
      }}
      for (let i = numbers.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [numbers[i], numbers[j]] = [numbers[j], numbers[i]];
      }}

      bubbleArena1.innerHTML = '';
      numbers.forEach((num, index) => {{
        const b = document.createElement('div');
        b.className = `number-bubble bubble-theme-${{(index % 5) + 1}}`;
        b.textContent = num;
        b.addEventListener('click', (e) => handleBubbleClick1(b, num, e));
        bubbleArena1.appendChild(b);
      }});

      setTimeout(() => speakCurrentTarget1(), 400);
    }}

    function speakCurrentTarget1() {{
      if (currentTargetNumber1 !== null) {{
        btnSpeakNumber1.classList.add('speaking');
        playVoice(currentTargetNumber1.toString(), () => {{
          btnSpeakNumber1.classList.remove('speaking');
        }});
      }}
    }}

    btnSpeakNumber1.addEventListener('click', () => speakCurrentTarget1());

    function handleBubbleClick1(bubbleEl, selectedNum, e) {{
      if (!isWaitingAnswer1) return;
      playBubblePop();

      if (selectedNum === currentTargetNumber1) {{
        isWaitingAnswer1 = false;
        score1 += 10;
        scoreVal1.textContent = score1;

        bubbleEl.classList.add('bubble-correct');
        const rect = bubbleEl.getBoundingClientRect();
        triggerCelebration(rect.left + rect.width / 2, rect.top + rect.height / 2);
        playVictoryChime();

        feedbackBanner1.className = 'feedback-banner show correct';
        feedbackIcon1.textContent = '🎉';
        feedbackText1.textContent = 'Đúng rồi nè! Bé giỏi quá chừng luôn!';
        playVoice('correct');

        setTimeout(() => {{
          if (currentRound1 < TOTAL_ROUNDS_1) {{
            currentRound1++;
            startRound1();
          }} else {{
            finishGame1();
          }}
        }}, 2200);

      }} else {{
        bubbleEl.classList.add('bubble-shake');
        playWrongSound();

        feedbackBanner1.className = 'feedback-banner show wrong';
        feedbackIcon1.textContent = '💡';
        feedbackText1.textContent = 'Chưa đúng rồi nghen, bé chọn lại nha!';
        playVoice('wrong');

        setTimeout(() => bubbleEl.classList.remove('bubble-shake'), 800);
      }}
    }}

    function finishGame1() {{
      navigateTo(screenSummary);
      document.getElementById('summaryTitle').textContent = 'HOÀN THÀNH ĐOÁN SỐ!';
      document.getElementById('summaryScoreVal').textContent = `${{score1}} / ${{TOTAL_ROUNDS_1 * 10}} Điểm`;
      document.getElementById('summaryComment').textContent = score1 >= 90 
        ? 'Trời ơi xuất sắc quá chừng! Bé nhớ hết các số rồi nghen! 🏆' 
        : 'Bé nhận biết chữ số rất tốt luôn nè, tiếp tục phát huy nha! 🌟';
      document.getElementById('summaryStatsDetails').style.display = 'none';

      triggerCelebration();
      playVoice('finish');
    }}

    /* =========================================================
     *  TRÒ CHƠI 2: ĐÂY LÀ SỐ GÌ? ĐÂY LÀ CHỮ GÌ? (LOGIC MỚI)
     * ========================================================= */
    let quizItems = []; // Danh sách ký tự đang hỏi: [{{ char: 'A', type: 'letter', status: null }}, ...]
    let lastHoveredChar = null;
    let hoverAudioTimeout = null;

    const parentConfigBox = document.getElementById('parentConfigBox');
    const quizActiveArea = document.getElementById('quizActiveArea');
    const inputCustomChars = document.getElementById('inputCustomChars');
    const btnStartQuiz = document.getElementById('btnStartQuiz');
    const charCardsGrid = document.getElementById('charCardsGrid');

    const quizTotalCount = document.getElementById('quizTotalCount');
    const quizCorrectCount = document.getElementById('quizCorrectCount');
    const quizWrongCount = document.getElementById('quizWrongCount');
    const btnFinishQuiz = document.getElementById('btnFinishQuiz');
    const btnResetConfig = document.getElementById('btnResetConfig');

    // Các mẫu Presets chọn nhanh
    const PRESETS = {{
      digits_all: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      letters_az: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y'],
      vowels: ['A', 'E', 'I', 'O', 'U'],
      rand_5: () => {{
        const pool = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','M','N','P','S','T'];
        return pool.sort(() => 0.5 - Math.random()).slice(0, 5);
      }},
      rand_10: () => {{
        const pool = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z'];
        return pool.sort(() => 0.5 - Math.random()).slice(0, 10);
      }},
      mix_common: ['0', '1', '2', '5', '9', 'A', 'B', 'C', 'D', 'E']
    }};

    document.querySelectorAll('.preset-chip').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const presetKey = btn.dataset.preset;
        let list = PRESETS[presetKey];
        if (typeof list === 'function') list = list();
        inputCustomChars.value = list.join(', ');
      }});
    }});

    // Phân tích chuỗi người dùng nhập thành danh sách ký tự chuẩn
    function parseCustomInput(rawText) {{
      const cleaned = rawText.toUpperCase().replace(/[^0-9A-Z, ]/g, '');
      const parts = cleaned.split(/[, ]+/).filter(Boolean);
      const result = [];

      parts.forEach(p => {{
        // Nếu nhập chuỗi liền như 'ABC' hoặc '123'
        for (let char of p) {{
          if (/^[0-9]$/.test(char)) {{
            result.push({{ char, type: 'number', status: null }});
          }} else if (/^[A-Z]$/.test(char)) {{
            result.push({{ char, type: 'letter', status: null }});
          }}
        }}
      }});

      return result;
    }}

    btnStartQuiz.addEventListener('click', () => {{
      const parsed = parseCustomInput(inputCustomChars.value);
      if (parsed.length === 0) {{
        alert('Phụ huynh vui lòng nhập ít nhất 1 chữ cái (A-Z) hoặc chữ số (0-9) để đố bé nhé!');
        return;
      }}

      quizItems = parsed;
      renderQuizCards();
      parentConfigBox.style.display = 'none';
      quizActiveArea.classList.add('show');
      updateQuizStats();
    }});

    btnResetConfig.addEventListener('click', () => {{
      quizActiveArea.classList.remove('show');
      parentConfigBox.style.display = 'block';
    }});

    // Vẽ danh sách thẻ ký tự lên màn hình
    function renderQuizCards() {{
      charCardsGrid.innerHTML = '';

      quizItems.forEach((item, index) => {{
        const card = document.createElement('div');
        card.className = 'char-card';
        card.dataset.index = index;

        // Huy hiệu loại (Số hay Chữ)
        const pill = document.createElement('div');
        pill.className = `char-type-pill ${{item.type === 'number' ? 'pill-number' : 'pill-letter'}}`;
        pill.textContent = item.type === 'number' ? 'Chữ Số' : 'Chữ Cái';

        // Ký tự hiển thị to
        const glyph = document.createElement('div');
        glyph.className = 'char-glyph';
        glyph.textContent = item.char;

        // Chỉ dẫn hover
        const hint = document.createElement('div');
        hint.className = 'hover-speaker-hint';
        hint.innerHTML = '<span>🔊</span><span>Di chuột để hỏi</span>';

        // Nút nghe phát âm mẫu
        const btnSample = document.createElement('button');
        btnSample.className = 'btn-reveal-sample';
        btnSample.innerHTML = '🎧 Nghe đáp án mẫu';
        btnSample.addEventListener('click', (e) => {{
          e.stopPropagation();
          playSampleAudio(item);
        }});

        // Khu vực Phụ Huynh Đánh Giá (✔️ / ❌)
        const evalBox = document.createElement('div');
        evalBox.className = 'parent-eval-controls';
        evalBox.innerHTML = '<div class="eval-label">Phụ huynh đánh giá:</div>';

        const evalBtnGroup = document.createElement('div');
        evalBtnGroup.className = 'eval-btn-group';

        const btnCorrect = document.createElement('button');
        btnCorrect.className = `btn-eval btn-eval-correct ${{item.status === 'correct' ? 'selected' : ''}}`;
        btnCorrect.innerHTML = '<span>✔️</span> Đúng';
        btnCorrect.addEventListener('click', (e) => {{
          e.stopPropagation();
          handleEvaluate(index, 'correct', card);
        }});

        const btnWrong = document.createElement('button');
        btnWrong.className = `btn-eval btn-eval-wrong ${{item.status === 'wrong' ? 'selected' : ''}}`;
        btnWrong.innerHTML = '<span>❌</span> Chưa đúng';
        btnWrong.addEventListener('click', (e) => {{
          e.stopPropagation();
          handleEvaluate(index, 'wrong', card);
        }});

        evalBtnGroup.appendChild(btnCorrect);
        evalBtnGroup.appendChild(btnWrong);
        evalBox.appendChild(evalBtnGroup);
        evalBox.appendChild(btnSample);

        card.appendChild(pill);
        card.appendChild(glyph);
        card.appendChild(hint);
        card.appendChild(evalBox);

        // =========================================================
        // SỰ KIỆN DI CHUỘT (HOVER) -> PHÁT GIỌNG ĐỌC HỎI BÉ!
        // =========================================================
        card.addEventListener('mouseenter', () => {{
          handleCardHover(item, card);
        }});

        card.addEventListener('mouseleave', () => {{
          card.classList.remove('hover-speaking');
        }});

        // Hỗ trợ cả thao tác chạm/click trên iPad/Điện thoại
        card.addEventListener('click', () => {{
          handleCardHover(item, card);
        }});

        charCardsGrid.appendChild(card);
      }});
    }}

    // Xử lý khi di chuột vào thẻ: Tự động hỏi "Đây là số gì?" hoặc "Đây là chữ gì?"
    function handleCardHover(item, cardElement) {{
      cardElement.classList.add('hover-speaking');

      // Giới hạn để không phát lặp liên tục nếu giữ chuột lâu
      clearTimeout(hoverAudioTimeout);
      hoverAudioTimeout = setTimeout(() => {{
        if (item.type === 'number') {{
          // Phát câu hỏi: "Đây là số gì?"
          playVoice('hoi_so', () => {{
            cardElement.classList.remove('hover-speaking');
          }});
        }} else {{
          // Phát câu hỏi: "Đây là chữ gì?"
          playVoice('hoi_chu', () => {{
            cardElement.classList.remove('hover-speaking');
          }});
        }}
      }}, 50);
    }}

    // Phát âm chuẩn mẫu của ký tự đó
    function playSampleAudio(item) {{
      if (item.type === 'number') {{
        playVoice(item.char);
      }} else {{
        const letterKey = `letter_${{item.char.toLowerCase()}}`;
        playVoice(letterKey);
      }}
    }}

    // Phụ huynh đánh giá kết quả của bé
    function handleEvaluate(index, status, cardElement) {{
      quizItems[index].status = status;

      cardElement.classList.remove('evaluated-correct', 'evaluated-wrong');
      const btnCorrect = cardElement.querySelector('.btn-eval-correct');
      const btnWrong = cardElement.querySelector('.btn-eval-wrong');

      btnCorrect.classList.remove('selected');
      btnWrong.classList.remove('selected');

      if (status === 'correct') {{
        cardElement.classList.add('evaluated-correct');
        btnCorrect.classList.add('selected');

        const rect = cardElement.getBoundingClientRect();
        triggerCelebration(rect.left + rect.width / 2, rect.top + rect.height / 2);
        playVictoryChime();

        // Khen ngợi bé
        setTimeout(() => {{
          playVoice('correct_eval');
        }}, 350);

      }} else {{
        cardElement.classList.add('evaluated-wrong');
        btnWrong.classList.add('selected');
        cardElement.classList.add('bubble-shake');
        playWrongSound();

        // Động viên bé
        setTimeout(() => {{
          playVoice('wrong_eval');
        }}, 300);

        setTimeout(() => cardElement.classList.remove('bubble-shake'), 700);
      }}

      updateQuizStats();
    }}

    function updateQuizStats() {{
      const total = quizItems.length;
      const correct = quizItems.filter(i => i.status === 'correct').length;
      const wrong = quizItems.filter(i => i.status === 'wrong').length;

      quizTotalCount.textContent = total;
      quizCorrectCount.textContent = correct;
      quizWrongCount.textContent = wrong;
    }}

    // Bấm hoàn thành bài đố
    btnFinishQuiz.addEventListener('click', () => {{
      const total = quizItems.length;
      const correct = quizItems.filter(i => i.status === 'correct').length;
      const wrong = quizItems.filter(i => i.status === 'wrong').length;

      navigateTo(screenSummary);
      document.getElementById('summaryTitle').textContent = 'KẾT QUẢ ĐỐ BÉ!';
      document.getElementById('summaryScoreVal').textContent = `${{correct}} / ${{total}} Đúng`;
      
      let comment = 'Bé rất cố gắng! Cùng ba mẹ ôn lại các ký tự chưa đúng nhé! 👏';
      if (correct === total) {{
        comment = 'Tuyệt đỉnh! Bé đã nhận biết chính xác 100% tất cả số và chữ! 🏆🌟';
        triggerCelebration();
        playVoice('finish');
      }} else if (correct >= total * 0.7) {{
        comment = 'Bé giỏi quá chừng! Đa số các ký tự bé đều nhận biết chuẩn xác nè! 🎉';
        triggerCelebration();
        playVoice('correct_eval');
      }} else {{
        playVoice('wrong_eval');
      }}

      document.getElementById('summaryComment').textContent = comment;

      // Chi tiết thống kê
      document.getElementById('summaryStatsDetails').style.display = 'grid';
      document.getElementById('sumCorrectBadge').textContent = correct;
      document.getElementById('sumWrongBadge').textContent = wrong;
    }});

    // Nút chơi lại trên màn hình tổng kết
    document.getElementById('btnRestartCurrentGame').addEventListener('click', () => {{
      if (currentActiveGame === 'game1') {{
        score1 = 0;
        currentRound1 = 1;
        scoreVal1.textContent = '0';
        navigateTo(screenGame1);
        startRound1();
      }} else {{
        // Reset trạng thái quiz
        quizItems.forEach(i => i.status = null);
        renderQuizCards();
        updateQuizStats();
        navigateTo(screenGame2);
      }}
    }});
  </script>
</body>
</html>
"""

out_html = os.path.join(base_dir, "index.html")
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Build complete: Menu and Game 2 integrated seamlessly into index.html!")
