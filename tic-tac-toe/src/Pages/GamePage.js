import Game from "../Components/Game";
import { useState, useEffect } from "react";
import { getBoard, play, resetBoard } from "../data";

const GamePage = ({ currGame }) => {
    const [board, setBoard] = useState("---------");

    const updateBoard = async () => {
        const res = await getBoard(currGame);

        if (res.success) {
            setBoard(res.board);
        }
    }

    const attemptMove = async (x, y) => {
        const res = await play(currGame, x, y);

        if (res.success) {
            setBoard(res.board);
        }
    }

    const reset = async () => {
        const res = await resetBoard(currGame);
    }

    useEffect(() => {
        setInterval(updateBoard, 500);
    }, [])

    return ( <div id="game-page" className="page">
        Game Code: {currGame}
        <button type="button" id="reset-button" onClick={reset}>Reset</button>
        <Game board={board} attemptMove={attemptMove}/>
    </div> );
}

export default GamePage;