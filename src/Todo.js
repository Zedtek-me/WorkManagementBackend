// contains logics for the todo screen. Meant to be rendered as child of the Body component
import React, {useState} from "react"


export default async function Todo(props){
    let [data, setData]= useState([])
    let queriedData= await fetch("all_todo")
    return (
        <div className="todoCont">
            {/* body goes here */}
        </div>
    )
}