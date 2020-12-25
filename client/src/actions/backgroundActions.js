const setDate = (date) => {
    return {
        type: "SET_DATE",
        payload: date
    }
}

const setWord = (word) => {
    return {
        type: "SET_WORD",
        payload: word
    }
}

export default {
    setDate,
    setWord
}