const setCategory = (cate='Hot') => {
    return {
        type: "SET_CATEGORY",
        category: cate
    }
}

const setCateIndex = (cateindex=0) => {
    return {
        type: "SET_CATEGORY",
        cateindex: cateindex
    }
}

export default {
    setCategory,
    setCateIndex
}