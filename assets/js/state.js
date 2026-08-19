// State Management
(function() {
  'use strict';
  
  const State = {
    data: {},
    
    init: function() {
      console.log('State management initialized');
      this.loadState();
    },
    
    loadState: function() {
      const saved = localStorage.getItem('appState');
      if (saved) {
        this.data = JSON.parse(saved);
      }
    },
    
    saveState: function() {
      localStorage.setItem('appState', JSON.stringify(this.data));
    },
    
    setState: function(key, value) {
      this.data[key] = value;
      this.saveState();
    },
    
    getState: function(key) {
      return this.data[key];
    }
  };
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => State.init());
  } else {
    State.init();
  }
  
  window.State = State;
})();
