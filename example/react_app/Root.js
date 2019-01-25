import React, { PureComponent } from 'react';
import { hot } from 'react-hot-loader';

class Root extends PureComponent {
  render() {
    return (
      <div style={{ backgroundColor: 'blue' }}>
        <p style={{ fontSize: 14, fontWeight: 'bold', color: 'red' }}>Hello, world!</p>
      </div>
    )
  }
}

export default hot(module)(Root)

