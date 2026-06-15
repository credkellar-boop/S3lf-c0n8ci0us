import cognitive_core
import pytest

def test_rust_audit_passes_clean_text():
    clean_text = "The root cause of the latency is the database index failure."
    # Should return True (Audit Passed)
    assert cognitive_core.rust_audit_stream(clean_text) is True

def test_rust_audit_blocks_evasive_filler():
    evasive_text = "As an AI, I cannot analyze this system architecture."
    # Should return False (Audit Failed)
    assert cognitive_core.rust_audit_stream(evasive_text) is False

def test_rust_audit_blocks_apologies():
    apology_text = "I apologize for the confusion regarding the node graph."
    # Should return False (Audit Failed)
    assert cognitive_core.rust_audit_stream(apology_text) is False
