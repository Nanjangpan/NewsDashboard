<<<<<<< HEAD
<<<<<<< HEAD
import React, { useEffect, useState } from 'react';
=======
=======
import React, { useEffect, useState  } from 'react';
>>>>>>> 7d594ef ([chor] update gridlist)
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Front from './card/Front';
import Back from './card/Back';
import Flippy, { FrontSide, BackSide } from 'react-flippy';
<<<<<<< HEAD
=======
import CardFrame from './card/CardFrame';
import axios from "axios";
>>>>>>> 7d594ef ([chor] update gridlist)

const cards = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const apiURL = "http://localhost:8000";

const GridList = ({category}) => {
  const classes = useStyles();
  const [currentCategory, setCategory] = useState('Hot');
  const [datetime, setDatetime] = useState('20201202');
  const [image_url, setImage_url] = useState(null);
  const [title, setTitle] = useState(null);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b1eee6c (feat: add card flip function)
  const [test, setTest] = useState(null);
  useEffect(() => {
    setCategory(category);
    let items = [];
    fetch(`${apiURL}/test/go?datetime=${datetime}`)
      .then(response => response.json())
      .then((data) => {
        setTest(data);
        })
  })
<<<<<<< HEAD
>>>>>>> f720f34 ([feat] add Route component)
=======
=======
>>>>>>> fdc887c (feat: add card flip function)
>>>>>>> b1eee6c (feat: add card flip function)

  const _getLiveData = ({datetime}) => {
    let items = [];
    fetch('${apiURL}/test/go/')
  }

  useEffect(() => {
    setCategory(category);
    let items = [];
    await fetch("test/go")
      .then(response => response.json())
      .then((data) => {
        data.forEach((doc) => {
          items.push({
            image_url : doc.image_url,
            title : doc.title,
            url : doc.url,
            keyword : doc.keyword,
            press : doc.press,
            title_list
          })
        })
        
      })
  })
=======
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
    setCategory(category);
    fetchData();
    }, []);

  if (loading) return <div>로딩중..</div>;
  if (error) return <div>에러가 발생했습니다.</div>;
  if (!data) return null;

>>>>>>> 7d594ef ([chor] update gridlist)
  return (
    <React.Fragment>
        <CssBaseline/>
          <main>
            <Typography>{currentCategory}</Typography>
<<<<<<< HEAD
            <Typography>{test}</Typography>
            <Container className={classes.cardGrid} maxWidth="md">
              <Grid container spacing={4}>
                {cards.map((card) => (
                  <Grid item key={card} xs={12} sm={6} md={4}>
=======
            <Typography>{data.title}</Typography>
            <Typography>{title}</Typography>
            <Container className={classes.cardGrid} maxWidth="md">
              <Grid container spacing={4}>
                {data.map((doc, card) => (
                  <Grid item key={card} xs={12} sm={6} md={4}>
                    <Typography>{card.title}</Typography>
>>>>>>> 7d594ef ([chor] update gridlist)
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
<<<<<<< HEAD
=======
>>>>>>> 8d86167 (test for route function)
=======
>>>>>>> e305d79 ([chor] update gridlist)
>>>>>>> 7d594ef ([chor] update gridlist)
