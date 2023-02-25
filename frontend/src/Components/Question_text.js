import { Component } from "react";
import { backend_url } from "../config";
import axios from "axios";

class Question_text extends Component
{

    constructor(props)
    {
        super(props);
        //this.state={"question_text":''}
    }

    // componentDidMount()
    // {
    //     axios.post(backend_url+"/")
    //     this.setState({question_text: this.props.question_number});
    // }
    // componentDidUpdate(prevprops)
    // {
    //     // console.log(prevprops,this.props,'update');
    //     if (prevprops.question_number!=this.props.question_number)
    //     {
    //         this.setState({'question_text':this.props.question_number});
    //         //console.log(this.props.question_number);
    //     }
    // }
    render()
    {
        return(

            <div>
                <br/><br/>
                <h6>Question : {this.props.question_number}</h6>
                <p>{this.props.question_text}</p>

            </div>

        )
    }
}
export default Question_text;