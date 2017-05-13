
# nounverbassociator
This is the server for our associator.

## Setup

When you download this, make sure to call `npm install`. This will install express (for easier specification of our routes), body-parser (so we can handle JSON in the messages
),  cors (to handle cross origin setup), and mongodb.


You will also need to create a data directory (`mkdir data`) for mongo to use


## Running

Start the database server. This will start the server running on port 5000

`mongod --config mongo.conf`

If this is the first time you have run the database server, the database will be empty. You can open it with

`mongoimport --db noun-verb --collection version# --jsonArray db-merged_v#.json --port 5000`

where # should be replaced with a model number

Now start the server

`node app.js`
