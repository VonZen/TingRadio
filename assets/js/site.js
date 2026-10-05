/* Locale URLs choose the language. The default entry point always stays in English. */
(() => {
  const menus = document.querySelectorAll('.language-menu');
  document.addEventListener('click', event => {
    menus.forEach(menu => {
      if (!menu.contains(event.target)) menu.open = false;
    });
  });
  document.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    menus.forEach(menu => {
      if (menu.open) {
        menu.open = false;
        menu.querySelector('summary').focus();
      }
    });
  });
})();
