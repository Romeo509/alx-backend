import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

// Initialize express app
const app = express();
const port = 1245;

// Initialize Redis client
const redisClient = redis.createClient();
const hgetAsync = promisify(redisClient.hget).bind(redisClient);
const hsetAsync = promisify(redisClient.hset).bind(redisClient);

// Initialize Kue queue
const queue = kue.createQueue();

// Initialize reservation status
let reservationEnabled = true;

// Set initial number of available seats
const initialSeats = 50;
await hsetAsync('available_seats', 'number', initialSeats);

// Function to reserve seats in Redis
async function reserveSeat(number) {
  await hsetAsync('available_seats', 'number', number);
}

// Function to get current available seats from Redis
async function getCurrentAvailableSeats() {
  try {
    const seats = await hgetAsync('available_seats', 'number');
    return parseInt(seats, 10) || 0;
  } catch (err) {
    console.error(err);
    return 0;
  }
}

// Route to get number of available seats
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats.toString() });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {}).save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

// Route to process the queue
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    try {
      const availableSeats = await getCurrentAvailableSeats();
      if (availableSeats <= 0) {
        reservationEnabled = false;
        return done(new Error('Not enough seats available'));
      }

      await reserveSeat(availableSeats - 1);
      done();
    } catch (err) {
      done(err);
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
