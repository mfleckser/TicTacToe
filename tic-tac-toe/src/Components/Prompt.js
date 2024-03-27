import "./Prompt.css";
import { useState } from "react";
import { getBoard } from "../data";

const Prompt = ({ setCurrGame, setShowPrompt }) => {
    const [code, setCode] = useState("");

    const handleCloseButton = () => {
        setShowPrompt(false);
    }

    const handleInputChange = e => {
        setCode(e.target.value);
    }

    const handleCodeSubmit = async () => {
        const data = await getBoard(code)

        if (data.success) {
            setCurrGame(code);
        }
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