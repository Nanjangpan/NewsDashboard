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

const cards = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const apiURL = "http://localhost:8000";

const GridList = ({category}) => {
  const classes = useStyles();
  const [currentCategory, setCategory] = useState('Hot');
  const [datetime, setDatetime] = useState('20201202');
  const [image_url, setImage_url] = useState(null);
  const [title, setTitle] = useState(null);
  const [test, setTest] = useState(null);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    try {
      setError(null);
      setData(null);
      setLoading(true);
      const response = await axios.get(`${apiURL}/test`, {
        params : {
          datetime : datetime,
          cate : currentCategory,
        }
      })
      setData(response.data);
    } catch(e) {
      setError(e);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchData()
  }, []);

  if (loading) return <div>로딩중..</div>;
  if (error) return <div>에러가 발생했습니다.</div>;
  if (!data) return null;

  return (
    <React.Fragment>
        <CssBaseline/>
          <main>
            <Typography>{currentCategory}</Typography>
            <Typography>{data.title}</Typography>
            <Typography>{title}</Typography>
            <Container className={classes.cardGrid} maxWidth="md">
              <Grid container spacing={4}>
                {data.map((doc, card) => (
                  <Grid item key={card} xs={12} sm={6} md={4}>
                    <Flippy className={classes.card}
                      flipOnHover={false} // default false
                      flipOnClick={true} // default false
                      flipDirection="horizontal" // horizontal or vertical
                      // if you pass isFlipped prop component will be controlled component.
                      // and other props, which will go to div
                      // these are optional style, it is not necessary
                    >
                      <FrontSide>
                        <Front />
                      </FrontSide>
                      <BackSide>
                        <Back />
                      </BackSide>
                    </Flippy>
                  </Grid>
                ))}
              </Grid>          
            </Container>
            <Grid container spacing={4}>
              {data.map((card) => (
                <Grid item xs={12} sm={6} md={4}>
                  <Typography>{card.title}</Typography>
                  <CardFrame />
                </Grid>
              ))}
            </Grid>
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