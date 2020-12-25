const currentCategory = (state = {}, action) => {
    switch(action.type){
        case "SET_CATEGORY":
            return {
                ...state,
                category: action.category,
            }
        case "SET_CATE_INDEX":
            return {
                ...state,
                cateindex: action.cateindex
            }
        default:
            return state
    }
}

export default currentCategory;