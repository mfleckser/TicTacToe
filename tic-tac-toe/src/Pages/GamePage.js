import Game from "../Components/Game";
import { useState } from "react";


const GamePage = ({ currGame }) => {
    const [board, setBoard] = useState("---------");

    return ( <div id="game-page" className="page">
        Game Code: {currGame}
        <Game board={board}/>
    </div> );
}

export default GamePage;