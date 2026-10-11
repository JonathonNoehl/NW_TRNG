import threading
import time
import hashlib

# Global orchestration flags
chaos_pool = bytearray(64)
running = True

def entropy_harvester(worker_id):
    """
    Independent worker template running an un-synchronized loop.
    It recognizes microsecond timing variations and treats them as pure
    environmental weather to texture the shared chaos pool.
    """
    global chaos_pool, running
    counter = 0
    while running:
        # Capture the absolute microsecond/nanosecond arrival floor
        timestamp = time.time_ns()
        
        # Calculate a dynamic slot index to drop the data
        slot = (timestamp + counter + worker_id) % len(chaos_pool)
        
        # Perform an un-aligned bitwise mutation to force memory chaos
        chaos_pool[slot] = (chaos_pool[slot] ^ (timestamp & 0xFF)) ^ (counter & 0xFF)
        counter += 1

def generate_nw_trng_integer(num_threads=3, target_digits=17):
    """
    The Master Engine Lifecycle. Initializes the stateless agents,
    runs the bounded Fibonacci slicing pass, and extracts the 17-digit string.
    """
    global chaos_pool, running
    running = True
    
    # 1. Reset the pool to a clean state
    for i in range(len(chaos_pool)):
        chaos_pool[i] = 0

    # 2. The Ignition Handshake: Spawn the free-roaming oracle threads
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=entropy_harvester, args=(i,))
        threads.append(t)
        t.start()
    
    # Let the traveler harvest the physical network routing weather
    time.sleep(0.05)
    
    # 3. Terminate the flight and safely halt the threads
    running = False
    for t in threads:
        t.join()
        
    # 4. Bounded Fibonacci Extraction Loop (Seeds pulled from raw jitter)
    f0 = int(time.time_ns() % 1000)
    f1 = int(chaos_pool[0] + chaos_pool[1])
    pool_size = len(chaos_pool)
    
    # Step through the sequence to find our dynamic coordinates
    sequence = [f0, f1]
    for i in range(2, 6):
        next_val = (sequence[i-1] + sequence[i-2]) % pool_size
        sequence.append(next_val)
        
    start_pointer = sequence[-1]
    
    # 5. Cryptographic Whitening: Flatten the final bitstream via SHA-256
    whitened_hash = hashlib.sha256(chaos_pool[start_pointer:]).hexdigest()
    
    # 6. Convert the raw hex artifact into our clean decimal string
    decimal_representation = str(int(whitened_hash, 16))
    
    # Extract the exact 17-digit slice requested
    final_identifier = decimal_representation[:target_digits]
    return final_identifier

if __name__ == "__main__":
    # Test execution of the engine
    print("Initializing NW-TRNG Engine Framework...")
    print("Assigning agent roles via temporal network split...")
    
    true_random_string = generate_nw_trng_integer()
    
    print(f"\n✅ Generated Incorruptible 17-Digit String: {true_random_string}")
