import React, {useEffect, useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListSubheader from '@material-ui/core/ListSubheader';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';
import DeleteIcon from '@material-ui/icons/Delete';
import IconButton from '@material-ui/core/IconButton';
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';
import { FixedSizeList } from 'react-window';
import PropTypes from 'prop-types';

const titleList = [
  {
      'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
      'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
      'press' : "YBIGTA",
  },{
      'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
      'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
      'press' : "YBIGTA",
  },{
      'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
      'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
      'press' : "YBIGTA",
  },{
      'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
      'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
      'press' : "YBIGTA",
  },{
      'title' : '22 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
      'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
  },{
      'title' : '33 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
      'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
  },{
      'title' : '44 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
      'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
  }
]


function renderRow(props) {
  const { index, style } = props;

  return (
    titleList.map(
      (news) => (<div>
                  {
                    true === true
                    ?(<div>
                      <ListItem button component="a" href={news.url} target="_blank">  
                        <ListItemText primary={news.title} secondary={news.press}/>
                        {/* <ListItemSecondaryAction>
                          <IconButton edge="end" aria-label="delete" onClick>
                            <DeleteIcon />
                          </IconButton>
                        </ListItemSecondaryAction> */}
                      </ListItem>
                      <Divider />
                    </div>) : (<div></div>)
                  }
                </div>)
    )
  );
}

renderRow.propTypes = {
  index: PropTypes.number.isRequired,
  style: PropTypes.object.isRequired,
};


function Back() {
  const classes = useStyles();

  return (
    <React.Fragment>
        <List component="nav" className={classes.root} aria-label="mailbox folders">
          <FixedSizeList height={330} width={"100%"} itemSize={70} itemCount={1}> 
            {renderRow}
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
  icon: {
    marginRight: theme.spacing(2),
  },
  titleText: {
    fontsize: 3
  },
}));

export default Back;