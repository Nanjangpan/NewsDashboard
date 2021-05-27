import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';
import { FixedSizeList } from 'react-window';
import PropTypes from 'prop-types';

function Back({data}) {
  const classes = useStyles();
  const titleList = data;

  function RenderRow() {
    return (
      titleList.map(
        (news) => (
                    <div>
                    {
                      true === true
                      ?(<div>
                        <ListItem button component="a" href={news.url} target="_blank">  
                          <ListItemText primary={news.title} secondary={news.press}/>
                        </ListItem>
                        <Divider />
                      </div>) : (<div></div>)
                    }
                  </div>)
      )
    );
  }
  
  RenderRow.propTypes = {
    index: PropTypes.number.isRequired,
    style: PropTypes.object.isRequired,
  };

  return (
    <React.Fragment>
        <List component="nav" className={classes.root} aria-label="mailbox folders">
          <FixedSizeList height={270} width={"100%"} itemSize={70} itemCount={1}> 
            {RenderRow}
          </FixedSizeList>
        </List>
    </React.Fragment>
  );
}

const useStyles = makeStyles((theme) => ({
  root: {
    width: '100%',
    height: '100%',
    maxWidth: 300,
    backgroundColor: theme.palette.background.paper,
  },
}));

export default Back;