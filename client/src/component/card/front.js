import React, {  } from 'react';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';


const Front = ({data}) => {
  const classes = useStyles();
  return (
    <Card className={classes.card}>
      <CardMedia
        className={classes.cardMedia}
        image={data.img_url}
      />
      <CardContent className={classes.cardContent}>
        <a href={data.url} target="_blank">
          {data.title.length < 43 ? data.title : data.title.substring(0,41)+"..."}
        </a> 
        <Typography variant='body2' align='right' color='textSecondary'>{data.press}</Typography>
      </CardContent>
    </Card>
  );
}

const useStyles = makeStyles((theme) => ({
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
    paddingTop: '70%', // 16:9
  },
  cardContent: {
    flexGrow: 1,
    textAlign: 'left',
  },
}));

export default Front;