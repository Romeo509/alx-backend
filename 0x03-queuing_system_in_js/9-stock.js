import express from 'express';
import { promisify } from 'util';
import redis from 'redis';

// Initialize express app
const app = express();
const port = 1245;

// Initialize Redis client
const redisClient = redis.createClient();
const hgetAsync = promisify(redisClient.hget).bind(redisClient);

// Define list of products
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

// Helper function to get product by ID
function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

// Reserve stock in Redis
function reserveStockById(itemId, stock) {
  return new Promise((resolve, reject) => {
    redisClient.hset(`item.${itemId}`, 'stock', stock, (err) => {
      if (err) reject(err);
      else resolve();
    });
  });
}

// Get current reserved stock from Redis
async function getCurrentReservedStockById(itemId) {
  try {
    const reservedStock = await hgetAsync(`item.${itemId}`, 'stock');
    return reservedStock ? parseInt(reservedStock, 10) : 0;
  } catch (err) {
    console.error(err);
    return 0;
  }
}

// Route to list all products
app.get('/list_products', (req, res) => {
  const response = listProducts.map(product => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));
  res.json(response);
});

// Route to get product by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);
  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  const availableStock = Math.max(product.stock - currentReservedStock, 0);

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: availableStock,
  });
});

// Route to reserve product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  const availableStock = Math.max(product.stock - currentReservedStock, 0);

  if (availableStock <= 0) {
    return res.json({
      status: 'Not enough stock available',
      itemId,
    });
  }

  await reserveStockById(itemId, currentReservedStock + 1);
  res.json({
    status: 'Reservation confirmed',
    itemId,
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
