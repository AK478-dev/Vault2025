#!/usr/bin/env python3

import sys
from datetime import datetime

def auto_approve(batch_id):
    print(f"Batch {batch_id} auto-approved at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 batch_qa.py <batch_id>")
        sys.exit(1)
    batch_id = sys.argv[1]
    auto_approve(batch_id)
