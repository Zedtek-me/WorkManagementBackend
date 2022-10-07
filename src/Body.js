import React, {useState} from "react"
import Nav from "./Nav"
import Todo from "./Todo"
export default function Body({children}){
    //the entire body
    return (
        <div className="childrenCont">
            <Nav/>
            <Todo/>
            This is some textdata contained in the body
            {children}
        </div>
    )
}