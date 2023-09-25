let axios = require('axios');
let FormData = require('form-data');
let fs = require('fs');
let data = new FormData();

let filepath='sample.pdf'

data.append('file', fs.createReadStream(filepath));
let config = {
  method: 'post',
  url: "https://api-v2.finovox.com/analyse",
  headers: { 
    'api-key': 'YOUR_API_KEY', 
    ...data.getHeaders()
  },
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
