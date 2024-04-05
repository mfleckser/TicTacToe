import "./Menu.css";
import { createGame } from "../data";

const Menu = ({ setCurrGame, setShowPrompt }) => {
    const handleCreateOnline = async () => {
        const res = await createGame();
        const id = res.id;

        setCurrGame(id);
    }

    const handleJoin = () => {
        setShowPrompt(true);
    }

    const handleCreateSPG = () => {}

    return ( 
        <div id="menu">
            <h1>Tic Tac Toe</h1>
            <div id="menu-buttons">
                <button type="button" onClick={handleCreateOnline}>New Online Game</button>
                <button type="button" onClick={handleJoin}>Join Game</button>
                <button type="button" onClick={handleCreateSPG}>Single Player</button>
            </div>
        </div>
     );
}

export default Menu;