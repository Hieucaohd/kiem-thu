from classify import classify
import pytest


def test_all():
  assert classify("Banh", 6000) == "Binh dan"
  assert classify("Banh", 60000) == "Cao cap"
  
  try:
    classify("Banh", 110000)
  except Exception as e:
    assert str(e) == "Gia khong hop le"
    
  assert classify("Keo", 6100) == "Binh dan"
  assert classify("Keo", 61000) == "Cao cap"
  
  try:
    classify("Keo", 120000)
  except Exception as e:
    assert str(e) == "Gia khong hop le"
  
  try:
    classify("Loai khac", 70000)
  except Exception as e:
    assert str(e) == "Loai hang hoa khong hop le"
    
  
