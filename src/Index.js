import React from "react"
import {createRoot}from "react-dom/client"
import App from "./App"
import ReactDom from "react-dom"

let root= ReactDom.createRoot(document.querySelector("#root"))
root.render(<App tab="home"/>)