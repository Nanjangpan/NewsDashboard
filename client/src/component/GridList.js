import React, { useEffect, useState  } from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Front from './card/Front';
import Back from './card/Back';
import Flippy, { FrontSide, BackSide } from 'react-flippy';
import CardFrame from './card/CardFrame';
import axios from "axios";
import {useSelector, useDispatch} from 'react-redux'
import allActions from '../actions'
import Moment from 'moment'

const cards = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const apiURL = "http://localhost:8000";

const GridList = () => {
  const classes = useStyles();
  const currentDate = useSelector(state => state.currentBackground)
  const currentCategory = useSelector(state => state.currentCategory)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const currentLiveData = useSelector(state => state.currentLiveData)
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

  useEffect(() => {
    fetchData();
  }, []);
  
  if (loading) return <div>로딩중..</div>;
  if (error) return <div>에러가 발생했습니다.</div>;
  if (!currentLiveData.data) return <div>데이터가 없습니다.</div>;

  return (
    
    <React.Fragment>
        <CssBaseline/>
          <main>
            <Container className={classes.cardGrid} maxWidth="md">
              <Grid container spacing={4}>
                {currentLiveData.data.map((card) => (
                  <Grid item key={card.cluster_num} xs={12} sm={6} md={4}>
                    <Typography>{card.title}</Typography>
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
}));

export default GridList;