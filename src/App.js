import React from "react"
import { BrowserRouter as Router, Routes, Route} from "react-router-dom"
import Body from "./Body"
import Nav from "./Nav"

export default function App(){
    // renders all of the app components
    <Router>
        <Routes>
            <div>
                <Body>
                    This is taking forever to work.
                </Body>
            </div>
            {/* browser routes */}
            <Route path="/" element="</Body>"></Route>
        </Routes>
    </Router>
}