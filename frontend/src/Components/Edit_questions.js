import { Component } from "react";
import { ModalFooter, Modal, ModalHeader, ModalBody } from "react-bootstrap";
//import { Modal } from "react-bootstrap/Modal";
//import { Modal } from "bootstrap";
import axios from "axios";
import { backend_url } from "../config";
class Edit_Questions extends Component
{
    constructor(props)
    {
        super(props);
        // this.state={"data":[[1,"question_1",2,1,"ab"], [2,"question_2",4,3,"ac"]],
		// 	'no_of_questions':2, 'display':false,"current_question":0, "question_text":'', "positive_marks":'',
		// 	"negative_marks":'', "answer_key":'', 'exam_id':0, "flash_message":"",'new':false};
		this.state={ "data":[], 'no_of_questions':0, 'display':false,"current_question":0, "question_text":'', 
		"positive_marks":'', "negative_marks":'', "answer_key":'', 'exam_id':0, "flash_message":"",'new':false };
    }
	componentDidMount()
	{
		axios.get(backend_url+"staff/view_examquestions/"+this.props.match.params.exam_id).then(response=>{
			this.setState({"data":response.data["data"],"no_of_questions":response.data["no_of_questions"]});
		}).catch(response=>{
			this.display_flash("error happened while loading");
		})
	}
	createquestion()
	{
		var data=['','','',''];
		var exam_id=parseInt(this.props.match.params.exam_id);
		data[0]=this.state.no_of_questions;
		data[1]=this.state.question_text;
		data[2]=this.state.positive_marks;
		data[3]= this.state.negative_marks;
		data[4]= this.state.answer_key;
		axios.post(backend_url+"staff/add_examquestion/"+this.props.match.params.exam_id, {"data":data})
		.then(response=>{
			window.location.reload();
		}).catch(error=>{
			this.display_flash("error");
			this.setState({"display":false});
		})
	}
	newquestionbox()
	{
		this.setState({"display":true, "question_text":'', "positive_marks":'', "negative_marks":'', "answer_key":'', 
		'current_question':this.state.no_of_questions,'new':true});
	}

    viewQuestion(e)
    {
		//console.log(e);
		e=parseInt(e);
		var data=this.state.data[e];
		var question_text=data[1];
		var positive_marks=data[2];
		var negative_marks= data[3];
		var answer_key= data[4];
		this.setState({"display": true, "current_question":e, "question_text":question_text, 
			"positive_marks":positive_marks, "negative_marks":negative_marks, "answer_key":answer_key,'new':false});
    }
	display_flash(message)
	{
		this.setState({"flash_message":message});
        setTimeout(()=> {this.setState({"flash_message":""})}, 3000);
	}
	closemodal()
	{
		this.setState({"display": false});
	}
	updatemodal(e)
	{
		var x = e.target.id;
		// console.log(this.state);
		this.setState({[x]: e.target.value});
	}
	updatequestions()
	{
		if(this.state.new==true)
		{
			this.createquestion();
		}
		else
		{
			var current_question=this.state.current_question;
			var data=this.state.data;
			data[current_question][1]=this.state.question_text;
			data[current_question][2]=this.state.positive_marks;
			data[current_question][3]= this.state.negative_marks;
			data[current_question][4]= this.state.answer_key;
			this.setState({"data":data, "display": false});
			var exam_id=this.props.match.params.exam_id;
			axios.post(backend_url+"staff/update_examquestion/"+this.props.match.params.exam_id, {"data":data[current_question]})
			.then(response=>{
				this.display_flash("success");
			}).catch(error=>{
				this.display_flash("error");
			})
		}
	}
	deletequestion()
	{
		var current_question=this.state.current_question;
		var data=this.state.data;
		var question_id=data[current_question][0].toString();
		axios.get(backend_url+"staff/delete_examquestion/"+this.props.match.params.exam_id+"/"+question_id)
			.then(response=>{
				window.location.reload();
			}).catch(error=>{
				this.display_flash("error");
			})
	}
	updatedata()
	{
		axios.get(backend_url+"staff/update_examdata/"+this.props.match.params.exam_id).then(response=>{
			window.location.reload();
		}).catch(error=>{
			this.display_flash("error");
		})
	}
    render()
    {
        var count=0;
        return(

            <div>
				<h1>{this.state.flash_message}</h1><br/><br/>
				{/* <button style={{"marginTop":"30px"}}class="btn btn-primary" onClick={()=>{this.updatequestions()}}>Save the changes</button><br/> */}
				<button class="btn btn-primary" onClick={()=>{this.newquestionbox()}}> Add Question </button>
				<br/><br/>
				<button class="btn btn-primary" onClick={()=>this.updatedata()}>Update all Data</button>
                <table style={{"marginLeft":"100px", "marginTop":"50px", "borderSpacing":"100px"}}>
					<thead> 
                    <tr>
                    <td> Question link</td>
                    <td>Positive marks</td>
                    <td>Negative marks</td>
                    <td>Answer key</td>
					<td></td>
                    </tr>
					</thead>
					<tbody>
                    {this.state.data.map(row=>
                        
                        <tr >
                            <td><button class="btn btn-primary"  id={count} onClick={(e)=>{this.viewQuestion(e.target.id)}}>
								Question {row[0]} </button></td>
                            <td> <label> {row[2]} </label></td>
                            <td> <label>{row[3]} </label></td>
                            <td> <label> {row[4]} </label></td>
							<td><label hidden>{count++}</label></td>
                        </tr>
                    )}
					</tbody>

                </table>

				<Modal show={this.state.display} >

					<ModalHeader>

						Question {this.state.current_question + 1} <br/>
						<button class="btn btn-primary" onClick={(e)=> this.closemodal()}>Close without saving</button>
						
					</ModalHeader>
					<ModalBody>

						<div>
						<label class="form-label">Question Text</label>
						<textarea onChange={(e)=>{this.updatemodal(e)}} class="form-textarea w-25" 
							id="question_text" value={this.state.question_text}/>
						</div>
						
						<div>
						<label class="form-label">Positive marks</label>
						<input type="number" onChange={(e)=>{this.updatemodal(e)}} class="form-input w-25" 
							id="positive_marks" value={this.state.positive_marks}/>
						</div>

						<div>
						<label class="form-label">Negative marks</label>
						<input type="number" onChange={(e)=>{this.updatemodal(e)}} class="form-input w-25" 
							id="negative_marks" value={this.state.negative_marks}/>
						</div>

						<div>
						<label class="form-label">ANSWER KEY </label>
						<input onChange={(e)=>{this.updatemodal(e)}} class="form-input w-25" 
							id="answer_key" value={this.state.answer_key}/>
						</div>

					</ModalBody>
					<ModalFooter>
						<button class="btn btn-primary" onClick={()=>{this.updatequestions()}}>Save </button>
						<button class="btn btn-primary" onClick={()=>{this.deletequestion()}}>Delete Question </button>
					</ModalFooter>

                </Modal>
                
            </div>
        )
    }
}
export default Edit_Questions;