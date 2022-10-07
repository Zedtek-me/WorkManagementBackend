import React from "react"
import { BrowserRouter as Router, Routes, Route, Link} from "react-router-dom"
import Body from "./Body"
import Nav from "./Nav"
import "./App.css"

export default function App(){
    // renders all of the app components
    <Router>
        <div className="parentCont">
            Hadoop
            <Body className="theBody">
                <Link to={"something/"}/>
                This is taking forever to work, but I'm gonna keep working on it till I get it.
            </Body>

            {/* browser routes */}
            <Routes>
                <Route exact path="/">
                    <Body children={<Nav/>}/>
                </Route>
                <Route exact path="something/">
                    Something Route
                </Route>
            </Routes>
        </div>
    </Router>
}