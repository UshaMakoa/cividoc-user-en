document.addEventListener("DOMContentLoaded", function() {
  if (!document.getElementById("lang-selector")) {
    var html = `
      <div id="lang-selector" style="position:fixed;top:1em;right:1em;z-index:9999;background:rgba(255,255,255,0.9);padding:0.3em 0.6em;border-radius:4px;box-shadow:0 1px 8px #aaa;">
        <select onchange="translateWithLibreTranslate(this.value)">
          <option value="en">English</option>
          <option value="fr">Français</option>
          <option value="it">Italiano</option>
          <option value="nl">Nederlands</option>
          <option value="es">Español</option>
          <option value="ca">Català</option>
        </select>
      </div>
    `;
    document.body.insertAdjacentHTML("beforeend", html);
  }
});

function translateWithLibreTranslate(targetLang) {
  const content = document.querySelector('main').innerText;
  fetch('https://libretranslate.com/translate', {
  method: 'POST',
  headers: {
    "Content-Type": "application/json",
    "Authorization": "Bearer MA_CLÉ_API"
  },
 body: JSON.stringify({
      q: content,
      source: 'en',
      target: targetLang,
      format: 'text'
    })
})
  .then(res => res.json())
  .then(data => {
    document.querySelector('main').innerText = data.translatedText;
    // Option : signaler la langue courante à l’utilisateur
  });
}

