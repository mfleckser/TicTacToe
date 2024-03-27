import Menu from "../Components/Menu";
import Prompt from "../Components/Prompt";
import { useState } from "react"

const MenuPage = ({ setCurrGame }) => {
    const [showPrompt, setShowPrompt] = useState(false);

    return ( <div id="menu-page" className="page">
        <Menu setCurrGame={setCurrGame} setShowPrompt={setShowPrompt} />
        {showPrompt && <Prompt setCurrGame={setCurrGame} setShowPrompt={setShowPrompt} />}
    </div> );
}

export default MenuPage;