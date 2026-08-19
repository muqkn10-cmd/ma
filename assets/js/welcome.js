// Welcome Page Script
(function() {
  'use strict';
  
  const Welcome = {
    init: function() {
      console.log('Welcome page initialized');
    }
  };
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => Welcome.init());
  } else {
    Welcome.init();
  }
  
  window.Welcome = Welcome;
})();
