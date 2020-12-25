const setNineButtonColor = (nine_color='secondary') => {
    return {
        type: "SET_NINE_BUTTON_COLOR",
        payload: nine_color
    }
}

const setAllButtonColor = (all_color='inherit') => {
    return {
        type: "SET_ALL_BUTTON_COLOR",
        payload: all_color
    }
}

export default {
    setNineButtonColor,
    setAllButtonColor
}