import React from "react"
import App from "./App"
import ReactDom from "react-dom"

let root= ReactDom.createRoot(document.getElementById("root"))
root.render(
    <React.StrictMode>
        <App/>
    </React.StrictMode>
)