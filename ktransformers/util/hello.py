#!/usr/bin/env python
# coding=utf-8
'''
Description  : Simple greeting utility for KTransformers
Version      : 1.0.0
Copyright (c) 2024 by KVCache.AI, All Rights Reserved. 
'''

def hello(name: str = "World", language: str = "en") -> str:
    """
    A simple greeting function that supports multiple languages.
    
    Args:
        name (str): The name to greet. Default is "World".
        language (str): The language for the greeting. Supported: "en", "zh". Default is "en".
    
    Returns:
        str: The greeting message.
    
    Examples:
        >>> hello()
        'Hello, World! Welcome to KTransformers.'
        >>> hello("User", "zh")
        '你好，User！欢迎使用 KTransformers。'
    """
    greetings = {
        "en": f"Hello, {name}! Welcome to KTransformers.",
        "zh": f"你好，{name}！欢迎使用 KTransformers。",
    }
    
    return greetings.get(language, greetings["en"])


def get_version() -> str:
    """
    Get the KTransformers version.
    
    Returns:
        str: The version string.
    """
    try:
        from ktransformers import __version__
        return __version__
    except ImportError:
        return "0.2.0"  # fallback version


def print_welcome():
    """
    Print a welcome message for KTransformers.
    """
    version = get_version()
    
    welcome_message = f"""
╔════════════════════════════════════════════════════════════╗
║                     KTransformers v{version}                    ║
║  A Flexible Framework for Cutting-edge LLM Inference      ║
║                                                            ║
║  你好 (Hello)! Welcome to KTransformers!                    ║
╚════════════════════════════════════════════════════════════╝
    """
    print(welcome_message)


if __name__ == "__main__":
    # Simple test when run directly
    print(hello())
    print(hello("张三", "zh"))
    print(hello("User", "en"))
    print(f"Version: {get_version()}")
    print_welcome()
