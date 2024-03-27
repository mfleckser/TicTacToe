import "./Prompt.css";
import { useState } from "react";

const Prompt = ({ setShowPrompt }) => {
    const [code, setCode] = useState("");

    const handleCloseButton = () => {
        setShowPrompt(false);
    }

    const handleInputChange = e => {
        setCode(e.target.value);
    }

    const handleCodeSubmit = () => {
        console.log(code);
    }

    return ( 
        <div id="prompt">
            <button id="close-button" type="button" onClick={handleCloseButton}>x</button>
            <h1>Enter the game code:</h1>
            <input id="code-input" type="text" placeholder="123456" maxLength="6" onChange={handleInputChange}/><br/>
            <button id="submit-code" type="button" onClick={handleCodeSubmit}>Enter</button>
        </div>
     );
}

export default Prompt;