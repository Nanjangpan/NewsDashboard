import currentCategory from './currentCategory'
import currentBackground from './currentBackground'
import currentLiveData from './currentLiveData'
import alert from './alert'
import currentButtonColor from './currentButtonColor'
import {combineReducers} from 'redux'

const rootReducer = combineReducers({
    currentCategory,
    currentBackground,
    currentLiveData,
    alert,
    currentButtonColor
})

export default rootReducer