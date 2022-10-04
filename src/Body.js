import React, {useState} from "react"
import Nav from "./Nav"

export default function Body(props, {children}){
    //the entire body
    return (
        <div className="childrenCont">
            {children}
        </div>
    )
}