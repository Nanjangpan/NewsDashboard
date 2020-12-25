const alert = (state = {}, action) => {
    switch(action.type){
        case "SET_LOADING":
            return {
                ...state,
                load: action.payload
            }
        case "SET_ERROR":
            return {
                ...state,
                error: action.payload
            }
        case "SET_DATE_ERROR":
            return {
                ...state,
                dateerror: action.payload
            }
        default:
            return state
    }
}

export default alert;