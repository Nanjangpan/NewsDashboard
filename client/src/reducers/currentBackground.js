const currentBackground = (state = {}, action) => {
    switch(action.type){
        case "SET_DATE":
            return {
                ...state,
                date: action.payload
            }
        case "SET_WORD":
            return {
                ...state,
                word: action.payload
            }
        default:
            return state
    }
}

export default currentBackground;