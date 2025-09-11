<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Gen Z GitHub README Animation — Full‑Stack Data Scientist</title>
  <style>
    /* --------- Variables --------- */
    :root{
      --bg1:#0f172a; /* navy */
      --accent1:#7c3aed; /* violet */
      --accent2:#06b6d4; /* teal */
      --glass: rgba(255,255,255,0.06);
      --glass-2: rgba(255,255,255,0.04);
      --text: #e6eef8;
      --muted: rgba(230,238,248,0.65);
    }
    /* --------- Reset --------- */n
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      font-family:Inter, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
      background: radial-gradient(1200px 600px at 10% 10%, rgba(124,58,237,0.12), transparent 6%),
                  radial-gradient(900px 500px at 90% 90%, rgba(6,182,212,0.08), transparent 6%),
                  var(--bg1);
      color:var(--text);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      display:flex;align-items:center;justify-content:center;padding:40px;
    }

    /* --------- Card container --------- */
    .card{
      width:min(980px,95%);
      border-radius:20px;
      padding:28px;
      background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      box-shadow: 0 8px 30px rgba(2,6,23,0.6);
      position:relative; overflow:hidden; backdrop-filter: blur(6px);
      border: 1px solid rgba(255,255,255,0.03);
    }

    /* floating neon blobs */
    .blob{position:absolute;border-radius:50%;filter:blur(36px);opacity:0.85;mix-blend-mode:screen}
    .blob.b1{width:360px;height:360px;left:-80px;top:-70px;background:linear-gradient(45deg,var(--accent1),transparent);animation:float 10s ease-in-out infinite;}
    .blob.b2{width:240px;height:240px;right:-60px;bottom:-40px;background:linear-gradient(120deg,var(--accent2),transparent);animation:float 12s ease-in-out infinite;}
    @keyframes float{0%{transform:translateY(0) rotate(0deg)}50%{transform:translateY(-18px) rotate(6deg)}100%{transform:translateY(0) rotate(0deg)}}

    /* header */
    .header{display:flex;gap:20px;align-items:center}
    .avatar{
      width:92px;height:92px;border-radius:14px;flex:0 0 92px;overflow:hidden;border:1px solid rgba(255,255,255,0.06);
      background:linear-gradient(135deg,var(--accent1),var(--accent2));display:grid;place-items:center;font-weight:700;font-size:30px;color:white;
      transform:translateZ(0);box-shadow:0 8px 24px rgba(12,16,40,0.6);
    }
    .title{flex:1}
    h1{margin:0;font-size:20px;letter-spacing:0.2px}
    p.lead{margin:6px 0 0;color:var(--muted);font-size:13px}

    /* ticker / badge */
    .badges{display:flex;gap:10px;margin-top:16px}
    .badge{background:var(--glass);padding:8px 12px;border-radius:999px;font-size:13px;border:1px solid rgba(255,255,255,0.02);box-shadow:inset 0 1px rgba(255,255,255,0.02)}

    /* skill chips */
    .skills{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}
    .skill{padding:10px 14px;border-radius:12px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));border:1px solid rgba(255,255,255,0.03);font-weight:600;font-size:13px}

    /* animated code window */
    .demo{
      margin-top:20px;display:grid;grid-template-columns:1fr 260px;gap:18px;align-items:start
    }
    .term{background:linear-gradient(180deg, rgba(2,6,23,0.6), rgba(2,6,23,0.5));padding:16px;border-radius:12px;border:1px solid rgba(255,255,255,0.03);box-shadow: 0 6px 18px rgba(2,6,23,0.6);overflow:hidden}
    .term .line{height:12px;background:linear-gradient(90deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));border-radius:6px;margin:8px 0}

    /* typing highlight animation */
    .typing {
      display:inline-block;
      color:transparent;
      background:linear-gradient(90deg, #c0d6ff, #fff8); -webkit-background-clip:text; background-clip:text;
      animation:shimmer 3.6s linear infinite;
    }
    @keyframes shimmer {0%{transform:translateX(-2px)}50%{transform:translateX(2px)}100%{transform:translateX(-2px)}}

    /* right column: quick links */
    .links{background:var(--glass-2);padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.02);display:flex;flex-direction:column;gap:10px}
    .link{padding:10px;border-radius:8px;background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.005));font-weight:600;text-align:center}

    /* subtle floating cards */
    .floating-cards{display:flex;gap:12px;margin-top:18px}
    .fcard{flex:1;padding:12px;border-radius:12px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));border:1px solid rgba(255,255,255,0.03);transform-origin:center;animation:pop 6s ease-in-out infinite}
    .fcard:nth-child(1){animation-delay:0s}
    .fcard:nth-child(2){animation-delay:0.6s}
    .fcard:nth-child(3){animation-delay:1.2s}
    @keyframes pop{0%{transform:translateY(0)}50%{transform:translateY(-8px)}100%{transform:translateY(0)}}

    /* small responsive tweaks */
    @media (max-width:760px){
      .demo{grid-template-columns:1fr}
      .avatar{width:74px;height:74px}
      .card{padding:18px}
    }
  </style>
</head>
<body>
  <div class="card" role="region" aria-label="GitHub README animated header">
    <div class="blob b1" aria-hidden="true"></div>
    <div class="blob b2" aria-hidden="true"></div>

    <div class="header">
      <div class="avatar">AC</div>
      <div class="title">
        <h1>Hi, I'm <strong>Abhijay Chauhan</strong> — aspiring Full‑Stack Data Scientist</h1>
        <p class="lead">I build data pipelines, ML models, and full-stack apps that turn data into real products.</p>

        <div class="badges">
          <div class="badge">Open to collaborate</div>
          <div class="badge">📚 Learning: Cloud • MLOps</div>
        </div>

        <div class="skills" aria-hidden="true">
          <div class="skill">Python</div>
          <div class="skill">Machine Learning</div>
          <div class="skill">React • Node</div>
          <div class="skill">Docker • Kubernetes</div>
          <div class="skill">SQL • BigQuery</div>
        </div>
      </div>

    </div>

    <div class="demo" aria-hidden="true">
      <div class="term" title="Quick preview">
        <div style="height:8px;width:36%;background:rgba(255,255,255,0.06);border-radius:6px;margin-bottom:8px"></div>
        <div class="line" style="width:92%"></div>
        <div class="line" style="width:70%"></div>
        <div class="line" style="width:60%"></div>

        <div style="margin-top:12px;font-family:monospace;font-size:13px;color:var(--muted)">
          <div>&gt; git clone <span class="typing">github.com/your-username/your-project</span></div>
          <div style="margin-top:8px">&gt; python train.py —epochs 12 —model transformer</div>
          <div style="margin-top:8px">&gt; docker build . —tag ac/data-app</div>
        </div>
      </div>

      <div class="links">
        <div class="link">⭐ Star my projects</div>
        <div class="link">📂 Latest: portfolio</div>
        <div class="link">✉️ Connect on LinkedIn</div>
      </div>
    </div>

    <div class="floating-cards" aria-hidden="true">
      <div class="fcard">Projects: End-to-end ML apps</div>
      <div class="fcard">Stack: Python • React • Node • SQL</div>
      <div class="fcard">Goal: 12+ LPA roles in DS/ML</div>
    </div>
  </div>

  <!--
    Notes:
    - GitHub README.md pages sanitize most external CSS/JS. To use this animation on your GitHub profile README:
      1) Convert this section to an animated GIF / WebP and embed the image in README.md, OR
      2) Host this HTML via GitHub Pages and link to it from your README, OR
      3) Use a static snapshot (PNG) plus a link to the live demo.

    - Replace initials in .avatar with your preferred image or initials.
    - Tweak skill chips and links to reflect your real projects.
  -->
</body>
</html>
