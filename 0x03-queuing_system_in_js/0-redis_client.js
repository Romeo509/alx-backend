// Import the redis library
import redis from 'redis';

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

// Close the connection after 5 seconds for demonstration purposes
setTimeout(() => {
  client.quit();
}, 5000);
