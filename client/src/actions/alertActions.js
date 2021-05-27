const setLoading = (load) => {
    return {
        type: "SET_LOADING",
        payload: load
    }
}

const setError = (error) => {
    return {
        type: "SET_ERROR",
        payload: error
    }
}

const setDateError = (dateerror) => {
    return {
        type: "SET_DATE_ERROR",
        payload: dateerror
    }
}
export default {
    setLoading,
    setError,
    setDateError
}