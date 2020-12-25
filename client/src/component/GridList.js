
import React, { useEffect, useState  } from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Front from './card/Front';
import Back from './card/Back';
import Flippy, { FrontSide, BackSide } from 'react-flippy';
import axios from "axios";
import {useSelector, useDispatch} from 'react-redux'
import allActions from '../actions'
import Moment from 'moment'
import Button from '@material-ui/core/Button';
import ButtonGroup from '@material-ui/core/ButtonGroup'

const apiURL = "http://localhost:8000";

const GridList = () => {
  const classes = useStyles();
  const currentDate = useSelector(state => state.currentBackground)
  const currentCategory = useSelector(state => state.currentCategory)
  const currentLiveData = useSelector(state => state.currentLiveData)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [bcolor1, setBColor1] = useState("secondary");
  const [bcolor2, setBColor2] = useState("inherit");
  const dispatch = useDispatch()

  const fetchData = async () => {
    try {
      setError(null);
      setLoading(true);
      const response = await axios.get(`${apiURL}/test`, {
        params : {
          datetime : Moment(currentDate.date).format('YYYY-MM-DD'),
          cate : currentCategory.category,
        }
      })
      dispatch(allActions.livedataActions.setLiveData(response.data))
    } catch(e) {
      setError(e);
    }
    setLoading(false);
  };

  const fetchDataAll = async () => {
    try {
      setError(null);
      setLoading(true);
      const response = await axios.get(`${apiURL}/tests`, {
        params : {
          datetime : Moment(currentDate.date).format('YYYY-MM-DD'),
          cate : currentCategory.category,
        }
      })
      dispatch(allActions.livedataActions.setLiveDataAll(response.data))
    } catch(e) {
      setError(e);
    }
    setLoading(false);
  };

  const handleClick1 = () => {
    setBColor1("secondary");
    setBColor2("inherit");
    fetchData();
  };

  const handleClick2 = () => {
    setBColor1("inherit");
    setBColor2("secondary");
    fetchDataAll();
  };

  useEffect(() => {
    fetchData();
  }, [currentDate, currentCategory]);
  

  if (loading) return <div>로딩중..</div>;
  if (error) return <div>에러가 발생했습니다.</div>;
  if (!currentLiveData.data) return <div>데이터가 없습니다.</div>;

  return (
    
    <React.Fragment>
        <CssBaseline/>
          <main>
            <Container maxWidth="md" align="left">
              <ButtonGroup className={classes.buttongroup} variant="contained" aria-label="split button">
                <Button color={bcolor1} onClick={handleClick1}>9개만 보기</Button>
                <Button color={bcolor2} onClick={handleClick2}>모두 보기</Button>
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
  icon: {
    marginRight: theme.spacing(2),
  },
  button: {
    marginTop: theme.spacing(1),
  },
  cardGrid: {
    paddingTop: theme.spacing(8),
    paddingBottom: theme.spacing(8),
  },
  card: {
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
  },
  cardMedia: {
    paddingTop: '56.25%', // 16:9
  },
  cardContent: {
    flexGrow: 1,
  },
  buttongroup: {
    marginTop: theme.spacing(2),
    
  },
}));

export default GridList;