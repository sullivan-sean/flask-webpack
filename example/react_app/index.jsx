import React from 'react';
import { render } from 'react-dom';
import Root from './Root';

const run = () => {
  console.log('reun');
  return render(<Root />, document.getElementById('root'));
}

const loadedStates = ['complete', 'loaded', 'interactive'];

if (loadedStates.includes(document.readyState) && document.body) {
  run();
} else {
  window.addEventListener('DOMContentLoaded', run, false);
}

if (module.hot) module.hot.accept();
