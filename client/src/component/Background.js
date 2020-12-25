import React, { useEffect } from 'react';
import AppBar from '@material-ui/core/AppBar';
import LibraryBooksIcon from '@material-ui/icons/LibraryBooks';
import CssBaseline from '@material-ui/core/CssBaseline';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import {NAVER_COLOR} from '../models/colors';
import DayPicker from 'react-day-picker';
import axios from "axios";
import 'react-day-picker/lib/style.css';
import Moment from 'react-moment';
import {useSelector, useDispatch} from 'react-redux'
import allActions from '../actions'
import Image from 'material-ui-image';

const apiURL = "http://k8s-default-backingr-2cc91ca44b-1343636340.ap-northeast-2.elb.amazonaws.com";

function Background(){
  const classes = useStyles(); 
  const currentBackground = useSelector(state => state.currentBackground)
  const dispatch = useDispatch()
  var day = new Date();
  
  const wordCloudData = async () => {
    try {
      const today = new Date();
      today.setHours(today.getHours()+9);
      if (currentBackground.date.getUTCDate() === today.getUTCDate() && 
      currentBackground.date.getUTCMonth() === today.getUTCMonth() &&
      currentBackground.date.getUTCFullYear() === today.getUTCFullYear()) {
        const response = await axios.get(`${apiURL}/word/live`, {
          params : {
            datetime : Moment(currentBackground.date).format(), // "2015-06-15T00:00:00+09:00"
          }
        })
        dispatch(allActions.backgroundActions.setWord(response.data))
      } else if((currentBackground.date.getUTCDate() < today.getUTCDate() &&
      currentBackground.date.getUTCMonth() === today.getUTCMonth() &&
      currentBackground.date.getUTCFullYear() === today.getUTCFullYear()) || 
        (currentBackground.date.getUTCMonth() < today.getUTCMonth() &&
        currentBackground.date.getUTCFullYear() == today.getUTCFullYear()) ||
        (currentBackground.date.getUTCFullYear() < today.getUTCFullYear())){
        const response = await axios.get(`${apiURL}/word/day`, {
          params : {
            datetime : Moment(currentBackground.date).format('YYYY-MM-DD'),
          }
        })
        dispatch(allActions.backgroundActions.setWord(response.data))
      } else {
        dispatch(allActions.alertActions.setWord(null));
      }
    } catch(e) {
      console.log("워드 클라우드를 가져오는 데 실패했습니다.")
    }
  };

  useEffect(() => {
    dispatch(allActions.backgroundActions.setDate(day))
    wordCloudData();
  }, [])

  return(
    <>
      <CssBaseline />
      <AppBar position="relative" style={{ background: NAVER_COLOR }}>
          <Toolbar>
          <LibraryBooksIcon className={classes.icon} />
          <Typography variant="h6" color="inherit" noWrap >YBIGTA NEWS DASHBOARD</Typography>
          </Toolbar>
      </AppBar>
      <main>
          <div className={classes.heroContent}>
              <Container className={classes.flexdi} maxWidth="md">
                  <Container className={classes.top_content}>
                      <Typography component="h1" variant="h2" align='left' color="textPrimary" >
                          Just Ten Minute
                      </Typography>
                      <div className={classes.wc}>
                        <Image src={currentBackground.word} aspectRatio={(16/9)} disableSpinner/>
                      </div>
                  </Container>
                  <Container className={classes.second_content}>
                    <div>
                      <DayPicker 
                        onDayClick={(day) => dispatch(allActions.backgroundActions.setDate(day))} />
                    </div>
                  </Container>
              </Container>
              <Container maxWidth="md">
                  <div className={classes.dateChild}>
                    <Typography>
                      <Moment format="YYYY년 MM월 DD일" date={currentBackground.date} />
                    </Typography>  
                  </div>
                  <div>
                    <Typography align='right' color="textSecondary">오후 8시 30분 업데이트</Typography>
                  </div>
              </Container>              
          </div>
      </main>
    </>
  );
}


const useStyles = makeStyles((theme) => ({
    icon: {
      marginRight: theme.spacing(2),
    },
    heroContent: {
      backgroundColor: theme.palette.background.paper,
      padding: theme.spacing(8, 0, 6),
    },
    flexdi: {
      display:'flex',
    },
    top_content: {
      margin:"auto",
      width:'65%',
    },
    second_content: {
      margin:"auto",
      width:'35%',
    },
    wc: {
      margin:"auto",  
      marginTop:'30px',
      width:"90%",
    },
    dateContent :{
      display : 'flex',
      flexDirection : 'row',
    },
    dateChild: {
      position : 'absolute',
      left: 0,
      right : 0,
      top : 'auto',
      bottom : 'auto',
    },
  }));

  export default Background;