import { Component } from "react";
import Header from "./Header";


class Exam_homepage extends Component
{
    constructor(props)
    {
        super(props);
    }
    startexam()
    {
        window.location.hash='#/write_exam';
    }
    render()
    {
        return(
            
            <div>
                <Header/>
                <button  onClick={()=>this.startexam()}>Start exam</button>

            </div>
        )
    }
}
export default Exam_homepage;