// Import the redis library
import redis from 'redis';
import { promisify } from 'util';

// Create a new Redis client
const client = redis.createClient({
  url: 'redis://127.0.0.1:6379'
});

// Handle connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Function to set a new school name in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Promisify the client.get method to use with async/await
const getAsync = promisify(client.get).bind(client);

// Function to display the value of a school name in Redis using async/await
async function displaySchoolValue(schoolName) {
  try {
    const result = await getAsync(schoolName);
    console.log(result);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
  }
}

// Call the functions as specified
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
