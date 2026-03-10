import reflex as rx


LANG_SCRIPT = """
(function() {
    var saved = localStorage.getItem('portfolio_lang') || 'en';
    applyLang(saved);

    function applyLang(lang) {
        localStorage.setItem('portfolio_lang', lang);
        var enEls = document.querySelectorAll('.lang-en');
        var esEls = document.querySelectorAll('.lang-es');
        var btnEn = document.getElementById('btn-lang-en');
        var btnEs = document.getElementById('btn-lang-es');

        if (lang === 'es') {
            enEls.forEach(function(el) { el.style.display = 'none'; });
            esEls.forEach(function(el) { el.style.display = ''; });
            if (btnEn) btnEn.style.opacity = '0.45';
            if (btnEs) btnEs.style.opacity = '1';
        } else {
            enEls.forEach(function(el) { el.style.display = ''; });
            esEls.forEach(function(el) { el.style.display = 'none'; });
            if (btnEn) btnEn.style.opacity = '1';
            if (btnEs) btnEs.style.opacity = '0.45';
        }
    }

    window.setLang = function(lang) {
        applyLang(lang);
    };

    // Re-apply after Reflex hydrates the DOM
    var observer = new MutationObserver(function() {
        var saved = localStorage.getItem('portfolio_lang') || 'en';
        applyLang(saved);
    });
    observer.observe(document.body, { childList: true, subtree: true });
    setTimeout(function() { observer.disconnect(); }, 3000);
})();
"""


def language_selector() -> rx.Component:
    return rx.hstack(
        rx.icon("globe", size=16),
        rx.el.button(
            "EN",
            id="btn-lang-en",
            on_click=rx.call_script("setLang('en')"),
            style={
                "background": "none",
                "border": "none",
                "color": "inherit",
                "cursor": "pointer",
                "font_size": "0.85rem",
                "font_weight": "600",
                "padding": "2px 6px",
                "border_radius": "4px",
            }
        ),
        rx.text("|", size="1", color_scheme="gray"),
        rx.el.button(
            "ES",
            id="btn-lang-es",
            on_click=rx.call_script("setLang('es')"),
            style={
                "background": "none",
                "border": "none",
                "color": "inherit",
                "cursor": "pointer",
                "font_size": "0.85rem",
                "font_weight": "600",
                "padding": "2px 6px",
                "border_radius": "4px",
                "opacity": "0.45",
            }
        ),
        rx.script(LANG_SCRIPT),
        spacing="1",
        align="center",
    )
