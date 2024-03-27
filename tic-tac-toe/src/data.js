const getBoard = async id => {
    const res = await fetch("http://127.0.0.1:5000/get?id=" + id);
    const data = await res.json();

    return data;
}

export { getBoard };