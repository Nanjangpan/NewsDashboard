const currentLiveData = (state = {}, action) => {
    switch(action.type){
        case "SET_LIVE_DATA":
            return {
                ...state,
                data: action.data,
            }
        case "SET_LIVE_DATA_ALL":
            return {
                ...state,
                data: action.data,
            }
        case "SET_LIVE_TIME":
            return {
                ...state,
                time: action.time
            }
        default:
            return state
    }
}

export default currentLiveData;