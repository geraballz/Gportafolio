import reflex as rx

LANG_SCRIPT = """
<script>
(function() {
    function applyLang(lang) {
        localStorage.setItem('portfolio_lang', lang);
        var enEls = document.querySelectorAll('.lang-en');
        var esEls = document.querySelectorAll('.lang-es');
        var btnEn = document.getElementById('btn-lang-en');
        var btnEs = document.getElementById('btn-lang-es');
        if (lang === 'es') {
            enEls.forEach(function(el) { el.style.display = 'none'; });
            esEls.forEach(function(el) { el.style.display = 'inline'; });
            if (btnEn) { btnEn.style.opacity = '0.4'; btnEn.style.fontWeight = 'normal'; }
            if (btnEs) { btnEs.style.opacity = '1'; btnEs.style.fontWeight = 'bold'; }
        } else {
            enEls.forEach(function(el) { el.style.display = 'inline'; });
            esEls.forEach(function(el) { el.style.display = 'none'; });
            if (btnEn) { btnEn.style.opacity = '1'; btnEn.style.fontWeight = 'bold'; }
            if (btnEs) { btnEs.style.opacity = '0.4'; btnEs.style.fontWeight = 'normal'; }
        }
    }
    window.setLang = applyLang;
    var saved = localStorage.getItem('portfolio_lang') || 'en';
    document.addEventListener('DOMContentLoaded', function() { applyLang(saved); });
    setTimeout(function() { applyLang(saved); }, 500);
    setTimeout(function() { applyLang(saved); }, 1500);
})();
</script>
"""

LANG_STYLE = """
<style>
.lang-es { display: none; }
</style>
"""

LANG_BUTTONS = """
<span style="display:inline-flex;align-items:center;gap:6px;">
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"
       fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
       stroke-linejoin="round" style="opacity:0.7">
    <circle cx="12" cy="12" r="10"/>
    <line x1="2" y1="12" x2="22" y2="12"/>
    <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
  </svg>
  <button id="btn-lang-en" onclick="setLang('en')"
    style="background:none;border:none;color:inherit;cursor:pointer;font-size:0.85rem;font-weight:bold;padding:2px 6px;border-radius:4px;opacity:1;">
    EN
  </button>
  <span style="opacity:0.4">|</span>
  <button id="btn-lang-es" onclick="setLang('es')"
    style="background:none;border:none;color:inherit;cursor:pointer;font-size:0.85rem;font-weight:normal;padding:2px 6px;border-radius:4px;opacity:0.4;">
    ES
  </button>
</span>
"""


def language_selector() -> rx.Component:
    return rx.hstack(
        rx.html(LANG_STYLE),
        rx.html(LANG_SCRIPT),
        rx.html(LANG_BUTTONS),
        align="center",
    )
