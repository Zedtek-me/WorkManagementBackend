// contains logics for the todo screen. Meant to be rendered as child of the Body component
import React, {useState} from "react"


export default function Todo(props){
    let [data, setData]= useState([])
    fetch("all_todo")
    .then((resp)=> resp.json())
    .then((data)=> setData(data))
    data ? console.log(data) : ''
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
                        data.map((item, idx)=>{
                            <div id="data" key={idx}>
                                item.date
                            </div>
                        })
                    }
                </div>
            </div>
        </div>
    )
}