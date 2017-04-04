import React from 'react';
import ReactDOM from 'react-dom';
import Decrypt from './components/Decrypt'

function init () {
  let app = document.querySelectorAll('[data-section="app"]')[0];
  ReactDOM.render(
    <Decrypt />,
    app
  );
}

// This would usually wait for the ready/DOMContentLoaded
// event, but we're loading this async, and it's up last
init();
