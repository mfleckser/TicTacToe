import { useRef, useEffect } from "react";
import "./Game.css";

const Game = ({ board, attemptMove }) => {
    const canvasRef = useRef(null);

    const line = (context, p1, p2) => {
        context.beginPath();
        context.moveTo(p1[0], p1[1])
        context.lineTo(p2[0], p2[1])
        context.stroke();
    }
    
    const draw = context => {
        context.lineWidth = 10;
        const size = context.canvas.width / 3; // size of each square

        context.clearRect(0, 0, size * 3, size * 3);
        
        // draw board
        line(context, [size, 0], [size, 3 * size]);
        line(context, [2 * size, 0], [2 * size, 3 * size]);
        line(context, [0, size], [3 * size, size]);
        line(context, [0, 2 * size], [3 * size, 2 * size]);

        // draw pieces
        context.font = "235px Arial";
        context.textBaseline = "top";
        context.textAlign = "center";
        for (let i = 0; i < 9; i++) {
            if (board[i] !== "-") {
                const x = (i % 3) * size + size / 2;
                const y = Math.floor(i / 3) * size;

                context.fillStyle = (board[i] === "X") ? "red" : "blue";
                context.fillText(board[i], x, y);
            }
        }
    }

    useEffect(() => {
        const canvas = canvasRef.current;
        const context = canvas.getContext("2d");

        draw(context);
    }, [board])

    const handleBoardClick = e => {
        const size = e.target.clientWidth / 3;
        const x = Math.floor((e.pageX - e.target.offsetLeft) / size);
        const y = Math.floor(e.pageY / size);
        
        attemptMove(x, y);
    }

    return ( 
        <canvas id="game-board" ref={canvasRef} width="600px" height="600px" onClick={handleBoardClick}></canvas>
     );
}

export default Game;