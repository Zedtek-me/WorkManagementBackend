import React, {useState} from "react"
import Nav from "./Nav"

export default function Body(props, {children}){
    //the entire body
    let color, changeColor= useState(["lightblue"])

    return (
        <div className="childrenCont">
            {
                props.style =`${color}`
            }
            {children}
        </div>
    )
}