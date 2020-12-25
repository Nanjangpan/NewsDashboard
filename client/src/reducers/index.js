import currentCategory from './currentCategory'
import currentBackground from './currentBackground'
import currentLiveData from './currentLiveData'
import {combineReducers} from 'redux'

const rootReducer = combineReducers({
    currentCategory,
    currentBackground,
    currentLiveData
})

export default rootReducer