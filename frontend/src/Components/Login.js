import { Component } from "react";
import axios from "axios";
import { backend_url } from "../config";
//import cookies from UniversalCookie;

class Login extends Component
{

    constructor(props)
    {
        super(props);
        // console.log(window.location.hash,'hash');
        // console.log(window.location);
    }

    login_function()
    {
        axios.post(backend_url+"login",{"username":"admin","password":"admin"}).then(response=>{

            // console.log(response);
            window.location.hash='#/questions';
            // window.location.href=backend_url+"frontend#/questions";
        })
    }

    render()
    {
        return(

            <div>
                <input type="text" placeholder="Username"></input><br/>
                <input type="password" placeholder="password"></input><br/>
                <button  onClick={()=>this.login_function()}>Submit</button>
            </div>

        )
    }
}
export default Login;