// Theme Bootstrap
(function() {
  'use strict';
  
  const ThemeBootstrap = {
    init: function() {
      console.log('Theme bootstrap initialized');
      this.setupTheme();
    },
    
    setupTheme: function() {
      const savedTheme = localStorage.getItem('theme') || 'light';
      document.documentElement.setAttribute('data-theme', savedTheme);
    }
  };
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => ThemeBootstrap.init());
  } else {
    ThemeBootstrap.init();
  }
  
  window.ThemeBootstrap = ThemeBootstrap;
})();
