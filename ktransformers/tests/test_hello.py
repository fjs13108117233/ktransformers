#!/usr/bin/env python
# coding=utf-8
'''
Description  : Test for hello utility functions
Version      : 1.0.0
Copyright (c) 2024 by KVCache.AI, All Rights Reserved. 
'''

import sys
import os

# Add ktransformers parent directory to path for imports
ktransformers_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, ktransformers_root)

from ktransformers.util.hello import hello, get_version, print_welcome


def test_hello_default():
    """Test hello function with default parameters."""
    result = hello()
    assert "Hello, World!" in result
    assert "KTransformers" in result
    print("✓ test_hello_default passed")


def test_hello_custom_name():
    """Test hello function with custom name."""
    result = hello("Alice")
    assert "Hello, Alice!" in result
    assert "KTransformers" in result
    print("✓ test_hello_custom_name passed")


def test_hello_chinese():
    """Test hello function with Chinese language."""
    result = hello("世界", "zh")
    assert "你好" in result
    assert "世界" in result
    assert "KTransformers" in result
    print("✓ test_hello_chinese passed")


def test_hello_fallback():
    """Test hello function with unsupported language (should fallback to English)."""
    result = hello("User", "fr")  # French not supported, should fallback to English
    assert "Hello, User!" in result
    print("✓ test_hello_fallback passed")


def test_get_version():
    """Test get_version function."""
    version = get_version()
    assert version is not None
    assert len(version) > 0
    print(f"✓ test_get_version passed (version: {version})")


def test_print_welcome():
    """Test print_welcome function (should not raise exceptions)."""
    try:
        print_welcome()
        print("✓ test_print_welcome passed")
    except Exception as e:
        print(f"✗ test_print_welcome failed: {e}")
        raise


if __name__ == "__main__":
    print("Running hello utility tests...\n")
    
    test_hello_default()
    test_hello_custom_name()
    test_hello_chinese()
    test_hello_fallback()
    test_get_version()
    test_print_welcome()
    
    print("\n✓ All tests passed!")
