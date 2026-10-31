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
  <title>Bé Vui Đoán Số 🎈 - Giọng Nữ Miền Nam Chuẩn</title>
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
    .cloud-1 {{
      width: 140px; height: 45px;
      top: 12%; left: -160px;
      animation-duration: 35s;
    }}
    .cloud-1::before {{ width: 50px; height: 50px; top: -22px; left: 25px; }}
    .cloud-1::after {{ width: 70px; height: 70px; top: -35px; right: 25px; }}

    .cloud-2 {{
      width: 180px; height: 55px;
      top: 35%; left: -200px;
      animation-duration: 45s;
      animation-delay: 15s;
      opacity: 0.6;
    }}
    .cloud-2::before {{ width: 60px; height: 60px; top: -30px; left: 30px; }}
    .cloud-2::after {{ width: 85px; height: 85px; top: -45px; right: 35px; }}

    .cloud-3 {{
      width: 120px; height: 40px;
      top: 75%; left: -150px;
      animation-duration: 28s;
      animation-delay: 7s;
      opacity: 0.8;
    }}
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
      max-width: 900px;
      padding: 1.2rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
    }}

    /* Header thanh trạng thái */
    .game-header {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.9);
      backdrop-filter: blur(10px);
      padding: 0.8rem 1.4rem;
      border-radius: 30px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08), 0 0 0 2px rgba(255, 255, 255, 0.9);
      margin-bottom: 1.2rem;
    }}

    .badge-item {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 1.15rem;
      font-weight: 700;
      color: #333;
    }}
    .badge-icon {{
      font-size: 1.6rem;
      display: inline-block;
      animation: pulse 2s infinite ease-in-out;
    }}

    .round-indicator {{
      background: linear-gradient(135deg, #FF6B6B, #FF8E53);
      color: white;
      padding: 6px 18px;
      border-radius: 20px;
      font-weight: 800;
      font-size: 1.05rem;
      box-shadow: 0 4px 12px rgba(255, 107, 107, 0.35);
    }}

    .audio-badge {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: #e8f5e9;
      color: #2e7d32;
      border: 1px solid #a5d6a7;
      padding: 5px 12px;
      border-radius: 20px;
      font-weight: 700;
      font-size: 0.88rem;
    }}

    /* Màn hình */
    .screen {{
      width: 100%;
      display: none;
      flex-direction: column;
      align-items: center;
      text-align: center;
      animation: fadeIn 0.4s ease-out;
    }}
    .screen.active {{
      display: flex;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(15px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .hero-title {{
      font-family: 'Sigmar', cursive;
      font-size: clamp(2.2rem, 5vw, 3.4rem);
      background: linear-gradient(135deg, #FF1361, #FFF800);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 4px 8px rgba(255, 19, 97, 0.25));
      margin-top: 1rem;
      margin-bottom: 0.5rem;
      letter-spacing: 1px;
    }}

    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #fff0f6;
      border: 1.5px solid #ffadd2;
      color: #c41d7f;
      padding: 6px 18px;
      border-radius: 20px;
      font-size: 1rem;
      font-weight: 800;
      margin-bottom: 1rem;
      box-shadow: 0 4px 12px rgba(255, 173, 210, 0.3);
    }}

    .hero-desc {{
      font-size: 1.25rem;
      font-weight: 600;
      color: #3f5175;
      max-width: 580px;
      margin-bottom: 1.8rem;
      line-height: 1.6;
    }}

    .mascot-box {{
      position: relative;
      width: 170px;
      height: 170px;
      margin-bottom: 1.8rem;
      animation: floatMascot 3s ease-in-out infinite;
    }}
    @keyframes floatMascot {{
      0%, 100% {{ transform: translateY(0) rotate(0deg); }}
      50% {{ transform: translateY(-15px) rotate(4deg); }}
    }}

    .btn-play-large {{
      background: linear-gradient(135deg, #00b09b, #96c93d);
      color: white;
      border: none;
      outline: none;
      padding: 1.1rem 2.8rem;
      font-size: 1.55rem;
      font-family: 'Quicksand', sans-serif;
      font-weight: 800;
      border-radius: 50px;
      cursor: pointer;
      box-shadow: 0 12px 25px rgba(0, 176, 155, 0.4), inset 0 2px 0 rgba(255, 255, 255, 0.5);
      transition: all 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .btn-play-large:hover {{
      transform: scale(1.08) translateY(-4px);
      box-shadow: 0 16px 30px rgba(0, 176, 155, 0.5);
    }}
    .btn-play-large:active {{
      transform: scale(0.96);
    }}

    /* Gameplay */
    .speaker-section {{
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(12px);
      padding: 1.5rem 2rem;
      border-radius: 35px;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08), 0 0 0 3px rgba(255, 255, 255, 0.85);
      width: 100%;
      max-width: 650px;
      margin-bottom: 1.8rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
    }}

    .voice-prompt {{
      font-size: 1.35rem;
      font-weight: 700;
      color: #2b3a4a;
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .speaker-btn {{
      position: relative;
      background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
      border: none;
      width: 95px;
      height: 95px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      box-shadow: 0 10px 25px rgba(255, 107, 107, 0.45);
      transition: transform 0.2s;
    }}
    .speaker-btn:hover {{
      transform: scale(1.06);
    }}
    .speaker-btn:active {{
      transform: scale(0.95);
    }}

    .speaker-btn::before,
    .speaker-btn::after {{
      content: '';
      position: absolute;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: rgba(255, 107, 107, 0.4);
      z-index: -1;
      opacity: 0;
    }}
    .speaker-btn.speaking::before {{
      animation: ripple 1.2s ease-out infinite;
    }}
    .speaker-btn.speaking::after {{
      animation: ripple 1.2s ease-out 0.4s infinite;
    }}

    @keyframes ripple {{
      0% {{ transform: scale(1); opacity: 0.85; }}
      100% {{ transform: scale(1.8); opacity: 0; }}
    }}

    .speaker-icon-svg {{
      width: 48px;
      height: 48px;
      fill: white;
    }}

    .speaker-subtext {{
      margin-top: 12px;
      font-size: 1.05rem;
      font-weight: 700;
      color: #e65100;
      background: #fff3e0;
      padding: 6px 18px;
      border-radius: 16px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .bubble-arena {{
      width: 100%;
      max-width: 840px;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      align-items: center;
      gap: 1.6rem;
      padding: 0.8rem 0 1.8rem;
      min-height: 240px;
    }}

    .number-bubble {{
      position: relative;
      width: 120px;
      height: 120px;
      border-radius: 50%;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
      font-family: 'Sigmar', cursive;
      font-size: 3.2rem;
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
      top: 12%;
      left: 20%;
      width: 32px;
      height: 18px;
      background: rgba(255, 255, 255, 0.7);
      border-radius: 50%;
      transform: rotate(-35deg);
      filter: blur(1px);
      pointer-events: none;
    }}

    .number-bubble::before {{
      content: '';
      position: absolute;
      bottom: -10px;
      width: 10px;
      height: 8px;
      background: inherit;
      border-radius: 3px 3px 6px 6px;
      filter: brightness(0.85);
    }}

    .number-bubble:hover {{
      transform: scale(1.15) translateY(-8px);
      box-shadow: 0 22px 38px rgba(0, 0, 0, 0.22),
                  inset -8px -8px 16px rgba(0, 0, 0, 0.2),
                  inset 12px 12px 24px rgba(255, 255, 255, 0.75);
    }}

    .number-bubble:active {{
      transform: scale(0.95);
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

    .summary-card {{
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(15px);
      padding: 2.5rem 2rem;
      border-radius: 40px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.12), 0 0 0 4px rgba(255, 255, 255, 0.8);
      max-width: 520px;
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

    .final-score {{
      font-size: 2.6rem;
      font-family: 'Sigmar', cursive;
      color: #FF5E7E;
      margin: 0.8rem 0;
    }}

    .final-comment {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #4a5568;
      margin-bottom: 2rem;
    }}

    #fireworksCanvas {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 999;
    }}

    .controls-row {{
      display: flex;
      gap: 12px;
      margin-top: 1.2rem;
      align-items: center;
    }}
    .icon-btn {{
      background: white;
      border: none;
      border-radius: 50%;
      width: 48px;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      transition: transform 0.2s;
      font-size: 1.4rem;
    }}
    .icon-btn:hover {{
      transform: scale(1.1);
    }}

    @media (max-width: 600px) {{
      .app-container {{ padding: 0.8rem; }}
      .game-header {{ padding: 0.6rem 0.9rem; }}
      .badge-item {{ font-size: 0.95rem; }}
      .speaker-section {{ padding: 1.2rem 1rem; }}
      .bubble-arena {{ gap: 1rem; }}
      .number-bubble {{ width: 95px; height: 95px; font-size: 2.6rem; }}
    }}
  </style>
</head>
<body>

  <div class="cloud cloud-1"></div>
  <div class="cloud cloud-2"></div>
  <div class="cloud cloud-3"></div>

  <canvas id="fireworksCanvas"></canvas>

  <div class="app-container">

    <header class="game-header">
      <div class="badge-item">
        <span class="badge-icon">⭐</span>
        <span>Điểm: <strong id="scoreVal" style="color: #FF6B6B">0</strong></span>
      </div>

      <div class="round-indicator" id="roundIndicator">
        Vòng 1 / 10
      </div>

      <div class="audio-badge">
        <span>🔊</span>
        <span>Giọng Nữ Miền Nam</span>
      </div>
    </header>

    <!-- 1. MÀN HÌNH BẮT ĐẦU -->
    <section class="screen active" id="startScreen">
      <div class="hero-badge">
        <span>👩‍🏫 Giọng Đọc Cô Giáo Miền Nam Chuẩn Tự Nhiên</span>
      </div>
      
      <h1 class="hero-title">BÉ VUI ĐOÁN SỐ</h1>
      <p class="hero-desc">
        Chào bé nghen! Cùng cô lắng nghe số bí mật từ <strong>1 đến 10</strong> rồi chạm vô quả bóng bay đúng nha! 🎈
      </p>

      <div class="mascot-box">
        <svg viewBox="0 0 120 120" width="100%" height="100%">
          <circle cx="60" cy="65" r="42" fill="#f6b26b" stroke="#d58b38" stroke-width="3"/>
          <circle cx="30" cy="30" r="16" fill="#f6b26b" stroke="#d58b38" stroke-width="3"/>
          <circle cx="30" cy="30" r="9" fill="#ffb4a2"/>
          <circle cx="90" cy="30" r="16" fill="#f6b26b" stroke="#d58b38" stroke-width="3"/>
          <circle cx="90" cy="30" r="9" fill="#ffb4a2"/>
          <circle cx="48" cy="58" r="6" fill="#2d3748"/>
          <circle cx="50" cy="56" r="2" fill="#ffffff"/>
          <circle cx="72" cy="58" r="6" fill="#2d3748"/>
          <circle cx="74" cy="56" r="2" fill="#ffffff"/>
          <circle cx="38" cy="68" r="7" fill="#ff8a80" opacity="0.6"/>
          <circle cx="82" cy="68" r="7" fill="#ff8a80" opacity="0.6"/>
          <ellipse cx="60" cy="72" rx="14" ry="10" fill="#fffaf0"/>
          <ellipse cx="60" cy="68" rx="5" ry="3.5" fill="#5d4037"/>
          <path d="M 57 74 Q 60 78 63 74" stroke="#5d4037" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        </svg>
      </div>

      <button class="btn-play-large" id="btnStartGame">
        <span>🎮 BẮT ĐẦU CHƠI NÈ!</span>
      </button>

      <div class="controls-row">
        <button class="icon-btn" id="btnSoundTest" title="Nghe cô chào nè">
          🔊
        </button>
        <span style="font-size: 1rem; font-weight: 700; color: #4b5563;">Bấm loa để nghe cô chào bé nha!</span>
      </div>
    </section>

    <!-- 2. MÀN HÌNH CHƠI CHÍNH -->
    <section class="screen" id="gameScreen">
      <div class="speaker-section">
        <div class="voice-prompt">
          <span>🎧 Bé bấm vô loa để nghe số bí mật nè:</span>
        </div>

        <button class="speaker-btn" id="btnSpeakNumber" title="Bấm nghe lại số bí mật nghen">
          <svg class="speaker-icon-svg" viewBox="0 0 24 24">
            <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
          </svg>
        </button>

        <span class="speaker-subtext" id="speakerStatus">Bấm loa để nghe lại nghen bé!</span>
      </div>

      <div class="bubble-arena" id="bubbleArena"></div>

      <div class="feedback-banner" id="feedbackBanner">
        <span id="feedbackIcon">🎉</span>
        <span id="feedbackText">Bé giỏi quá chừng luôn!</span>
      </div>
    </section>

    <!-- 3. MÀN HÌNH KẾT THÚC -->
    <section class="screen" id="summaryScreen">
      <div class="summary-card">
        <div class="trophy-icon">🏆</div>
        <h2 style="font-family: 'Sigmar', cursive; color: #333; margin-top: 10px;">XUẤT SẮC QUÁ BÉ ƠI!</h2>
        
        <div class="final-score" id="finalScoreVal">10 / 10</div>
        <p class="final-comment" id="finalCommentText">Bé nhận biết chữ số siêu đỉnh luôn nghen!</p>

        <button class="btn-play-large" id="btnRestartGame">
          <span>🔄 CHƠI LẠI VÒNG MỚI NÈ</span>
        </button>
      </div>
    </section>

  </div>

  <script>
{js_content}

    /* =========================================================
     *  TRÌNH PHÁT GIỌNG ĐỌC NHÚNG CHUẨN (EMBEDDED AUDIO PLAYER)
     * ========================================================= */
    let currentAudioObj = null;

    function playVoice(key, onEndCallback) {{
      const speakerBtn = document.getElementById('btnSpeakNumber');
      if (speakerBtn) speakerBtn.classList.add('speaking');

      if (currentAudioObj) {{
        currentAudioObj.pause();
        currentAudioObj.currentTime = 0;
      }}

      const audioSrc = (typeof EMBEDDED_AUDIO !== 'undefined' && EMBEDDED_AUDIO[key]) ? EMBEDDED_AUDIO[key] : `audio/${{key}}.mp3`;
      currentAudioObj = new Audio(audioSrc);

      currentAudioObj.onended = () => {{
        if (speakerBtn) speakerBtn.classList.remove('speaking');
        if (onEndCallback) onEndCallback();
      }};

      currentAudioObj.onerror = (e) => {{
        console.warn('Lỗi phát audio nhúng:', e);
        if (speakerBtn) speakerBtn.classList.remove('speaking');
        if (onEndCallback) onEndCallback();
      }};

      currentAudioObj.play().catch(err => {{
        console.log('Chờ bé tương tác để phát âm thanh:', err);
        if (speakerBtn) speakerBtn.classList.remove('speaking');
      }});
    }}

    /* Web Audio Effects */
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
        setTimeout(() => playTone(freq, 0.25, 'triangle', 0.3), idx * 90);
      }});
    }}

    function playWrongSound() {{
      if (audioCtx.state === 'suspended') audioCtx.resume();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(260, audioCtx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(120, audioCtx.currentTime + 0.35);
      gain.gain.setValueAtTime(0.18, audioCtx.currentTime);
      gain.gain.linearRampToValueAtTime(0.01, audioCtx.currentTime + 0.35);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + 0.35);
    }}

    function playBubblePop() {{
      playTone(600 + Math.random() * 200, 0.08, 'sine', 0.2);
    }}

    /* Pháo hoa Canvas */
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
        this.x = x;
        this.y = y;
        this.color = color;
        const angle = Math.random() * Math.PI * 2;
        const speed = Math.random() * 7 + 2;
        this.vx = Math.cos(angle) * speed;
        this.vy = Math.sin(angle) * speed;
        this.alpha = 1;
        this.friction = 0.96;
        this.gravity = 0.15;
        this.size = Math.random() * 4 + 2;
      }}
      update() {{
        this.vx *= this.friction;
        this.vy *= this.friction;
        this.vy += this.gravity;
        this.x += this.vx;
        this.y += this.vy;
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
          particleCount: 80,
          spread: 80,
          origin: {{
            x: originX ? originX / window.innerWidth : 0.5,
            y: originY ? originY / window.innerHeight : 0.5
          }},
          colors: ['#ff0055', '#ff9900', '#00ddff', '#33ff33', '#9933ff']
        }});
      }}
    }}

    /* Game Controller */
    const TOTAL_ROUNDS = 10;
    let currentRound = 1;
    let score = 0;
    let currentTargetNumber = null;
    let isWaitingAnswer = false;

    const startScreen = document.getElementById('startScreen');
    const gameScreen = document.getElementById('gameScreen');
    const summaryScreen = document.getElementById('summaryScreen');

    const scoreVal = document.getElementById('scoreVal');
    const roundIndicator = document.getElementById('roundIndicator');
    const bubbleArena = document.getElementById('bubbleArena');
    const btnSpeakNumber = document.getElementById('btnSpeakNumber');
    const feedbackBanner = document.getElementById('feedbackBanner');
    const feedbackText = document.getElementById('feedbackText');
    const feedbackIcon = document.getElementById('feedbackIcon');

    function showScreen(screen) {{
      [startScreen, gameScreen, summaryScreen].forEach(s => s.classList.remove('active'));
      screen.classList.add('active');
    }}

    function generateBubbleNumbers(target) {{
      const numbers = [target];
      while (numbers.length < 5) {{
        const rand = Math.floor(Math.random() * 10) + 1;
        if (!numbers.includes(rand)) {{
          numbers.push(rand);
        }}
      }}
      for (let i = numbers.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [numbers[i], numbers[j]] = [numbers[j], numbers[i]];
      }}
      return numbers;
    }}

    function startRound() {{
      isWaitingAnswer = true;
      hideFeedback();

      roundIndicator.textContent = `Vòng ${{currentRound}} / ${{TOTAL_ROUNDS}}`;
      currentTargetNumber = Math.floor(Math.random() * 10) + 1;

      const bubbleNumbers = generateBubbleNumbers(currentTargetNumber);
      renderBubbles(bubbleNumbers);

      setTimeout(() => {{
        speakCurrentTarget();
      }}, 400);
    }}

    function speakCurrentTarget() {{
      if (currentTargetNumber !== null) {{
        playVoice(currentTargetNumber.toString());
      }}
    }}

    function renderBubbles(numbers) {{
      bubbleArena.innerHTML = '';
      numbers.forEach((num, index) => {{
        const bubble = document.createElement('div');
        bubble.className = `number-bubble bubble-theme-${{(index % 5) + 1}}`;
        bubble.textContent = num;
        bubble.dataset.number = num;

        bubble.addEventListener('click', (e) => handleBubbleClick(bubble, num, e));
        bubbleArena.appendChild(bubble);
      }});
    }}

    function handleBubbleClick(bubbleElement, selectedNumber, event) {{
      if (!isWaitingAnswer) return;

      playBubblePop();

      if (selectedNumber === currentTargetNumber) {{
        isWaitingAnswer = false;
        score += 10;
        scoreVal.textContent = score;

        bubbleElement.classList.add('bubble-correct');

        const rect = bubbleElement.getBoundingClientRect();
        const originX = rect.left + rect.width / 2;
        const originY = rect.top + rect.height / 2;
        triggerCelebration(originX, originY);
        playVictoryChime();

        showFeedback('Đúng rồi nè! Bé giỏi quá chừng luôn! 🎉', 'correct');
        playVoice('correct');

        setTimeout(() => {{
          if (currentRound < TOTAL_ROUNDS) {{
            currentRound++;
            startRound();
          }} else {{
            finishGame();
          }}
        }}, 2200);

      }} else {{
        bubbleElement.classList.add('bubble-shake');
        playWrongSound();

        showFeedback('Chưa đúng rồi nghen, bé chọn lại nha! 💡', 'wrong');
        playVoice('wrong');

        setTimeout(() => {{
          bubbleElement.classList.remove('bubble-shake');
        }}, 800);
      }}
    }}

    function showFeedback(msg, type) {{
      feedbackBanner.className = `feedback-banner show ${{type}}`;
      feedbackText.textContent = msg;
      feedbackIcon.textContent = type === 'correct' ? '🎉' : '💡';
    }}

    function hideFeedback() {{
      feedbackBanner.className = 'feedback-banner';
    }}

    function finishGame() {{
      showScreen(summaryScreen);
      document.getElementById('finalScoreVal').textContent = `${{score}} / ${{TOTAL_ROUNDS * 10}}`;

      let comment = 'Bé cố gắng luyện thêm với cô nghen! Rất chăm chỉ nè! 👏';
      if (score >= 90) {{
        comment = 'Trời ơi xuất sắc quá chừng! Bé nhớ hết các số rồi nghen! 🏆🎈';
      }} else if (score >= 70) {{
        comment = 'Bé nghe số rất chuẩn xác luôn đó nè! Giỏi lắm! 🌟';
      }}
      document.getElementById('finalCommentText').textContent = comment;

      triggerCelebration();
      setTimeout(triggerCelebration, 600);

      playVoice('finish');
    }}

    function resetGame() {{
      score = 0;
      currentRound = 1;
      scoreVal.textContent = score;
      showScreen(gameScreen);
      startRound();
    }}

    document.getElementById('btnStartGame').addEventListener('click', resetGame);
    document.getElementById('btnRestartGame').addEventListener('click', resetGame);

    btnSpeakNumber.addEventListener('click', () => {{
      speakCurrentTarget();
    }});

    document.getElementById('btnSoundTest').addEventListener('click', () => {{
      playVoice('intro');
    }});
  </script>
</body>
</html>
"""

out_html = os.path.join(base_dir, "index.html")
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Build complete: index.html updated successfully with 100% embedded audio!")
