const currentButtonColor = (state = {}, action) => {
    switch(action.type){
        case "SET_NINE_BUTTON_COLOR":
            return {
                ...state,
                nine_color: action.payload
            }
        case "SET_ALL_BUTTON_COLOR":
            return {
                ...state,
                all_color: action.payload
            }
        default:
            return state
    }
}

export default currentButtonColor;