import React, { Component } from 'react';
import { DriveControl } from './queries/drive'
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1>Snobot :D</h1>
          <DriveControl />
        </header>
      </div>
    );
  }
}

export default App;
