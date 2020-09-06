import React from 'react';
import Navbar from './components/Navbar';
import './App.css';
import Home from './components/pages/Home';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import About from './components/pages/about';
import face_rec from './components/pages/face_rec';
import Disguise from './components/pages/disguise';

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/about' component={About} />
          <Route path='/face_rec' component={face_rec} />
          <Route path='/disguise' component={Disguise} />
        </Switch>
      </Router>
    </>
  );
}

export default App;
