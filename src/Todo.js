// contains logics for the todo screen. Meant to be rendered as child of the Body component
import React, {useState} from "react"


export default async function Todo(props){
    let [data, setData]= useState([])
    let queriedData= await fetch("all_todo")
    return (
        <div className="todoCont">
            {/* items go here */}
            <div className="profile-nd-todo">
                <div className="profile">
                    <img src="" alt="activity owner" />
                    <div id="user-info">
                        <h4 id="user-name">
                            {/* takes in the username */}
                        </h4>
                    </div>
                </div>
                <div className="todo-div">
                    {
                        queriedData ? queriedData.map((data, idx)=>{
                            <div id="data" key={idx}>
                                data.date
                            </div>
                        }) : ''
                    }
                </div>
            </div>
        </div>
    )
}