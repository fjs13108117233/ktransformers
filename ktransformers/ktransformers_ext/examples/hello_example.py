#!/usr/bin/env python
# coding=utf-8
'''
Description  : Simple hello example demonstrating KTransformers greeting utility
Version      : 1.0.0
Copyright (c) 2024 by KVCache.AI, All Rights Reserved. 
'''

from ktransformers.util.hello import hello, print_welcome, get_version

def main():
    """
    Demonstrate the hello utility functions.
    """
    # Print welcome banner
    print_welcome()
    
    # Demonstrate basic greetings
    print("\n=== Basic Greetings ===")
    print(hello())  # Default: English, World
    print(hello("KTransformers User"))
    
    # Demonstrate Chinese greetings
    print("\n=== Chinese Greetings (中文问候) ===")
    print(hello("世界", "zh"))
    print(hello("用户", "zh"))
    
    # Show version
    print(f"\n=== Version Information ===")
    print(f"KTransformers Version: {get_version()}")


if __name__ == "__main__":
    main()
