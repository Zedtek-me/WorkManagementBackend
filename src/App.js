import React from "react"
import { BrowserRouter as Router, Routes, Route} from "react-router-dom"
import Body from "./Body"
import Nav from "./Nav"

export default function App(){
    // renders all of the app components
    <div className="parentCont">
        <Body>
            This is taking forever to work, but I'm gonna keep working on it till I get it.
        </Body>
        <Router>
            <Routes>
                {/* browser routes */}
                <Route exact path="/" element= {<Body></Body>}></Route>
            </Routes>
        </Router>
    </div>
}