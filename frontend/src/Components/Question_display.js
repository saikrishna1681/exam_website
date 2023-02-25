import { Component } from "react";
import { backend_url } from "../config";
import axios from "axios";
import Question_text from "./Question_text";
import Header from "./Header";


class Question_display extends Component
{
    constructor(props)
    {
        super(props);
        //console.log(props);
        this.state={'no_of_questions':0,'question_numbers':[],'current_question':'',
            'answer_list':[],'questions_list':[], 'question_text':'','flash_message':''}
        var no_of_questions=0;
        var question_numbers=[];
    }
    changequestion(number)
    {
        // console.log(number);
        number=parseInt(number);
        //var text='q';
        var text=this.state.questions_list[number-1][1];
        document.getElementById("answer_box").value=this.state.answer_list[number-1];
        this.setState({'current_question':number, 'question_text':text});
        
    }
    display_flash(message)
    {
        this.setState({"flash_message":message});
        setTimeout(this.setState({"flash_message":""}), 3000);
    }
    save_and_continue()
    {
        //console.log("start");
        var current_question=this.state.current_question;
        var answers=this.state.answer_list;
        var ans=document.getElementById("answer_box").value;
        //console.log(ans,'strt');
        var next_question=(parseInt(current_question))%(parseInt(this.state.no_of_questions))+1;
        answers[current_question-1]=ans;
        //console.log();
        axios.post(backend_url+"save_answer",{"question_number":current_question,"answer":ans}).then(response=>
            {
                this.display_flash("success");

            }).catch(response=>
            {
                this.display_flash("error");
            })
        this.setState({"answer_list":answers});
        this.changequestion(next_question);

    }
    componentDidMount()
    {
        axios.post(backend_url+"get_question_statements").then(response=>{

            var no_of_questions=response.data.no_of_questions;
            var questions_list=response.data.questions_list;
            var answer_list=response.data.answer_list;
            // console.log(answer_list,'answer_list');
            var question_numbers=[];
            for(var i=1;i<=no_of_questions;i++)
            {
                question_numbers.push(i)
            }
            // console.log(response.data.no_of_questions);
            this.setState({'no_of_questions':no_of_questions, 'questions_list':questions_list, 
                    'answer_list':answer_list, 'current_question':'', "question_numbers":question_numbers,
                    'question_text':''})
        })
        // var no_of_questions=100;
        // var question_numbers=[];
        // for(var i=1;i<=no_of_questions;i++)
        // {
        //     question_numbers.push(i)
        // }
        // this.setState({'no_of_questions':no_of_questions,'question_numbers':question_numbers,});

    }

    render()
    {
        var count=1;
        return(

            <div>
                <Header/>
                {this.state.flash_message}
                <br/><br/>
                <div style={{float:"left", width: "30%", overflow:"auto"}}>
                    <label hidden >{count}</label>
                    {this.state.question_numbers.map(number=>

                        <button class="btn btn-primary" style={{margin:"5px"}} key={count++}
                        onClick={(event)=>this.changequestion(event.target.innerHTML)}>{count}</button>

                    )}

                </div>
                <div style={{float:"right", width: "70%", overflow:"auto"}}>

                    <Question_text question_number= {this.state.current_question} 
                            question_text= {this.state.question_text}   />

                    <br/>
                    <input  placeholder="enter your answer here" id="answer_box" type="text"></input><br/><br/>

                    {/* <button>Next</button>
                    <button>Previous</button> */}
                    <button  class="btn btn-primary" onClick={()=>this.save_and_continue()}>Save and continue</button>


                </div>



            </div>
            
        )
    }
}
export default Question_display;