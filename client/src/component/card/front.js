import React, {  } from 'react';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';

const TitleText = (data) => {
  const length = data.length;
  if (length <= 42) {
    return (
      <Typography variant="subtitle1">{data}</Typography>
    )
  } else {
    return (
      <Typography variant="subtitle1">{data}...</Typography>
    )
  }
}

const Front = ({data}) => {
  const classes = useStyles();
  
  return (
    <Card className={classes.card}>
      <CardMedia
        className={classes.cardMedia}
        image={data.image_url}
      />
      <CardContent className={classes.cardContent}>
          {/* <TitleText data={data.title}/> */}
          <Typography variant="subtitle1">{data.title}</Typography>
      </CardContent>
      {/* <CardActions>
        <Button size="small" color="primary">
          View
        </Button>
        <Button size="small" color="primary">
          Edit
        </Button>
      </CardActions> */}
    </Card>
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
    paddingTop: '70%', // 16:9
  },
  cardContent: {
    flexGrow: 1,
    textAlign: 'left',
  },
}));

export default Front;