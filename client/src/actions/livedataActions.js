const setLiveData = (data) => {
    return {
        type: "SET_LIVE_DATA",
        data: data
    }
}

const setLiveDataAll = (data) => {
    return {
        type: "SET_LIVE_DATA_ALL",
        data: data
    }
}
export default {
    setLiveData,
    setLiveDataAll
}