// UI Components
(function() {
  'use strict';
  
  const UI = {
    init: function() {
      console.log('UI components initialized');
      this.setupComponents();
    },
    
    setupComponents: function() {
      // Setup UI components
    }
  };
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => UI.init());
  } else {
    UI.init();
  }
  
  window.UI = UI;
})();
