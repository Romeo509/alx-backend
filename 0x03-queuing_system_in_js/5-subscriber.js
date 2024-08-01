// Import the redis library
import redis from 'redis';

// Create a Redis client
const subscriber = redis.createClient({
  url: 'redis://127.0.0.1:6379'
});

// Handle connection errors
subscriber.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Handle successful connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Subscribe to the channel 'holberton school channel'
subscriber.subscribe('holberton school channel');

// Listen for messages on the channel
subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
