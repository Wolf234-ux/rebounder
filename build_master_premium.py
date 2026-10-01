import os
import base64

base_dir = r"c:\Users\saura\OneDrive\Desktop\rebounder"

def get_base64_img(rel_path):
    full_path = os.path.join(base_dir, rel_path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode("utf-8")
            return f"data:image/jpeg;base64,{encoded}"
    return rel_path

hero_b64 = get_base64_img(os.path.join("assets", "hero_rebounder.jpg"))
dr_b64 = get_base64_img(os.path.join("assets", "dr_gaikwad.jpg"))
senior_b64 = get_base64_img(os.path.join("assets", "senior_routine.jpg"))

html_content = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Change Mee Medical Longevity Platform — Executive Pitch & Live Experience</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Syne:wght@600;700;800&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    /* ==========================================================================
       CHANGE MEE MEDICAL LONGEVITY PLATFORM - LUXURY CRYO-GLASS DESIGN SYSTEM
       Theme: Ultra-Premium Bio-Engineering & High-Trust Clinical Medicine
       ========================================================================== */
    :root {{
      --bg-midnight: #050b14;
      --bg-surface: #0a1526;
      --bg-elevated: rgba(15, 34, 61, 0.75);
      --glass-base: rgba(10, 21, 38, 0.7);
      --glass-border: rgba(195, 245, 255, 0.12);
      --glass-border-hover: rgba(0, 229, 255, 0.45);
      
      --cyan-neon: #00e5ff;
      --cyan-glow: rgba(0, 229, 255, 0.35);
      --cyan-soft: #9cf0ff;
      --emerald-healing: #10b981;
      --emerald-glow: rgba(16, 185, 129, 0.3);
      --rose-alert: #f43f5e;
      --amber-warn: #f59e0b;
      --purple-royal: #8b5cf6;
      
      --text-main: #f8fafc;
      --text-sub: #cbd5e1;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      --font-display: 'Syne', sans-serif;
      --font-body: 'Plus Jakarta Sans', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      
      --radius-sm: 6px;
      --radius-md: 12px;
      --radius-lg: 18px;
      --radius-xl: 24px;
      --radius-pill: 9999px;
      
      --shadow-cryo: 0 16px 40px -10px rgba(0, 0, 0, 0.8), 0 0 30px -4px rgba(0, 229, 255, 0.12);
      --shadow-elevation: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      background-color: var(--bg-midnight);
      background-image: 
        radial-gradient(circle at 10% 15%, rgba(0, 229, 255, 0.08) 0%, transparent 45%),
        radial-gradient(circle at 90% 85%, rgba(16, 185, 129, 0.07) 0%, transparent 50%),
        radial-gradient(circle at 50% 50%, rgba(139, 92, 246, 0.04) 0%, transparent 60%);
      color: var(--text-main);
      font-family: var(--font-body);
      line-height: 1.5;
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }}

    /* Global Cryo-Glass Utility */
    .cryo-card {{
      background: var(--glass-base);
      backdrop-filter: blur(20px) saturate(160%);
      -webkit-backdrop-filter: blur(20px) saturate(160%);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-elevation);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }}
    .cryo-card:hover {{
      border-color: var(--glass-border-hover);
      box-shadow: var(--shadow-cryo);
    }}

    /* Top Navigation Bar */
    .master-header {{
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(5, 11, 20, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--glass-border);
      padding: 0.85rem 2rem;
    }}
    .header-inner {{
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }}
    .brand-group {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }}
    .pulsing-orb {{
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: var(--cyan-neon);
      box-shadow: 0 0 15px var(--cyan-neon);
      position: relative;
    }}
    .pulsing-orb::after {{
      content: '';
      position: absolute;
      inset: -4px;
      border-radius: 50%;
      border: 1px solid var(--cyan-neon);
      animation: ripple 2s infinite ease-out;
    }}
    @keyframes ripple {{
      0% {{ transform: scale(0.8); opacity: 1; }}
      100% {{ transform: scale(2.2); opacity: 0; }}
    }}
    .brand-title {{
      font-family: var(--font-display);
      font-size: 1.35rem;
      font-weight: 800;
      letter-spacing: 0.04em;
      color: #ffffff;
    }}
    .brand-tag {{
      font-family: var(--font-mono);
      font-size: 0.65rem;
      font-weight: 700;
      padding: 0.2rem 0.6rem;
      background: rgba(0, 229, 255, 0.12);
      border: 1px solid rgba(0, 229, 255, 0.35);
      color: var(--cyan-neon);
      border-radius: var(--radius-sm);
      letter-spacing: 0.08em;
    }}

    /* Navigation Pills */
    .tab-nav-bar {{
      display: flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.03);
      padding: 0.35rem;
      border-radius: var(--radius-pill);
      border: 1px solid var(--glass-border);
      gap: 0.25rem;
    }}
    .nav-pill {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-family: var(--font-body);
      font-size: 0.825rem;
      font-weight: 600;
      padding: 0.5rem 1.1rem;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all 0.25s ease;
    }}
    .nav-pill .num {{
      font-family: var(--font-mono);
      font-size: 0.7rem;
      opacity: 0.6;
    }}
    .nav-pill:hover {{
      color: #ffffff;
      background: rgba(255, 255, 255, 0.06);
    }}
    .nav-pill.active {{
      background: linear-gradient(135deg, rgba(0, 229, 255, 0.25), rgba(16, 185, 129, 0.25));
      color: #ffffff;
      border: 1px solid var(--cyan-neon);
      box-shadow: 0 0 20px var(--cyan-glow);
    }}
    .nav-pill.active .num {{
      color: var(--cyan-neon);
      opacity: 1;
    }}

    .header-ctrls {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}
    .pill-btn {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--glass-border);
      color: var(--text-sub);
      padding: 0.4rem 0.85rem;
      border-radius: var(--radius-pill);
      font-size: 0.75rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
    }}
    .pill-btn:hover {{
      background: rgba(255, 255, 255, 0.12);
      color: #ffffff;
    }}
    .badge-live {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: var(--emerald-healing);
      font-family: var(--font-mono);
      font-size: 0.7rem;
      font-weight: 700;
      padding: 0.35rem 0.8rem;
      border-radius: var(--radius-pill);
    }}

    /* Main Container */
    .main-wrap {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 2rem;
    }}
    .tab-section {{
      display: none;
      animation: fadeSlide 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .tab-section.active {{
      display: block;
    }}
    @keyframes fadeSlide {{
      from {{ opacity: 0; transform: translateY(12px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Section Banner */
    .sec-hero {{
      margin-bottom: 2rem;
    }}
    .eyebrow-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      padding: 0.3rem 0.75rem;
      border-radius: var(--radius-pill);
      margin-bottom: 0.85rem;
    }}
    .eyebrow-alert {{
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid rgba(244, 63, 94, 0.35);
      color: #fda4af;
    }}
    .eyebrow-clinical {{
      background: rgba(0, 229, 255, 0.15);
      border: 1px solid rgba(0, 229, 255, 0.35);
      color: var(--cyan-neon);
    }}
    .eyebrow-routine {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.35);
      color: var(--emerald-healing);
    }}
    .eyebrow-roi {{
      background: rgba(139, 92, 246, 0.15);
      border: 1px solid rgba(139, 92, 246, 0.35);
      color: #c4b5fd;
    }}
    .sec-title {{
      font-family: var(--font-display);
      font-size: 2.3rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #ffffff;
      margin-bottom: 0.6rem;
      line-height: 1.2;
    }}
    .sec-desc {{
      color: var(--text-muted);
      font-size: 1rem;
      max-width: 900px;
      line-height: 1.6;
    }}

    /* ==========================================================
       TAB 1: DIGITAL AUDIT & INTERACTIVE 3D HOTSPOT EXPLORER
       ========================================================== */
    .audit-split {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
      margin-bottom: 2rem;
    }}
    .audit-pane {{
      padding: 1.75rem;
    }}
    .audit-top-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.25rem;
    }}
    .audit-top-bar h3 {{
      font-family: var(--font-display);
      font-size: 1.15rem;
      color: #ffffff;
    }}
    .audit-tag-danger {{
      background: rgba(244, 63, 94, 0.15);
      color: #fda4af;
      border: 1px solid rgba(244, 63, 94, 0.3);
      padding: 0.2rem 0.6rem;
      border-radius: var(--radius-sm);
      font-size: 0.7rem;
      font-weight: 700;
      font-family: var(--font-mono);
    }}
    .audit-tag-success {{
      background: rgba(16, 185, 129, 0.15);
      color: #6ee7b7;
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 0.2rem 0.6rem;
      border-radius: var(--radius-sm);
      font-size: 0.7rem;
      font-weight: 700;
      font-family: var(--font-mono);
    }}

    .browser-mock {{
      background: #080f18;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-md);
      overflow: hidden;
    }}
    .browser-dots {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.5rem 0.85rem;
      background: #0f172a;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }}
    .b-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
    }}
    .b-red {{ background: #ef4444; }}
    .b-yellow {{ background: #f59e0b; }}
    .b-green {{ background: #10b981; }}
    .b-url {{
      font-family: var(--font-mono);
      font-size: 0.65rem;
      color: var(--text-dim);
      margin-left: 0.5rem;
    }}

    .mock-body {{
      padding: 1.25rem;
    }}
    .mock-alert {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      background: rgba(244, 63, 94, 0.12);
      border: 1px solid rgba(244, 63, 94, 0.3);
      padding: 0.85rem 1rem;
      border-radius: var(--radius-sm);
      margin-bottom: 1.25rem;
    }}
    .mock-alert strong {{
      color: #fecdd3;
      font-size: 0.85rem;
      display: block;
    }}
    .mock-alert span {{
      color: #fda4af;
      font-size: 0.75rem;
    }}

    .check-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }}
    .check-list li {{
      font-size: 0.85rem;
      color: var(--text-sub);
      display: flex;
      align-items: flex-start;
      gap: 0.65rem;
      line-height: 1.4;
    }}
    .icon-fail {{ color: var(--rose-alert); font-weight: bold; }}
    .icon-pass {{ color: var(--emerald-healing); font-weight: bold; }}

    /* Hotspot Hero Viewer */
    .hero-hotspot-container {{
      position: relative;
      border-radius: var(--radius-md);
      overflow: hidden;
      margin-bottom: 1.25rem;
      aspect-ratio: 16 / 9;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
    }}
    .hero-hotspot-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .hotspot-pin {{
      position: absolute;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: rgba(0, 229, 255, 0.85);
      color: #000;
      font-family: var(--font-mono);
      font-weight: 800;
      font-size: 0.75rem;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 0 15px var(--cyan-neon);
      transform: translate(-50%, -50%);
      transition: all 0.2s ease;
      z-index: 10;
    }}
    .hotspot-pin:hover {{
      transform: translate(-50%, -50%) scale(1.3);
      background: #ffffff;
    }}
    .hotspot-card {{
      position: absolute;
      background: rgba(5, 11, 20, 0.95);
      border: 1px solid var(--cyan-neon);
      backdrop-filter: blur(12px);
      padding: 0.75rem 1rem;
      border-radius: var(--radius-md);
      max-width: 250px;
      font-size: 0.75rem;
      color: #ffffff;
      box-shadow: var(--shadow-cryo);
      display: none;
      z-index: 20;
    }}
    .hotspot-card.active {{
      display: block;
      animation: popIn 0.2s ease-out;
    }}
    @keyframes popIn {{
      from {{ opacity: 0; transform: scale(0.9); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}
    .hotspot-card strong {{
      color: var(--cyan-neon);
      display: block;
      margin-bottom: 0.2rem;
      font-family: var(--font-mono);
    }}

    /* ==========================================================
       TAB 2: REMASTERED DOCTOR BROADCAST VIDEO (DR. GAIKWAD)
       ========================================================== */
    .video-studio-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 2rem;
    }}
    .video-player-frame {{
      position: relative;
      aspect-ratio: 16 / 9;
      background: #000;
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.85);
      border: 1px solid var(--glass-border);
    }}
    .video-feed-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      filter: brightness(0.88);
      transition: filter 0.3s ease;
    }}
    .video-overlay-hud {{
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 1.5rem;
      background: linear-gradient(180deg, rgba(0,0,0,0.7) 0%, transparent 35%, rgba(0,0,0,0.85) 100%);
    }}
    .hud-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }}
    .doctor-badge-chip {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      background: rgba(5, 11, 20, 0.85);
      backdrop-filter: blur(10px);
      border: 1px solid var(--cyan-neon);
      padding: 0.5rem 1rem;
      border-radius: var(--radius-pill);
      box-shadow: 0 0 15px rgba(0, 229, 255, 0.2);
    }}
    .verified-check {{
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: var(--cyan-neon);
      color: #000;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      font-size: 0.75rem;
    }}
    .doc-name {{
      font-family: var(--font-display);
      font-size: 0.85rem;
      font-weight: 700;
      color: #ffffff;
      display: block;
    }}
    .doc-sub {{
      font-size: 0.68rem;
      color: var(--cyan-soft);
      display: block;
    }}

    .hud-vital-group {{
      display: flex;
      gap: 0.65rem;
    }}
    .vital-tile {{
      background: rgba(5, 11, 20, 0.85);
      border: 1px solid var(--glass-border);
      padding: 0.4rem 0.75rem;
      border-radius: var(--radius-sm);
      text-align: right;
    }}
    .vital-title {{
      font-family: var(--font-mono);
      font-size: 0.55rem;
      color: var(--text-dim);
      display: block;
    }}
    .vital-stat {{
      font-family: var(--font-mono);
      font-size: 0.8rem;
      font-weight: 700;
    }}
    .text-emerald {{ color: var(--emerald-healing); }}
    .text-cyan {{ color: var(--cyan-neon); }}

    /* Live Voice Waveform Bar */
    .waveform-hud {{
      align-self: center;
      display: flex;
      align-items: center;
      gap: 3px;
      height: 30px;
      padding: 0.25rem 0.75rem;
      background: rgba(0, 0, 0, 0.6);
      border-radius: var(--radius-pill);
      border: 1px solid var(--glass-border);
    }}
    .wave-bar {{
      width: 3px;
      background: var(--cyan-neon);
      border-radius: 3px;
      height: 6px;
      transition: height 0.1s ease;
    }}

    /* Subtitles Container */
    .subtitles-hud-card {{
      background: rgba(5, 11, 20, 0.88);
      border: 1px solid rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(12px);
      border-radius: var(--radius-md);
      padding: 0.85rem 1.25rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }}
    .sub-lang-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.45rem;
    }}
    .sub-label {{
      font-family: var(--font-mono);
      font-size: 0.65rem;
      color: var(--cyan-neon);
      font-weight: 700;
    }}
    .lang-chips {{
      display: flex;
      gap: 0.35rem;
    }}
    .lang-chip {{
      background: rgba(255, 255, 255, 0.08);
      border: none;
      color: var(--text-muted);
      font-family: var(--font-mono);
      font-size: 0.65rem;
      font-weight: 600;
      padding: 0.2rem 0.6rem;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .lang-chip.active {{
      background: var(--cyan-neon);
      color: #000;
      font-weight: 700;
    }}
    .sub-text-rendered {{
      font-size: 0.95rem;
      line-height: 1.45;
      color: #ffffff;
      font-weight: 500;
      text-shadow: 0 2px 4px rgba(0,0,0,0.9);
    }}

    /* Player Controls */
    .video-timeline-bar {{
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-top: 0.65rem;
    }}
    .ctrl-play-btn {{
      background: var(--cyan-neon);
      color: #000;
      border: none;
      font-family: var(--font-body);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.45rem 1.1rem;
      border-radius: var(--radius-pill);
      cursor: pointer;
      box-shadow: 0 0 15px var(--cyan-glow);
      transition: all 0.2s ease;
    }}
    .ctrl-play-btn:hover {{
      transform: scale(1.04);
      background: #ffffff;
    }}
    .timeline-track {{
      flex: 1;
      height: 6px;
      background: rgba(255, 255, 255, 0.2);
      border-radius: var(--radius-pill);
      position: relative;
      cursor: pointer;
      overflow: hidden;
    }}
    .timeline-progress {{
      height: 100%;
      background: linear-gradient(90deg, var(--cyan-neon), var(--emerald-healing));
      width: 25%;
      border-radius: var(--radius-pill);
      transition: width 0.2s linear;
    }}
    .timeline-stamp {{
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    /* Chapters */
    .chapter-cards-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 0.75rem;
      margin-top: 1rem;
    }}
    .chapter-tile {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-md);
      padding: 0.75rem;
      cursor: pointer;
      text-align: left;
      transition: all 0.2s ease;
    }}
    .chapter-tile:hover {{
      background: rgba(255, 255, 255, 0.08);
    }}
    .chapter-tile.active {{
      background: rgba(0, 229, 255, 0.15);
      border-color: var(--cyan-neon);
      box-shadow: 0 0 15px rgba(0, 229, 255, 0.15);
    }}
    .chapter-tile .ch-idx {{
      font-family: var(--font-mono);
      font-size: 0.7rem;
      color: var(--cyan-neon);
      font-weight: 700;
    }}
    .chapter-tile strong {{
      display: block;
      font-size: 0.78rem;
      color: #ffffff;
      margin: 0.2rem 0;
    }}
    .chapter-tile p {{
      font-size: 0.68rem;
      color: var(--text-dim);
    }}

    /* Clinical Sidebar */
    .clinical-meta-pane {{
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 1.5rem;
    }}
    .clinical-headline {{
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--cyan-neon);
      letter-spacing: 0.06em;
      margin-bottom: 0.5rem;
    }}
    .hero-stat-card {{
      background: linear-gradient(135deg, rgba(0, 229, 255, 0.1), rgba(16, 185, 129, 0.1));
      border: 1px solid rgba(0, 229, 255, 0.25);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      text-align: center;
    }}
    .hero-stat-num {{
      font-family: var(--font-display);
      font-size: 3.2rem;
      font-weight: 800;
      background: linear-gradient(135deg, var(--cyan-neon), var(--emerald-healing));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: block;
      line-height: 1;
      margin-bottom: 0.5rem;
    }}
    .hero-stat-sub {{
      font-size: 0.8rem;
      color: var(--text-sub);
      line-height: 1.4;
    }}

    .whatsapp-conversion-btn {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.6rem;
      background: #25d366;
      color: #000;
      font-family: var(--font-body);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.85rem 1.25rem;
      border-radius: var(--radius-md);
      text-decoration: none;
      box-shadow: 0 4px 20px rgba(37, 211, 102, 0.35);
      transition: all 0.2s ease;
    }}
    .whatsapp-conversion-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 25px rgba(37, 211, 102, 0.5);
    }}

    /* ==========================================================
       TAB 3: 10-MINUTE SENIOR MORNING ROUTINE PLAYER
       ========================================================== */
    .routine-stage-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 2rem;
    }}
    .routine-screen-frame {{
      position: relative;
      aspect-ratio: 16 / 9;
      background: #000;
      border-radius: var(--radius-lg);
      overflow: hidden;
      border: 1px solid var(--glass-border);
      box-shadow: var(--shadow-cryo);
    }}
    .routine-bg-photo {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      filter: brightness(0.82);
    }}
    .routine-hud-content {{
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 1.5rem;
      background: linear-gradient(180deg, rgba(0,0,0,0.65) 0%, transparent 35%, rgba(0,0,0,0.9) 100%);
    }}
    .routine-top-hud {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .phase-pill-chip {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
      background: rgba(5, 11, 20, 0.85);
      backdrop-filter: blur(10px);
      padding: 0.45rem 1rem;
      border-radius: var(--radius-pill);
      border: 1px solid rgba(16, 185, 129, 0.4);
    }}
    .phase-indicator-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--emerald-healing);
      box-shadow: 0 0 10px var(--emerald-healing);
    }}
    .phase-chip-title {{
      font-family: var(--font-display);
      font-size: 0.85rem;
      font-weight: 700;
      color: #ffffff;
    }}
    .clock-hud-box {{
      background: rgba(5, 11, 20, 0.85);
      border: 1px solid rgba(16, 185, 129, 0.4);
      padding: 0.4rem 1rem;
      border-radius: var(--radius-md);
      text-align: center;
    }}
    .clock-digits {{
      font-family: var(--font-mono);
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--emerald-healing);
      line-height: 1;
      display: block;
    }}
    .clock-sub {{
      font-family: var(--font-mono);
      font-size: 0.55rem;
      color: var(--text-dim);
    }}

    .cue-floating-pill {{
      align-self: center;
      background: rgba(10, 21, 38, 0.95);
      border: 1px solid var(--cyan-neon);
      backdrop-filter: blur(16px);
      padding: 0.85rem 2rem;
      border-radius: var(--radius-pill);
      color: #ffffff;
      font-size: 0.95rem;
      font-weight: 600;
      text-align: center;
      max-width: 85%;
      box-shadow: 0 0 30px var(--cyan-glow);
    }}

    .vital-telemetry-row {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
    }}
    .gauge-tile {{
      background: rgba(5, 11, 20, 0.85);
      border: 1px solid var(--glass-border);
      backdrop-filter: blur(10px);
      padding: 0.65rem 0.85rem;
      border-radius: var(--radius-sm);
    }}
    .gauge-lbl {{
      font-family: var(--font-mono);
      font-size: 0.6rem;
      color: var(--text-dim);
      margin-bottom: 0.3rem;
      display: block;
    }}
    .gauge-bar-outer {{
      height: 6px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: var(--radius-pill);
      overflow: hidden;
      margin-bottom: 0.3rem;
    }}
    .gauge-bar-inner {{
      height: 100%;
      border-radius: var(--radius-pill);
    }}
    .fill-emerald {{ background: var(--emerald-healing); }}
    .fill-cyan {{ background: var(--cyan-neon); }}
    .fill-purple {{ background: var(--purple-royal); }}
    .gauge-val-text {{
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 700;
      color: #ffffff;
    }}

    .routine-btn-bar {{
      display: flex;
      justify-content: center;
      gap: 0.75rem;
      margin-top: 0.65rem;
    }}
    .routine-action-btn {{
      background: linear-gradient(135deg, var(--emerald-healing), #059669);
      color: #ffffff;
      border: none;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.6rem 1.5rem;
      border-radius: var(--radius-pill);
      cursor: pointer;
      box-shadow: 0 0 15px var(--emerald-glow);
      transition: all 0.2s ease;
    }}
    .routine-action-btn:hover {{ transform: scale(1.03); }}
    .routine-sub-btn {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--glass-border);
      color: #ffffff;
      font-size: 0.8rem;
      padding: 0.6rem 1.1rem;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .routine-sub-btn:hover {{ background: rgba(255, 255, 255, 0.15); }}

    /* Routine Guide Sidebar */
    .protocol-guide-pane {{
      padding: 1.75rem;
    }}
    .protocol-guide-pane h3 {{
      font-family: var(--font-display);
      font-size: 1.15rem;
      color: #ffffff;
      margin-bottom: 0.25rem;
    }}
    .guide-item {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-md);
      padding: 1rem;
      margin-bottom: 0.75rem;
      transition: all 0.2s ease;
    }}
    .guide-item.active {{
      background: rgba(16, 185, 129, 0.12);
      border-color: var(--emerald-healing);
      box-shadow: 0 0 20px var(--emerald-glow);
    }}
    .guide-item .time-tag {{
      font-family: var(--font-mono);
      font-size: 0.65rem;
      color: var(--cyan-neon);
      background: rgba(0, 229, 255, 0.1);
      padding: 0.15rem 0.5rem;
      border-radius: var(--radius-sm);
      margin-bottom: 0.35rem;
      display: inline-block;
    }}
    .guide-item strong {{
      display: block;
      color: #ffffff;
      font-size: 0.85rem;
      margin-bottom: 0.25rem;
    }}
    .guide-item p {{
      font-size: 0.75rem;
      color: var(--text-muted);
      line-height: 1.4;
    }}

    .inbox-qr-card {{
      display: flex;
      align-items: center;
      gap: 1rem;
      background: rgba(0, 229, 255, 0.06);
      border: 1px dashed rgba(0, 229, 255, 0.35);
      border-radius: var(--radius-md);
      padding: 1rem;
      margin-top: 1.5rem;
    }}
    .qr-badge-mock {{
      font-family: var(--font-mono);
      font-size: 0.8rem;
      font-weight: 800;
      background: #000;
      color: var(--cyan-neon);
      border: 1px solid var(--cyan-neon);
      padding: 0.65rem;
      border-radius: var(--radius-sm);
    }}
    .qr-text-info strong {{
      color: #ffffff;
      font-size: 0.85rem;
      display: block;
    }}
    .qr-text-info p {{
      color: var(--text-dim);
      font-size: 0.72rem;
    }}

    /* ==========================================================
       TAB 4: PRICING, CAREGIVER ROI & BOARDROOM SOW GENERATOR
       ========================================================== */
    .calculator-layout {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
    }}
    .calculator-pane, .sow-contract-pane {{
      padding: 2rem;
    }}
    .calc-slider-card {{
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      margin-bottom: 2rem;
    }}
    .slider-tile label {{
      display: flex;
      justify-content: space-between;
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-bottom: 0.5rem;
    }}
    .slider-tile strong {{
      font-family: var(--font-mono);
      color: #ffffff;
      font-size: 0.95rem;
    }}
    input[type=range] {{
      width: 100%;
      height: 6px;
      background: rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-pill);
      outline: none;
      -webkit-appearance: none;
    }}
    input[type=range]::-webkit-slider-thumb {{
      -webkit-appearance: none;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: var(--cyan-neon);
      box-shadow: 0 0 15px var(--cyan-neon);
      cursor: pointer;
      transition: transform 0.15s ease;
    }}
    input[type=range]::-webkit-slider-thumb:hover {{
      transform: scale(1.25);
    }}

    .roi-output-matrix {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      background: rgba(5, 11, 20, 0.8);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      text-align: center;
    }}
    .roi-output-tile .lbl {{
      font-family: var(--font-mono);
      font-size: 0.65rem;
      color: var(--text-dim);
      display: block;
      margin-bottom: 0.25rem;
    }}
    .roi-output-tile .val {{
      font-family: var(--font-display);
      font-size: 1.6rem;
      font-weight: 800;
    }}
    .roi-featured {{
      background: rgba(0, 229, 255, 0.08);
      border-radius: var(--radius-sm);
      border: 1px solid rgba(0, 229, 255, 0.25);
      padding: 0.5rem;
    }}

    /* SOW Agreement Card */
    .sow-tier-select {{
      background: linear-gradient(135deg, rgba(26, 54, 93, 0.4), rgba(139, 92, 246, 0.18));
      border: 1px solid var(--purple-royal);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      box-shadow: 0 0 30px rgba(139, 92, 246, 0.2);
      position: relative;
      margin-bottom: 1.5rem;
    }}
    .sow-badge-rec {{
      position: absolute;
      top: -12px;
      right: 1.5rem;
      background: var(--purple-royal);
      color: #ffffff;
      font-family: var(--font-mono);
      font-size: 0.68rem;
      font-weight: 800;
      padding: 0.25rem 0.85rem;
      border-radius: var(--radius-pill);
    }}
    .sow-plan-title {{
      font-family: var(--font-display);
      font-size: 1.25rem;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 0.35rem;
    }}
    .sow-price-row {{
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
      margin-bottom: 0.25rem;
    }}
    .sow-main-price {{
      font-family: var(--font-display);
      font-size: 2.2rem;
      font-weight: 800;
      color: #ffffff;
    }}
    .sow-main-price span {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 400;
    }}
    .sow-commission-pill {{
      font-family: var(--font-mono);
      font-size: 0.9rem;
      color: var(--emerald-healing);
      font-weight: 700;
      margin-bottom: 1.25rem;
    }}
    .sow-feature-checklist {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
    }}
    .sow-feature-checklist li {{
      font-size: 0.825rem;
      color: var(--text-sub);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .sow-feature-checklist li span {{
      color: var(--cyan-neon);
      font-weight: bold;
    }}

    .btn-sow-execute {{
      width: 100%;
      background: linear-gradient(135deg, var(--cyan-neon), #0284c7);
      color: #000;
      font-family: var(--font-body);
      font-size: 1rem;
      font-weight: 800;
      padding: 1.1rem;
      border: none;
      border-radius: var(--radius-pill);
      cursor: pointer;
      box-shadow: 0 4px 25px var(--cyan-glow);
      transition: all 0.25s ease;
    }}
    .btn-sow-execute:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 35px var(--cyan-glow);
      background: #ffffff;
    }}

    /* Agreement Modal */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(5, 11, 20, 0.9);
      backdrop-filter: blur(20px);
      z-index: 99999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 2rem;
    }}
    .modal-backdrop.open {{
      display: flex;
      animation: modalFade 0.25s ease-out;
    }}
    @keyframes modalFade {{
      from {{ opacity: 0; transform: scale(0.95); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}
    .modal-sheet {{
      background: #0a1526;
      border: 1px solid var(--cyan-neon);
      border-radius: var(--radius-xl);
      max-width: 680px;
      width: 100%;
      padding: 2.5rem;
      box-shadow: 0 25px 70px rgba(0,0,0,0.9), 0 0 40px var(--cyan-glow);
      position: relative;
    }}
    .modal-close-btn {{
      position: absolute;
      top: 1.5rem;
      right: 1.5rem;
      background: rgba(255,255,255,0.1);
      border: none;
      color: #fff;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-weight: bold;
    }}
    .modal-header h2 {{
      font-family: var(--font-display);
      font-size: 1.6rem;
      color: #ffffff;
      margin-bottom: 0.25rem;
    }}
    .modal-header p {{
      font-size: 0.85rem;
      color: var(--cyan-soft);
      margin-bottom: 1.5rem;
    }}
    .contract-summary-box {{
      background: rgba(5, 11, 20, 0.85);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      margin-bottom: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-sub);
      line-height: 1.6;
    }}
    .contract-summary-box table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 0.5rem;
    }}
    .contract-summary-box td {{
      padding: 0.4rem 0;
      border-bottom: 1px solid rgba(255,255,255,0.06);
    }}
    .contract-summary-box td:first-child {{
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--text-dim);
    }}
    .contract-summary-box td:last-child {{
      font-weight: 700;
      color: #ffffff;
      text-align: right;
    }}
    .modal-actions {{
      display: flex;
      gap: 1rem;
    }}
    .modal-btn-print {{
      flex: 1;
      background: var(--cyan-neon);
      color: #000;
      font-weight: 700;
      border: none;
      padding: 0.85rem;
      border-radius: var(--radius-pill);
      cursor: pointer;
    }}

    /* Toast Notification */
    .toast-pill {{
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: #0f223d;
      border: 1px solid var(--cyan-neon);
      color: #ffffff;
      padding: 0.85rem 1.4rem;
      border-radius: var(--radius-pill);
      display: flex;
      align-items: center;
      gap: 0.65rem;
      font-size: 0.85rem;
      font-weight: 600;
      box-shadow: 0 10px 35px rgba(0, 0, 0, 0.7), 0 0 20px var(--cyan-glow);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 999999;
    }}
    .toast-pill.show {{
      transform: translateY(0);
      opacity: 1;
    }}
    .toast-icon {{
      background: var(--cyan-neon);
      color: #000;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: bold;
    }}

    @media (max-width: 1024px) {{
      .audit-split, .video-studio-grid, .routine-stage-grid, .calculator-layout {{
        grid-template-columns: 1fr;
      }}
      .chapter-cards-grid {{
        grid-template-columns: 1fr 1fr;
      }}
      .header-inner {{
        flex-direction: column;
        align-items: flex-start;
      }}
    }}
  </style>
</head>
<body>

  <!-- MASTER EXECUTIVE HEADER -->
  <header class="master-header">
    <div class="header-inner">
      <div class="brand-group">
        <div class="pulsing-orb"></div>
        <div>
          <span class="brand-title">CHANGE MEE</span>
          <span class="brand-tag">MEDICAL BIO-ENGINEERING</span>
        </div>
      </div>

      <!-- High-End Navigation Pills -->
      <nav class="tab-nav-bar" id="tabNavBar">
        <button class="nav-pill active" data-tab="tab-audit" id="navAudit">
          <span class="num">01</span>
          <span>Digital Audit ("Toys" Trap)</span>
        </button>
        <button class="nav-pill" data-tab="tab-video" id="navVideo">
          <span class="num">02</span>
          <span>Doctor Broadcast Video</span>
        </button>
        <button class="nav-pill" data-tab="tab-routine" id="navRoutine">
          <span class="num">03</span>
          <span>10-Min Senior Routine</span>
        </button>
        <button class="nav-pill" data-tab="tab-calculator" id="navCalc">
          <span class="num">04</span>
          <span>ROI Funnel & SOW Terms</span>
        </button>
      </nav>

      <!-- Action Utilities -->
      <div class="header-ctrls">
        <span class="badge-live">Boardroom Pitch Live</span>
        <button class="pill-btn" id="audioToggle">
          <span id="audioIcon">🔊</span> Audio FX
        </button>
        <button class="pill-btn" id="btnFullscreen">⛶ Fullscreen</button>
      </div>
    </div>
  </header>

  <!-- MAIN VIEWPORT -->
  <main class="main-wrap">

    <!-- ==================== TAB 1: FORENSIC DIGITAL AUDIT ==================== -->
    <section class="tab-section active" id="tab-audit">
      <div class="sec-hero">
        <div class="eyebrow-badge eyebrow-alert">CRITICAL COMMERCIAL AUDIT • LIVE BOTTLENECK</div>
        <h1 class="sec-title">The "Toys & Games" Category Trap vs. ₹43,000 Medical Longevity Platform</h1>
        <p class="sec-desc">Mr. Kalkunde, Change Mee manufactures German-grade 304 stainless steel rehabilitation hardware in Kolhapur, but your current digital presence devalues it into a children's toy. Here is why online sales are blocked today—and how we fix it immediately.</p>
      </div>

      <div class="audit-split">
        <!-- Live Problem Card -->
        <div class="cryo-card audit-pane">
          <div class="audit-top-bar">
            <h3>CURRENT LIVE REALITY (changemee.in)</h3>
            <span class="audit-tag-danger">Leaking ₹43k Value</span>
          </div>

          <div class="browser-mock">
            <div class="browser-dots">
              <span class="b-dot b-red"></span>
              <span class="b-dot b-yellow"></span>
              <span class="b-dot b-green"></span>
              <span class="b-url">https://changemee.in/index.php?route=product/category&path=224</span>
            </div>
            <div class="mock-body">
              <div class="mock-alert">
                <span style="font-size:1.3rem;">⚠️</span>
                <div>
                  <strong>Storefront Category: Toys & Games</strong>
                  <span>Product SKU: CHANGEMEYELLOWR (44" Rebounder)</span>
                </div>
              </div>

              <ul class="check-list">
                <li><span class="icon-fail">✕</span> <strong>Categorized under "Toys & Games"</strong> next to cheap plastic recreational items.</li>
                <li><span class="icon-fail">✕</span> <strong>Severe Price Sticker Shock:</strong> When a 65-year-old or orthopedic doctor sees a ₹30,000–₹43,000 price on a "toy", they bounce in 5 seconds.</li>
                <li><span class="icon-fail">✕</span> <strong>Mobile App Zero Traction:</strong> Android app built with zero conversion funnel or download loop.</li>
                <li><span class="icon-fail">✕</span> <strong>Scraped on Marketplaces:</strong> Desertcart and aggregators scrape raw unbranded data without A+ content.</li>
                <li><span class="icon-fail">✕</span> <strong>Under-Leveraged Clinical Gold:</strong> Dr. Sanjay Gaikwad's recovery video sits raw on YouTube with zero ad funnel.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Future State Hotspot Explorer -->
        <div class="cryo-card audit-pane">
          <div class="audit-top-bar">
            <h3>STRATEGIC TARGET STATE (Interactive Hotspot Model)</h3>
            <span class="audit-tag-success">Unlocks ₹43,000 MSRP</span>
          </div>

          <!-- Interactive Hotspot Container -->
          <div class="hero-hotspot-container">
            <img src="{hero_b64}" alt="Change Mee Medical Rebounder" class="hero-hotspot-img">
            
            <!-- Hotspot Pins -->
            <div class="hotspot-pin" style="top: 25%; left: 65%;" data-spot="tbar">1</div>
            <div class="hotspot-pin" style="top: 72%; left: 40%;" data-spot="frame">2</div>
            <div class="hotspot-pin" style="top: 60%; left: 70%;" data-spot="bungees">3</div>
            <div class="hotspot-pin" style="top: 65%; left: 52%;" data-spot="mat">4</div>

            <!-- Hotspot Cards -->
            <div class="hotspot-card" id="card-tbar" style="top: 10%; left: 35%;">
              <strong>T-BAR STABILITY SYSTEM</strong>
              Rigid dual-support stainless steel handlebar eliminates ptophobia (fear of falling) for seniors with neuropathy.
            </div>
            <div class="hotspot-card" id="card-frame" style="top: 45%; left: 10%;">
              <strong>304 STAINLESS STEEL CHASSIS</strong>
              Commercial-grade 6-leg architecture supports up to 140 kg with zero wobble, flexing, or coastal rust.
            </div>
            <div class="hotspot-card" id="card-bungees" style="top: 35%; left: 45%;">
              <strong>36 PROGRESSIVE BUNGEES</strong>
              Extends deceleration time (Δt ≈ 0.20s), eliminating 85% of downward shock vs harsh steel springs.
            </div>
            <div class="hotspot-card" id="card-mat" style="top: 40%; left: 25%;">
              <strong>WOVEN POLYPROPYLENE MAT</strong>
              High-tensile, low-friction landing surface prevents diabetic shear blisters during grounded health bounce.
            </div>
          </div>

          <ul class="check-list">
            <li><span class="icon-pass">✓</span> <strong>Reclassified as Medical Mobility Platform:</strong> Justifies the investment as a knee surgery alternative.</li>
            <li><span class="icon-pass">✓</span> <strong>Official Amazon Brand Registry:</strong> 7-image clinical stack, medical bullets, and A+ comparison charts.</li>
            <li><span class="icon-pass">✓</span> <strong>15-Day Risk-Free In-Home Mobility Trial:</strong> Eliminates caregiver hesitation completely.</li>
          </ul>
        </div>
      </div>

      <!-- Bottom Next CTA Banner -->
      <div class="cryo-card" style="padding: 1.5rem 2rem; display: flex; align-items: center; justify-content: space-between; border-color: var(--cyan-neon);">
        <div>
          <h4 style="font-family: var(--font-display); font-size: 1.15rem; color:#fff; margin-bottom: 0.2rem;">Next Demonstration: The Remastered Doctor Case Study Video</h4>
          <p style="color: var(--text-muted); font-size: 0.85rem;">See how Dr. Sanjay Gaikwad's authentic testimony is transformed into a high-trust broadcast asset.</p>
        </div>
        <button class="btn-sow-execute" style="width: auto; padding: 0.75rem 1.75rem;" id="btnSwitchToVideo">Watch Doctor Video Demo →</button>
      </div>
    </section>

    <!-- ==================== TAB 2: REMASTERED DOCTOR BROADCAST VIDEO ==================== -->
    <section class="tab-section" id="tab-video">
      <div class="sec-hero">
        <div class="eyebrow-badge eyebrow-clinical">CLINICAL AUTHORITY ASSET • DR. SANJAY GAIKWAD CASE STUDY</div>
        <h1 class="sec-title">Broadcast Video Remastering: High-Trust Physician Testimonial</h1>
        <p class="sec-desc">Caregiver adult children (Ages 38–58) are wary of fitness gimmicks. When they hear a practicing Kolhapur physician explain his own recovery from Type 2 diabetes and knee stiffness, skepticism turns into immediate purchase urgency.</p>
      </div>

      <div class="video-studio-grid">
        <!-- Video Simulation Screen -->
        <div class="cryo-card" style="padding: 1rem;">
          <div class="video-player-frame">
            <img src="{dr_b64}" alt="Dr. Sanjay Gaikwad" class="video-feed-img" id="docVideoImg">

            <!-- HUD Overlay -->
            <div class="video-overlay-hud">
              <!-- Top HUD -->
              <div class="hud-header">
                <div class="doctor-badge-chip">
                  <span class="verified-check">✓</span>
                  <div>
                    <span class="doc-name">Dr. Sanjay Gaikwad, M.B.B.S.</span>
                    <span class="doc-sub">Practicing Physician & Chronic Patient • Kolhapur</span>
                  </div>
                </div>

                <div class="hud-vital-group">
                  <div class="vital-tile">
                    <span class="vital-title">JOINT SHOCK</span>
                    <span class="vital-stat text-emerald">-85% IMPACT</span>
                  </div>
                  <div class="vital-tile">
                    <span class="vital-title">AMPK PATHWAY</span>
                    <span class="vital-stat text-cyan">ACTIVE GLUCOSE</span>
                  </div>
                </div>
              </div>

              <!-- Audio Waveform Visualizer -->
              <div class="waveform-hud" id="voiceWaveform">
                <div class="wave-bar" style="height: 12px;"></div>
                <div class="wave-bar" style="height: 24px;"></div>
                <div class="wave-bar" style="height: 8px;"></div>
                <div class="wave-bar" style="height: 18px;"></div>
                <div class="wave-bar" style="height: 28px;"></div>
                <div class="wave-bar" style="height: 14px;"></div>
                <div class="wave-bar" style="height: 20px;"></div>
                <div class="wave-bar" style="height: 10px;"></div>
                <span style="font-family: var(--font-mono); font-size: 0.6rem; color: var(--cyan-neon); margin-left: 0.35rem;">DR. GAIKWAD AUDIO TRACK</span>
              </div>

              <!-- Subtitles Card -->
              <div class="subtitles-hud-card">
                <div class="sub-lang-row">
                  <span class="sub-label">BROADCAST SUBTITLES</span>
                  <div class="lang-chips">
                    <button class="lang-chip active" data-lang="en">English</button>
                    <button class="lang-chip" data-lang="hi">हिंदी (Hindi)</button>
                    <button class="lang-chip" data-lang="mr">मराठी (Original)</button>
                  </div>
                </div>
                <p class="sub-text-rendered" id="docSubText">
                  "When I searched online for exercise and rehabilitation, Change Mee caught my attention. The complaints I had in my hands, legs, diabetes, blood pressure, and heart stiffness have resolved since using this protocol."
                </p>
              </div>

              <!-- Video Scrubber Controls -->
              <div class="video-timeline-bar">
                <button class="ctrl-play-btn" id="btnPlayDoc">▶ Play Segment</button>
                <div class="timeline-track" id="docScrubberTrack">
                  <div class="timeline-progress" id="docProgress" style="width: 20%;"></div>
                </div>
                <span class="timeline-stamp" id="docTimecode">01:15 / 05:45</span>
              </div>
            </div>
          </div>

          <!-- Video Chapter Tiles -->
          <div class="chapter-cards-grid">
            <div class="chapter-tile active" data-ch="1">
              <span class="ch-idx">CH 01</span>
              <strong>Medical Profile & Symptoms</strong>
              <p>Type 2 Diabetes, Walking Pain & Stiffness</p>
            </div>
            <div class="chapter-tile" data-ch="2">
              <span class="ch-idx">CH 02</span>
              <strong>Biomechanical Deceleration</strong>
              <p>Why Outdoor Footstrikes Damaged Knees</p>
            </div>
            <div class="chapter-tile" data-ch="3">
              <span class="ch-idx">CH 03</span>
              <strong>Soleus Muscle AMPK Pump</strong>
              <p>Blood Sugar Clearance Without Insulin</p>
            </div>
            <div class="chapter-tile" data-ch="4">
              <span class="ch-idx">CH 04</span>
              <strong>Physician's Recommendation</strong>
              <p>Why Every Indian Household Needs This</p>
            </div>
          </div>
        </div>

        <!-- Sidebar Conversion Card -->
        <div class="cryo-card clinical-meta-pane">
          <div>
            <div class="clinical-headline">WHY THIS ASSET CONVERTS CAREGIVERS</div>
            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 1.25rem;">
              Adult sons and daughters looking for knee surgery alternatives respond instantly to peer medical authority. Dr. Gaikwad’s story bridges the gap between raw hardware and an orthopedic health investment.
            </p>

            <div class="hero-stat-card">
              <span class="hero-stat-num">3.8x</span>
              <span class="hero-stat-sub">Higher Meta Ad Click-Through & Conversion Rate when anchored by Dr. Gaikwad's video.</span>
            </div>
          </div>

          <div>
            <h4 style="font-family: var(--font-display); font-size: 1rem; color:#fff; margin-bottom: 0.35rem;">Direct WhatsApp Clinical Concierge</h4>
            <p style="font-size: 0.75rem; color: var(--text-dim); margin-bottom: 0.85rem;">Every video ad directly connects caregivers to Change Mee's clinical team for free parent mobility advice.</p>
            <a href="https://wa.me/919876543210?text=Hello%20Change%20Mee,%20I%20saw%20Dr.%20Gaikwad's%20case%20study%20and%20want%20to%20know%20if%20this%20is%20safe%20for%20my%20parents" target="_blank" class="whatsapp-conversion-btn">
              <span>💬</span> Chat with Clinical Physio on WhatsApp
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== TAB 3: 10-MIN SENIOR MORNING ROUTINE ==================== -->
    <section class="tab-section" id="tab-routine">
      <div class="sec-hero">
        <div class="eyebrow-badge eyebrow-routine">PATIENT ONBOARDING EXPERIENCE • IN-BOX STREAMING</div>
        <h1 class="sec-title">The 10-Minute Follow-Along Morning Routine for Seniors</h1>
        <p class="sec-desc">Indian elders do not need to jump. Soles remain safely planted on the mat while the 36 bungees absorb 85% of downward shock and activate the soleus calf pump—delivering 45 minutes of walking benefits in 10 minutes at home.</p>
      </div>

      <div class="routine-stage-grid">
        <!-- Interactive Routine Stage -->
        <div class="cryo-card" style="padding: 1rem;">
          <div class="routine-screen-frame">
            <img src="{senior_b64}" alt="Senior Morning Routine" class="routine-bg-photo">

            <div class="routine-hud-content">
              <!-- Top HUD -->
              <div class="routine-top-hud">
                <div class="phase-pill-chip">
                  <span class="phase-indicator-dot"></span>
                  <span class="phase-chip-title" id="routinePhaseTitle">PHASE 1: THE GROUNDED HEALTH BOUNCE</span>
                </div>
                <div class="clock-hud-box">
                  <span class="clock-digits" id="routineClock">10:00</span>
                  <span class="clock-sub">REMAINING</span>
                </div>
              </div>

              <!-- Cue Pill -->
              <div class="cue-floating-pill" id="routineCue">
                "Hands firmly on T-Bar. Soften your knees. Gently push into the mat without lifting your soles."
              </div>

              <!-- Telemetry Gauges -->
              <div class="vital-telemetry-row">
                <div class="gauge-tile">
                  <span class="gauge-lbl">JOINT SHOCK ABSORPTION</span>
                  <div class="gauge-bar-outer">
                    <div class="gauge-bar-inner fill-emerald" style="width: 85%;"></div>
                  </div>
                  <span class="gauge-val-text">85% Shock Absorption</span>
                </div>
                <div class="gauge-tile">
                  <span class="gauge-lbl">LYMPH VALVE CYCLING</span>
                  <div class="gauge-bar-outer">
                    <div class="gauge-bar-inner fill-cyan" id="lymphBar" style="width: 65%;"></div>
                  </div>
                  <span class="gauge-val-text" id="lymphText">110 Oscillations / Min</span>
                </div>
                <div class="gauge-tile">
                  <span class="gauge-lbl">FALL RISK (PTOPHOBIA)</span>
                  <div class="gauge-bar-outer">
                    <div class="gauge-bar-inner fill-purple" style="width: 0%;"></div>
                  </div>
                  <span class="gauge-val-text">0% Fall Risk (T-Bar Dual Support)</span>
                </div>
              </div>

              <!-- Control Buttons -->
              <div class="routine-btn-bar">
                <button class="routine-action-btn" id="btnToggleRoutine">▶ Start Morning Routine</button>
                <button class="routine-sub-btn" id="btnNextPhase">Next Phase →</button>
                <button class="routine-sub-btn" id="btnResetClock">↺ Reset</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Protocol Guide Sidebar -->
        <div class="cryo-card protocol-guide-pane">
          <h3>THE 3-PHASE GERIATRIC PROTOCOL</h3>
          <p style="font-size: 0.8rem; color: var(--text-dim); margin-bottom: 1.25rem;">Physician-prescribed for osteoarthritis, balance recovery, and diabetic edema:</p>

          <div class="guide-item active" id="guidePhase1">
            <span class="time-tag">00:00 – 03:00</span>
            <strong>Phase 1: Grounded Health Bounce</strong>
            <p>Soles never leave the woven mat. Gentle rhythmic knee flexes cycle lymphatic valves in the lower legs to drain morning swelling.</p>
          </div>

          <div class="guide-item" id="guidePhase2">
            <span class="time-tag">03:00 – 07:00</span>
            <strong>Phase 2: Alternating Soleus Pump</strong>
            <p>Gently lifting alternate heels while toes remain anchored. Activates the 'second heart' calf muscle to clear post-meal glucose.</p>
          </div>

          <div class="guide-item" id="guidePhase3">
            <span class="time-tag">07:00 – 10:00</span>
            <strong>Phase 3: Diaphragmatic Breath Down</strong>
            <p>Deep rhythmic breathing with minimal bounce. Decompresses lumbar discs, resets dynamic equilibrium, and lowers cortisol.</p>
          </div>

          <div class="inbox-qr-card">
            <span class="qr-badge-mock">📱 QR CODE</span>
            <div class="qr-text-info">
              <strong>Printed Inside Every Rebounder Box</strong>
              <p>Customers scan with their phone or TV on Day 1 for instant follow-along guidance.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== TAB 4: PRICING, CAREGIVER ROI & BOARDROOM SOW ==================== -->
    <section class="tab-section" id="tab-calculator">
      <div class="sec-hero">
        <div class="eyebrow-badge eyebrow-roi">FINANCIAL ECONOMICS • BOARDROOM EXECUTION</div>
        <h1 class="sec-title">The ₹43,000 Justification & Boardroom Partnership Sign-Off</h1>
        <p class="sec-desc">How to justify the ₹43,000 investment to Indian households: it is not a ₹4,000 toy trampoline—it is an economic alternative to knee replacement surgery and monthly clinic visits, with a complete 90-day growth partnership for Change Mee.</p>
      </div>

      <div class="calculator-layout">
        <!-- Interactive ROI Tool -->
        <div class="cryo-card calculator-pane">
          <h3 style="font-family: var(--font-display); font-size: 1.25rem; color:#fff; margin-bottom: 0.25rem;">CAREGIVER HOUSEHOLD ROI CALCULATOR</h3>
          <p style="font-size: 0.8rem; color: var(--text-dim); margin-bottom: 1.5rem;">Adjust sliders to calculate avoided outpatient and surgical expenses:</p>

          <div class="calc-slider-card">
            <div class="slider-tile">
              <label>Monthly Physiotherapy & Pain Clinic Fees: <strong id="lblPhysio">₹6,000</strong></label>
              <input type="range" id="inputPhysio" min="2000" max="15000" step="500" value="6000">
            </div>
            <div class="slider-tile">
              <label>Knee Replacement Surgery Risk (Per Knee): <strong id="lblKnee">₹3,50,000</strong></label>
              <input type="range" id="inputKnee" min="200000" max="600000" step="25000" value="350000">
            </div>
            <div class="slider-tile">
              <label>Generations Using the Apparatus: <strong id="lblUsers">3 Generations</strong></label>
              <input type="range" id="inputUsers" min="1" max="5" step="1" value="3">
            </div>
          </div>

          <div class="roi-output-matrix">
            <div class="roi-output-tile">
              <span class="lbl">1-Year Avoided Fees</span>
              <span class="val text-emerald" id="outYearSavings">₹72,000</span>
            </div>
            <div class="roi-output-tile">
              <span class="lbl">Change Mee 1-Time</span>
              <span class="val" style="color:#ffffff;">₹43,000</span>
            </div>
            <div class="roi-output-tile roi-featured">
              <span class="lbl">Household Payback</span>
              <span class="val text-cyan" id="outPayback">2.4 Months</span>
            </div>
          </div>
        </div>

        <!-- Boardroom SOW Agreement Generator -->
        <div class="cryo-card sow-contract-pane">
          <div class="sow-tier-select">
            <span class="sow-badge-rec">RECOMMENDED PARTNERSHIP</span>
            <h4 class="sow-plan-title">Hybrid Performance Growth Partnership</h4>
            <div class="sow-price-row">
              <span class="sow-main-price">₹55,000 <span>/ month base</span></span>
            </div>
            <div class="sow-commission-pill">+ ₹3,000 per Rebounder Sold (Revenue Share)</div>

            <ul class="sow-feature-checklist">
              <li><span>✓</span> Full Amazon India Brand Registry rewrite & 7-image clinical stack.</li>
              <li><span>✓</span> Dr. Sanjay Gaikwad video remastering (subtitles, B-roll cutaways).</li>
              <li><span>✓</span> Dedicated high-ticket D2C landing page & WhatsApp concierge.</li>
              <li><span>✓</span> Meta & Google Ads management targeting caregiver adult children (38–58).</li>
              <li><span>✓</span> <strong>Direct Skin-in-the-Game:</strong> We scale our revenue when you sell units.</li>
            </ul>
          </div>

          <button class="btn-sow-execute" id="btnOpenContractModal">
            ✓ Generate Official Boardroom SOW Agreement
          </button>
          <p style="text-align: center; font-size: 0.72rem; color: var(--text-dim); margin-top: 0.75rem;">
            Includes 14-day creative approval guarantee. Cancel with zero penalty if assets do not meet standards.
          </p>
        </div>
      </div>
    </section>

  </main>

  <!-- OFFICIAL BOARDROOM SOW AGREEMENT MODAL -->
  <div class="modal-backdrop" id="contractModal">
    <div class="modal-sheet">
      <button class="modal-close-btn" id="btnCloseModal">✕</button>
      <div class="modal-header">
        <h2>COMMERCIAL ENGAGEMENT AGREEMENT</h2>
        <p>Change Mee Physio Pilates Rehabilitation Studio × Strategic Growth Partners</p>
      </div>

      <div class="contract-summary-box">
        <p>This Statement of Work (SOW) formalizes Phase 1 of the <strong>Change Mee Medical Longevity Platform</strong> commercialization architecture as outlined in the 12-Page Master Dossier.</p>
        <table>
          <tr>
            <td>Client / Founder</td>
            <td>Mr. Sanjeev Kalkunde (Change Mee)</td>
          </tr>
          <tr>
            <td>Headquarters</td>
            <td>Kolhapur, Maharashtra</td>
          </tr>
          <tr>
            <td>Hero Product</td>
            <td>ChangeMe 44" Stainless Steel Bungee Rebounder</td>
          </tr>
          <tr>
            <td>Target Retail MSRP</td>
            <td>₹43,000 (Amazon) / ₹30,000 (D2C Ex-Tax)</td>
          </tr>
          <tr>
            <td>Engagement Structure</td>
            <td>Hybrid Performance (Base + Unit Share)</td>
          </tr>
          <tr>
            <td>Monthly Base Retainer</td>
            <td>₹55,000 / month</td>
          </tr>
          <tr>
            <td>Sales Performance Share</td>
            <td>₹3,000 per verified rebounder sale</td>
          </tr>
          <tr>
            <td>Pilot Ad Spend</td>
            <td>₹50,000 / month (Direct Meta/Google ad account)</td>
          </tr>
          <tr>
            <td>Immediate Deliverables</td>
            <td>Amazon 7-Image Stack, Dr. Gaikwad Video Remaster, D2C Funnel</td>
          </tr>
        </table>
      </div>

      <div class="modal-actions">
        <button class="modal-btn-print" onclick="window.print()">🖨️ Print / Save Official Agreement (PDF)</button>
        <button class="pill-btn" style="padding: 0.85rem 1.5rem;" id="btnSignContract">✓ Approve & Initiate Phase 1</button>
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div class="toast-pill" id="toastBox">
    <span class="toast-icon">✓</span>
    <span id="toastText">Action executed</span>
  </div>

  <!-- Interactive JavaScript Engine -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      // Web Audio API Sound Feedback
      let audioEnabled = true;
      let audioCtx = null;

      function initAudio() {{
        if (!audioCtx) {{
          audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }}
      }}

      function playTone(freq, type = 'sine', duration = 0.08, gainVal = 0.05) {{
        if (!audioEnabled) return;
        try {{
          initAudio();
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
        }} catch(e) {{}}
      }}

      function playClick() {{ playTone(800, 'sine', 0.04, 0.03); }}
      function playSuccess() {{ playTone(587.33, 'triangle', 0.1, 0.05); setTimeout(() => playTone(880, 'sine', 0.2, 0.05), 80); }}
      function playBounce() {{ playTone(130, 'sine', 0.15, 0.08); }}

      const audioToggle = document.getElementById('audioToggle');
      const audioIcon = document.getElementById('audioIcon');
      if (audioToggle) {{
        audioToggle.addEventListener('click', () => {{
          audioEnabled = !audioEnabled;
          audioIcon.textContent = audioEnabled ? '🔊' : '🔇';
          showToast(audioEnabled ? 'Sound FX Enabled' : 'Sound FX Muted');
          if (audioEnabled) playSuccess();
        }});
      }}

      // Fullscreen Mode
      const btnFullscreen = document.getElementById('btnFullscreen');
      if (btnFullscreen) {{
        btnFullscreen.addEventListener('click', () => {{
          if (!document.fullscreenElement) {{
            document.documentElement.requestFullscreen().catch(err => {{}});
            btnFullscreen.textContent = '✕ Exit Fullscreen';
          }} else {{
            document.exitFullscreen();
            btnFullscreen.textContent = '⛶ Fullscreen';
          }}
          playClick();
        }});
      }}

      // Toast System
      const toastBox = document.getElementById('toastBox');
      const toastText = document.getElementById('toastText');
      let toastTimeout = null;

      function showToast(msg) {{
        if (!toastBox) return;
        toastText.textContent = msg;
        toastBox.classList.add('show');
        clearTimeout(toastTimeout);
        toastTimeout = setTimeout(() => {{
          toastBox.classList.remove('show');
        }}, 2800);
      }}

      // Tab Navigation
      const navPills = document.querySelectorAll('.nav-pill');
      const tabSections = document.querySelectorAll('.tab-section');

      function switchTab(tabId) {{
        navPills.forEach(p => {{
          if (p.getAttribute('data-tab') === tabId) p.classList.add('active');
          else p.classList.remove('active');
        }});
        tabSections.forEach(s => {{
          if (s.id === tabId) s.classList.add('active');
          else s.classList.remove('active');
        }});
        playClick();
      }}

      navPills.forEach(p => {{
        p.addEventListener('click', () => switchTab(p.getAttribute('data-tab')));
      }});

      const btnSwitchToVideo = document.getElementById('btnSwitchToVideo');
      if (btnSwitchToVideo) {{
        btnSwitchToVideo.addEventListener('click', () => switchTab('tab-video'));
      }}

      // Hotspots on Hero
      const pins = document.querySelectorAll('.hotspot-pin');
      pins.forEach(pin => {{
        pin.addEventListener('click', (e) => {{
          e.stopPropagation();
          const spot = pin.getAttribute('data-spot');
          document.querySelectorAll('.hotspot-card').forEach(c => c.classList.remove('active'));
          const targetCard = document.getElementById(`card-${{spot}}`);
          if (targetCard) {{
            targetCard.classList.add('active');
            playSuccess();
          }}
        }});
      }});
      document.addEventListener('click', () => {{
        document.querySelectorAll('.hotspot-card').forEach(c => c.classList.remove('active'));
      }});

      // Tab 2: Doctor Broadcast Video
      const btnPlayDoc = document.getElementById('btnPlayDoc');
      const docProgress = document.getElementById('docProgress');
      const docTimecode = document.getElementById('docTimecode');
      const docSubText = document.getElementById('docSubText');
      const langChips = document.querySelectorAll('.lang-chip');
      const chapterTiles = document.querySelectorAll('.chapter-tile');
      const waveBars = document.querySelectorAll('.wave-bar');

      let isDocPlaying = false;
      let docInterval = null;
      let docPct = 20;
      let curLang = 'en';
      let curCh = 1;

      const subData = {{
        1: {{
          en: '"When I searched online for exercise and rehabilitation, Change Mee caught my attention. The complaints I had in my hands, legs, diabetes, blood pressure, and heart stiffness have resolved since using this protocol."',
          hi: '"जब मैंने व्यायाम और पुनर्वास के लिए ऑनलाइन खोजा, तो चेंज मी ने मेरा ध्यान आकर्षित किया। हाथ, पैर, मधुमेह, रक्तचाप और जकड़न की समस्याएं यहाँ आने के बाद पूरी तरह ठीक हो गईं।"',
          mr: '"जेव्हा मी व्यायाम आणि पुनर्वसनासाठी ऑनलाइन शोध घेतला तेव्हा चेंज मीने लगेचच माझे लक्ष वेधून घेतले. मला हात, पाय, मधुमेह, रक्तदाब आणि हृदयाच्या तक्रारी होत्या त्या येथे आल्यापासून पूर्णपणे दूर झाल्या आहेत."'
        }},
        2: {{
          en: '"As a physician, I know road walking generates 3x body weight in harsh pavement impact. With the 36-cord bungee, my knees experience zero ground footstrike shock."',
          hi: '"एक डॉक्टर के रूप में, मैं जानता हूँ कि सड़क पर चलने से 3 गुना कठोर झटका लगता है। 36 बंजी कॉर्ड्स के साथ, मेरे घुटनों को ज़ीरो झटका लगता है।"',
          mr: '"एक डॉक्टर म्हणून मला माहित आहे की रस्त्यावर चालल्याने शरीराच्या 3 पट धक्का बसतो. 36 बंजी कॉर्डमुळे माझ्या गुडघ्यांना शॉक लागत नाही."'
        }},
        3: {{
          en: '"The grounded bounce contracts the soleus muscle pump—clearing blood glucose directly through AMPK activation without needing high insulin spikes."',
          hi: '"ग्राउंडेड बाउंस सोलियस मांसपेशी को सक्रिय करता है—बिना उच्च इंसुलिन के एएमपीके सक्रियण के माध्यम से रक्त शर्करा को तुरंत साफ करता है।"',
          mr: '"ग्राउंडेड बाउंस सोलियस स्नायूंना सक्रिय करतो—इन्सुलिनच्या स्पाइक्सशिवाय रक्तातील साखर नियंत्रित करतो."'
        }},
        4: {{
          en: '"This is truly a medical gift for any Indian family managing chronic conditions or elderly parent care. It pays for itself in avoided hospital and clinic bills."',
          hi: '"यह किसी भी भारतीय परिवार के लिए एक वास्तविक चिकित्सा उपहार है। यह टाले गए अस्पताल और क्लिनिक के बिलों में अपनी पूरी कीमत वसूल करता है।"',
          mr: '"कोणत्याही भारतीय कुटुंबासाठी ही खरोखरच एक वैद्यकीय देणगी आहे. टाळलेल्या हॉस्पिटलच्या बिलांमधून याची किंमत लगेच वसूल होते."'
        }}
      }};

      function updateDocSub() {{
        if (docSubText && subData[curCh]) {{
          docSubText.textContent = subData[curCh][curLang];
        }}
      }}

      langChips.forEach(chip => {{
        chip.addEventListener('click', () => {{
          langChips.forEach(c => c.classList.remove('active'));
          chip.classList.add('active');
          curLang = chip.getAttribute('data-lang');
          updateDocSub();
          playClick();
          showToast(`Subtitles: ${{chip.textContent}}`);
        }});
      }});

      chapterTiles.forEach(tile => {{
        tile.addEventListener('click', () => {{
          chapterTiles.forEach(t => t.classList.remove('active'));
          tile.classList.add('active');
          curCh = parseInt(tile.getAttribute('data-ch'));
          const chPct = {{ 1: 15, 2: 38, 3: 65, 4: 88 }};
          const chTimes = {{ 1: '00:45', 2: '02:10', 3: '03:45', 4: '05:10' }};
          docPct = chPct[curCh] || 20;
          docProgress.style.width = `${{docPct}}%`;
          docTimecode.textContent = `${{chTimes[curCh]}} / 05:45`;
          updateDocSub();
          playSuccess();
        }});
      }});

      if (btnPlayDoc) {{
        btnPlayDoc.addEventListener('click', () => {{
          isDocPlaying = !isDocPlaying;
          if (isDocPlaying) {{
            btnPlayDoc.textContent = '❚❚ Pause Segment';
            btnPlayDoc.style.background = '#ffffff';
            playSuccess();
            docInterval = setInterval(() => {{
              docPct += 0.5;
              if (docPct >= 100) {{
                docPct = 0;
                curCh = (curCh % 4) + 1;
                const targetTile = document.querySelector(`.chapter-tile[data-ch="${{curCh}}"]`);
                if (targetTile) targetTile.click();
              }}
              docProgress.style.width = `${{docPct}}%`;
              const totalSecs = Math.floor((docPct / 100) * 345);
              const m = String(Math.floor(totalSecs / 60)).padStart(2, '0');
              const s = String(totalSecs % 60).padStart(2, '0');
              docTimecode.textContent = `${{m}}:${{s}} / 05:45`;

              // Waveform animation
              waveBars.forEach(b => {{
                b.style.height = `${{Math.floor(Math.random() * 22) + 6}}px`;
              }});
            }}, 250);
          }} else {{
            btnPlayDoc.textContent = '▶ Play Segment';
            btnPlayDoc.style.background = 'var(--cyan-neon)';
            clearInterval(docInterval);
            playClick();
          }}
        }});
      }}

      // Tab 3: Senior Morning Routine
      const btnToggleRoutine = document.getElementById('btnToggleRoutine');
      const btnNextPhase = document.getElementById('btnNextPhase');
      const btnResetClock = document.getElementById('btnResetClock');
      const routineClock = document.getElementById('routineClock');
      const routinePhaseTitle = document.getElementById('routinePhaseTitle');
      const routineCue = document.getElementById('routineCue');
      const lymphBar = document.getElementById('lymphBar');
      const lymphText = document.getElementById('lymphText');

      let isRoutineOn = false;
      let routineSecs = 600;
      let routineTimerInt = null;
      let curPhase = 1;

      const phaseDict = {{
        1: {{
          title: 'PHASE 1: THE GROUNDED HEALTH BOUNCE',
          cue: '"Hands firmly on T-Bar. Soften your knees. Gently push into the mat without lifting your soles."',
          lymph: '110 Oscillations / Min',
          lymphWidth: '65%',
          guideId: 'guidePhase1'
        }},
        2: {{
          title: 'PHASE 2: ALTERNATING SOLEUS PUMP',
          cue: '"Lift right heel, press down. Lift left heel, press down. Activate your soleus second heart to clear blood sugar."',
          lymph: '135 Oscillations / Min',
          lymphWidth: '88%',
          guideId: 'guidePhase2'
        }},
        3: {{
          title: 'PHASE 3: DIAPHRAGMATIC BREATH DOWN',
          cue: '"Slow your bounce. Inhale deeply through the nose for 4 seconds, exhale slowly. Decompress your lower back."',
          lymph: '75 Oscillations / Min',
          lymphWidth: '45%',
          guideId: 'guidePhase3'
        }}
      }};

      function updatePhaseUI() {{
        const p = phaseDict[curPhase];
        routinePhaseTitle.textContent = p.title;
        routineCue.textContent = p.cue;
        lymphText.textContent = p.lymph;
        lymphBar.style.width = p.lymphWidth;

        ['guidePhase1', 'guidePhase2', 'guidePhase3'].forEach(id => {{
          const el = document.getElementById(id);
          if (el) {{
            if (id === p.guideId) el.classList.add('active');
            else el.classList.remove('active');
          }}
        }});
      }}

      function formatClock(secs) {{
        const m = String(Math.floor(secs / 60)).padStart(2, '0');
        const s = String(secs % 60).padStart(2, '0');
        return `${{m}}:${{s}}`;
      }}

      if (btnToggleRoutine) {{
        btnToggleRoutine.addEventListener('click', () => {{
          isRoutineOn = !isRoutineOn;
          if (isRoutineOn) {{
            btnToggleRoutine.textContent = '❚❚ Pause Routine';
            btnToggleRoutine.style.background = 'var(--cyan-neon)';
            btnToggleRoutine.style.color = '#000';
            playSuccess();
            routineTimerInt = setInterval(() => {{
              if (routineSecs > 0) {{
                routineSecs--;
                routineClock.textContent = formatClock(routineSecs);

                if (routineSecs === 420 && curPhase === 1) {{
                  curPhase = 2;
                  updatePhaseUI();
                  showToast('Advanced to Phase 2: Soleus Pump');
                }} else if (routineSecs === 180 && curPhase === 2) {{
                  curPhase = 3;
                  updatePhaseUI();
                  showToast('Advanced to Phase 3: Breath Down');
                }}

                if (routineSecs % 2 === 0) playBounce();
              }} else {{
                clearInterval(routineTimerInt);
                isRoutineOn = false;
                btnToggleRoutine.textContent = '✓ Routine Completed!';
                showToast('10-Minute Morning Routine Finished!');
              }}
            }}, 1000);
          }} else {{
            btnToggleRoutine.textContent = '▶ Resume Morning Routine';
            btnToggleRoutine.style.background = 'linear-gradient(135deg, var(--emerald-healing), #059669)';
            btnToggleRoutine.style.color = '#fff';
            clearInterval(routineTimerInt);
            playClick();
          }}
        }});
      }}

      if (btnNextPhase) {{
        btnNextPhase.addEventListener('click', () => {{
          curPhase = (curPhase % 3) + 1;
          updatePhaseUI();
          playSuccess();
          showToast(`Switched to Phase ${{curPhase}}`);
        }});
      }}

      if (btnResetClock) {{
        btnResetClock.addEventListener('click', () => {{
          clearInterval(routineTimerInt);
          isRoutineOn = false;
          routineSecs = 600;
          curPhase = 1;
          routineClock.textContent = '10:00';
          btnToggleRoutine.textContent = '▶ Start Morning Routine';
          btnToggleRoutine.style.background = 'linear-gradient(135deg, var(--emerald-healing), #059669)';
          btnToggleRoutine.style.color = '#fff';
          updatePhaseUI();
          playClick();
          showToast('Routine Reset to 10:00');
        }});
      }}

      // Tab 4: Pricing & ROI Calculator
      const inputPhysio = document.getElementById('inputPhysio');
      const inputKnee = document.getElementById('inputKnee');
      const inputUsers = document.getElementById('inputUsers');
      const lblPhysio = document.getElementById('lblPhysio');
      const lblKnee = document.getElementById('lblKnee');
      const lblUsers = document.getElementById('lblUsers');
      const outYearSavings = document.getElementById('outYearSavings');
      const outPayback = document.getElementById('outPayback');

      function recalculateROI() {{
        const physio = parseInt(inputPhysio.value);
        const knee = parseInt(inputKnee.value);
        const users = parseInt(inputUsers.value);

        lblPhysio.textContent = `₹${{physio.toLocaleString('en-IN')}}`;
        lblKnee.textContent = `₹${{knee.toLocaleString('en-IN')}}`;
        lblUsers.textContent = users === 1 ? '1 Senior' : `${{users}} Generations`;

        const annualPhysioSavings = physio * 12;
        const familyAddValue = (users - 1) * 3000 * 12;
        const totalSavingsYear = annualPhysioSavings + familyAddValue;

        outYearSavings.textContent = `₹${{totalSavingsYear.toLocaleString('en-IN')}}`;
        const monthlyTotal = physio + ((users - 1) * 3000);
        const payback = (43000 / monthlyTotal).toFixed(1);
        outPayback.textContent = `${{payback}} Months`;
      }}

      [inputPhysio, inputKnee, inputUsers].forEach(slider => {{
        if (slider) slider.addEventListener('input', recalculateROI);
      }});

      // Agreement Modal
      const contractModal = document.getElementById('contractModal');
      const btnOpenContractModal = document.getElementById('btnOpenContractModal');
      const btnCloseModal = document.getElementById('btnCloseModal');
      const btnSignContract = document.getElementById('btnSignContract');

      if (btnOpenContractModal) {{
        btnOpenContractModal.addEventListener('click', () => {{
          contractModal.classList.add('open');
          playSuccess();
        }});
      }}
      if (btnCloseModal) {{
        btnCloseModal.addEventListener('click', () => {{
          contractModal.classList.remove('open');
          playClick();
        }});
      }}
      if (btnSignContract) {{
        btnSignContract.addEventListener('click', () => {{
          contractModal.classList.remove('open');
          playSuccess();
          showToast('✓ Boardroom SOW Agreement Approved & Signed!');
        }});
      }}

      // Init
      updateDocSub();
      updatePhaseUI();
      recalculateROI();
    }});
  </script>
</body>
</html>
"""

# Write out the state-of-the-art master index.html
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully created ultra-premium master index.html! Size: {os.path.getsize(os.path.join(base_dir, 'index.html'))} bytes")
