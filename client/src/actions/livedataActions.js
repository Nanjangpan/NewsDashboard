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

const setLiveTime = (time) => {
    return {
        type: "SET_LIVE_TIME",
        time: time
    }
}
export default {
    setLiveData,
    setLiveDataAll,
    setLiveTime
}