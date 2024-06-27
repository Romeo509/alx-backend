README - 0x01. Caching Project
Caching System Concepts
What a Caching System Is

A caching system is a mechanism for temporarily storing frequently accessed data to speed up retrieval times and improve overall performance. It reduces the need to repeatedly access slower primary data sources.
What FIFO Means

FIFO (First-In-First-Out) is a caching algorithm where the oldest cached data (the first to be added) is the first to be removed when the cache reaches its capacity.
What LIFO Means

LIFO (Last-In-First-Out) is a caching algorithm where the most recently added data is the first to be removed when the cache reaches its capacity.
What LRU Means

LRU (Least Recently Used) is a caching algorithm that removes the data that has not been accessed for the longest period when the cache reaches its capacity.
What MRU Means

MRU (Most Recently Used) is a caching algorithm that removes the most recently accessed data first when the cache reaches its capacity.
What LFU Means

LFU (Least Frequently Used) is a caching algorithm that removes the data that has been accessed the least number of times when the cache reaches its capacity.
What the Purpose of a Caching System Is

The purpose of a caching system is to reduce data retrieval times, improve application performance, and decrease the load on primary data sources by storing and providing quick access to frequently used data.
What Limits a Caching System Have

The limitations of a caching system include:

    Memory Constraints: Limited by the available memory for storing cache data.
    Eviction Policies: Inefficiencies can arise if the chosen eviction policy does not align well with the data access patterns.
    Consistency: Ensuring cache consistency with the primary data source can be challenging.
    Complexity: Managing and implementing effective caching strategies can add complexity to the system design.

Implementation Details
BasicCache Implementation

This class inherits from BaseCaching and uses a basic dictionary for caching without any eviction policy.
FIFOCache Implementation

This class inherits from BaseCaching and implements a FIFO eviction policy, discarding the oldest entry when the cache exceeds its maximum size.
LIFOCache Implementation

This class inherits from BaseCaching and implements a LIFO eviction policy, discarding the most recently added entry when the cache exceeds its maximum size.
LRUCache Implementation

This class inherits from BaseCaching and implements an LRU eviction policy, discarding the least recently used entry when the cache exceeds its maximum size.
MRUCache Implementation

This class inherits from BaseCaching and implements an MRU eviction policy, discarding the most recently used entry when the cache exceeds its maximum size.
LFUCache Implementation

This class inherits from BaseCaching and implements an LFU eviction policy, discarding the least frequently used entry when the cache exceeds its maximum size. In case of a tie, it uses the LRU algorithm to discard the least recently used entry among the least frequently used ones.
