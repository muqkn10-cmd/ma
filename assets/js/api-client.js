// API Client
(function() {
  'use strict';
  
  const APIClient = {
    baseURL: '/api',
    
    init: function() {
      console.log('API client initialized');
    },
    
    async request: function(endpoint, options = {}) {
      const url = `${this.baseURL}${endpoint}`;
      const config = {
        headers: {
          'Content-Type': 'application/json',
          ...options.headers
        },
        ...options
      };
      
      try {
        const response = await fetch(url, config);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
      } catch (error) {
        console.error('API request failed:', error);
        throw error;
      }
    },
    
    get: function(endpoint) {
      return this.request(endpoint, { method: 'GET' });
    },
    
    post: function(endpoint, data) {
      return this.request(endpoint, { method: 'POST', body: JSON.stringify(data) });
    },
    
    put: function(endpoint, data) {
      return this.request(endpoint, { method: 'PUT', body: JSON.stringify(data) });
    },
    
    delete: function(endpoint) {
      return this.request(endpoint, { method: 'DELETE' });
    }
  };
  
  APIClient.init();
  window.APIClient = APIClient;
})();
