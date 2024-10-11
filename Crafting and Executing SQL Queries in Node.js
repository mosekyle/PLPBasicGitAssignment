// Connection Setup: We establish a connection to our database using the mysql library.
// SQL Query Definition: The SQL query is defined in the sql variable.
// Query Execution: The connection.query method executes this query. It takes two arguments: the query itself and a callback function that handles results or errors.
// Error Handling: The callback checks for errors during execution and logs them if they occur.
// Data Utilization: Upon successful retrieval, the results variable contains data from the database, which you can use within your application




// Import necessary modules
const mysql = require('mysql');

// Create a connection to the database
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'your_username',
  password: 'your_password',
  database: 'your_database'
});

// Connect to the database
connection.connect((err) => {
  if (err) {
    console.error('Error connecting: ' + err.stack);
    return;
  }
  console.log('Connected as id ' + connection.threadId);

  // Define the SQL query
  const sql = 'SELECT * FROM expenses';

  // Execute the query
  connection.query(sql, (error, results) => {
    if (error) {
      console.error('Query error: ' + error.stack);
      return;
    }

    console.log('Query results:', results);
    // Utilize retrieved data here
  });
});
