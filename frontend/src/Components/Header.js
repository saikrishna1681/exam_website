import { Component } from "react";
import Submit_exam from "./Submit_exam";


class Header extends Component
{
    constructor(props)
    {
        super(props);
    }

    render()
    {
        return(
            <div style={{width:"100%" , height: "10%", backgroundColor:"#000000", marginBottom:"50px" }}>
                <Submit_exam/>
        

            </div>
        )
    }
}
export default Header;