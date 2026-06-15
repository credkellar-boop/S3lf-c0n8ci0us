import cognitive_core
import pytest

def test_rust_memory_capacity():
    # Initialize buffer with capacity of 2
    mem = cognitive_core.RustMemoryBuffer(2)
    
    mem.add_context("Memory 1")
    mem.add_context("Memory 2")
    mem.add_context("Memory 3") # Should push out Memory 1
    
    context = mem.get_full_context()
    
    assert "Memory 1" not in context
    assert "Memory 2" in context
    assert "Memory 3" in context

def test_rust_memory_clear():
    mem = cognitive_core.RustMemoryBuffer(5)
    mem.add_context("Test data")
    mem.clear()
    
    assert mem.get_full_context() == ""
