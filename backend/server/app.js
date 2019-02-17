const axios = require('axios');

const grabTrafficCamData = () => {
  axios.get('https://data.calgary.ca/resource/35kd-jzrv.json').then((res) => {
    res.data.map((obj) => {
      console.log(obj.url);
    })
  });
}

grabTrafficCamData();