const currentLiveData = (state = {}, action) => {
    switch(action.type){
        case "SET_LIVE_DATA":
            return {
                ...state,
                data: action.data,
            }
        default:
            return state
    }
}

export default currentLiveData;