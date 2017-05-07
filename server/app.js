
const http = require('http'),
    express = require('express'),
    app = express(),
    cors = require('cors'),
    bodyParser = require('body-parser'),
    server = http.createServer(app),
    mongoClient = require('mongodb').MongoClient,
    mongoURL = 'mongodb://localhost:5000/noun-verb',
    ObjectID = require('mongodb').ObjectID;
    let db;

  const corsOptions = {
    methods: ['GET'],
    origin: '*',
    allowedHeaders: ['Content-Type']
  };

  app.use(cors(corsOptions));
  app.use(express.static(__dirname +'/site'));
  app.use(bodyParser.json());


  app.get('/api/version1/:noun', (request, response) =>{
    const nounId = request.params.noun;

    db.collection('version1').find({'noun':nounId}).next((err, document)=>{
      if (err){
        console.error(err);
        response.sendStatus(500);
      }else{
        response.send(document);}
    });
  });

  app.get('/api/version2/:noun', (request, response) =>{
    const nounId = request.params.noun;

    db.collection('version2').find({'noun':nounId}).next((err, document)=>{
      if (err){
        console.error(err);
        response.sendStatus(500);
      }else{
        response.send(document);}
    });
  });


mongoClient.connect(mongoURL, (err, database)=>{
  if (err){
    console.log('Unable to connect to Mongo.')
    console.error(err);
  }else{
    db = database;
    // db.collection('version1').find({'noun': 'cat'}).toArray(function(err, docs) {
    //   console.log(docs[0])
    //   db.close()
    // })
    server.listen(5042);
    console.log('Listening on port %d', server.address().port);
  }
});
