const http = require('http');
let url = require('url');


const requestListener = function (req, res) {
  res.writeHead(200);


  let url_parts = url.parse(req.url, true);
  let query = url_parts.query;
  console.log("Received request from: " + query.node_id)

    //  Processing...


  res.end('Request ok!');
}

const server = http.createServer(requestListener);
server.listen(8080);