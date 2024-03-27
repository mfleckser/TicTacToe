import "./App.css";
import GamePage from "./Pages/GamePage";
import MenuPage from "./Pages/MenuPage";
import { useState } from "react";

function App() {
  const [currGame, setCurrGame] = useState("");

  return (
    <div className="App">
      {currGame ? <GamePage currGame={currGame}/> : <MenuPage setCurrGame={setCurrGame}/>}
    </div>
  );
}

export default App;
