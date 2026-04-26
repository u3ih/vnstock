import sys
import os
import time

# Add current directory to path
sys.path.insert(0, os.path.abspath('.'))

from vnstock import Fund

def final_real_test_vnstock_lib(requests_count=50):
    print(f"--- FINAL REAL TEST USING VNSTOCK LIB ({requests_count} requests) ---")
    print("This test calls Fund().listing() repeatedly to trigger real rate limiting.")
    
    # Initialize Fund object from your modified library
    # show_log is True by default in client.send_request for better visibility
    f = Fund(random_agent=True)
    
    success_count = 0
    
    for i in range(1, requests_count + 1):
        try:
            print(f"\n[Request {i}/{requests_count}] Calling f.listing()...")
            # This is the HIGH-LEVEL API of your library
            df = f.listing()
            
            if df is not None and not df.empty:
                success_count += 1
                print(f"✓ Success: Received {len(df)} funds.")
            else:
                print("! Received empty data.")
                
        except Exception as e:
            # Our library will print WARNINGs in the log when bypassing.
            # If it fails completely after retries, it comes here.
            print(f"✗ Request {i} failed even after bypass: {e}")
            
    print(f"\n--- TEST COMPLETED ---")
    print(f"Total Success: {success_count}/{requests_count}")
    print("If you see 'Switching to AUTO-PROXY' in the logs, it means the bypass worked!")

if __name__ == "__main__":
    final_real_test_vnstock_lib(50)
