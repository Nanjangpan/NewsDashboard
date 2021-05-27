
import React, { useEffect } from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Front from './card/front';
import Back from './card/back';
import Flippy, { FrontSide, BackSide } from 'react-flippy';
import axios from "axios";
import {useSelector, useDispatch} from 'react-redux'
import allActions from '../actions'
import Moment, { parseTwoDigitYear } from 'moment'
import Button from '@material-ui/core/Button';
import ButtonGroup from '@material-ui/core/ButtonGroup'
import { Alert, AlertTitle } from '@material-ui/lab';

const apiURL = "http://k8s-default-backingr-2cc91ca44b-1343636340.ap-northeast-2.elb.amazonaws.com";

const GridList = () => {
  const classes = useStyles();
  const currentDate = useSelector(state => state.currentBackground)
  const currentCategory = useSelector(state => state.currentCategory)
  const currentLiveData = useSelector(state => state.currentLiveData)
  const alert = useSelector(state => state.alert)
  const currentButtonColor = useSelector(state => state.currentButtonColor)
  const dispatch = useDispatch()

  const fetchData = async () => {
    try {
      dispatch(allActions.alertActions.setLoading(true));
      dispatch(allActions.alertActions.setError(null));
      dispatch(allActions.alertActions.setDateError(false));
      dispatch(allActions.livedataActions.setLiveTime(''))
      const today = new Date();
      today.setHours(today.getHours()+9);
      if (currentDate.date.getUTCDate() === today.getUTCDate() && 
        currentDate.date.getUTCMonth() === today.getUTCMonth() &&
        currentDate.date.getUTCFullYear() === today.getUTCFullYear()) {
        const response = await axios.get(`${apiURL}/cate/live_nine`, {
          params : {
            datetime : Moment(currentDate.date).format(), // "2015-06-15T00:00:00+09:00"
            cate : currentCategory.category,
          }
        })
        const response_time = await axios.get(`${apiURL}/time/live`)
        dispatch(allActions.livedataActions.setLiveData(response.data))
        dispatch(allActions.livedataActions.setLiveTime(response_time.data))
      } else if((currentDate.date.getUTCDate() < today.getUTCDate() &&
        currentDate.date.getUTCMonth() === today.getUTCMonth() &&
        currentDate.date.getUTCFullYear() === today.getUTCFullYear()) || 
        (currentDate.date.getUTCMonth() < today.getUTCMonth() &&
        currentDate.date.getUTCFullYear() == today.getUTCFullYear()) ||
        (currentDate.date.getUTCFullYear() < today.getUTCFullYear())){
        const response = await axios.get(`${apiURL}/cate/day_nine`, {
          params : {
            datetime : Moment(currentDate.date).format('YYYY-MM-DD'),
            cate : currentCategory.category,
          }
        })
        dispatch(allActions.livedataActions.setLiveData(response.data))
      } else {
        dispatch(allActions.alertActions.setDateError(true));
      }
    } catch(e) {
      dispatch(allActions.alertActions.setError(e));
    }
    dispatch(allActions.alertActions.setLoading(false));
  };

  const fetchDataAll = async () => {
    try {
      dispatch(allActions.alertActions.setLoading(true));
      dispatch(allActions.alertActions.setError(null));
      dispatch(allActions.alertActions.setDateError(false));
      const today = new Date();
      today.setHours(today.getHours()+9);
      if (currentDate.date.getUTCDate() === today.getUTCDate() &&
      currentDate.date.getUTCMonth() === today.getUTCMonth() &&
      currentDate.date.getUTCFullYear() === today.getUTCFullYear()) {
        const response = await axios.get(`${apiURL}/cate/live`, {
          params : {
            datetime : Moment(currentDate.date).format(), // "2015-06-15T00:00:00+09:00"
            cate : currentCategory.category,
          }
        })
        const response_time = await axios.get(`${apiURL}/time/live`)
        dispatch(allActions.livedataActions.setLiveData(response.data))
        dispatch(allActions.livedataActions.setLiveTime(response_time.data))
      } else if ((currentDate.date.getUTCDate() < today.getUTCDate() &&
        currentDate.date.getUTCMonth() === today.getUTCMonth() &&
        currentDate.date.getUTCFullYear() === today.getUTCFullYear()) || 
        (currentDate.date.getUTCMonth() < today.getUTCMonth() &&
        currentDate.date.getUTCFullYear() == today.getUTCFullYear()) ||
        (currentDate.date.getUTCFullYear() < today.getUTCFullYear())){
        const response = await axios.get(`${apiURL}/cate/day`, {
          params : {
            datetime : Moment(currentDate.date).format('YYYY-MM-DD'),
            cate : currentCategory.category,
          }
        })
        dispatch(allActions.livedataActions.setLiveDataAll(response.data))
      } else {
        dispatch(allActions.alertActions.setDateError(true));
      }
    } catch(e) {
      dispatch(allActions.alertActions.setError(e));
    }
    dispatch(allActions.alertActions.setLoading(false));
  };

  const handleClick1 = () => {
    dispatch(allActions.buttoncolorActions.setNineButtonColor('secondary'));
    dispatch(allActions.buttoncolorActions.setAllButtonColor('inherit'));
    fetchData();
  };

  const handleClick2 = () => {
    dispatch(allActions.buttoncolorActions.setNineButtonColor('inherit'));
    dispatch(allActions.buttoncolorActions.setAllButtonColor('secondary'));
    fetchDataAll();
  };

  useEffect(() => {
    fetchData();
  }, [currentDate, currentCategory]);
  

  if (alert.load) return <div>로딩중..</div>;
  if (alert.error) return <div>에러가 발생했습니다.</div>;
  if (alert.dateerror) return(
    <Container maxWidth="md" align="center" className={classes.alertstyle}>
      <Alert severity="error" variant="filled" >
        <AlertTitle>Error</AlertTitle>
        날짜가 유효하지 않습니다. <strong>다시 선택해주시기 바랍니다.</strong>
      </Alert>
    </Container>
  );
  if (!currentLiveData.data) return (
    <Container maxWidth="md" align="center" className={classes.alertstyle}>
      <Alert severity="warning" variant="filled" >
        <AlertTitle>Warning</AlertTitle>
        데이터가 없습니다. <strong>2020년 12월 23일 이후로 다시 선택해주시기 바랍니다.</strong>
      </Alert>
    </Container>
  );

  return (
    <React.Fragment>
        <CssBaseline/>
          <main>
            <Container maxWidth="md" align="left">
              <ButtonGroup className={classes.buttongroup} variant="contained" aria-label="split button">
                <Button color={currentButtonColor.nine_color} onClick={handleClick1}>9개만 보기</Button>
                <Button color={currentButtonColor.all_color} onClick={handleClick2}>모두 보기</Button>
              </ButtonGroup>
            </Container>  
            <Container className={classes.cardGrid} maxWidth="md">
              <Grid container spacing={4}>
                {currentLiveData.data.map((card) => (
                  <Grid item key={card.cluster_num} xs={12} sm={6} md={4}>
                    <Grid container direction="row">
                      {card.keyword.map((tag) => (
                        <Typography>#{tag}&nbsp;&nbsp;</Typography>
                      ))}
                     </Grid>
                    <Flippy className={classes.card}
                      flipOnHover={false} // default false
                      flipOnClick={true} // default false
                      flipDirection="horizontal" // horizontal or vertical
                      // if you pass isFlipped prop component will be controlled component.
                      // and other props, which will go to div
                      // these are optional style, it is not necessary
                    >
                      <FrontSide>
                        <Front data={card}/>
                      </FrontSide>
                      <BackSide>
                        <Back data={card.title_list}/>
                      </BackSide>
                    </Flippy>
                  </Grid>
                ))}
              </Grid>         
            </Container>
          </main>
    </React.Fragment>
  );  
}

const useStyles = makeStyles((theme) => ({
  button: {
    marginTop: theme.spacing(1),
  },
  cardGrid: {
    paddingTop: theme.spacing(8),
    paddingBottom: theme.spacing(8),
  },
  buttongroup: {
    marginTop: theme.spacing(2),
  },
  alertstyle: {
    marginTop: theme.spacing(2),
    width: '100%',
    alignItems: 'center',
    '& > * + *': {
      marginTop: theme.spacing(2),
    },
  }
}));

export default GridList;