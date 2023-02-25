import logo from './logo.svg';
import './App.css';
import {BrowserRouter,Route, HashRouter, Switch} from 'react-router-dom';
//import { HashRouter as Router, Route, Switch } from "react-router-dom";

import Question_display from './Components/Question_display';
import Login from './Components/Login';
import Exam_homepage from './Components/Exam_homepage';
import Edit_Questions from './Components/Edit_questions';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';

// import { Component } from "react";
// import { backend_url } from "../config";
// import axios from "axios";

function App() {
  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reloads.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}

      
      <HashRouter basename="/static/">
          
              <Switch>
                <Route  path = "/login" component={Login} />
                <Route  path = "/write_exam" component={Question_display} />
                <Route  path = "/:exam_id/view" component={Edit_Questions}/>
                <Route  path = "/" component={Exam_homepage} /> 
              </Switch> 
          
      </HashRouter>
      
      {/* <Login/> 

      <Question_display/> */}

      {/* <BrowserRouter>

      <Route path= "/logins" component={Login}/>
      <Route  path = "frontend/write_exam" component={Question_display} />
      
      <Route path="/exam/questions" component={Question_display}  />
      
      
      </BrowserRouter> */}

    </div>
  );
}

export default App;



// {
//   "name": "new-panel_ui",
//   "version": "0.1.0",
//   "private": true,
//   "dependencies": {
//     "axios": "^0.21.4",
//     "bootstrap": "^5.1.3",
//     "cra-template": "1.2.0",
//     "jquery": "^3.6.0",
//     "react": "^17.0.2",
//     "react-bootstrap": "^2.5.0",
//     "react-dom": "^17.0.2",
//     "react-router": "^6.3.0",
//     "react-router-dom": "^5.2.0",
//     "react-scripts": "4.0.3",
//     "serve": "14.0.1"
//   },
//   "scripts": {
//     "start": "react-scripts start",
//     "build": "react-scripts build",
//     "test": "react-scripts test",
//     "eject": "react-scripts eject"
//   },
//   "eslintConfig": {
//     "extends": [
//       "react-app",
//       "react-app/jest"
//     ]
//   },
//   "browserslist": {
//     "production": [
//       ">0.2%",
//       "not dead",
//       "not op_mini all"
//     ],
//     "development": [
//       "last 1 chrome version",
//       "last 1 firefox version",
//       "last 1 safari version"
//     ]
//   },
//   "devDependencies": {
//     "web-vitals": "^2.1.4"
//   },
//   "homepage": "https://panelsdev.vmock.com/capabilities-database-panel"
// }
