import currentUser from './currentUser'
import counter from './counter'
import currentCategory from './currentCategory'
import currentBackground from './currentBackground'
import currentLiveData from './currentLiveData'

import {combineReducers} from 'redux'

const rootReducer = combineReducers({
    currentUser,
    counter,
    currentCategory,
    currentBackground,
    currentLiveData
})

export default rootReducer