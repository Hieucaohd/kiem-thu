def classify(type, price):
  if type == "Banh":
    if 5000 <= price < 40000:
      return "Binh dan"
    elif 40000 <= price <= 100000:
      return "Cao cap"
    else:
      raise Exception("Gia khong hop le")
  elif type == "Keo":
    if 5000 <= price < 50000:
      return "Binh dan"
    elif 50000 <= price <= 100000:
      return "Cao cap"
    else:
      raise Exception("Gia khong hop le")
  else:
    raise Exception("Loai hang hoa khong hop le")

print(classify("Loai khac", 5000))