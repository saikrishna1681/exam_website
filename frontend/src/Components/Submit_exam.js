import { Component } from "react";
import { ModalFooter, Modal, ModalHeader, ModalBody } from "react-bootstrap";

class Submit_exam extends Component
{
    constructor(props)
    {
        super(props);
        this.state={"display":false}
    }
    submitexam()
    {
        var text=document.getElementById("submit_box").value;
        if(text=="submit")
        {
            document.getElementById("submit_box").value="done";
        }
        else
        {
            this.setState({"display":false});
        }
    }

    render()
    {
        return(
            
            <div>

                <button onClick={()=>{this.setState({"display":true})}} class="btn btn-danger">Submit the exam</button>

                <Modal show={this.state.display} >

					<ModalHeader>

						Are you sure you want to submit?
                        This action cannot be undone
                        <button onClick={()=>{this.setState({"display":false})}} class="btn btn-primary">Don't Submit</button>
						
					</ModalHeader>
					<ModalBody>


                        <h3>type "submit" in the bottom box and click submit button</h3>

						<input id="submit_box"></input>

                        <button onClick={()=>{this.submitexam()}} class="btn btn-danger">I want to submit</button>

					</ModalBody>

                    <ModalFooter>

                    <button onClick={()=>{this.setState({"display":false})}} class="btn btn-primary">Don't Submit</button>

                    </ModalFooter>
					

                </Modal>

            </div>
        )
    }
}

export default Submit_exam;