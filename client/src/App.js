import React, {useState, useEffect} from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import {useSelector, useDispatch} from 'react-redux'
import './App.css';
import allActions from './actions'
import Background from './component/Background';
import GridList from './component/GridList';
import {Copyright} from './component/Copyright';
import Paper from '@material-ui/core/Paper';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';

const App = () => {
  const currentCategory = useSelector(state => state.currentCategory)
  const dispatch = useDispatch()
  const [value, setValue] = useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div className="App">
      <Background/>
      <React.Fragment>
        <CssBaseline/>
          <Paper>
            <Tabs
              value={value}
              onChange={handleChange}
              indicatorColor="primary"
              textColor="primary"
              centered={true}
            >
              <Tab label="Hot" onClick={()=> {
                dispatch(allActions.categoryActions.setCategory("Hot"));
              }}/>
              <Tab label="정치" onClick={()=> {
                dispatch(allActions.categoryActions.setCategory("정치"));
              }}/>
              <Tab label="경제" onClick={()=> {
                dispatch(allActions.categoryActions.setCategory("경제"));
              }}/>
              <Tab label="사회" onClick={()=> {
                dispatch(allActions.categoryActions.setCategory("사회"));
              }}/>
              <Tab label="생활문화" onClick={()=> {
                dispatch(allActions.categoryActions.setCategory("생활문화"));
              }}/>
              <Tab label="세계" onClick={()=> {
                dispatch(allActions.categoryActions.setCategory("세계"));
              }}/>
              <Tab label="IT과학" onClick={()=> {
                dispatch(allActions.categoryActions.setCategory("IT과학"));
              }}/>
              <Tab label="오피니언" onClick={()=> {
                dispatch(allActions.categoryActions.setCategory("오피니언"));
              }}/>
            </Tabs>
          </Paper>
        <GridList/>
        <Copyright/>
      </React.Fragment>
    </div>
  );
}

export default App;