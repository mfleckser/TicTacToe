const serverURL = "http://127.0.0.1:5000";

const getBoard = async id => {
    const res = await fetch(`${serverURL}/get?id=${id}`);
    const data = await res.json();

    return data;
}

const createGame = async () => {
    const res = await fetch(`${serverURL}/create`);
    const data = await res.json();

    return data;
}

const play = async (id, x, y) => {
    const res = await fetch(`${serverURL}/play`, {
        method: "POST",
        headers: {
            "Content-Type": "text/plain"
        },
        body: JSON.stringify({
            "id": id,
            "x": x,
            "y": y
        })
    });
    const data = await res.json()

    return data;
}

const resetBoard = async (id) => {
    const res = await fetch(`${serverURL}/reset?id=${id}`);
    const data = await res.json()

    return data;
}

export { getBoard, createGame, play, resetBoard };