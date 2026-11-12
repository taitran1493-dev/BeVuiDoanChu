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
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Bé Vui Học Tập 🎈 - Bé Đoán Số & Chữ Cái Tiếng Việt</title>
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
      -webkit-tap-highlight-color: transparent;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Quicksand', sans-serif;
      min-height: 100vh;
      min-height: 100dvh;
      background: var(--bg-gradient);
      overflow-x: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      padding-bottom: env(safe-area-inset-bottom, 20px);
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
    .cloud-1 {{ width: 140px; height: 45px; top: 10%; left: -160px; animation-duration: 35s; }}
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
      max-width: 980px;
      padding: 0.8rem 1rem 2.5rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
      min-height: 100dvh;
    }}

    /* Thanh Điều Hướng Menu Toàn Cục */
    .nav-bar {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      padding: 0.6rem 1.2rem;
      border-radius: 30px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08), 0 0 0 2px rgba(255, 255, 255, 0.95);
      margin-bottom: 1.2rem;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: 'Sigmar', cursive;
      font-size: clamp(1.1rem, 3.5vw, 1.35rem);
      color: #FF5E7E;
      cursor: pointer;
      text-decoration: none;
      transition: transform 0.2s;
    }}
    .nav-brand:active {{ transform: scale(0.96); }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }}

    .nav-btn {{
      background: #f1f5f9;
      color: #334155;
      border: 1.5px solid transparent;
      padding: 6px 14px;
      border-radius: 18px;
      font-family: inherit;
      font-weight: 700;
      font-size: clamp(0.85rem, 2.5vw, 0.95rem);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      min-height: 38px;
    }}
    .nav-btn:hover {{ background: #e2e8f0; }}
    .nav-btn:active {{ transform: scale(0.95); }}
    .nav-btn.active {{
      background: linear-gradient(135deg, #6366f1, #8b5cf6);
      color: white;
      box-shadow: 0 4px 12px rgba(99, 102, 241, 0.35);
    }}

    /* Các màn hình chính */
    .screen {{
      width: 100%;
      display: none;
      flex-direction: column;
      align-items: center;
      text-align: center;
      animation: fadeIn 0.3s ease-out;
    }}
    .screen.active {{
      display: flex;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(10px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* =========================================================
     *  MÀN HÌNH TRANG CHỦ / MENU CHỌN TRÒ CHƠI
     * ========================================================= */
    .home-hero {{
      margin-top: 0.2rem;
      margin-bottom: 1.5rem;
    }}
    .home-title {{
      font-family: 'Sigmar', cursive;
      font-size: clamp(1.8rem, 5.5vw, 3.2rem);
      background: linear-gradient(135deg, #FF1361, #FFA000);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 3px 6px rgba(255, 19, 97, 0.25));
      margin-bottom: 0.4rem;
      letter-spacing: 0.5px;
    }}
    .home-desc {{
      font-size: clamp(1rem, 2.8vw, 1.2rem);
      font-weight: 600;
      color: #334155;
      max-width: 650px;
      line-height: 1.55;
      padding: 0 0.5rem;
    }}

    .game-cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.4rem;
      width: 100%;
      max-width: 880px;
    }}

    .game-card {{
      background: rgba(255, 255, 255, 0.95);
      border-radius: 30px;
      padding: clamp(1.5rem, 4vw, 2.2rem) clamp(1.2rem, 3vw, 1.8rem);
      box-shadow: 0 14px 30px rgba(0, 0, 0, 0.08), 0 0 0 3px rgba(255, 255, 255, 0.9);
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: all 0.28s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    .game-card:hover {{
      transform: translateY(-6px) scale(1.02);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12), 0 0 0 4px rgba(255, 255, 255, 1);
    }}
    .game-card:active {{ transform: scale(0.98); }}

    .game-card-icon {{
      width: clamp(75px, 14vw, 90px);
      height: clamp(75px, 14vw, 90px);
      border-radius: 26px;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: clamp(2.6rem, 5vw, 3.2rem);
      margin-bottom: 1rem;
      box-shadow: 0 8px 18px rgba(0, 0, 0, 0.1);
    }}

    .card-theme-1 .game-card-icon {{ background: linear-gradient(135deg, #ff758c, #ff4070); }}
    .card-theme-2 .game-card-icon {{ background: linear-gradient(135deg, #4facfe, #00f2fe); }}

    .game-card-badge {{
      position: absolute;
      top: 14px;
      right: 16px;
      font-size: 0.78rem;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 12px;
      text-transform: uppercase;
    }}
    .badge-hot {{ background: #ffe3e3; color: #e03131; }}
    .badge-new {{ background: #d3f9d8; color: #2b8a3e; border: 1px solid #b2f2bb; }}

    .game-card-title {{
      font-family: 'Sigmar', cursive;
      font-size: clamp(1.4rem, 4vw, 1.7rem);
      color: #1e293b;
      margin-bottom: 0.5rem;
    }}

    .game-card-info {{
      font-size: clamp(0.95rem, 2.5vw, 1.05rem);
      color: #64748b;
      font-weight: 600;
      line-height: 1.5;
      margin-bottom: 1.4rem;
      flex-grow: 1;
    }}

    .btn-card-action {{
      width: 100%;
      border: none;
      padding: clamp(0.8rem, 2.5vw, 0.95rem) 1.5rem;
      border-radius: 22px;
      font-family: inherit;
      font-weight: 800;
      font-size: clamp(1rem, 3vw, 1.15rem);
      color: white;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      min-height: 48px;
    }}
    .card-theme-1 .btn-card-action {{
      background: linear-gradient(135deg, #FF5E7E, #FF8E53);
      box-shadow: 0 6px 16px rgba(255, 94, 126, 0.35);
    }}
    .card-theme-2 .btn-card-action {{
      background: linear-gradient(135deg, #38ef7d, #11998e);
      box-shadow: 0 6px 16px rgba(17, 153, 142, 0.35);
    }}

    /* =========================================================
     *  TRÒ CHƠI 1: BÉ VUI ĐOÁN SỐ (6 BÓNG SỐ TỐI ƯU CẢ ĐIỆN THOẠI)
     * ========================================================= */
    .game1-header {{
      width: 100%;
      max-width: 820px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.92);
      padding: 0.6rem 1.2rem;
      border-radius: 22px;
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.06);
      margin-bottom: 1rem;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .score-badge {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: clamp(0.95rem, 3vw, 1.1rem);
      font-weight: 700;
      color: #333;
    }}
    .round-tag {{
      background: linear-gradient(135deg, #FF6B6B, #FF8E53);
      color: white;
      padding: 4px 14px;
      border-radius: 18px;
      font-weight: 800;
      font-size: clamp(0.85rem, 2.5vw, 1rem);
    }}

    .speaker-section {{
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(12px);
      padding: clamp(1rem, 3vw, 1.4rem) clamp(1rem, 4vw, 2rem);
      border-radius: 28px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08), 0 0 0 2px rgba(255, 255, 255, 0.9);
      width: 100%;
      max-width: 650px;
      margin-bottom: 1.2rem;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    .speaker-btn {{
      position: relative;
      background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
      border: none;
      width: clamp(75px, 16vw, 90px);
      height: clamp(75px, 16vw, 90px);
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      box-shadow: 0 10px 22px rgba(255, 107, 107, 0.45);
      transition: transform 0.2s;
    }}
    .speaker-btn:hover {{ transform: scale(1.06); }}
    .speaker-btn:active {{ transform: scale(0.94); }}
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

    /* Khu vực hiển thị 6 bong bóng số */
    .bubble-arena {{
      width: 100%;
      max-width: 860px;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: clamp(0.8rem, 2.5vw, 1.4rem);
      padding: 0.5rem 0.2rem 1.2rem;
      justify-items: center;
    }}

    @media (min-width: 768px) {{
      .bubble-arena {{
        grid-template-columns: repeat(6, 1fr);
      }}
    }}

    .number-bubble {{
      position: relative;
      width: clamp(80px, 20vw, 110px);
      height: clamp(80px, 20vw, 110px);
      border-radius: 50%;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
      font-family: 'Sigmar', cursive;
      font-size: clamp(2.3rem, 6vw, 3.1rem);
      color: white;
      text-shadow: 0 3px 6px rgba(0, 0, 0, 0.3);
      box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15),
                  inset -6px -6px 14px rgba(0, 0, 0, 0.2),
                  inset 8px 8px 18px rgba(255, 255, 255, 0.6);
      transition: transform 0.22s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      animation: bubbleFloat 4s ease-in-out infinite alternate;
    }}
    .number-bubble::after {{
      content: '';
      position: absolute;
      top: 12%; left: 20%;
      width: clamp(20px, 4vw, 28px);
      height: clamp(10px, 2.5vw, 15px);
      background: rgba(255, 255, 255, 0.7);
      border-radius: 50%;
      transform: rotate(-35deg);
      filter: blur(1px);
      pointer-events: none;
    }}
    .number-bubble:hover {{ transform: scale(1.1) translateY(-6px); }}
    .number-bubble:active {{ transform: scale(0.92); }}

    .bubble-theme-1 {{ background: radial-gradient(circle at 35% 35%, #ff758c, #ff4070); animation-delay: 0s; }}
    .bubble-theme-2 {{ background: radial-gradient(circle at 35% 35%, #4facfe, #00f2fe); animation-delay: 0.5s; }}
    .bubble-theme-3 {{ background: radial-gradient(circle at 35% 35%, #43e97b, #38f9d7); animation-delay: 1.0s; }}
    .bubble-theme-4 {{ background: radial-gradient(circle at 35% 35%, #fa709a, #fee140); animation-delay: 1.5s; }}
    .bubble-theme-5 {{ background: radial-gradient(circle at 35% 35%, #b176ff, #6234f4); animation-delay: 2.0s; }}
    .bubble-theme-6 {{ background: radial-gradient(circle at 35% 35%, #00c6ff, #0072ff); animation-delay: 2.5s; }}

    @keyframes bubbleFloat {{
      0% {{ transform: translateY(0px) rotate(0deg); }}
      100% {{ transform: translateY(-12px) rotate(3deg); }}
    }}

    .bubble-shake {{
      animation: shake 0.5s ease-in-out !important;
      background: radial-gradient(circle at 35% 35%, #ff6b6b, #c92a2a) !important;
      opacity: 0.7;
    }}
    @keyframes shake {{
      0%, 100% {{ transform: translateX(0); }}
      20%, 60% {{ transform: translateX(-10px) rotate(-5deg); }}
      40%, 80% {{ transform: translateX(10px) rotate(5deg); }}
    }}

    .bubble-correct {{
      animation: popSuccess 0.8s forwards !important;
      background: radial-gradient(circle at 35% 35%, #51cf66, #2b8a3e) !important;
      z-index: 10;
    }}
    @keyframes popSuccess {{
      0% {{ transform: scale(1); }}
      50% {{ transform: scale(1.3) rotate(8deg); filter: brightness(1.2); }}
      100% {{ transform: scale(1.1) rotate(0deg); }}
    }}

    .feedback-banner {{
      min-height: 50px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      font-size: clamp(1.05rem, 3.2vw, 1.3rem);
      font-weight: 800;
      border-radius: 20px;
      padding: 0.5rem 1.4rem;
      margin-top: 0.4rem;
      opacity: 0;
      transform: translateY(8px);
      transition: all 0.3s;
    }}
    .feedback-banner.show {{ opacity: 1; transform: translateY(0); }}
    .feedback-banner.correct {{ background: #d3f9d8; color: #2b8a3e; border: 2px solid #69db7c; }}
    .feedback-banner.wrong {{ background: #ffe3e3; color: #c92a2a; border: 2px solid #ffa8a8; }}

    /* =========================================================
     *  TRÒ CHƠI 2: ĐÂY LÀ SỐ GÌ? ĐÂY LÀ CHỮ GÌ? (BẢNG CHỮ TIẾNG VIỆT)
     * ========================================================= */
    .game2-card-container {{
      width: 100%;
      max-width: 920px;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      border-radius: 30px;
      padding: clamp(1rem, 3vw, 2rem);
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.08), 0 0 0 2px rgba(255, 255, 255, 0.95);
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    .game2-title {{
      font-family: 'Sigmar', cursive;
      font-size: clamp(1.5rem, 4.5vw, 2.2rem);
      background: linear-gradient(135deg, #0284c7, #6366f1);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 0.3rem;
    }}

    .game2-subdesc {{
      color: #475569;
      font-weight: 600;
      font-size: clamp(0.92rem, 2.5vw, 1.05rem);
      margin-bottom: 1.2rem;
      max-width: 680px;
      line-height: 1.5;
    }}

    .rule-notice-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #eff6ff;
      border: 1.5px solid #bfdbfe;
      color: #1d4ed8;
      padding: 5px 12px;
      border-radius: 16px;
      font-weight: 700;
      font-size: clamp(0.82rem, 2.4vw, 0.92rem);
      margin-bottom: 1rem;
      text-align: center;
    }}

    /* Bảng thiết lập của Phụ huynh */
    .parent-config-box {{
      width: 100%;
      background: #f8fafc;
      border: 2px dashed #cbd5e1;
      border-radius: 24px;
      padding: clamp(1rem, 3vw, 1.5rem);
      margin-bottom: 1.2rem;
      text-align: left;
    }}

    .parent-config-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.8rem;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .parent-badge {{
      background: #e0e7ff;
      color: #4338ca;
      font-weight: 800;
      font-size: clamp(0.78rem, 2.4vw, 0.88rem);
      padding: 4px 10px;
      border-radius: 12px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }}

    .char-input-group {{
      margin-bottom: 1rem;
    }}
    .char-input-group label {{
      display: block;
      font-weight: 700;
      color: #1e293b;
      margin-bottom: 6px;
      font-size: clamp(0.92rem, 2.6vw, 1.02rem);
    }}
    .char-input-field {{
      width: 100%;
      padding: clamp(0.7rem, 2vw, 0.85rem) clamp(0.8rem, 2vw, 1.1rem);
      border-radius: 16px;
      border: 2px solid #cbd5e1;
      font-family: 'Quicksand', sans-serif;
      font-weight: 700;
      font-size: clamp(1.05rem, 3vw, 1.25rem);
      color: #0f172a;
      background: white;
      outline: none;
    }}
    .char-input-field:focus {{
      border-color: #6366f1;
      box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15);
    }}

    .preset-chips-container {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 1.2rem;
    }}
    .preset-chip {{
      background: white;
      border: 1.5px solid #e2e8f0;
      color: #475569;
      padding: 5px 12px;
      border-radius: 16px;
      font-family: inherit;
      font-weight: 700;
      font-size: clamp(0.8rem, 2.4vw, 0.88rem);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      min-height: 36px;
    }}
    .preset-chip:active {{ transform: scale(0.96); }}
    .preset-chip:hover {{ background: #f1f5f9; border-color: #6366f1; color: #4338ca; }}

    .btn-start-quiz {{
      background: linear-gradient(135deg, #6366f1, #3b82f6);
      color: white;
      border: none;
      padding: clamp(0.85rem, 2.5vw, 1rem) 1.8rem;
      border-radius: 25px;
      font-family: inherit;
      font-weight: 800;
      font-size: clamp(1.05rem, 3vw, 1.2rem);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
      box-shadow: 0 8px 18px rgba(99, 102, 241, 0.35);
      min-height: 50px;
    }}
    .btn-start-quiz:active {{ transform: scale(0.98); }}

    /* Vùng Đố Bé (Interactive Flashcards Grid) */
    .quiz-active-area {{
      display: none;
      width: 100%;
      flex-direction: column;
      align-items: center;
    }}
    .quiz-active-area.show {{ display: flex; }}

    .device-touch-hint {{
      background: #fefce8;
      border: 1px solid #fef08a;
      color: #854d0e;
      padding: 6px 14px;
      border-radius: 14px;
      font-size: 0.86rem;
      font-weight: 700;
      margin-bottom: 1rem;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .quiz-stats-bar {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #f8fafc;
      padding: 0.7rem 1.2rem;
      border-radius: 18px;
      margin-bottom: 1.2rem;
      border: 1.5px solid #e2e8f0;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .quiz-stat-item {{
      font-size: clamp(0.88rem, 2.5vw, 1rem);
      font-weight: 700;
      color: #334155;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    /* Lưới hiển thị các thẻ ký tự - Tối ưu di động & Tablet */
    .char-cards-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: clamp(0.7rem, 2.5vw, 1.2rem);
      width: 100%;
      margin-bottom: 1.5rem;
    }}

    /* Màn hình điện thoại lớn hoặc Tablet nhỏ */
    @media (min-width: 480px) {{
      .char-cards-grid {{
        grid-template-columns: repeat(3, 1fr);
      }}
    }}
    /* Tablet & Desktop */
    @media (min-width: 768px) {{
      .char-cards-grid {{
        grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
      }}
    }}

    /* Từng thẻ ký tự 3D với dấu mũ Tiếng Việt rõ ràng */
    .char-card {{
      background: white;
      border-radius: 22px;
      padding: clamp(0.8rem, 2vw, 1.1rem) clamp(0.5rem, 1.5vw, 0.8rem);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06), 0 0 0 2px #e2e8f0;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      cursor: pointer;
      transition: all 0.22s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    .char-card:hover {{
      transform: translateY(-5px) scale(1.03);
      box-shadow: 0 14px 28px rgba(0, 0, 0, 0.1), 0 0 0 3px #6366f1;
    }}
    .char-card:active {{ transform: scale(0.97); }}

    .char-card.hover-speaking {{
      animation: cardPulse 1.2s infinite alternate;
      border-color: #f59e0b;
      box-shadow: 0 0 0 3px #fbbf24, 0 12px 24px rgba(245, 158, 11, 0.25);
    }}
    @keyframes cardPulse {{
      from {{ transform: scale(1.01); }}
      to {{ transform: scale(1.06); }}
    }}

    .char-card.evaluated-correct {{
      background: #f0fdf4;
      border-color: #22c55e !important;
      box-shadow: 0 8px 20px rgba(34, 197, 94, 0.18), 0 0 0 2px #86efac;
    }}
    .char-card.evaluated-wrong {{
      background: #fef2f2;
      border-color: #ef4444 !important;
      box-shadow: 0 8px 20px rgba(239, 68, 68, 0.18), 0 0 0 2px #fca5a5;
    }}

    .char-type-pill {{
      font-size: 0.72rem;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 10px;
      margin-bottom: 0.2rem;
      text-transform: uppercase;
    }}
    .pill-number {{ background: #e0f2fe; color: #0369a1; }}
    .pill-letter {{ background: #fce7f3; color: #be185d; }}

    /* Ký tự Tiếng Việt hiển thị lớn, không bị che dấu mũ/râu */
    .char-glyph {{
      font-family: 'Sigmar', 'Quicksand', sans-serif;
      font-size: clamp(3rem, 9vw, 4.2rem);
      line-height: 1.15;
      padding-top: 4px;
      margin: 0.2rem 0 0.5rem;
      color: #1e293b;
      text-shadow: 0 3px 8px rgba(0, 0, 0, 0.08);
      transition: transform 0.2s;
      min-height: 60px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .char-card.evaluated-correct .char-glyph {{ color: #15803d; }}
    .char-card.evaluated-wrong .char-glyph {{ color: #b91c1c; }}

    .hover-speaker-hint {{
      font-size: 0.76rem;
      font-weight: 700;
      color: #64748b;
      display: flex;
      align-items: center;
      gap: 4px;
      margin-bottom: 0.6rem;
      background: #f8fafc;
      padding: 2px 8px;
      border-radius: 10px;
    }}

    .parent-eval-controls {{
      width: 100%;
      border-top: 1.5px solid #f1f5f9;
      padding-top: 0.6rem;
      display: flex;
      flex-direction: column;
      gap: 5px;
    }}
    .eval-label {{
      font-size: 0.72rem;
      font-weight: 800;
      color: #94a3b8;
      text-align: center;
      text-transform: uppercase;
    }}
    .eval-btn-group {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 5px;
    }}
    .btn-eval {{
      border: none;
      padding: 8px 4px;
      border-radius: 12px;
      font-family: inherit;
      font-weight: 800;
      font-size: clamp(0.78rem, 2.2vw, 0.86rem);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 3px;
      min-height: 40px;
    }}
    .btn-eval-correct {{
      background: #dcfce7;
      color: #166534;
      border: 1.5px solid #86efac;
    }}
    .btn-eval-correct:active, .btn-eval-correct.selected {{
      background: #22c55e;
      color: white;
      border-color: #16a34a;
    }}

    .btn-eval-wrong {{
      background: #fee2e2;
      color: #991b1b;
      border: 1.5px solid #fca5a5;
    }}
    .btn-eval-wrong:active, .btn-eval-wrong.selected {{
      background: #ef4444;
      color: white;
      border-color: #dc2626;
    }}

    .btn-reveal-sample {{
      background: #f1f5f9;
      border: none;
      padding: 5px 6px;
      border-radius: 10px;
      font-family: inherit;
      font-size: 0.75rem;
      font-weight: 700;
      color: #475569;
      cursor: pointer;
      min-height: 32px;
    }}
    .btn-reveal-sample:active {{ background: #e2e8f0; }}

    .btn-finish-quiz {{
      background: linear-gradient(135deg, #10b981, #059669);
      color: white;
      border: none;
      padding: 0.85rem 2rem;
      border-radius: 25px;
      font-family: inherit;
      font-weight: 800;
      font-size: clamp(1.05rem, 3vw, 1.2rem);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 8px 20px rgba(16, 185, 129, 0.35);
      min-height: 50px;
      width: 100%;
      max-width: 420px;
    }}
    .btn-finish-quiz:active {{ transform: scale(0.98); }}

    /* Màn hình tổng kết (Summary) */
    .summary-card {{
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(15px);
      padding: clamp(1.5rem, 4vw, 2.4rem) clamp(1.2rem, 3vw, 2rem);
      border-radius: 30px;
      box-shadow: 0 16px 45px rgba(0, 0, 0, 0.12), 0 0 0 3px rgba(255, 255, 255, 0.9);
      max-width: 540px;
      width: 100%;
      margin-top: 0.5rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      animation: popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    @keyframes popIn {{
      0% {{ opacity: 0; transform: scale(0.7); }}
      100% {{ opacity: 1; transform: scale(1); }}
    }}

    .trophy-icon {{
      font-size: clamp(3.5rem, 10vw, 4.6rem);
      animation: bounce 1s infinite alternate ease-in-out;
    }}
    @keyframes bounce {{
      from {{ transform: translateY(0); }}
      to {{ transform: translateY(-10px); }}
    }}

    .summary-stats-box {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      width: 100%;
      margin: 1rem 0;
    }}
    .stat-pill-box {{
      padding: 0.8rem;
      border-radius: 18px;
      text-align: center;
    }}
    .box-green {{ background: #f0fdf4; border: 2px solid #bbf7d0; color: #166534; }}
    .box-red {{ background: #fef2f2; border: 2px solid #fecaca; color: #991b1b; }}

    #fireworksCanvas {{
      position: fixed;
      top: 0; left: 0;
      width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 999;
    }}

    .btn-play-large {{
      background: linear-gradient(135deg, #00b09b, #96c93d);
      color: white;
      border: none;
      outline: none;
      padding: 0.9rem 2rem;
      font-size: clamp(1.1rem, 3.2vw, 1.4rem);
      font-family: 'Quicksand', sans-serif;
      font-weight: 800;
      border-radius: 40px;
      cursor: pointer;
      box-shadow: 0 10px 22px rgba(0, 176, 155, 0.4);
      min-height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }}
    .btn-play-large:active {{ transform: scale(0.96); }}
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
          <span>🏠 Menu</span>
        </button>
        <button class="nav-btn" id="btnNavGame1">
          <span>🎈 Trò 1 (6 Bóng)</span>
        </button>
        <button class="nav-btn" id="btnNavGame2">
          <span>🔤 Trò 2 (Chữ Tiếng Việt)</span>
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
          Chào mừng các bé và ba mẹ! Hãy chọn trò chơi bên dưới để cùng luyện nghe, luyện mắt và phát âm chuẩn chữ cái Tiếng Việt nhé!
        </p>
      </div>

      <div class="game-cards-grid">
        <!-- Card Trò chơi 1 -->
        <div class="game-card card-theme-1" id="cardChooseGame1">
          <div class="game-card-badge badge-hot">Rất Vui ⭐</div>
          <div class="game-card-icon">🎈</div>
          <h2 class="game-card-title">Bé Vui Đoán Số</h2>
          <p class="game-card-info">
            Lắng nghe giọng đọc bí mật từ <strong>1 đến 10</strong>, màn hình hiển thị <strong>6 bong bóng số</strong> rực rỡ để bé chọn và bắn pháo hoa!
          </p>
          <button class="btn-card-action">
            <span>🎮 CHƠI ĐOÁN SỐ (6 BÓNG)</span>
            <span>➔</span>
          </button>
        </div>

        <!-- Card Trò chơi 2 -->
        <div class="game-card card-theme-2" id="cardChooseGame2">
          <div class="game-card-badge badge-new">Bảng Chữ Tiếng Việt ✨</div>
          <div class="game-card-icon">🔤</div>
          <h2 class="game-card-title">Đố Bé: Số Gì? Chữ Gì?</h2>
          <p class="game-card-info">
            Chuẩn <strong>29 chữ cái Tiếng Việt</strong> (A, Ă, Â, B, C, D, Đ,...). Tối thiểu <strong>6 thẻ lớn</strong> hiển thị rõ ràng trên điện thoại & iPad!
          </p>
          <button class="btn-card-action">
            <span>👨‍👩‍👧 VÀO ĐỐ BÉ NGAY (≥6 THẺ)</span>
            <span>➔</span>
          </button>
        </div>
      </div>
    </section>

    <!-- =========================================================
         MÀN HÌNH 1: TRÒ CHƠI 1 - BÉ VUI ĐOÁN SỐ (6 BÓNG SỐ)
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
        <button class="nav-btn" id="btnBackToHomeFromG1" style="padding: 4px 10px; font-size: 0.85rem;">
          🏠 Đổi Trò Chơi
        </button>
      </div>

      <div class="speaker-section">
        <div style="font-size: clamp(1.1rem, 3vw, 1.3rem); font-weight: 700; color: #2b3a4a; margin-bottom: 0.6rem;">
          🎧 Bé bấm vô loa để nghe số bí mật nè:
        </div>

        <button class="speaker-btn" id="btnSpeakNumber1" title="Bấm nghe lại số bí mật nghen">
          <svg style="width: 44px; height: 44px; fill: white;" viewBox="0 0 24 24">
            <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
          </svg>
        </button>

        <span style="margin-top: 8px; font-size: clamp(0.85rem, 2.5vw, 0.98rem); font-weight: 700; color: #e65100; background: #fff3e0; padding: 4px 14px; border-radius: 12px;">
          Bấm loa để nghe lại nghen! (Chọn 1 trong 6 bóng)
        </span>
      </div>

      <!-- Khu vực hiển thị 6 bong bóng số -->
      <div class="bubble-arena" id="bubbleArena1"></div>

      <div class="feedback-banner" id="feedbackBanner1">
        <span id="feedbackIcon1">🎉</span>
        <span id="feedbackText1">Bé giỏi quá chừng luôn!</span>
      </div>
    </section>

    <!-- =========================================================
         MÀN HÌNH 2: TRÒ CHƠI 2 - ĐÂY LÀ SỐ GÌ? ĐÂY LÀ CHỮ GÌ? (BẢNG CHỮ TIẾNG VIỆT)
         ========================================================= -->
    <section class="screen" id="screenGame2">
      <div class="game2-card-container">
        <h1 class="game2-title">ĐÂY LÀ SỐ GÌ? ĐÂY LÀ CHỮ GÌ?</h1>
        <p class="game2-subdesc">
          Chuẩn <strong>bảng chữ cái Tiếng Việt</strong> (A, Ă, Â, B, C, D, Đ, E, Ê,...) và các số 0-9. Di chuột hoặc <strong>chạm tay vào thẻ</strong> để nghe câu hỏi!
        </p>

        <div class="rule-notice-badge">
          <span>🇻🇳</span>
          <span>Bảng chữ Tiếng Việt chuẩn Bộ Giáo Dục • Hiển thị <strong>tối thiểu 6 thẻ</strong></span>
        </div>

        <!-- BẢNG CÀI ĐẶT DÀNH CHO PHỤ HUYNH -->
        <div class="parent-config-box" id="parentConfigBox">
          <div class="parent-config-header">
            <div class="parent-badge">
              <span>👨‍👩‍👧 DÀNH CHO PHỤ HUYNH THIẾT LẬP</span>
            </div>
            <span style="font-size: 0.82rem; color: #64748b; font-weight: 700;">Hỗ trợ 29 chữ cái Tiếng Việt & số 0-9</span>
          </div>

          <div class="char-input-group">
            <label for="inputCustomChars">Nhập danh sách số hoặc chữ cần hỏi bé (tối thiểu 6 thẻ):</label>
            <input type="text" id="inputCustomChars" class="char-input-field" placeholder="Ví dụ: A, Ă, Â, B, C, D, Đ, 0, 1, 5" value="A, Ă, Â, B, C, D, Đ, 0, 1, 5">
            <div style="font-size: 0.82rem; color: #64748b; margin-top: 5px;">
              💡 <em>Mẹo: Hỗ trợ gõ đầy đủ các chữ có dấu: Ă, Â, Đ, Ê, Ô, Ơ, Ư. Nếu nhập dưới 6 ký tự, máy sẽ tự bù thêm cho đủ 6 thẻ!</em>
            </div>
          </div>

          <!-- Nút chọn nhanh (Presets Tiếng Việt) -->
          <div style="font-weight: 700; font-size: 0.88rem; color: #475569; margin-bottom: 6px;">Chọn nhanh bộ ký tự Tiếng Việt có sẵn:</div>
          <div class="preset-chips-container">
            <button class="preset-chip" data-preset="vi_vowels_special">🌟 7 Chữ có dấu đặc trưng (Ă, Â, Đ, Ê, Ô, Ơ, Ư)</button>
            <button class="preset-chip" data-preset="vi_first_6">👶 6 Chữ cái đầu (A, Ă, Â, B, C, D)</button>
            <button class="preset-chip" data-preset="vi_vowels_12">✨ 12 Nguyên âm Tiếng Việt (A, Ă, Â, E, Ê,...)</button>
            <button class="preset-chip" data-preset="vi_mix_6">🎈 6 Số & Chữ Tiếng Việt cơ bản</button>
            <button class="preset-chip" data-preset="digits_all">🔢 Toàn bộ 10 số (0 - 9)</button>
            <button class="preset-chip" data-preset="rand_6_vi">🎲 Ngẫu nhiên 6 chữ Tiếng Việt</button>
            <button class="preset-chip" data-preset="rand_10_vi">🎲 Ngẫu nhiên 10 chữ Tiếng Việt & Số</button>
            <button class="preset-chip" data-preset="vi_all_29">🇻🇳 Toàn bộ 29 chữ cái Tiếng Việt</button>
          </div>

          <button class="btn-start-quiz" id="btnStartQuiz">
            <span>🚀 BẮT ĐẦU ĐỐ BÉ NGAY (TỐI THIỂU 6 THẺ)</span>
          </button>
        </div>

        <!-- VÙNG BÀI ĐỐ CHO BÉ (HIỆN KHI ĐÃ BẤM BẮT ĐẦU) -->
        <div class="quiz-active-area" id="quizActiveArea">
          <div class="device-touch-hint">
            <span>📱</span>
            <span>Trên iPad/Điện thoại: <strong>Chạm tay vào thẻ</strong> để nghe cô đọc câu hỏi nghen!</span>
          </div>

          <div class="quiz-stats-bar">
            <div class="quiz-stat-item">
              <span>📋 Thẻ hiển thị:</span>
              <strong id="quizTotalCount" style="color: #6366f1;">6</strong>
            </div>
            <div class="quiz-stat-item">
              <span>✔️ Đã đúng:</span>
              <strong id="quizCorrectCount" style="color: #16a34a;">0</strong>
            </div>
            <div class="quiz-stat-item">
              <span>❌ Cần ôn:</span>
              <strong id="quizWrongCount" style="color: #dc2626;">0</strong>
            </div>
            <button class="nav-btn" id="btnResetConfig" style="font-size: 0.82rem; padding: 4px 10px; min-height: 32px;">
              ⚙️ Đổi danh sách
            </button>
          </div>

          <!-- Lưới hiển thị các thẻ ký tự (Tối ưu responsive điện thoại & tablet) -->
          <div class="char-cards-grid" id="charCardsGrid"></div>

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
        <h2 style="font-family: 'Sigmar', cursive; color: #1e293b; margin-top: 8px; font-size: clamp(1.4rem, 4vw, 1.8rem);" id="summaryTitle">XUẤT SẮC QUÁ BÉ ƠI!</h2>
        
        <div style="font-size: clamp(2.2rem, 6vw, 2.8rem); font-family: 'Sigmar', cursive; color: #FF5E7E; margin: 0.4rem 0;" id="summaryScoreVal">
          10 / 10
        </div>
        
        <p style="font-size: clamp(1rem, 2.8vw, 1.2rem); font-weight: 700; color: #475569; margin-bottom: 1rem; line-height: 1.5;" id="summaryComment">
          Bé nhận biết chữ cái Tiếng Việt siêu đỉnh luôn nghen!
        </p>

        <div class="summary-stats-box" id="summaryStatsDetails" style="display: none;">
          <div class="stat-pill-box box-green">
            <div style="font-size: 1.6rem; font-weight: 800;" id="sumCorrectBadge">0</div>
            <div style="font-weight: 700; font-size: 0.88rem;">Ký tự đọc đúng ✔️</div>
          </div>
          <div class="stat-pill-box box-red">
            <div style="font-size: 1.6rem; font-weight: 800;" id="sumWrongBadge">0</div>
            <div style="font-weight: 700; font-size: 0.88rem;">Ký tự cần ôn lại ❌</div>
          </div>
        </div>

        <div style="display: flex; gap: 10px; width: 100%; margin-top: 0.6rem; flex-wrap: wrap;">
          <button class="btn-play-large" id="btnRestartCurrentGame" style="flex: 1; padding: 0.8rem 1.2rem; font-size: 1.1rem; min-width: 140px;">
            <span>🔄 Chơi Lại</span>
          </button>
          <button class="nav-btn" id="btnBackHomeFromSummary" style="flex: 1; justify-content: center; font-size: 1.05rem; border-radius: 30px; min-height: 48px; min-width: 140px;">
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
        console.log('Chờ bé tương tác để phát âm thanh:', err);
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
        setTimeout(() => playTone(freq, 0.22, 'triangle', 0.25), idx * 85);
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
        const speed = Math.random() * 6 + 2;
        this.vx = Math.cos(angle) * speed;
        this.vy = Math.sin(angle) * speed;
        this.alpha = 1; this.friction = 0.96; this.gravity = 0.15;
        this.size = Math.random() * 3.5 + 2;
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
      for (let i = 0; i < 40; i++) {{
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
          particleCount: 70,
          spread: 75,
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

    let currentActiveGame = 'game1';

    function navigateTo(targetScreen) {{
      [screenHome, screenGame1, screenGame2, screenSummary].forEach(s => s.classList.remove('active'));
      targetScreen.classList.add('active');

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
     *  TRÒ CHƠI 1: BÉ VUI ĐOÁN SỐ (ĐẢM BẢO 6 BÓNG SỐ HIỂN THỊ)
     * ========================================================= */
    const TOTAL_ROUNDS_1 = 10;
    const NUM_BUBBLES_GAME1 = 6;
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

      // Sinh 6 bong bóng số khác nhau (1 số đúng + 5 số khác từ 1..10)
      const numbers = [currentTargetNumber1];
      while (numbers.length < NUM_BUBBLES_GAME1) {{
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
        b.className = `number-bubble bubble-theme-${{(index % 6) + 1}}`;
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
     *  TRÒ CHƠI 2: ĐÂY LÀ SỐ GÌ? ĐÂY LÀ CHỮ GÌ? (BẢNG CHỮ TIẾNG VIỆT)
     * ========================================================= */
    const MIN_CHARS_GAME2 = 6;
    let quizItems = [];
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

    // 29 CHỮ CÁI TIẾNG VIỆT CHUẨN
    const VIETNAMESE_ALPHABET = [
      'A', 'Ă', 'Â', 'B', 'C', 'D', 'Đ', 'E', 'Ê', 'G', 'H', 'I', 'K', 'L', 'M',
      'N', 'O', 'Ô', 'Ơ', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ư', 'V', 'X', 'Y'
    ];

    // CÁC BỘ PRESETS TIẾNG VIỆT ĐỀU >= 6 KÝ TỰ
    const PRESETS = {{
      vi_vowels_special: ['Ă', 'Â', 'Đ', 'Ê', 'Ô', 'Ơ', 'Ư'],
      vi_first_6: ['A', 'Ă', 'Â', 'B', 'C', 'D'],
      vi_vowels_12: ['A', 'Ă', 'Â', 'E', 'Ê', 'I', 'O', 'Ô', 'Ơ', 'U', 'Ư', 'Y'],
      vi_mix_6: ['0', '1', '5', 'A', 'Ă', 'Đ'],
      digits_all: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      rand_6_vi: () => {{
        return [...VIETNAMESE_ALPHABET].sort(() => 0.5 - Math.random()).slice(0, 6);
      }},
      rand_10_vi: () => {{
        const pool = [...VIETNAMESE_ALPHABET, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
        return pool.sort(() => 0.5 - Math.random()).slice(0, 10);
      }},
      vi_all_29: VIETNAMESE_ALPHABET
    }};

    document.querySelectorAll('.preset-chip').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const presetKey = btn.dataset.preset;
        let list = PRESETS[presetKey];
        if (typeof list === 'function') list = list();
        inputCustomChars.value = list.join(', ');
      }});
    }});

    // Phân tích chuỗi Tiếng Việt và tự động bù đủ tối thiểu 6 ký tự
    function parseCustomInputWithMin6(rawText) {{
      // Tách chuỗi theo dấu phẩy hoặc khoảng trắng
      const parts = rawText.toUpperCase().split(/[, ]+/).filter(Boolean);
      const seen = new Set();
      const result = [];

      parts.forEach(p => {{
        // Lấy từng ký tự bao gồm cả dấu tiếng Việt
        for (let char of p) {{
          if (!seen.has(char)) {{
            if (/^[0-9]$/.test(char)) {{
              seen.add(char);
              result.push({{ char, type: 'number', status: null }});
            }} else if (VIETNAMESE_ALPHABET.includes(char) || /^[A-Z]$/.test(char)) {{
              seen.add(char);
              result.push({{ char, type: 'letter', status: null }});
            }}
          }}
        }}
      }});

      // TỰ ĐỘNG BÙ ĐỦ TỐI THIỂU 6 KÝ TỰ TỪ BẢNG CHỮ TIẾNG VIỆT
      if (result.length < MIN_CHARS_GAME2) {{
        const fallbackPool = ['A', 'Ă', 'Â', 'B', 'C', 'Đ', '0', '1', '2', '5', '8', '9'];
        for (let fb of fallbackPool) {{
          if (result.length >= MIN_CHARS_GAME2) break;
          if (!seen.has(fb)) {{
            seen.add(fb);
            const type = /^[0-9]$/.test(fb) ? 'number' : 'letter';
            result.push({{ char: fb, type, status: null }});
          }}
        }}
      }}

      return result;
    }}

    btnStartQuiz.addEventListener('click', () => {{
      const parsed = parseCustomInputWithMin6(inputCustomChars.value);
      quizItems = parsed;

      inputCustomChars.value = quizItems.map(i => i.char).join(', ');

      renderQuizCards();
      parentConfigBox.style.display = 'none';
      quizActiveArea.classList.add('show');
      updateQuizStats();
    }});

    btnResetConfig.addEventListener('click', () => {{
      quizActiveArea.classList.remove('show');
      parentConfigBox.style.display = 'block';
    }});

    // Lấy key audio chính xác cho từng ký tự tiếng Việt
    function getAudioKeyForChar(item) {{
      if (item.type === 'number') return item.char;
      const lower = item.char.toLowerCase();
      return `letter_${{lower}}`;
    }}

    // Vẽ danh sách thẻ ký tự lên màn hình
    function renderQuizCards() {{
      charCardsGrid.innerHTML = '';

      quizItems.forEach((item, index) => {{
        const card = document.createElement('div');
        card.className = 'char-card';
        card.dataset.index = index;

        const pill = document.createElement('div');
        pill.className = `char-type-pill ${{item.type === 'number' ? 'pill-number' : 'pill-letter'}}`;
        pill.textContent = item.type === 'number' ? 'Chữ Số' : 'Chữ Cái';

        const glyph = document.createElement('div');
        glyph.className = 'char-glyph';
        glyph.textContent = item.char;

        const hint = document.createElement('div');
        hint.className = 'hover-speaker-hint';
        hint.innerHTML = '<span>🔊</span><span>Chạm / Di chuột</span>';

        const btnSample = document.createElement('button');
        btnSample.className = 'btn-reveal-sample';
        btnSample.innerHTML = '🎧 Nghe phát âm mẫu';
        btnSample.addEventListener('click', (e) => {{
          e.stopPropagation();
          playSampleAudio(item);
        }});

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

        // DI CHUỘT (PC) HOẶC CHẠM TAY (ĐIỆN THOẠI/TABLET) -> PHÁT CÂU HỎI
        card.addEventListener('mouseenter', () => {{
          handleCardInteract(item, card);
        }});

        card.addEventListener('mouseleave', () => {{
          card.classList.remove('hover-speaking');
        }});

        card.addEventListener('click', () => {{
          handleCardInteract(item, card);
        }});

        charCardsGrid.appendChild(card);
      }});
    }}

    function handleCardInteract(item, cardElement) {{
      cardElement.classList.add('hover-speaking');

      clearTimeout(hoverAudioTimeout);
      hoverAudioTimeout = setTimeout(() => {{
        if (item.type === 'number') {{
          playVoice('hoi_so', () => cardElement.classList.remove('hover-speaking'));
        }} else {{
          playVoice('hoi_chu', () => cardElement.classList.remove('hover-speaking'));
        }}
      }}, 50);
    }}

    function playSampleAudio(item) {{
      const key = getAudioKeyForChar(item);
      playVoice(key);
    }}

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

        setTimeout(() => {{
          playVoice('correct_eval');
        }}, 350);

      }} else {{
        cardElement.classList.add('evaluated-wrong');
        btnWrong.classList.add('selected');
        cardElement.classList.add('bubble-shake');
        playWrongSound();

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

    btnFinishQuiz.addEventListener('click', () => {{
      const total = quizItems.length;
      const correct = quizItems.filter(i => i.status === 'correct').length;
      const wrong = quizItems.filter(i => i.status === 'wrong').length;

      navigateTo(screenSummary);
      document.getElementById('summaryTitle').textContent = 'KẾT QUẢ ĐỐ BÉ!';
      document.getElementById('summaryScoreVal').textContent = `${{correct}} / ${{total}} Đúng`;
      
      let comment = 'Bé rất cố gắng! Cùng ba mẹ ôn lại các chữ cái chưa đúng nhé! 👏';
      if (correct === total) {{
        comment = 'Tuyệt đỉnh! Bé đã nhận biết chính xác 100% tất cả số và chữ cái Tiếng Việt! 🏆🌟';
        triggerCelebration();
        playVoice('finish');
      }} else if (correct >= total * 0.7) {{
        comment = 'Bé giỏi quá chừng! Đa số các chữ cái Tiếng Việt bé đều phát âm chuẩn xác nè! 🎉';
        triggerCelebration();
        playVoice('correct_eval');
      }} else {{
        playVoice('wrong_eval');
      }}

      document.getElementById('summaryComment').textContent = comment;
      document.getElementById('summaryStatsDetails').style.display = 'grid';
      document.getElementById('sumCorrectBadge').textContent = correct;
      document.getElementById('sumWrongBadge').textContent = wrong;
    }});

    document.getElementById('btnRestartCurrentGame').addEventListener('click', () => {{
      if (currentActiveGame === 'game1') {{
        score1 = 0;
        currentRound1 = 1;
        scoreVal1.textContent = '0';
        navigateTo(screenGame1);
        startRound1();
      }} else {{
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

print("Build complete: Vietnamese alphabet & mobile/tablet responsiveness fully optimized!")
